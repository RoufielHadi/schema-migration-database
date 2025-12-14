from pathlib import Path
import time
import hashlib

from src.visitor.SchemaBuilderVisitor import parse_dsl_text
from src.validator.SemanticValidator import SemanticValidator
from src.generator.PostgreSQLGenerator import PostgreSQLGenerator

ROOT = Path(__file__).resolve().parents[1]


def main():
    dsl = (ROOT / 'examples' / 'shop.dsl').read_text(encoding='utf-8')
    schema = parse_dsl_text(dsl)
    val = SemanticValidator().validate(schema)
    if val.errors:
        for e in val.errors:
            print('Validation error:', e)
        raise SystemExit(2)

    gen = PostgreSQLGenerator(schema)
    up_sql = gen.generate_up()
    down_sql = gen.generate_down()

    meta = schema.meta or {}
    header = [
        '-- MIGRATION',
        f"-- MIGRATION ID: {meta.get('id','')}",
        f"-- DESC: {meta.get('desc','')}",
        f"-- AUTHOR: {meta.get('author','')}",
        f"-- DB: {meta.get('db','')}",
    ]
    checksum = hashlib.sha256((up_sql + '\n' + down_sql).encode('utf-8')).hexdigest()
    header.append(f"-- CHECKSUM: {checksum}")
    header.append('--')
    content = '\n'.join(header) + '\n\n-- UP\n' + up_sql + '\n\n-- DOWN\n' + down_sql + '\n'

    outdir = ROOT / 'migrations'
    outdir.mkdir(exist_ok=True)
    ts = time.strftime('%Y%m%d_%H%M%S')
    out = outdir / f"{ts}_create_shop_v1.sql"
    out.write_text(content, encoding='utf-8')
    print('Wrote:', out)


if __name__ == '__main__':
    main()
