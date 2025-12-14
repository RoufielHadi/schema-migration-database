# Generated from grammar/DBSchema.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DBSchemaParser import DBSchemaParser
else:
    from DBSchemaParser import DBSchemaParser

# This class defines a complete listener for a parse tree produced by DBSchemaParser.
class DBSchemaListener(ParseTreeListener):

    # Enter a parse tree produced by DBSchemaParser#migrationFile.
    def enterMigrationFile(self, ctx:DBSchemaParser.MigrationFileContext):
        pass

    # Exit a parse tree produced by DBSchemaParser#migrationFile.
    def exitMigrationFile(self, ctx:DBSchemaParser.MigrationFileContext):
        pass


    # Enter a parse tree produced by DBSchemaParser#migrationDecl.
    def enterMigrationDecl(self, ctx:DBSchemaParser.MigrationDeclContext):
        pass

    # Exit a parse tree produced by DBSchemaParser#migrationDecl.
    def exitMigrationDecl(self, ctx:DBSchemaParser.MigrationDeclContext):
        pass


    # Enter a parse tree produced by DBSchemaParser#migrationId.
    def enterMigrationId(self, ctx:DBSchemaParser.MigrationIdContext):
        pass

    # Exit a parse tree produced by DBSchemaParser#migrationId.
    def exitMigrationId(self, ctx:DBSchemaParser.MigrationIdContext):
        pass


    # Enter a parse tree produced by DBSchemaParser#schemaDecl.
    def enterSchemaDecl(self, ctx:DBSchemaParser.SchemaDeclContext):
        pass

    # Exit a parse tree produced by DBSchemaParser#schemaDecl.
    def exitSchemaDecl(self, ctx:DBSchemaParser.SchemaDeclContext):
        pass


    # Enter a parse tree produced by DBSchemaParser#schemaBody.
    def enterSchemaBody(self, ctx:DBSchemaParser.SchemaBodyContext):
        pass

    # Exit a parse tree produced by DBSchemaParser#schemaBody.
    def exitSchemaBody(self, ctx:DBSchemaParser.SchemaBodyContext):
        pass


    # Enter a parse tree produced by DBSchemaParser#schemaMember.
    def enterSchemaMember(self, ctx:DBSchemaParser.SchemaMemberContext):
        pass

    # Exit a parse tree produced by DBSchemaParser#schemaMember.
    def exitSchemaMember(self, ctx:DBSchemaParser.SchemaMemberContext):
        pass


    # Enter a parse tree produced by DBSchemaParser#tableDecl.
    def enterTableDecl(self, ctx:DBSchemaParser.TableDeclContext):
        pass

    # Exit a parse tree produced by DBSchemaParser#tableDecl.
    def exitTableDecl(self, ctx:DBSchemaParser.TableDeclContext):
        pass


    # Enter a parse tree produced by DBSchemaParser#tableBody.
    def enterTableBody(self, ctx:DBSchemaParser.TableBodyContext):
        pass

    # Exit a parse tree produced by DBSchemaParser#tableBody.
    def exitTableBody(self, ctx:DBSchemaParser.TableBodyContext):
        pass


    # Enter a parse tree produced by DBSchemaParser#columnDecl.
    def enterColumnDecl(self, ctx:DBSchemaParser.ColumnDeclContext):
        pass

    # Exit a parse tree produced by DBSchemaParser#columnDecl.
    def exitColumnDecl(self, ctx:DBSchemaParser.ColumnDeclContext):
        pass


    # Enter a parse tree produced by DBSchemaParser#typeSpec.
    def enterTypeSpec(self, ctx:DBSchemaParser.TypeSpecContext):
        pass

    # Exit a parse tree produced by DBSchemaParser#typeSpec.
    def exitTypeSpec(self, ctx:DBSchemaParser.TypeSpecContext):
        pass


    # Enter a parse tree produced by DBSchemaParser#columnAttr.
    def enterColumnAttr(self, ctx:DBSchemaParser.ColumnAttrContext):
        pass

    # Exit a parse tree produced by DBSchemaParser#columnAttr.
    def exitColumnAttr(self, ctx:DBSchemaParser.ColumnAttrContext):
        pass


    # Enter a parse tree produced by DBSchemaParser#fkDecl.
    def enterFkDecl(self, ctx:DBSchemaParser.FkDeclContext):
        pass

    # Exit a parse tree produced by DBSchemaParser#fkDecl.
    def exitFkDecl(self, ctx:DBSchemaParser.FkDeclContext):
        pass


    # Enter a parse tree produced by DBSchemaParser#indexDecl.
    def enterIndexDecl(self, ctx:DBSchemaParser.IndexDeclContext):
        pass

    # Exit a parse tree produced by DBSchemaParser#indexDecl.
    def exitIndexDecl(self, ctx:DBSchemaParser.IndexDeclContext):
        pass


    # Enter a parse tree produced by DBSchemaParser#idList.
    def enterIdList(self, ctx:DBSchemaParser.IdListContext):
        pass

    # Exit a parse tree produced by DBSchemaParser#idList.
    def exitIdList(self, ctx:DBSchemaParser.IdListContext):
        pass


    # Enter a parse tree produced by DBSchemaParser#enumDecl.
    def enterEnumDecl(self, ctx:DBSchemaParser.EnumDeclContext):
        pass

    # Exit a parse tree produced by DBSchemaParser#enumDecl.
    def exitEnumDecl(self, ctx:DBSchemaParser.EnumDeclContext):
        pass


    # Enter a parse tree produced by DBSchemaParser#seedDecl.
    def enterSeedDecl(self, ctx:DBSchemaParser.SeedDeclContext):
        pass

    # Exit a parse tree produced by DBSchemaParser#seedDecl.
    def exitSeedDecl(self, ctx:DBSchemaParser.SeedDeclContext):
        pass


    # Enter a parse tree produced by DBSchemaParser#seedRow.
    def enterSeedRow(self, ctx:DBSchemaParser.SeedRowContext):
        pass

    # Exit a parse tree produced by DBSchemaParser#seedRow.
    def exitSeedRow(self, ctx:DBSchemaParser.SeedRowContext):
        pass


    # Enter a parse tree produced by DBSchemaParser#seedField.
    def enterSeedField(self, ctx:DBSchemaParser.SeedFieldContext):
        pass

    # Exit a parse tree produced by DBSchemaParser#seedField.
    def exitSeedField(self, ctx:DBSchemaParser.SeedFieldContext):
        pass


    # Enter a parse tree produced by DBSchemaParser#literal.
    def enterLiteral(self, ctx:DBSchemaParser.LiteralContext):
        pass

    # Exit a parse tree produced by DBSchemaParser#literal.
    def exitLiteral(self, ctx:DBSchemaParser.LiteralContext):
        pass


    # Enter a parse tree produced by DBSchemaParser#functionCall.
    def enterFunctionCall(self, ctx:DBSchemaParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by DBSchemaParser#functionCall.
    def exitFunctionCall(self, ctx:DBSchemaParser.FunctionCallContext):
        pass



del DBSchemaParser