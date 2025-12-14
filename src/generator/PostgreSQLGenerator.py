from typing import List, Dict, Any
from src.ast.models import Schema, Table, Column, FK, Seed, Enum, Index


class PostgreSQLGenerator:
    def __init__(self, schema: Schema):
        self.schema = schema
        self._enum_names = {e.name for e in (schema.enums or [])}

    @staticmethod
    def _q(name: str) -> str:
        return f'"{name}"'

    @staticmethod
    def _sql_literal(v: Any) -> str:
        if isinstance(v, int):
            return str(v)
        if isinstance(v, str):
            if v.startswith('"') and v.endswith('"'):
                inner = v[1:-1].replace("'", "''")
                return f"'{inner}'"
            return v
        return str(v)

    def create_schema(self) -> str:
        return f"CREATE SCHEMA IF NOT EXISTS {self._q(self.schema.name)};"

    def create_enum(self, enum: Enum) -> str:
        vals = ', '.join(self._sql_literal(f'"{v}"') for v in enum.values)
        tname = f"{self._q(self.schema.name)}.{self._q(enum.name)}"
        return (
            "DO $$ BEGIN\n"
            f"  CREATE TYPE {tname} AS ENUM ({vals});\n"
            "EXCEPTION\n"
            "  WHEN duplicate_object THEN NULL;\n"
            "END $$;"
        )

    def column_sql(self, col: Column) -> str:
        parts: List[str] = [self._q(col.name)]
        # Type reference (schema-qualify enums)
        if col.type in self._enum_names:
            type_ref = f"{self._q(self.schema.name)}.{self._q(col.type)}"
        else:
            type_ref = col.type if col.length is None else f"{col.type}({col.length})"
        parts.append(type_ref)
        if col.not_null:
            parts.append("NOT NULL")
        if col.unique:
            parts.append("UNIQUE")
        if col.default is not None:
            default_sql = None
            # If default is bare identifier and column is enum, quote it as enum label
            if isinstance(col.default, str) and not col.default.startswith('\"') and '(' not in col.default and col.type in self._enum_names:
                default_sql = self._sql_literal(f'"{col.default}"')
            else:
                default_sql = self._sql_literal(col.default)
            parts.append(f"DEFAULT {default_sql}")
        if col.primary:
            parts.append("PRIMARY KEY")
        return ' '.join(parts)

    def create_table(self, table: Table) -> str:
        cols = ',\n  '.join(self.column_sql(c) for c in table.columns)
        return (
            f"CREATE TABLE IF NOT EXISTS {self._q(self.schema.name)}.{self._q(table.name)} (\n  {cols}\n);"
        )

    def create_fk(self, table: Table, fk: FK) -> str:
        cname = f"fk_{table.name}_{fk.column}"
        return (
            f"ALTER TABLE {self._q(self.schema.name)}.{self._q(table.name)}\n"
            f"  ADD CONSTRAINT {self._q(cname)} FOREIGN KEY ({self._q(fk.column)})\n"
            f"  REFERENCES {self._q(self.schema.name)}.{self._q(fk.ref_table)} ({self._q(fk.ref_column)});"
        )

    def create_index(self, table: Table, idx: Index) -> str:
        uq = "UNIQUE " if idx.unique else ""
        cols = ', '.join(self._q(c) for c in idx.columns)
        iname = idx.name
        return (
            f"CREATE {uq}INDEX IF NOT EXISTS {self._q(iname)} ON {self._q(self.schema.name)}.{self._q(table.name)} ({cols});"
        )

    def drop_table(self, table: Table) -> str:
        return f"DROP TABLE IF EXISTS {self._q(self.schema.name)}.{self._q(table.name)};"  # TODO: handle cascade option

    def seed_inserts(self, seed: Seed) -> List[str]:
        stmts: List[str] = []
        if not seed.rows:
            return stmts
        # use keys from first row to define column order
        cols = list(seed.rows[0].keys())
        col_sql = ', '.join(self._q(c) for c in cols)
        for r in seed.rows:
            vals = ', '.join(self._sql_literal(r[c]) for c in cols)
            stmts.append(
                f"INSERT INTO {self._q(self.schema.name)}.{self._q(seed.table)} ({col_sql}) VALUES ({vals});"
            )
        return stmts

    def generate_up(self) -> str:
        lines: List[str] = []
        lines.append(self.create_schema())
        for e in self.schema.enums:
            lines.append(self.create_enum(e))
        for t in self.schema.tables:
            lines.append(self.create_table(t))
        for t in self.schema.tables:
            for fk in t.fks:
                lines.append(self.create_fk(t, fk))
            for idx in t.indexes:
                lines.append(self.create_index(t, idx))
        for s in self.schema.seeds:
            lines.extend(self.seed_inserts(s))
        return "\n\n".join(lines)

    def generate_down(self) -> str:
        lines: List[str] = []
        # TODO: consider FK drops explicitly to avoid dependency issues
        for t in reversed(self.schema.tables):
            lines.append(self.drop_table(t))
        for e in reversed(self.schema.enums):
            lines.append(f"DROP TYPE IF EXISTS {self._q(self.schema.name)}.{self._q(e.name)};")
        return "\n".join(lines)
