from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Optional


@dataclass
class Column:
    name: str
    type: str
    length: Optional[int] = None
    primary: bool = False
    unique: bool = False
    not_null: bool = False
    default: Optional[Any] = None
    line: int = 0
    column: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FK:
    column: str
    ref_table: str
    ref_column: str
    line: int = 0
    column_pos: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Index:
    name: str
    columns: List[str]
    unique: bool = False
    line: int = 0
    column: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Table:
    name: str
    columns: List[Column] = field(default_factory=list)
    fks: List[FK] = field(default_factory=list)
    indexes: List[Index] = field(default_factory=list)
    line: int = 0
    column: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "columns": [c.to_dict() for c in self.columns],
            "fks": [f.to_dict() for f in self.fks],
            "indexes": [i.to_dict() for i in self.indexes],
            "line": self.line,
            "column": self.column,
        }


@dataclass
class Enum:
    name: str
    values: List[str]
    line: int = 0
    column: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Seed:
    table: str
    rows: List[Dict[str, Any]] = field(default_factory=list)
    line: int = 0
    column: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Schema:
    name: str
    tables: List[Table] = field(default_factory=list)
    enums: List[Enum] = field(default_factory=list)
    seeds: List[Seed] = field(default_factory=list)
    meta: Dict[str, Any] = field(default_factory=dict)
    line: int = 0
    column: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "tables": [t.to_dict() for t in self.tables],
            "enums": [e.to_dict() for e in self.enums],
            "seeds": [s.to_dict() for s in self.seeds],
            "meta": self.meta,
            "line": self.line,
            "column": self.column,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Schema":
        tables = []
        for td in d.get("tables", []):
            cols = [Column(**cd) for cd in td.get("columns", [])]
            fks = [FK(**fk) for fk in td.get("fks", [])]
            idxs = [Index(**ix) for ix in td.get("indexes", [])]
            tables.append(Table(name=td["name"], columns=cols, fks=fks, indexes=idxs, line=td.get("line", 0), column=td.get("column", 0)))
        enums = [Enum(**ed) for ed in d.get("enums", [])]
        seeds = [Seed(**sd) for sd in d.get("seeds", [])]
        return Schema(
            name=d["name"],
            tables=tables,
            enums=enums,
            seeds=seeds,
            meta=d.get("meta", {}),
            line=d.get("line", 0),
            column=d.get("column", 0),
        )
