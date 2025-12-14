import argparse
import json
import os
import time
import hashlib
import subprocess
from pathlib import Path

from src.ast.models import Schema
from src.validator.SemanticValidator import SemanticValidator, diff_schemas
from src.generator.PostgreSQLGenerator import PostgreSQLGenerator
from src.visitor.SchemaBuilderVisitor import parse_dsl_text
from src.utils.setup_check import ensure_runtime_ready

ROOT = Path(__file__).resolve().parents[2]
ANTLR_JAR = os.environ.get('ANTLR_JAR', r'C:\\tools\\antlr\\antlr-4.13.2-complete.jar')


def cmd_compile(args: argparse.Namespace) -> int:
    g4 = Path(args.grammar).resolve()
    out = ROOT / 'generated'
    out.mkdir(parents=True, exist_ok=True)
    cmd = [
        'java', '-cp', ANTLR_JAR,
        'org.antlr.v4.Tool', '-Dlanguage=Python3', '-visitor', str(g4), '-o', str(out)
    ]
    print('Running:', ' '.join(cmd))
    res = subprocess.run(cmd, cwd=ROOT)
    return res.returncode


def _read_text(p: Path) -> str:
    return p.read_text(encoding='utf-8')


def cmd_compile_dsl(args: argparse.Namespace) -> int:
    ensure_runtime_ready()
    dsl_path = Path(args.file).resolve()
    # Preflight: ensure parser exists
    gen_parser = ROOT / 'generated' / 'DBSchemaParser.py'
    gen_visitor = ROOT / 'generated' / 'DBSchemaVisitor.py'
    if not gen_parser.exists() or not gen_visitor.exists():
        print('Parser not found. Generating with ANTLR...')
        rc = cmd_compile(argparse.Namespace(grammar=str(ROOT / 'grammar' / 'DBSchema.g4')))
        if rc != 0:
            print('ANTLR generation failed with exit code', rc)
            return rc
    text = _read_text(dsl_path)
    schema = parse_dsl_text(text)
    val_res = SemanticValidator().validate(schema)
    if val_res.errors:
        print('Validation errors:')
        for e in val_res.errors:
            print('-', e)
        return 2
    snap_dir = ROOT / '.snapshots'
    snap_dir.mkdir(exist_ok=True)
    ts = time.strftime('%Y%m%d_%H%M%S')
    snap_path = snap_dir / f'{ts}_{dsl_path.stem}.json'
    snap_path.write_text(json.dumps(schema.to_dict(), ensure_ascii=False, indent=2), encoding='utf-8')
    print('Wrote snapshot:', snap_path)
    return 0


def cmd_diff(args: argparse.Namespace) -> int:
    old = json.loads(Path(args.old).read_text(encoding='utf-8'))
    new = json.loads(Path(args.new).read_text(encoding='utf-8'))
    old_s = Schema.from_dict(old)
    new_s = Schema.from_dict(new)
    d = diff_schemas(old_s, new_s)
    print(json.dumps(d, indent=2))
    if d.get('destructive'):
        print('WARNING: Destructive changes detected.')
    return 0


def _write_migration_file(schema: Schema, up_sql: str, down_sql: str) -> Path:
    mig_dir = ROOT / 'migrations'
    mig_dir.mkdir(exist_ok=True)
    meta = schema.meta or {}
    header = [
        '-- MIGRATION',
        f"-- MIGRATION ID: {meta.get('id', '')}",
        f"-- DESC: {meta.get('desc', '')}",
        f"-- AUTHOR: {meta.get('author', '')}",
        f"-- DB: {meta.get('db', '')}",
    ]
    checksum = hashlib.sha256((up_sql + '\n' + down_sql).encode('utf-8')).hexdigest()
    header.append(f"-- CHECKSUM: {checksum}")
    header.append('--')
    combined = '\n'.join(header) + '\n\n-- UP\n' + up_sql + '\n\n-- DOWN\n' + down_sql + '\n'
    ts = time.strftime('%Y%m%d_%H%M%S')
    desc_slug = (meta.get('desc', 'migration').lower().replace(' ', '_'))[:30]
    out_path = mig_dir / f"{ts}_{desc_slug}.sql"
    out_path.write_text(combined, encoding='utf-8')
    return out_path


def cmd_migrate_up(args: argparse.Namespace) -> int:
    ensure_runtime_ready()
    dsl_path = Path(args.dsl).resolve() if args.dsl else (ROOT / 'examples' / 'shop.dsl')
    # Preflight: ensure parser exists
    gen_parser = ROOT / 'generated' / 'DBSchemaParser.py'
    gen_visitor = ROOT / 'generated' / 'DBSchemaVisitor.py'
    if not gen_parser.exists() or not gen_visitor.exists():
        print('Parser not found. Generating with ANTLR...')
        rc = cmd_compile(argparse.Namespace(grammar=str(ROOT / 'grammar' / 'DBSchema.g4')))
        if rc != 0:
            print('ANTLR generation failed with exit code', rc)
            return rc
    text = _read_text(dsl_path)
    schema = parse_dsl_text(text)
    val_res = SemanticValidator().validate(schema)
    if val_res.errors:
        print('Validation errors:')
        for e in val_res.errors:
            print('-', e)
        return 2
    gen = PostgreSQLGenerator(schema)
    up_sql = gen.generate_up()
    down_sql = gen.generate_down()
    out_path = _write_migration_file(schema, up_sql, down_sql)
    print('Wrote migration file:', out_path)
    if args.apply:
        print('Apply is not implemented for safety. Review and execute SQL manually.')
    return 0


def _find_migration_by_id(mig_id: str) -> Path:
    mig_dir = ROOT / 'migrations'
    for p in sorted(mig_dir.glob('*')):
        if p.is_file() and (f"MIGRATION ID: {mig_id}") in p.read_text(encoding='utf-8'):
            return p
    raise FileNotFoundError(f'Migration with id {mig_id} not found in migrations/')


def cmd_migrate_down(args: argparse.Namespace) -> int:
    mig_path = _find_migration_by_id(args.migration_id)
    txt = mig_path.read_text(encoding='utf-8')
    down_idx = txt.find('\n-- DOWN\n')
    if down_idx == -1:
        print('DOWN section not found in migration:', mig_path)
        return 2
    down_sql = txt[down_idx + len('\n-- DOWN\n'):].strip()
    ts = time.strftime('%Y%m%d_%H%M%S')
    out = mig_path.parent / f"{ts}_down_{args.migration_id}.sql"
    out.write_text(down_sql + '\n', encoding='utf-8')
    print('Wrote down migration SQL:', out)
    if args.apply:
        print('Apply is not implemented for safety. Review and execute SQL manually.')
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog='dslc', description='Database Schema DSL CLI')
    sub = p.add_subparsers(dest='cmd')

    p_compile = sub.add_parser('compile', help='Generate ANTLR parser from grammar')
    p_compile.add_argument('grammar', help='Path to .g4 file')
    p_compile.set_defaults(func=cmd_compile)

    p_compile_dsl = sub.add_parser('compile-dsl', help='Parse DSL and write AST snapshot')
    p_compile_dsl.add_argument('file', help='Path to .dsl file')
    p_compile_dsl.set_defaults(func=cmd_compile_dsl)

    p_diff = sub.add_parser('diff', help='Diff two schema snapshots (JSON)')
    p_diff.add_argument('old')
    p_diff.add_argument('new')
    p_diff.set_defaults(func=cmd_diff)

    p_migrate = sub.add_parser('migrate', help='Generate migration SQL')
    sub_m = p_migrate.add_subparsers(dest='migrate_cmd')

    p_up = sub_m.add_parser('up', help='Generate UP migration SQL from DSL')
    p_up.add_argument('--dsl', help='Path to .dsl file')
    p_up.add_argument('--target', default='postgres')
    p_up.add_argument('--apply', action='store_true')
    p_up.set_defaults(func=cmd_migrate_up)

    p_down = sub_m.add_parser('down', help='Extract DOWN SQL by migration id')
    p_down.add_argument('migration_id')
    p_down.add_argument('--target', default='postgres')
    p_down.add_argument('--apply', action='store_true')
    p_down.set_defaults(func=cmd_migrate_down)

    return p


def main(argv=None) -> int:
    argv = argv or os.sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)
    if not hasattr(args, 'func'):
        parser.print_help()
        return 1
    return args.func(args)


if __name__ == '__main__':
    raise SystemExit(main())
