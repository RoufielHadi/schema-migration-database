from dataclasses import dataclass, field
from typing import List, Dict, Any, Tuple
from src.ast.models import Schema, Table, Column


@dataclass
class ValidationResult:
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    destructive: bool = False


class SemanticValidator:
    def validate(self, schema: Schema) -> ValidationResult:
        res = ValidationResult()
        table_map: Dict[str, Table] = {t.name: t for t in schema.tables}
        enum_names = {e.name for e in schema.enums}

        for t in schema.tables:
            col_map = {c.name: c for c in t.columns}
            for c in t.columns:
                if not c.type:
                    res.errors.append(f"Column {t.name}.{c.name} has no type")
                if c.type in enum_names:
                    pass
            for fk in t.fks:
                if fk.column not in col_map:
                    res.errors.append(f"FK column not found: {t.name}.{fk.column}")
                if fk.ref_table not in table_map:
                    res.errors.append(f"FK ref table not found: {fk.ref_table}")
                else:
                    ref_cols = {rc.name for rc in table_map[fk.ref_table].columns}
                    if fk.ref_column not in ref_cols:
                        res.errors.append(f"FK ref column not found: {fk.ref_table}.{fk.ref_column}")
        return res


def _type_and_len(col: Column) -> Tuple[str, int]:
    t = col.type.lower()
    ln = col.length or 0
    return t, ln


def diff_schemas(old: Schema, new: Schema) -> Dict[str, Any]:
    ops: List[Dict[str, Any]] = []
    destructive = False
    ot = {t.name: t for t in old.tables}
    nt = {t.name: t for t in new.tables}

    for tname in nt.keys() - ot.keys():
        ops.append({"op": "create_table", "table": tname})
    for tname in ot.keys() - nt.keys():
        ops.append({"op": "drop_table", "table": tname, "destructive": True})
        destructive = True
    for tname in nt.keys() & ot.keys():
        ocols = {c.name: c for c in ot[tname].columns}
        ncols = {c.name: c for c in nt[tname].columns}
        for cname in ncols.keys() - ocols.keys():
            ops.append({"op": "add_column", "table": tname, "column": cname})
        for cname in ocols.keys() - ncols.keys():
            ops.append({"op": "drop_column", "table": tname, "column": cname, "destructive": True})
            destructive = True
        for cname in ncols.keys() & ocols.keys():
            otl = _type_and_len(ocols[cname])
            ntl = _type_and_len(ncols[cname])
            if otl[0] == ntl[0] and otl[1] > ntl[1] and ntl[1] > 0:
                ops.append({"op": "shorten_varchar", "table": tname, "column": cname, "from": otl[1], "to": ntl[1], "destructive": True})
                destructive = True
    return {"ops": ops, "destructive": destructive}
