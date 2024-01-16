grammar Cgrammer;

// �⺯������
MEMSET: 'void *memset(void *s, int ch, size_t n)';
STRLEN: 'size_t strlen(const char *_Str)';
PRINTF: 'int printf( const char *restrict format, ... )';
SCANF: 'int scanf(const char *__format, ...)';

// ��������
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

// �ؼ��ֹ���
INT: 'int';
FLOAT: 'float';
CHAR: 'char';
BOOL: 'bool';
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

// ���������
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

// �ָ�������
SEMICOLON: ';';
COMMA: ',';
LROUND: '(';
RROUND: ')';
LSQUARE: '[';
RSQUARE: ']';
LCURLY: '{';
RCURLY: '}';
COLON: ':';

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// ���Կհ��ַ���ע��
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* '\r'? '\n' -> skip ;

// ??��???��
// �����������??
announcer: INT # int | FLOAT # float | CHAR # char | BOOL # bool;
pointer_flag: MULTIPLYorREFERENCEorPTR;
type: announcer # originalType | announcer pointer_flag # pointer;
index: LSQUARE ( value | expression | function_call ) RSQUARE;
lib_function: MEMSETFUNC # memset| STRLENFUC # strlen | PRINTFFUNC # printf| SCANFFUNC # scanf;

variable_declaration: type IDENTIFIER index?;
params: BITANDorADDRESS? ( expression | IDENTIFIER ) (COMMA BITANDorADDRESS? ( expression | IDENTIFIER ) )*;
params_definition: variable_declaration (COMMA variable_declaration)*;
function_call: ( IDENTIFIER  | lib_function ) LROUND params? RROUND;

value: IDENTIFIER # id
        | INTVALUE # int_value
        | FLOATVALUE # float_value
        | CHARVALUE # char_value
        | STRINGVALUE # string_value
        | BOOLVALUE # bool_value
        | function_call # function_call_;

// ������ȼ������� ֵ
expr_unit: LROUND expression RROUND # round
           | value # expr_value;

// ���ȼ�1��ȡ���� ȡַ ����
expr_addr: MULTIPLYorREFERENCEorPTR expr_unit # content_of
            | BITANDorADDRESS expr_unit # address_of
            | expr_unit LSQUARE expression RSQUARE # array
            | expr_unit # unit;

// ���ȼ�2: ���� �Լ� ȡ�� ���� ����
expr_unary: SELFPLUS expr_addr # lincrese
            | expr_addr SELFPLUS # rincrease
            | SELFMINUS expr_addr # ldecrease
            | expr_addr SELFMINUS # rdecrease
            | NOT expr_addr # not
            | PLUS expr_addr # positive
            | MINUS expr_addr # negative
            | expr_addr # addr;

// ���ȼ�3���� �� ��
expr_calc1: expr_calc1 MULTIPLYorREFERENCEorPTR expr_unary # multiply
            | expr_calc1 DIVIDE expr_unary # divide
            | expr_calc1 MODULO expr_unary # modulo
            | expr_unary # unary;

// ���ȼ�4���� �� ��
expr_calc2: expr_calc2 PLUS expr_calc1 # add
            | expr_calc2 MINUS expr_calc1 # subtract
            | expr_calc1 # calc1;

// ���ȼ�5: ���� ������
expr_rop1: expr_calc2 EQUAL expr_calc2 # equal
          | expr_calc2 NOTEQUAL expr_calc2 # nequal
          | expr_calc2 # calc2;

// ���ȼ�6: ����(����) С��(����)
expr_rop2: expr_rop1 GREATER expr_rop1 # greater
           | expr_rop1 GEQUAL expr_rop1 # gequal
           | expr_rop1 LESS expr_rop1 # less
           | expr_rop1 LEQUAL expr_rop1 # leuqal
           | expr_rop1 # rop1;

// ����7���߼��� �߼���
expr_logic: expr_logic AND expr_rop2 # and
            | expr_logic OR expr_rop2 # or
            | expr_rop2 # rop2;

expression: expr_logic;

assignment_operator: ASSIGN # assign
                     | PLUSASSIGN # addeqaul
                     | MINUSASSIGN # suvequal
                     | MULTIPLYASSIGN # multiplyequal
                     | DIVIDEASSIGN # divideequal
                     | MODULOASSIGN # moduloequal;
assignment: IDENTIFIER(index)* assignment_operator expression;

variable_definition: ( type | VOID ) assignment ( COMMA assignment )*;

// ���ɴ����
lib_announce: MEMSET # memest_announce
            | STRLEN # strlen_announce
            | PRINTF # printf_announce
            | SCANF # scanf_annouce;
function_definition: ( type | VOID ) IDENTIFIER LROUND params_definition? RROUND LCURLY code RCURLY;

if_block: IF LROUND expression RROUND code_with_domain
          ( ELIF LROUND expression RROUND code_with_domain )*
          ( ELSE code_with_domain )?;
while_block: WHILE LROUND expression RROUND code_with_domain;
for_block: FOR LROUND ( variable_declaration | variable_definition | assignment | expression )? SEMICOLON expression SEMICOLON ( assignment | expression )? RROUND code_with_domain;
switch_block: SWITCH LROUND expression RROUND LCURLY (CASE value COLON code)+ RCURLY;

statement: variable_declaration # declaration
           | variable_definition # definition
           | assignment # assign_state
           | expression # expr
           | lib_announce # lib_func
           | BREAK # break
           | CONTINUE # continue
           | RETURN expression? # return;
line: statement? SEMICOLON;
block: if_block # if | while_block # while | for_block # for | switch_block # switch | line # single | function_definition # function;
code_with_domain: code # simple_code | LCURLY code RCURLY # domained_code;
code: block*;
