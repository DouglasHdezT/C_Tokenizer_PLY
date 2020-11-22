from tokens import tokens

# dictionary of names
names = { }
 
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
        p[0] = 0

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc(debug=1)
 
while 1:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)
