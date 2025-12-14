# Generated from grammar/DBSchema.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DBSchemaParser import DBSchemaParser
else:
    from DBSchemaParser import DBSchemaParser

# This class defines a complete generic visitor for a parse tree produced by DBSchemaParser.

class DBSchemaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DBSchemaParser#migrationFile.
    def visitMigrationFile(self, ctx:DBSchemaParser.MigrationFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DBSchemaParser#migrationDecl.
    def visitMigrationDecl(self, ctx:DBSchemaParser.MigrationDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DBSchemaParser#migrationId.
    def visitMigrationId(self, ctx:DBSchemaParser.MigrationIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DBSchemaParser#schemaDecl.
    def visitSchemaDecl(self, ctx:DBSchemaParser.SchemaDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DBSchemaParser#schemaBody.
    def visitSchemaBody(self, ctx:DBSchemaParser.SchemaBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DBSchemaParser#schemaMember.
    def visitSchemaMember(self, ctx:DBSchemaParser.SchemaMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DBSchemaParser#tableDecl.
    def visitTableDecl(self, ctx:DBSchemaParser.TableDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DBSchemaParser#tableBody.
    def visitTableBody(self, ctx:DBSchemaParser.TableBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DBSchemaParser#columnDecl.
    def visitColumnDecl(self, ctx:DBSchemaParser.ColumnDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DBSchemaParser#typeSpec.
    def visitTypeSpec(self, ctx:DBSchemaParser.TypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DBSchemaParser#columnAttr.
    def visitColumnAttr(self, ctx:DBSchemaParser.ColumnAttrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DBSchemaParser#fkDecl.
    def visitFkDecl(self, ctx:DBSchemaParser.FkDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DBSchemaParser#indexDecl.
    def visitIndexDecl(self, ctx:DBSchemaParser.IndexDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DBSchemaParser#idList.
    def visitIdList(self, ctx:DBSchemaParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DBSchemaParser#enumDecl.
    def visitEnumDecl(self, ctx:DBSchemaParser.EnumDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DBSchemaParser#seedDecl.
    def visitSeedDecl(self, ctx:DBSchemaParser.SeedDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DBSchemaParser#seedRow.
    def visitSeedRow(self, ctx:DBSchemaParser.SeedRowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DBSchemaParser#seedField.
    def visitSeedField(self, ctx:DBSchemaParser.SeedFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DBSchemaParser#literal.
    def visitLiteral(self, ctx:DBSchemaParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DBSchemaParser#functionCall.
    def visitFunctionCall(self, ctx:DBSchemaParser.FunctionCallContext):
        return self.visitChildren(ctx)



del DBSchemaParser