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
IF: 'if';
ELSE: 'else';
FOR: 'for';
// ...

// 运算符规则
ASSIGN: '=';
PLUS: '+';
MINUS: '-';
MULTIPLE: '*';
DIVIDE: '/';
LOAD: '&';
// ...

// 分隔符规则
SEMICOLON: ';';
COMMA: ',';
// ...

// 忽略空白字符和注释
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]*;