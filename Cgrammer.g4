grammar Cgrammer;

// 库函�?
MEMSET: 'void *memset(void *s, int ch, size_t n)';
STRLEN: 'size_t strlen(const char *_Str)';
PRINTF: 'int printf( const char *restrict format, ... )';
SCANF: 'int scanf(const char *__format, ...)';

// 变量规则
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
FLOATVALUE: [0-9]+'.'[0-9]+;
INTVALUE: [-+]?([1-9][0-9]* | '0');
fragment CHARCONTENT: '\''[0rntvbfa?'"\\] | .;
CHARVALUE: '\'' CHARCONTENT '\'';
STRINGVALUE: '"' CHARCONTENT*? '"';
BOOLVALUE: 'true' | 'false';
MEMSETFUNC: 'memset';
STRLENFUC: 'strlen';
PRINTFFUNC: 'printf';
SCANFFUNC: 'scanf';

// 关键字�?�则
INT: 'int';
FLOAT: 'float';
CHAR: 'char';
BOOL: 'bool;';
STRING: 'string';
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
STRUCT: 'struct';

// 运算符�?�则
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

// 分隔符�?�则
SEMICOLON: ';';
COMMA: ',';
LROUND: '(';
RROUND: ')';
LSQUARE: '[';
RSQUARE: ']';
LCURLY: '{';
RCURLY: '}';
COLON: ':';

// 忽略空白字�?�和注释
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* '\r'? '\n' -> skip ;

// �?法�?�则
// 生成运算表达�?
announcer: INT # int | FLOAT # float | CHAR # char | BOOL # bool | STRING # string;
pointer_flag: MULTIPLYorREFERENCEorPTR | MULTIPLYorREFERENCEorPTR pointer_flag;
type: announcer # originalType| announcer pointer_flag # pointer;
index: LSQUARE INTVALUE RSQUARE;
lib_function: MEMSETFUNC # memset| STRLENFUC # strlen | PRINTFFUNC # printf| SCANFFUNC # scanf;

variable_declaration: type IDENTIFIER (index)*;
params: variable_declaration (COMMA variable_declaration)*;
function_call: IDENTIFIER  | lib_function LROUND params? RROUND;

value: IDENTIFIER # id
        | INTVALUE # int_value
        | FLOATVALUE # float_value
        | CHARVALUE # char_value
        | STRINGVALUE # string_value
        | BOOLVALUE # bool_value
        | function_call # function_call_;
// 生成运算表达�?

// 最高优先级：括�? �?
expr_l0: LROUND expression RROUND # round
           | value #value_;

// 优先�?1: 取内�? 取址 数组
expr_l1_s1: MULTIPLYorREFERENCEorPTR expr_l0 # content_of_
            | BITANDorADDRESS expr_l0 # address_of_
            | expr_l0 LSQUARE expression RSQUARE # array_
            | expr_l0 # next_11;
expr_l1: MULTIPLYorREFERENCEorPTR expr_l1_s1 # content_of
         | BITANDorADDRESS expr_l1_s1 # address_of
         | expr_l1_s1 LSQUARE expression RSQUARE # array
         | expr_l1_s1 # next_1;

// 优先�?2: �?�? �?�? 取非 正号 负号
expr_l2_s1: SELFPLUS expr_l2_s1 # liecrese
            | SELFMINUS expr_l2_s1 # ldecrease
            | NOT expr_l2_s1 # not
            | PLUS expr_l2_s1 # positive
            | MINUS expr_l2_s1 # negative
            | expr_l1 # next_2;

rop_l2: SELFPLUS # rincrease | SELFMINUS # dincrease;
expr_l2: expr_l2_s1 rop_l2*;

// 优先�?3：乘 �? �?
expr_l3_s1: expr_l2 MULTIPLYorREFERENCEorPTR expr_l2 # multiply_
            | expr_l2 DIVIDE expr_l2 # divide_
            | expr_l2 MODULO expr_l2 # modulo_
            | expr_l2 # next_31;

expr_l3: expr_l3_s1 MULTIPLYorREFERENCEorPTR expr_l3 # multiply
         | expr_l3_s1 DIVIDE expr_l3 # divide
         | expr_l3_s1 MODULO expr_l3 # modulo
         | expr_l3_s1 # next_3;

// 优先�?4: �? �?
expr_l4_s1: expr_l3 PLUS expr_l3 # add_
            | expr_l3 MINUS expr_l3 # subtract_
            | expr_l3 # next_41;

expr_l4: expr_l4_s1 PLUS expr_l4 # add
         | expr_l4_s1 MINUS expr_l4 # subtract
         | expr_l4_s1 # next_4;

// 优先�?5: 左移 右移
expr_l5_s1: expr_l4 LSHIFT expr_l4 # lshift_
            | expr_l4 RSHIFT expr_l4 # rshift_
            | expr_l4 # next_51;

expr_l5: expr_l5_s1 LSHIFT expr_l5 # lshift
         | expr_l5_s1 RSHIFT expr_l5 # rshift
         | expr_l5_s1 # next_5;

// 优先�?6: 等于 不等�?
expr_l6_s1: expr_l5 EQUAL expr_l5 # equal_
            | expr_l5 NOTEQUAL expr_l5 # nequal_
            | expr_l5 # next_61;

expr_l6: expr_l6_s1 EQUAL expr_l6 # equal
         | expr_l6_s1 EQUAL expr_l6 # nequal
         | expr_l6_s1 # next_6;

// 优先�?7: 大于(等于) 小于(等于)
expr_l7_s1: expr_l6 GREATER expr_l6 # greater_
            | expr_l6 GEQUAL expr_l6 # gequal_
            | expr_l6 LESS expr_l6 # less_
            | expr_l6 LEQUAL expr_l6 # leuqal_
            | expr_l6 # next_71;

expr_l7: expr_l7_s1 GREATER expr_l7 # greater
         | expr_l7_s1 GEQUAL expr_l7 # gequal
         | expr_l7_s1 LESS expr_l7 # less
         | expr_l7_s1 LEQUAL expr_l7 # leuqal
         | expr_l6_s1 # next_7;

// 优先�?8: 位运�?
expr_l8_s1: BITNOT expr_l8_s1 # bitnot__
            | expr_l7 # next_81;

expr_l8_s2: expr_l8_s1 BITANDorADDRESS expr_l8_s1 # bitandd_
            | expr_l8_s1 BITOR expr_l8_s1 # bitor_
            | expr_l8_s1 BITXOR expr_l8_s1 # bitnot_
            | expr_l8_s1 # next_82;

expr_l8: expr_l8_s2 BITANDorADDRESS expr_l8 # bitandd
         | expr_l8_s2 BITOR expr_l8 # bitor
         | expr_l8_s2 BITXOR expr_l8 # bitnot
         | expr_l8_s2 # next_8;

// 优先�?9：逻辑�? 逻辑�?
expr_l9_s1: expr_l8 AND expr_l8 # and_
            | expr_l8 OR expr_l8 # or_
            | expr_l8 # next_91;

expr_l9: expr_l9_s1 AND expr_l9 # and
         | expr_l9_s1 OR expr_l9 # or
         | expr_l8_s1 # next_9;

expression: expr_l9;

assignment_operator: ASSIGN # assign
                     | PLUSASSIGN # addeqaul
                     | MINUSASSIGN # suvequal
                     | MULTIPLYASSIGN # multiplyequal
                     | DIVIDEASSIGN # divideequal
                     | MODULOASSIGN # moduloequal;
assignment: IDENTIFIER(index)* assignment_operator expression;

variable_definition: type assignment;
// 生成代码�?
lib_announce: MEMSET # memest_announce
            | STRLEN # strlen_announce
            | PRINTF # printf_announce
            | SCANF # scanf_annouce;
function_definition: type IDENTIFIER LROUND params? RROUND LCURLY code ( RETURN value? SEMICOLON)? RCURLY;

if_block: IF LROUND expression RROUND expression LCURLY code RCURLY
          ( ELIF LROUND expression RROUND LCURLY code RCURLY )*
          ( ELSE LCURLY code RCURLY )?;
while_block: WHILE LROUND expression RROUND LCURLY code RCURLY;
for_block: FOR LROUND (variable_declaration | assignment | expression )? SEMICOLON expression SEMICOLON assignment? RROUND LCURLY code RCURLY;
switch_block: SWITCH LROUND expression RROUND LCURLY (CASE value COLON code)+ RCURLY;

line: variable_declaration | variable_definition | assignment | expression | lib_announce | BREAK | CONTINUE SEMICOLON;
block: if_block # if | while_block # while | for_block # for | switch_block # switch | line # single | function_definition # function;
code: block*;

