from typing import Any, Dict, List, Optional

from antlr4 import CommonTokenStream, InputStream, ParseTreeVisitor, Token

try:
    from generated.DBSchemaLexer import DBSchemaLexer  # type: ignore
    from generated.DBSchemaParser import DBSchemaParser  # type: ignore
except Exception as e:  # pragma: no cover
    DBSchemaLexer = None  # type: ignore
    DBSchemaParser = None  # type: ignore

try:
    from generated.DBSchemaVisitor import DBSchemaVisitor as _BaseVisitor  # type: ignore
except Exception:
    _BaseVisitor = ParseTreeVisitor  # type: ignore

from src.ast.models import Schema, Table, Column, FK, Enum, Seed


def _loc(ctx) -> Dict[str, int]:
    tok = getattr(ctx, 'start', None)
    return {"line": getattr(tok, 'line', 0) or 0, "column": getattr(tok, 'column', 0) or 0}


def parse_dsl_text(text: str) -> Schema:
    if DBSchemaLexer is None or DBSchemaParser is None:
        raise RuntimeError("Grammar not generated. Run the VS Code task 'Generate ANTLR (Python)' on grammar/DBSchema.g4 first.")
    input_stream = InputStream(text)
    lexer = DBSchemaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DBSchemaParser(stream)
    tree = parser.migrationFile()
    if getattr(parser, 'getNumberOfSyntaxErrors', lambda: 0)() > 0:
        raise RuntimeError("DSL contains syntax errors. Please fix the .dsl according to grammar/DBSchema.g4")
    visitor = SchemaBuilderVisitor()
    result = visitor.visit(tree)
    if result is None:
        raise RuntimeError("Parser returned no schema (None). Check that your DSL starts with 'migration ... { ... schema <name> { ... } }' or 'schema <name> { ... }'.")
    return result


class SchemaBuilderVisitor(_BaseVisitor):  # type: ignore
    def _node_text(self, node: Any) -> str:
        if node is None:
            return ""
        # Most nodes (ParserRuleContext, TerminalNode) implement getText()
        if hasattr(node, "getText"):
            try:
                return node.getText()
            except Exception:
                pass
        # Some nodes provide getSymbol() returning a Token
        if hasattr(node, "getSymbol"):
            try:
                sym = node.getSymbol()
                if sym is not None and hasattr(sym, "text"):
                    return sym.text or ""
            except Exception:
                pass
        # Direct Token (e.g., CommonToken)
        if isinstance(node, Token):
            return getattr(node, "text", "") or ""
        # Plain strings
        if isinstance(node, str):
            return node
        # Fallback to a 'text' attribute if present
        t = getattr(node, "text", None)
        if t is not None:
            return t
        # Last resort
        try:
            return str(node)
        except Exception:
            return ""

    def _id(self, ctx_ids: Any, i: Optional[int] = None, where: str = "") -> str:
        try:
            if i is None:
                node = ctx_ids.ID()
                if node is None:
                    raise ValueError("missing ID")
                return self._node_text(node)
            node = ctx_ids.ID(i)
            if node is None:
                raise IndexError(f"missing ID[{i}]")
            return self._node_text(node)
        except Exception as e:
            line = getattr(getattr(ctx_ids, 'start', None), 'line', 0) or 0
            raise ValueError(f"Invalid identifier {where} at line {line}: {e}")
    def visitMigrationFile(self, ctx):  # (migrationDecl | schemaDecl)* EOF
        # Prefer the last migrationDecl if present, else the last schemaDecl
        migs = ctx.migrationDecl() if hasattr(ctx, 'migrationDecl') else []
        if migs:
            if isinstance(migs, list):
                return self.visit(migs[-1])
            return self.visit(migs)
        schemas = ctx.schemaDecl() if hasattr(ctx, 'schemaDecl') else []
        if schemas:
            if isinstance(schemas, list):
                sc = self.visit(schemas[-1])
            else:
                sc = self.visit(schemas)
            if getattr(sc, 'meta', None) is None:
                sc.meta = {}
            return sc
        # Fallback empty schema
        return Schema(name="default")

    def visitMigrationDecl(self, ctx):
        # MIGRATION migrationId LBRACE DESC STRING AUTHOR author=ID DB db=ID schemaDecl RBRACE
        schema: Schema = self.visit(ctx.schemaDecl())
        meta = {
            "id": self._node_text(ctx.migrationId()),
            "desc": self._node_text(ctx.STRING()).strip('"'),
            "author": self._node_text(getattr(ctx, 'author', None)),
            "db": self._node_text(getattr(ctx, 'db', None)),
        }
        schema.meta = meta
        return schema

    def visitSchemaDecl(self, ctx):
        # SCHEMA schemaBody
        return self.visit(ctx.schemaBody())

    def visitSchemaBody(self, ctx):
        # ID LBRACE schemaMember* RBRACE
        sc = Schema(name=self._id(ctx, where='schema name'), line=_loc(ctx)["line"], column=_loc(ctx)["column"])
        for m in ctx.schemaMember():
            item = self.visit(m)
            if isinstance(item, Table):
                sc.tables.append(item)
            elif isinstance(item, Enum):
                sc.enums.append(item)
            elif isinstance(item, Seed):
                sc.seeds.append(item)
        return sc

    def visitTableDecl(self, ctx):
        t = Table(name=self._id(ctx, where='table name'), line=_loc(ctx)["line"], column=_loc(ctx)["column"])
        for b in ctx.tableBody():
            node = self.visit(b)
            if isinstance(node, Column):
                t.columns.append(node)
            elif isinstance(node, FK):
                t.fks.append(node)
            elif isinstance(node, dict) and node.get("__index__"):
                t.indexes.append(node["node"])  # type: ignore
        return t

    def visitColumnDecl(self, ctx):
        name = self._id(ctx, where='column name')
        type_name, length = self.visit(ctx.typeSpec())
        col = Column(name=name, type=type_name, length=length, line=_loc(ctx)["line"], column=_loc(ctx)["column"])
        for a in ctx.columnAttr():
            first = (self._node_text(a.getChild(0)) or '').lower()
            if first == 'primary':
                col.primary = True
            elif first == 'unique':
                col.unique = True
            elif first == 'not' and a.getChildCount() >= 2 and (self._node_text(a.getChild(1)) or '').lower() == 'null':
                col.not_null = True
            elif first == 'default':
                if hasattr(a, 'literal') and a.literal() is not None:
                    col.default = self.visit(a.literal())
                else:
                    # fallback to raw text
                    txt = self._node_text(a)[len('default'):]
                    col.default = self._parse_literal_text(txt)
        return col

    def visitTypeSpec(self, ctx):
        tname = self._id(ctx, where='type name')
        length = None
        if ctx.INT():
            length = int(self._node_text(ctx.INT()))
        return tname, length

    def visitFkDecl(self, ctx):
        col = self._id(ctx, 0, 'fk column')
        ref_table = self._id(ctx, 1, 'fk ref table')
        ref_col = self._id(ctx, 2, 'fk ref column')
        return FK(column=col, ref_table=ref_table, ref_column=ref_col, line=_loc(ctx)["line"], column_pos=_loc(ctx)["column"])  # type: ignore

    def visitIndexDecl(self, ctx):
        name = self._id(ctx, where='index name')
        ids = ctx.idList().ID() if hasattr(ctx, 'idList') and ctx.idList() else []
        cols = [self._node_text(c) for c in (ids or [])]
        unique = any((self._node_text(ch) or '').lower() == 'unique' for ch in (getattr(ctx, 'children', []) or []))
        from src.ast.models import Index
        idx = Index(name=name, columns=cols, unique=unique, line=_loc(ctx)["line"], column=_loc(ctx)["column"])
        return {"__index__": True, "node": idx}

    def visitEnumDecl(self, ctx):
        name = self._id(ctx, 0, 'enum name')
        all_ids = list(ctx.ID() or [])
        vals = [self._node_text(t) for t in (all_ids[1:] if len(all_ids) > 1 else [])]
        return Enum(name=name, values=vals, line=_loc(ctx)["line"], column=_loc(ctx)["column"])

    def visitSeedDecl(self, ctx):
        table = self._id(ctx, where='seed table')
        rows: List[Dict[str, Any]] = []
        for r in ctx.seedRow():
            row: Dict[str, Any] = {}
            for f in r.seedField():
                k = self._node_text(f.ID())
                v = self.visit(f.literal()) if f.literal() else self._parse_literal_text(self._node_text(f).split('=',1)[1])
                row[k] = v
            rows.append(row)
        return Seed(table=table, rows=rows, line=_loc(ctx)["line"], column=_loc(ctx)["column"])

    def visitLiteral(self, ctx):
        if ctx.STRING():
            return self._node_text(ctx.STRING())
        if ctx.INT():
            return int(self._node_text(ctx.INT()))
        if ctx.ID():
            return self._node_text(ctx.ID())
        return self._node_text(ctx.functionCall())

    def _parse_literal_text(self, text: str):
        text = text.strip()
        if text.startswith('"') and text.endswith('"'):
            return text
        if text.isdigit():
            return int(text)
        return text
