lexer grammar Cgrammer;

// 变量规则
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [-+]?([1-9][0-9]* | '0');
FLOAT: [0-9]+.[0-9]+;
CHAR: '\''[a-zA-Z_]'\'';

ANNOUNCER: 'int' | 'float' | 'char';
PTR: ANNOUNCER'*';
ARRAY: ANNOUNCER'[]';

// 关键字规则
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
MULTIPLYorREFERENCE: '*';
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