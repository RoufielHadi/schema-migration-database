grammar DBSchema;

// Entry point for a migration file
migrationFile
  : (migrationDecl | schemaDecl)* EOF
  ;

// migration <id> { desc "..." author <name> db <target> schema <name> { ... } }
migrationDecl
  : MIGRATION migrationId LBRACE
      DESC STRING
      AUTHOR author=ID
      DB db=ID
      schemaDecl
    RBRACE
  ;

// Identifier for migration version/id
migrationId
  : ID
  ;

// schema <name> { table|enum|seed ... }
schemaDecl
  : SCHEMA schemaBody
  ;

schemaBody
  : ID LBRACE schemaMember* RBRACE
  ;

schemaMember
  : tableDecl
  | enumDecl
  | seedDecl
  ;

// table <name> { columnDecl* fkDecl* indexDecl* }
tableDecl
  : TABLE ID LBRACE tableBody* RBRACE
  ;

tableBody
  : columnDecl
  | fkDecl
  | indexDecl
  ;

// columnDecl: name typeSpec columnAttr* ;
columnDecl
  : ID typeSpec columnAttr* SEMI? 
  ;

// typeSpec: ID ('(' INT ')')?
typeSpec
  : ID (LPAREN INT RPAREN)?
  ;

// column attributes: primary | unique | not null | default literal
columnAttr
  : PRIMARY
  | UNIQUE
  | NOT NULL
  | DEFAULT literal
  ;

// fkDecl: fk '(' ID ')' references ID '(' ID ')'
fkDecl
  : FK LPAREN ID RPAREN REFERENCES ID LPAREN ID RPAREN SEMI?
  ;

// indexDecl: index <name> '(' ID (',' ID)* ')' ('unique')?
indexDecl
  : INDEX ID LPAREN idList RPAREN (UNIQUE)? SEMI?
  ;

idList
  : ID (COMMA ID)*
  ;

// enumDecl: enum ID '{' ID (',' ID)* '}'
enumDecl
  : ENUM ID LBRACE ID (COMMA ID)* RBRACE
  ;

// seedDecl: seed tableName { (field=literal (',' field=literal)*) ; }+
seedDecl
  : SEED ID LBRACE seedRow+ RBRACE
  ;

seedRow
  : seedField (COMMA seedField)* SEMI
  ;

seedField
  : ID EQ literal
  ;

// literal: STRING | INT | functionCall | ID (e.g., enum values like PENDING)
literal
  : STRING
  | INT
  | functionCall
  | ID
  ;

// function call literal: now(), uuid_generate_v4(), etc.
functionCall
  : ID LPAREN (literal (COMMA literal)*)? RPAREN
  ;

// LEXER
MIGRATION  : 'migration' ;
DESC       : 'desc' ;
AUTHOR     : 'author' ;
DB         : 'db' ;
SCHEMA     : 'schema' ;
TABLE      : 'table' ;
ENUM       : 'enum' ;
SEED       : 'seed' ;
FK         : 'fk' ;
REFERENCES : 'references' ;
INDEX      : 'index' ;
UNIQUE     : 'unique' ;
PRIMARY    : 'primary' ;
NOT        : 'not' ;
NULL       : 'null' ;
DEFAULT    : 'default' ;

LBRACE : '{' ;
RBRACE : '}' ;
LPAREN : '(' ;
RPAREN : ')' ;
COMMA  : ',' ;
SEMI   : ';' ;
EQ     : '=' ;

ID      : [a-zA-Z_] [a-zA-Z_0-9]* ;
INT     : [0-9]+ ;
STRING  : '"' (ESC | ~["\\\r\n])* '"' ;
fragment ESC : '\\' ["\\/bfnrt] ;
WS      : [ \t\r\n]+ -> skip ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT: '/*' .*? '*/' -> skip ;
