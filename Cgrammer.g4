grammar Cgrammer;

variant: IDENTIFIER | FLOAT | INT;
expr: (expr) | expr *;
while: WHILE LROUND expr RROUND;
code_block: expression+;




// 库函数
MEMSET: 'void *memset(void *s, int ch, size_t n)';
STRLEN: 'size_t strlen(const char *_Str)';
PRINTF: 'int printf( const char *restrict format, ... )';
SCANF: 'int scanf(const char *__format, ...)';

// 变量规则
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
FLOAT: [0-9]+'.'[0-9]+;
INT: [-+]?([1-9][0-9]* | '0');
fragment CHARCONTENT: '\''[0rntvbfa?'"\\] | .;
CHAR: '\'' CHARCONTENT '\'';
STRING: '"' CHARCONTENT*? '"';
BOOL: 'true' | 'false';

// 关键字规则
ANNOUNCER: 'int' | 'float' | 'char' | 'bool';
ARRAY: ANNOUNCER'[]';
CONST: 'const';
IF: 'if';
ELSE: 'else';
ELIF: 'else if';
SWITCH: 'switch';
CASE: 'case';
DEFAULT: 'default';
FOR: 'for';
DO: 'do';
WHILE: 'while';
BREAK: 'break';
CONTINUE: 'continue';
RETURN: 'return';
VOID: 'void';

// 运算符规则
EQUAL: '==';
NOTEQUAL: '!=';
ASSIGN: '=';
PLUSASSIGN: '+=';
MINUSASSIGN: '-=';
MULTIPLYASSIGN: '*=';
DIVIDEASSIGN: '/=';
MODULOASSIGN: '%=';
SELFPLUS: '++';
SELFMINUS: '--';
PLUS: '+';
MINUS: '-';
MULTIPLYorREFERENCEorPTR: '*';
DIVIDE: '/';
MODULO: '%';
GEQUAL: '>=';
GREATER: '>';
LEQUAL: '<=';
LESS: '<';
AND: '&&';
OR: '||';
NOT: '!';
BITANDorADDRESS: '&';
BITOR: '|';
BITNOT: '~';
BITXOR: '^';
LSHIFT: '<<';
RSHIFT: '>>';
ELLIPSIS: '...';

// 分隔符规则
SEMICOLON: ';';
COMMA: ',';
LROUND: '(';
RROUND: ')';
LSQUARE: '[';
RSQUARE: ']';
LCURLY: '{';
RCURLY: '}';

// 忽略空白字符和注释
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* '\r'? '\n' -> skip ;