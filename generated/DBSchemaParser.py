# Generated from grammar/DBSchema.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,29,211,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,5,0,43,8,0,10,0,12,0,46,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,5,4,70,8,
        4,10,4,12,4,73,9,4,1,4,1,4,1,5,1,5,1,5,3,5,80,8,5,1,6,1,6,1,6,1,
        6,5,6,86,8,6,10,6,12,6,89,9,6,1,6,1,6,1,7,1,7,1,7,3,7,96,8,7,1,8,
        1,8,1,8,5,8,101,8,8,10,8,12,8,104,9,8,1,8,3,8,107,8,8,1,9,1,9,1,
        9,1,9,3,9,113,8,9,1,10,1,10,1,10,1,10,1,10,1,10,3,10,121,8,10,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,133,8,11,1,
        12,1,12,1,12,1,12,1,12,1,12,3,12,141,8,12,1,12,3,12,144,8,12,1,13,
        1,13,1,13,5,13,149,8,13,10,13,12,13,152,9,13,1,14,1,14,1,14,1,14,
        1,14,1,14,5,14,160,8,14,10,14,12,14,163,9,14,1,14,1,14,1,15,1,15,
        1,15,1,15,4,15,171,8,15,11,15,12,15,172,1,15,1,15,1,16,1,16,1,16,
        5,16,180,8,16,10,16,12,16,183,9,16,1,16,1,16,1,17,1,17,1,17,1,17,
        1,18,1,18,1,18,1,18,3,18,195,8,18,1,19,1,19,1,19,1,19,1,19,5,19,
        202,8,19,10,19,12,19,205,9,19,3,19,207,8,19,1,19,1,19,1,19,0,0,20,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,0,0,216,0,
        44,1,0,0,0,2,49,1,0,0,0,4,61,1,0,0,0,6,63,1,0,0,0,8,66,1,0,0,0,10,
        79,1,0,0,0,12,81,1,0,0,0,14,95,1,0,0,0,16,97,1,0,0,0,18,108,1,0,
        0,0,20,120,1,0,0,0,22,122,1,0,0,0,24,134,1,0,0,0,26,145,1,0,0,0,
        28,153,1,0,0,0,30,166,1,0,0,0,32,176,1,0,0,0,34,186,1,0,0,0,36,194,
        1,0,0,0,38,196,1,0,0,0,40,43,3,2,1,0,41,43,3,6,3,0,42,40,1,0,0,0,
        42,41,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,47,1,
        0,0,0,46,44,1,0,0,0,47,48,5,0,0,1,48,1,1,0,0,0,49,50,5,1,0,0,50,
        51,3,4,2,0,51,52,5,17,0,0,52,53,5,2,0,0,53,54,5,26,0,0,54,55,5,3,
        0,0,55,56,5,24,0,0,56,57,5,4,0,0,57,58,5,24,0,0,58,59,3,6,3,0,59,
        60,5,18,0,0,60,3,1,0,0,0,61,62,5,24,0,0,62,5,1,0,0,0,63,64,5,5,0,
        0,64,65,3,8,4,0,65,7,1,0,0,0,66,67,5,24,0,0,67,71,5,17,0,0,68,70,
        3,10,5,0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,
        72,74,1,0,0,0,73,71,1,0,0,0,74,75,5,18,0,0,75,9,1,0,0,0,76,80,3,
        12,6,0,77,80,3,28,14,0,78,80,3,30,15,0,79,76,1,0,0,0,79,77,1,0,0,
        0,79,78,1,0,0,0,80,11,1,0,0,0,81,82,5,6,0,0,82,83,5,24,0,0,83,87,
        5,17,0,0,84,86,3,14,7,0,85,84,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,
        0,87,88,1,0,0,0,88,90,1,0,0,0,89,87,1,0,0,0,90,91,5,18,0,0,91,13,
        1,0,0,0,92,96,3,16,8,0,93,96,3,22,11,0,94,96,3,24,12,0,95,92,1,0,
        0,0,95,93,1,0,0,0,95,94,1,0,0,0,96,15,1,0,0,0,97,98,5,24,0,0,98,
        102,3,18,9,0,99,101,3,20,10,0,100,99,1,0,0,0,101,104,1,0,0,0,102,
        100,1,0,0,0,102,103,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,105,
        107,5,22,0,0,106,105,1,0,0,0,106,107,1,0,0,0,107,17,1,0,0,0,108,
        112,5,24,0,0,109,110,5,19,0,0,110,111,5,25,0,0,111,113,5,20,0,0,
        112,109,1,0,0,0,112,113,1,0,0,0,113,19,1,0,0,0,114,121,5,13,0,0,
        115,121,5,12,0,0,116,117,5,14,0,0,117,121,5,15,0,0,118,119,5,16,
        0,0,119,121,3,36,18,0,120,114,1,0,0,0,120,115,1,0,0,0,120,116,1,
        0,0,0,120,118,1,0,0,0,121,21,1,0,0,0,122,123,5,9,0,0,123,124,5,19,
        0,0,124,125,5,24,0,0,125,126,5,20,0,0,126,127,5,10,0,0,127,128,5,
        24,0,0,128,129,5,19,0,0,129,130,5,24,0,0,130,132,5,20,0,0,131,133,
        5,22,0,0,132,131,1,0,0,0,132,133,1,0,0,0,133,23,1,0,0,0,134,135,
        5,11,0,0,135,136,5,24,0,0,136,137,5,19,0,0,137,138,3,26,13,0,138,
        140,5,20,0,0,139,141,5,12,0,0,140,139,1,0,0,0,140,141,1,0,0,0,141,
        143,1,0,0,0,142,144,5,22,0,0,143,142,1,0,0,0,143,144,1,0,0,0,144,
        25,1,0,0,0,145,150,5,24,0,0,146,147,5,21,0,0,147,149,5,24,0,0,148,
        146,1,0,0,0,149,152,1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,
        27,1,0,0,0,152,150,1,0,0,0,153,154,5,7,0,0,154,155,5,24,0,0,155,
        156,5,17,0,0,156,161,5,24,0,0,157,158,5,21,0,0,158,160,5,24,0,0,
        159,157,1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,
        162,164,1,0,0,0,163,161,1,0,0,0,164,165,5,18,0,0,165,29,1,0,0,0,
        166,167,5,8,0,0,167,168,5,24,0,0,168,170,5,17,0,0,169,171,3,32,16,
        0,170,169,1,0,0,0,171,172,1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,
        0,173,174,1,0,0,0,174,175,5,18,0,0,175,31,1,0,0,0,176,181,3,34,17,
        0,177,178,5,21,0,0,178,180,3,34,17,0,179,177,1,0,0,0,180,183,1,0,
        0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,184,1,0,0,0,183,181,1,0,
        0,0,184,185,5,22,0,0,185,33,1,0,0,0,186,187,5,24,0,0,187,188,5,23,
        0,0,188,189,3,36,18,0,189,35,1,0,0,0,190,195,5,26,0,0,191,195,5,
        25,0,0,192,195,3,38,19,0,193,195,5,24,0,0,194,190,1,0,0,0,194,191,
        1,0,0,0,194,192,1,0,0,0,194,193,1,0,0,0,195,37,1,0,0,0,196,197,5,
        24,0,0,197,206,5,19,0,0,198,203,3,36,18,0,199,200,5,21,0,0,200,202,
        3,36,18,0,201,199,1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,204,
        1,0,0,0,204,207,1,0,0,0,205,203,1,0,0,0,206,198,1,0,0,0,206,207,
        1,0,0,0,207,208,1,0,0,0,208,209,5,20,0,0,209,39,1,0,0,0,20,42,44,
        71,79,87,95,102,106,112,120,132,140,143,150,161,172,181,194,203,
        206
    ]

class DBSchemaParser ( Parser ):

    grammarFileName = "DBSchema.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'migration'", "'desc'", "'author'", "'db'", 
                     "'schema'", "'table'", "'enum'", "'seed'", "'fk'", 
                     "'references'", "'index'", "'unique'", "'primary'", 
                     "'not'", "'null'", "'default'", "'{'", "'}'", "'('", 
                     "')'", "','", "';'", "'='" ]

    symbolicNames = [ "<INVALID>", "MIGRATION", "DESC", "AUTHOR", "DB", 
                      "SCHEMA", "TABLE", "ENUM", "SEED", "FK", "REFERENCES", 
                      "INDEX", "UNIQUE", "PRIMARY", "NOT", "NULL", "DEFAULT", 
                      "LBRACE", "RBRACE", "LPAREN", "RPAREN", "COMMA", "SEMI", 
                      "EQ", "ID", "INT", "STRING", "WS", "LINE_COMMENT", 
                      "BLOCK_COMMENT" ]

    RULE_migrationFile = 0
    RULE_migrationDecl = 1
    RULE_migrationId = 2
    RULE_schemaDecl = 3
    RULE_schemaBody = 4
    RULE_schemaMember = 5
    RULE_tableDecl = 6
    RULE_tableBody = 7
    RULE_columnDecl = 8
    RULE_typeSpec = 9
    RULE_columnAttr = 10
    RULE_fkDecl = 11
    RULE_indexDecl = 12
    RULE_idList = 13
    RULE_enumDecl = 14
    RULE_seedDecl = 15
    RULE_seedRow = 16
    RULE_seedField = 17
    RULE_literal = 18
    RULE_functionCall = 19

    ruleNames =  [ "migrationFile", "migrationDecl", "migrationId", "schemaDecl", 
                   "schemaBody", "schemaMember", "tableDecl", "tableBody", 
                   "columnDecl", "typeSpec", "columnAttr", "fkDecl", "indexDecl", 
                   "idList", "enumDecl", "seedDecl", "seedRow", "seedField", 
                   "literal", "functionCall" ]

    EOF = Token.EOF
    MIGRATION=1
    DESC=2
    AUTHOR=3
    DB=4
    SCHEMA=5
    TABLE=6
    ENUM=7
    SEED=8
    FK=9
    REFERENCES=10
    INDEX=11
    UNIQUE=12
    PRIMARY=13
    NOT=14
    NULL=15
    DEFAULT=16
    LBRACE=17
    RBRACE=18
    LPAREN=19
    RPAREN=20
    COMMA=21
    SEMI=22
    EQ=23
    ID=24
    INT=25
    STRING=26
    WS=27
    LINE_COMMENT=28
    BLOCK_COMMENT=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MigrationFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DBSchemaParser.EOF, 0)

        def migrationDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DBSchemaParser.MigrationDeclContext)
            else:
                return self.getTypedRuleContext(DBSchemaParser.MigrationDeclContext,i)


        def schemaDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DBSchemaParser.SchemaDeclContext)
            else:
                return self.getTypedRuleContext(DBSchemaParser.SchemaDeclContext,i)


        def getRuleIndex(self):
            return DBSchemaParser.RULE_migrationFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMigrationFile" ):
                listener.enterMigrationFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMigrationFile" ):
                listener.exitMigrationFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMigrationFile" ):
                return visitor.visitMigrationFile(self)
            else:
                return visitor.visitChildren(self)




    def migrationFile(self):

        localctx = DBSchemaParser.MigrationFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_migrationFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==5:
                self.state = 42
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 40
                    self.migrationDecl()
                    pass
                elif token in [5]:
                    self.state = 41
                    self.schemaDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 47
            self.match(DBSchemaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MigrationDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.author = None # Token
            self.db = None # Token

        def MIGRATION(self):
            return self.getToken(DBSchemaParser.MIGRATION, 0)

        def migrationId(self):
            return self.getTypedRuleContext(DBSchemaParser.MigrationIdContext,0)


        def LBRACE(self):
            return self.getToken(DBSchemaParser.LBRACE, 0)

        def DESC(self):
            return self.getToken(DBSchemaParser.DESC, 0)

        def STRING(self):
            return self.getToken(DBSchemaParser.STRING, 0)

        def AUTHOR(self):
            return self.getToken(DBSchemaParser.AUTHOR, 0)

        def DB(self):
            return self.getToken(DBSchemaParser.DB, 0)

        def schemaDecl(self):
            return self.getTypedRuleContext(DBSchemaParser.SchemaDeclContext,0)


        def RBRACE(self):
            return self.getToken(DBSchemaParser.RBRACE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DBSchemaParser.ID)
            else:
                return self.getToken(DBSchemaParser.ID, i)

        def getRuleIndex(self):
            return DBSchemaParser.RULE_migrationDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMigrationDecl" ):
                listener.enterMigrationDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMigrationDecl" ):
                listener.exitMigrationDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMigrationDecl" ):
                return visitor.visitMigrationDecl(self)
            else:
                return visitor.visitChildren(self)




    def migrationDecl(self):

        localctx = DBSchemaParser.MigrationDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_migrationDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(DBSchemaParser.MIGRATION)
            self.state = 50
            self.migrationId()
            self.state = 51
            self.match(DBSchemaParser.LBRACE)
            self.state = 52
            self.match(DBSchemaParser.DESC)
            self.state = 53
            self.match(DBSchemaParser.STRING)
            self.state = 54
            self.match(DBSchemaParser.AUTHOR)
            self.state = 55
            localctx.author = self.match(DBSchemaParser.ID)
            self.state = 56
            self.match(DBSchemaParser.DB)
            self.state = 57
            localctx.db = self.match(DBSchemaParser.ID)
            self.state = 58
            self.schemaDecl()
            self.state = 59
            self.match(DBSchemaParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MigrationIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DBSchemaParser.ID, 0)

        def getRuleIndex(self):
            return DBSchemaParser.RULE_migrationId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMigrationId" ):
                listener.enterMigrationId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMigrationId" ):
                listener.exitMigrationId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMigrationId" ):
                return visitor.visitMigrationId(self)
            else:
                return visitor.visitChildren(self)




    def migrationId(self):

        localctx = DBSchemaParser.MigrationIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_migrationId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(DBSchemaParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SchemaDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCHEMA(self):
            return self.getToken(DBSchemaParser.SCHEMA, 0)

        def schemaBody(self):
            return self.getTypedRuleContext(DBSchemaParser.SchemaBodyContext,0)


        def getRuleIndex(self):
            return DBSchemaParser.RULE_schemaDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSchemaDecl" ):
                listener.enterSchemaDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSchemaDecl" ):
                listener.exitSchemaDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSchemaDecl" ):
                return visitor.visitSchemaDecl(self)
            else:
                return visitor.visitChildren(self)




    def schemaDecl(self):

        localctx = DBSchemaParser.SchemaDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_schemaDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(DBSchemaParser.SCHEMA)
            self.state = 64
            self.schemaBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SchemaBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DBSchemaParser.ID, 0)

        def LBRACE(self):
            return self.getToken(DBSchemaParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(DBSchemaParser.RBRACE, 0)

        def schemaMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DBSchemaParser.SchemaMemberContext)
            else:
                return self.getTypedRuleContext(DBSchemaParser.SchemaMemberContext,i)


        def getRuleIndex(self):
            return DBSchemaParser.RULE_schemaBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSchemaBody" ):
                listener.enterSchemaBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSchemaBody" ):
                listener.exitSchemaBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSchemaBody" ):
                return visitor.visitSchemaBody(self)
            else:
                return visitor.visitChildren(self)




    def schemaBody(self):

        localctx = DBSchemaParser.SchemaBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_schemaBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(DBSchemaParser.ID)
            self.state = 67
            self.match(DBSchemaParser.LBRACE)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0):
                self.state = 68
                self.schemaMember()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(DBSchemaParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SchemaMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableDecl(self):
            return self.getTypedRuleContext(DBSchemaParser.TableDeclContext,0)


        def enumDecl(self):
            return self.getTypedRuleContext(DBSchemaParser.EnumDeclContext,0)


        def seedDecl(self):
            return self.getTypedRuleContext(DBSchemaParser.SeedDeclContext,0)


        def getRuleIndex(self):
            return DBSchemaParser.RULE_schemaMember

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSchemaMember" ):
                listener.enterSchemaMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSchemaMember" ):
                listener.exitSchemaMember(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSchemaMember" ):
                return visitor.visitSchemaMember(self)
            else:
                return visitor.visitChildren(self)




    def schemaMember(self):

        localctx = DBSchemaParser.SchemaMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_schemaMember)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.tableDecl()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.enumDecl()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.seedDecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TABLE(self):
            return self.getToken(DBSchemaParser.TABLE, 0)

        def ID(self):
            return self.getToken(DBSchemaParser.ID, 0)

        def LBRACE(self):
            return self.getToken(DBSchemaParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(DBSchemaParser.RBRACE, 0)

        def tableBody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DBSchemaParser.TableBodyContext)
            else:
                return self.getTypedRuleContext(DBSchemaParser.TableBodyContext,i)


        def getRuleIndex(self):
            return DBSchemaParser.RULE_tableDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableDecl" ):
                listener.enterTableDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableDecl" ):
                listener.exitTableDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableDecl" ):
                return visitor.visitTableDecl(self)
            else:
                return visitor.visitChildren(self)




    def tableDecl(self):

        localctx = DBSchemaParser.TableDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tableDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(DBSchemaParser.TABLE)
            self.state = 82
            self.match(DBSchemaParser.ID)
            self.state = 83
            self.match(DBSchemaParser.LBRACE)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16779776) != 0):
                self.state = 84
                self.tableBody()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.match(DBSchemaParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnDecl(self):
            return self.getTypedRuleContext(DBSchemaParser.ColumnDeclContext,0)


        def fkDecl(self):
            return self.getTypedRuleContext(DBSchemaParser.FkDeclContext,0)


        def indexDecl(self):
            return self.getTypedRuleContext(DBSchemaParser.IndexDeclContext,0)


        def getRuleIndex(self):
            return DBSchemaParser.RULE_tableBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableBody" ):
                listener.enterTableBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableBody" ):
                listener.exitTableBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableBody" ):
                return visitor.visitTableBody(self)
            else:
                return visitor.visitChildren(self)




    def tableBody(self):

        localctx = DBSchemaParser.TableBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tableBody)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.columnDecl()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.fkDecl()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.indexDecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DBSchemaParser.ID, 0)

        def typeSpec(self):
            return self.getTypedRuleContext(DBSchemaParser.TypeSpecContext,0)


        def columnAttr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DBSchemaParser.ColumnAttrContext)
            else:
                return self.getTypedRuleContext(DBSchemaParser.ColumnAttrContext,i)


        def SEMI(self):
            return self.getToken(DBSchemaParser.SEMI, 0)

        def getRuleIndex(self):
            return DBSchemaParser.RULE_columnDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnDecl" ):
                listener.enterColumnDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnDecl" ):
                listener.exitColumnDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnDecl" ):
                return visitor.visitColumnDecl(self)
            else:
                return visitor.visitChildren(self)




    def columnDecl(self):

        localctx = DBSchemaParser.ColumnDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_columnDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(DBSchemaParser.ID)
            self.state = 98
            self.typeSpec()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 94208) != 0):
                self.state = 99
                self.columnAttr()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 105
                self.match(DBSchemaParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DBSchemaParser.ID, 0)

        def LPAREN(self):
            return self.getToken(DBSchemaParser.LPAREN, 0)

        def INT(self):
            return self.getToken(DBSchemaParser.INT, 0)

        def RPAREN(self):
            return self.getToken(DBSchemaParser.RPAREN, 0)

        def getRuleIndex(self):
            return DBSchemaParser.RULE_typeSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpec" ):
                listener.enterTypeSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpec" ):
                listener.exitTypeSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSpec" ):
                return visitor.visitTypeSpec(self)
            else:
                return visitor.visitChildren(self)




    def typeSpec(self):

        localctx = DBSchemaParser.TypeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_typeSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(DBSchemaParser.ID)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 109
                self.match(DBSchemaParser.LPAREN)
                self.state = 110
                self.match(DBSchemaParser.INT)
                self.state = 111
                self.match(DBSchemaParser.RPAREN)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnAttrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRIMARY(self):
            return self.getToken(DBSchemaParser.PRIMARY, 0)

        def UNIQUE(self):
            return self.getToken(DBSchemaParser.UNIQUE, 0)

        def NOT(self):
            return self.getToken(DBSchemaParser.NOT, 0)

        def NULL(self):
            return self.getToken(DBSchemaParser.NULL, 0)

        def DEFAULT(self):
            return self.getToken(DBSchemaParser.DEFAULT, 0)

        def literal(self):
            return self.getTypedRuleContext(DBSchemaParser.LiteralContext,0)


        def getRuleIndex(self):
            return DBSchemaParser.RULE_columnAttr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnAttr" ):
                listener.enterColumnAttr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnAttr" ):
                listener.exitColumnAttr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnAttr" ):
                return visitor.visitColumnAttr(self)
            else:
                return visitor.visitChildren(self)




    def columnAttr(self):

        localctx = DBSchemaParser.ColumnAttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_columnAttr)
        try:
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.match(DBSchemaParser.PRIMARY)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.match(DBSchemaParser.UNIQUE)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 116
                self.match(DBSchemaParser.NOT)
                self.state = 117
                self.match(DBSchemaParser.NULL)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 118
                self.match(DBSchemaParser.DEFAULT)
                self.state = 119
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FkDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FK(self):
            return self.getToken(DBSchemaParser.FK, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(DBSchemaParser.LPAREN)
            else:
                return self.getToken(DBSchemaParser.LPAREN, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DBSchemaParser.ID)
            else:
                return self.getToken(DBSchemaParser.ID, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(DBSchemaParser.RPAREN)
            else:
                return self.getToken(DBSchemaParser.RPAREN, i)

        def REFERENCES(self):
            return self.getToken(DBSchemaParser.REFERENCES, 0)

        def SEMI(self):
            return self.getToken(DBSchemaParser.SEMI, 0)

        def getRuleIndex(self):
            return DBSchemaParser.RULE_fkDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFkDecl" ):
                listener.enterFkDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFkDecl" ):
                listener.exitFkDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFkDecl" ):
                return visitor.visitFkDecl(self)
            else:
                return visitor.visitChildren(self)




    def fkDecl(self):

        localctx = DBSchemaParser.FkDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_fkDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(DBSchemaParser.FK)
            self.state = 123
            self.match(DBSchemaParser.LPAREN)
            self.state = 124
            self.match(DBSchemaParser.ID)
            self.state = 125
            self.match(DBSchemaParser.RPAREN)
            self.state = 126
            self.match(DBSchemaParser.REFERENCES)
            self.state = 127
            self.match(DBSchemaParser.ID)
            self.state = 128
            self.match(DBSchemaParser.LPAREN)
            self.state = 129
            self.match(DBSchemaParser.ID)
            self.state = 130
            self.match(DBSchemaParser.RPAREN)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 131
                self.match(DBSchemaParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDEX(self):
            return self.getToken(DBSchemaParser.INDEX, 0)

        def ID(self):
            return self.getToken(DBSchemaParser.ID, 0)

        def LPAREN(self):
            return self.getToken(DBSchemaParser.LPAREN, 0)

        def idList(self):
            return self.getTypedRuleContext(DBSchemaParser.IdListContext,0)


        def RPAREN(self):
            return self.getToken(DBSchemaParser.RPAREN, 0)

        def UNIQUE(self):
            return self.getToken(DBSchemaParser.UNIQUE, 0)

        def SEMI(self):
            return self.getToken(DBSchemaParser.SEMI, 0)

        def getRuleIndex(self):
            return DBSchemaParser.RULE_indexDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexDecl" ):
                listener.enterIndexDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexDecl" ):
                listener.exitIndexDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexDecl" ):
                return visitor.visitIndexDecl(self)
            else:
                return visitor.visitChildren(self)




    def indexDecl(self):

        localctx = DBSchemaParser.IndexDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_indexDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(DBSchemaParser.INDEX)
            self.state = 135
            self.match(DBSchemaParser.ID)
            self.state = 136
            self.match(DBSchemaParser.LPAREN)
            self.state = 137
            self.idList()
            self.state = 138
            self.match(DBSchemaParser.RPAREN)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 139
                self.match(DBSchemaParser.UNIQUE)


            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 142
                self.match(DBSchemaParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DBSchemaParser.ID)
            else:
                return self.getToken(DBSchemaParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DBSchemaParser.COMMA)
            else:
                return self.getToken(DBSchemaParser.COMMA, i)

        def getRuleIndex(self):
            return DBSchemaParser.RULE_idList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdList" ):
                listener.enterIdList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdList" ):
                listener.exitIdList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdList" ):
                return visitor.visitIdList(self)
            else:
                return visitor.visitChildren(self)




    def idList(self):

        localctx = DBSchemaParser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(DBSchemaParser.ID)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 146
                self.match(DBSchemaParser.COMMA)
                self.state = 147
                self.match(DBSchemaParser.ID)
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENUM(self):
            return self.getToken(DBSchemaParser.ENUM, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DBSchemaParser.ID)
            else:
                return self.getToken(DBSchemaParser.ID, i)

        def LBRACE(self):
            return self.getToken(DBSchemaParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(DBSchemaParser.RBRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DBSchemaParser.COMMA)
            else:
                return self.getToken(DBSchemaParser.COMMA, i)

        def getRuleIndex(self):
            return DBSchemaParser.RULE_enumDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumDecl" ):
                listener.enterEnumDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumDecl" ):
                listener.exitEnumDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumDecl" ):
                return visitor.visitEnumDecl(self)
            else:
                return visitor.visitChildren(self)




    def enumDecl(self):

        localctx = DBSchemaParser.EnumDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_enumDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(DBSchemaParser.ENUM)
            self.state = 154
            self.match(DBSchemaParser.ID)
            self.state = 155
            self.match(DBSchemaParser.LBRACE)
            self.state = 156
            self.match(DBSchemaParser.ID)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 157
                self.match(DBSchemaParser.COMMA)
                self.state = 158
                self.match(DBSchemaParser.ID)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 164
            self.match(DBSchemaParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeedDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEED(self):
            return self.getToken(DBSchemaParser.SEED, 0)

        def ID(self):
            return self.getToken(DBSchemaParser.ID, 0)

        def LBRACE(self):
            return self.getToken(DBSchemaParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(DBSchemaParser.RBRACE, 0)

        def seedRow(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DBSchemaParser.SeedRowContext)
            else:
                return self.getTypedRuleContext(DBSchemaParser.SeedRowContext,i)


        def getRuleIndex(self):
            return DBSchemaParser.RULE_seedDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeedDecl" ):
                listener.enterSeedDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeedDecl" ):
                listener.exitSeedDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeedDecl" ):
                return visitor.visitSeedDecl(self)
            else:
                return visitor.visitChildren(self)




    def seedDecl(self):

        localctx = DBSchemaParser.SeedDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_seedDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(DBSchemaParser.SEED)
            self.state = 167
            self.match(DBSchemaParser.ID)
            self.state = 168
            self.match(DBSchemaParser.LBRACE)
            self.state = 170 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 169
                self.seedRow()
                self.state = 172 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==24):
                    break

            self.state = 174
            self.match(DBSchemaParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeedRowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def seedField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DBSchemaParser.SeedFieldContext)
            else:
                return self.getTypedRuleContext(DBSchemaParser.SeedFieldContext,i)


        def SEMI(self):
            return self.getToken(DBSchemaParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DBSchemaParser.COMMA)
            else:
                return self.getToken(DBSchemaParser.COMMA, i)

        def getRuleIndex(self):
            return DBSchemaParser.RULE_seedRow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeedRow" ):
                listener.enterSeedRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeedRow" ):
                listener.exitSeedRow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeedRow" ):
                return visitor.visitSeedRow(self)
            else:
                return visitor.visitChildren(self)




    def seedRow(self):

        localctx = DBSchemaParser.SeedRowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_seedRow)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.seedField()
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 177
                self.match(DBSchemaParser.COMMA)
                self.state = 178
                self.seedField()
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 184
            self.match(DBSchemaParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeedFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DBSchemaParser.ID, 0)

        def EQ(self):
            return self.getToken(DBSchemaParser.EQ, 0)

        def literal(self):
            return self.getTypedRuleContext(DBSchemaParser.LiteralContext,0)


        def getRuleIndex(self):
            return DBSchemaParser.RULE_seedField

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeedField" ):
                listener.enterSeedField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeedField" ):
                listener.exitSeedField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeedField" ):
                return visitor.visitSeedField(self)
            else:
                return visitor.visitChildren(self)




    def seedField(self):

        localctx = DBSchemaParser.SeedFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_seedField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(DBSchemaParser.ID)
            self.state = 187
            self.match(DBSchemaParser.EQ)
            self.state = 188
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(DBSchemaParser.STRING, 0)

        def INT(self):
            return self.getToken(DBSchemaParser.INT, 0)

        def functionCall(self):
            return self.getTypedRuleContext(DBSchemaParser.FunctionCallContext,0)


        def ID(self):
            return self.getToken(DBSchemaParser.ID, 0)

        def getRuleIndex(self):
            return DBSchemaParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = DBSchemaParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_literal)
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.match(DBSchemaParser.STRING)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.match(DBSchemaParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 192
                self.functionCall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 193
                self.match(DBSchemaParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DBSchemaParser.ID, 0)

        def LPAREN(self):
            return self.getToken(DBSchemaParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(DBSchemaParser.RPAREN, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DBSchemaParser.LiteralContext)
            else:
                return self.getTypedRuleContext(DBSchemaParser.LiteralContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DBSchemaParser.COMMA)
            else:
                return self.getToken(DBSchemaParser.COMMA, i)

        def getRuleIndex(self):
            return DBSchemaParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = DBSchemaParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(DBSchemaParser.ID)
            self.state = 197
            self.match(DBSchemaParser.LPAREN)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 117440512) != 0):
                self.state = 198
                self.literal()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==21:
                    self.state = 199
                    self.match(DBSchemaParser.COMMA)
                    self.state = 200
                    self.literal()
                    self.state = 205
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 208
            self.match(DBSchemaParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





