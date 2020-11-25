from tokens import tokens

# dictionary of names
""" names = { }
 
def p_statement_assign(p):
    '''statement : INT ID ASSIGN expression EOI
                 | FLOAT ID ASSIGN expression EOI
                 | CHAR ID ASSIGN CHARACTER EOI
    '''
    if p[1] == "char":
        names[p[2]] = p[4][1]
    else:    
        names[p[2]] = p[4]
 
def p_statement_expr(p):
    'statement : expression'
    print(p[1])
 
def p_expression_binop(p):
    'expression : expression ARITMETIC_OP_EX expression'
    if p[2] == '+':
        p[0] = p[1] + p[3]
    else:
        p[0] = p[1] - p[3]
 
def p_expression_group(p):
    "expression : LPAREN expression RPAREN"
    p[0] = p[2]
 
def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]
 
def p_expression_name(p):
    "expression : ID"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0 """


# Cuerpo principal

def p_program(p):
    "program : include_directives declaration_l"

def p_empty(p):
    'empty :'
    pass

# Directivas de inclusión y declaración

def p_include_directives(p):
    '''include_directives : include_directives include_directive
                          | include_directive
                          | empty
    '''

def p_include_directive(p):
    '''include_directive : HASH INCLUDE STRING
                         | HASH DEFINE ID simple_expression 
    '''

def p_declaration_l(p):
    '''declaration_l : declaration_l declaration
                     | declaration
    '''

def p_declaration(p):
    '''declaration : type var_declaration EOI
                   | fun_declaration
    '''

# Declaraciones

def p_var_declaration(p):
    '''var_declaration : var_declaration COMMA var_definition
                       | var_definition
    '''

def p_var_definition(p):
    '''var_definition : ID
                      | ID ASSIGN simple_expression
    '''

def p_fun_declaration(p):
    '''fun_declaration : type ID LPAREN params RPAREN compound_stmt
                       | VOID ID LPAREN params RPAREN compound_stmt
    '''

def p_params(p):
    '''params : params_l
              | VOID
              | empty
    '''

def p_params_l(p):
    '''params_l : params_l COMMA param
                | param
    '''

def p_param(p):
    "param : type ID"

def p_type(p):
    '''type : INT
            | FLOAT
            | CHAR
    '''

# Expresiones y bloques de código

def p_expression(p):
    '''expression : ID ASSIGN expression
                  | simple_expression
    '''

def p_expression_stmt(p):
    '''expression_stmt : expression EOI
                       | EOI
    '''

def p_compound_stmt(p):
    '''compound_stmt : BLOCK_START local_instructions BLOCK_END
    '''

def p_local_instructions(p):
    '''local_instructions : local_instructions type var_declaration EOI
                          | local_instructions statement
                          | empty
    '''

def p_statement(p):
    '''statement : expression_stmt 
                 | compound_stmt 
                 | if_stmt 
                 | while_stmt 
                 | return_stmt
    '''

def p_return_stmt(p):
    '''return_stmt : RETURN EOI
                   | RETURN expression EOI
    '''

def p_if_stmt(p):
    '''if_stmt : IF LPAREN condition RPAREN statement
               | IF LPAREN condition RPAREN statement ELSE statement
    '''

def p_while_stmt(p):
    '''while_stmt : WHILE LPAREN condition RPAREN statement
    '''

# Condiciones

def p_condition(p):
    '''condition : NEGATION simple_expression
                 | simple_expression LOGIC_OP simple_expression
                 | simple_expression  
    '''

# Expresiones

def p_simple_expression(p):
    '''simple_expression : simple_expression RELATION_OP bit_operation
                         | bit_operation
    '''

def p_bit_operation(p):
    '''bit_operation : bit_operation BIT_OP additive_operation
                     | additive_operation
    '''

def p_additive_operation(p):
    '''additive_operation : additive_operation ARITMETIC_OP_ADD prod_operation
                          | prod_operation
    '''

def p_prod_operation(p):
    '''prod_operation : prod_operation ARITMETIC_OP_PROD factor
                      | factor
    '''

def p_factor(p):
    '''factor : LPAREN simple_expression RPAREN
              | call
              | ID
              | NUMBER
              | CHARACTER   
    '''

# Llamadas a funciones

def p_call(p):
    "call : ID LPAREN args RPAREN"

def p_args(p):
    '''args : args_l
            | empty
    '''

def p_args_l(p):
    '''args_l : args_l COMMA simple_expression
              | simple_expression 
    '''

def p_error(p):
    if p:
        print("Syntax error at " + p.value + ", line: " + str(p.lineno))
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()
 
while 1:
    try:
        s = input('Filename > ')
        codeFile = open(s, "r")
        code = codeFile.read()
    except EOFError:
        break
    if not code: continue
    yacc.parse(code)
