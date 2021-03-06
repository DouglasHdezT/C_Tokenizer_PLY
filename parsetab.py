
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARITMETIC_OP_ADD ARITMETIC_OP_PROD ASSIGN BIT_OP BLOCK_END BLOCK_START CHAR CHARACTER COMMA DEFINE ELSE EOI FLOAT HASH ID IF INCLUDE INT LOGIC_OP LPAREN NEGATION NUMBER RELATION_OP RETURN RPAREN STRING VOID WHILEprogram : include_directives declaration_lempty :include_directives : include_directives include_directive\n                          | include_directive\n                          | empty\n    include_directive : HASH INCLUDE STRING\n                         | HASH DEFINE ID simple_expression \n    declaration_l : declaration_l declaration\n                     | declaration\n    declaration : type var_declaration EOI\n                   | fun_declaration\n    var_declaration : var_declaration COMMA var_definition\n                       | var_definition\n    var_definition : ID\n                      | ID ASSIGN simple_expression\n    fun_declaration : type ID LPAREN params RPAREN compound_stmt\n                       | VOID ID LPAREN params RPAREN compound_stmt\n    params : params_l\n              | VOID\n              | empty\n    params_l : params_l COMMA param\n                | param\n    param : type IDtype : INT\n            | FLOAT\n            | CHAR\n    expression : ID ASSIGN simple_expression\n                  | simple_expression\n    expression_stmt : expression EOI\n                       | EOI\n    compound_stmt : BLOCK_START local_instructions BLOCK_END\n    local_instructions : local_instructions type var_declaration EOI\n                          | local_instructions statement\n                          | empty\n    statement : expression_stmt \n                 | compound_stmt \n                 | if_stmt \n                 | while_stmt \n                 | return_stmt\n    return_stmt : RETURN EOI\n                   | RETURN expression EOI\n    if_stmt : IF LPAREN condition RPAREN statement\n               | IF LPAREN condition RPAREN statement ELSE statement\n    while_stmt : WHILE LPAREN condition RPAREN statement\n    condition : NEGATION simple_expression\n                 | condition LOGIC_OP simple_expression\n                 | simple_expression  \n    simple_expression : simple_expression RELATION_OP bit_operation\n                         | bit_operation\n    bit_operation : bit_operation BIT_OP additive_operation\n                     | additive_operation\n    additive_operation : additive_operation ARITMETIC_OP_ADD prod_operation\n                          | prod_operation\n    prod_operation : prod_operation ARITMETIC_OP_PROD factor\n                      | factor\n    factor : LPAREN simple_expression RPAREN\n              | call\n              | ID\n              | NUMBER\n              | CHARACTER   \n    call : ID LPAREN args RPARENargs : args_l\n            | empty\n    args_l : args_l COMMA simple_expression\n              | simple_expression \n    '
    
_lr_action_items = {'HASH':([0,2,3,4,7,22,29,30,31,32,33,34,36,37,38,63,64,65,66,67,72,],[5,5,-4,-5,-3,-6,-58,-7,-49,-51,-53,-55,-57,-59,-60,-48,-50,-52,-54,-56,-61,]),'INT':([0,2,3,4,6,7,8,10,17,22,24,26,28,29,30,31,32,33,34,36,37,38,57,63,64,65,66,67,68,69,71,72,74,75,77,79,80,81,82,83,84,85,93,96,99,104,110,112,114,],[-2,11,-4,-5,11,-3,-9,-11,-8,-6,-10,11,11,-58,-7,-49,-51,-53,-55,-57,-59,-60,11,-48,-50,-52,-54,-56,-16,-2,-17,-61,11,-34,-31,-30,-33,-35,-36,-37,-38,-39,-29,-40,-32,-41,-42,-44,-43,]),'FLOAT':([0,2,3,4,6,7,8,10,17,22,24,26,28,29,30,31,32,33,34,36,37,38,57,63,64,65,66,67,68,69,71,72,74,75,77,79,80,81,82,83,84,85,93,96,99,104,110,112,114,],[-2,12,-4,-5,12,-3,-9,-11,-8,-6,-10,12,12,-58,-7,-49,-51,-53,-55,-57,-59,-60,12,-48,-50,-52,-54,-56,-16,-2,-17,-61,12,-34,-31,-30,-33,-35,-36,-37,-38,-39,-29,-40,-32,-41,-42,-44,-43,]),'CHAR':([0,2,3,4,6,7,8,10,17,22,24,26,28,29,30,31,32,33,34,36,37,38,57,63,64,65,66,67,68,69,71,72,74,75,77,79,80,81,82,83,84,85,93,96,99,104,110,112,114,],[-2,13,-4,-5,13,-3,-9,-11,-8,-6,-10,13,13,-58,-7,-49,-51,-53,-55,-57,-59,-60,13,-48,-50,-52,-54,-56,-16,-2,-17,-61,13,-34,-31,-30,-33,-35,-36,-37,-38,-39,-29,-40,-32,-41,-42,-44,-43,]),'VOID':([0,2,3,4,6,7,8,10,17,22,24,26,28,29,30,31,32,33,34,36,37,38,63,64,65,66,67,68,71,72,77,],[-2,14,-4,-5,14,-3,-9,-11,-8,-6,-10,44,44,-58,-7,-49,-51,-53,-55,-57,-59,-60,-48,-50,-52,-54,-56,-16,-17,-61,-31,]),'$end':([1,6,8,10,17,24,68,71,77,],[0,-1,-9,-11,-8,-10,-16,-17,-31,]),'INCLUDE':([5,],[15,]),'DEFINE':([5,],[16,]),'ID':([9,11,12,13,14,16,23,25,27,35,41,49,50,51,52,53,69,73,74,75,77,78,79,80,81,82,83,84,85,89,93,94,95,96,98,99,101,104,106,107,109,110,112,113,114,],[19,-24,-25,-26,21,23,29,40,29,29,55,29,29,29,29,29,-2,29,90,-34,-31,40,-30,-33,-35,-36,-37,-38,-39,90,-29,29,29,-40,29,-32,29,-41,90,29,90,-42,-44,90,-43,]),'STRING':([15,],[22,]),'EOI':([18,19,20,29,31,32,33,34,36,37,38,39,40,47,63,64,65,66,67,69,72,74,75,77,79,80,81,82,83,84,85,86,89,90,91,92,93,96,97,99,104,105,106,109,110,112,113,114,],[24,-14,-13,-58,-49,-51,-53,-55,-57,-59,-60,-12,-14,-15,-48,-50,-52,-54,-56,-2,-61,79,-34,-31,-30,-33,-35,-36,-37,-38,-39,93,96,-58,-28,99,-29,-40,104,-32,-41,-27,79,79,-42,-44,79,-43,]),'COMMA':([18,19,20,29,31,32,33,34,36,37,38,39,40,43,46,47,55,60,62,63,64,65,66,67,70,72,76,92,],[25,-14,-13,-58,-49,-51,-53,-55,-57,-59,-60,-12,-14,57,-22,-15,-23,73,-65,-48,-50,-52,-54,-56,-21,-61,-64,25,]),'LPAREN':([19,21,23,27,29,35,49,50,51,52,53,69,73,74,75,77,79,80,81,82,83,84,85,87,88,89,90,93,94,95,96,98,99,101,104,106,107,109,110,112,113,114,],[26,28,35,35,49,35,35,35,35,35,35,-2,35,35,-34,-31,-30,-33,-35,-36,-37,-38,-39,94,95,35,49,-29,35,35,-40,35,-32,35,-41,35,35,35,-42,-44,35,-43,]),'ASSIGN':([19,40,90,],[27,27,98,]),'NUMBER':([23,27,35,49,50,51,52,53,69,73,74,75,77,79,80,81,82,83,84,85,89,93,94,95,96,98,99,101,104,106,107,109,110,112,113,114,],[37,37,37,37,37,37,37,37,-2,37,37,-34,-31,-30,-33,-35,-36,-37,-38,-39,37,-29,37,37,-40,37,-32,37,-41,37,37,37,-42,-44,37,-43,]),'CHARACTER':([23,27,35,49,50,51,52,53,69,73,74,75,77,79,80,81,82,83,84,85,89,93,94,95,96,98,99,101,104,106,107,109,110,112,113,114,],[38,38,38,38,38,38,38,38,-2,38,38,-34,-31,-30,-33,-35,-36,-37,-38,-39,38,-29,38,38,-40,38,-32,38,-41,38,38,38,-42,-44,38,-43,]),'RPAREN':([26,28,29,31,32,33,34,36,37,38,42,43,44,45,46,48,49,54,55,59,60,61,62,63,64,65,66,67,70,72,76,100,102,103,108,111,],[-2,-2,-58,-49,-51,-53,-55,-57,-59,-60,56,-18,-19,-20,-22,58,-2,67,-23,72,-62,-63,-65,-48,-50,-52,-54,-56,-21,-61,-64,106,-47,109,-45,-46,]),'ARITMETIC_OP_PROD':([29,33,34,36,37,38,65,66,67,72,90,],[-58,53,-55,-57,-59,-60,53,-54,-56,-61,-58,]),'ARITMETIC_OP_ADD':([29,32,33,34,36,37,38,64,65,66,67,72,90,],[-58,52,-53,-55,-57,-59,-60,52,-52,-54,-56,-61,-58,]),'BIT_OP':([29,31,32,33,34,36,37,38,63,64,65,66,67,72,90,],[-58,51,-51,-53,-55,-57,-59,-60,51,-50,-52,-54,-56,-61,-58,]),'RELATION_OP':([29,30,31,32,33,34,36,37,38,47,54,62,63,64,65,66,67,72,76,90,91,102,105,108,111,],[-58,50,-49,-51,-53,-55,-57,-59,-60,50,50,50,-48,-50,-52,-54,-56,-61,50,-58,50,50,50,50,50,]),'LOGIC_OP':([29,31,32,33,34,36,37,38,63,64,65,66,67,72,100,102,103,108,111,],[-58,-49,-51,-53,-55,-57,-59,-60,-48,-50,-52,-54,-56,-61,107,-47,107,-45,-46,]),'BLOCK_START':([56,58,69,74,75,77,79,80,81,82,83,84,85,93,96,99,104,106,109,110,112,113,114,],[69,69,-2,69,-34,-31,-30,-33,-35,-36,-37,-38,-39,-29,-40,-32,-41,69,69,-42,-44,69,-43,]),'BLOCK_END':([69,74,75,77,79,80,81,82,83,84,85,93,96,99,104,110,112,114,],[-2,77,-34,-31,-30,-33,-35,-36,-37,-38,-39,-29,-40,-32,-41,-42,-44,-43,]),'IF':([69,74,75,77,79,80,81,82,83,84,85,93,96,99,104,106,109,110,112,113,114,],[-2,87,-34,-31,-30,-33,-35,-36,-37,-38,-39,-29,-40,-32,-41,87,87,-42,-44,87,-43,]),'WHILE':([69,74,75,77,79,80,81,82,83,84,85,93,96,99,104,106,109,110,112,113,114,],[-2,88,-34,-31,-30,-33,-35,-36,-37,-38,-39,-29,-40,-32,-41,88,88,-42,-44,88,-43,]),'RETURN':([69,74,75,77,79,80,81,82,83,84,85,93,96,99,104,106,109,110,112,113,114,],[-2,89,-34,-31,-30,-33,-35,-36,-37,-38,-39,-29,-40,-32,-41,89,89,-42,-44,89,-43,]),'ELSE':([77,79,81,82,83,84,85,93,96,104,110,112,114,],[-31,-30,-35,-36,-37,-38,-39,-29,-40,-41,113,-44,-43,]),'NEGATION':([94,95,],[101,101,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'include_directives':([0,],[2,]),'include_directive':([0,2,],[3,7,]),'empty':([0,26,28,49,69,],[4,45,45,61,75,]),'declaration_l':([2,],[6,]),'declaration':([2,6,],[8,17,]),'type':([2,6,26,28,57,74,],[9,9,41,41,41,78,]),'fun_declaration':([2,6,],[10,10,]),'var_declaration':([9,78,],[18,92,]),'var_definition':([9,25,78,],[20,39,20,]),'simple_expression':([23,27,35,49,73,74,89,94,95,98,101,106,107,109,113,],[30,47,54,62,76,91,91,102,102,105,108,91,111,91,91,]),'bit_operation':([23,27,35,49,50,73,74,89,94,95,98,101,106,107,109,113,],[31,31,31,31,63,31,31,31,31,31,31,31,31,31,31,31,]),'additive_operation':([23,27,35,49,50,51,73,74,89,94,95,98,101,106,107,109,113,],[32,32,32,32,32,64,32,32,32,32,32,32,32,32,32,32,32,]),'prod_operation':([23,27,35,49,50,51,52,73,74,89,94,95,98,101,106,107,109,113,],[33,33,33,33,33,33,65,33,33,33,33,33,33,33,33,33,33,33,]),'factor':([23,27,35,49,50,51,52,53,73,74,89,94,95,98,101,106,107,109,113,],[34,34,34,34,34,34,34,66,34,34,34,34,34,34,34,34,34,34,34,]),'call':([23,27,35,49,50,51,52,53,73,74,89,94,95,98,101,106,107,109,113,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'params':([26,28,],[42,48,]),'params_l':([26,28,],[43,43,]),'param':([26,28,57,],[46,46,70,]),'args':([49,],[59,]),'args_l':([49,],[60,]),'compound_stmt':([56,58,74,106,109,113,],[68,71,82,82,82,82,]),'local_instructions':([69,],[74,]),'statement':([74,106,109,113,],[80,110,112,114,]),'expression_stmt':([74,106,109,113,],[81,81,81,81,]),'if_stmt':([74,106,109,113,],[83,83,83,83,]),'while_stmt':([74,106,109,113,],[84,84,84,84,]),'return_stmt':([74,106,109,113,],[85,85,85,85,]),'expression':([74,89,106,109,113,],[86,97,86,86,86,]),'condition':([94,95,],[100,103,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> include_directives declaration_l','program',2,'p_program','main.py',6),
  ('empty -> <empty>','empty',0,'p_empty','main.py',9),
  ('include_directives -> include_directives include_directive','include_directives',2,'p_include_directives','main.py',15),
  ('include_directives -> include_directive','include_directives',1,'p_include_directives','main.py',16),
  ('include_directives -> empty','include_directives',1,'p_include_directives','main.py',17),
  ('include_directive -> HASH INCLUDE STRING','include_directive',3,'p_include_directive','main.py',21),
  ('include_directive -> HASH DEFINE ID simple_expression','include_directive',4,'p_include_directive','main.py',22),
  ('declaration_l -> declaration_l declaration','declaration_l',2,'p_declaration_l','main.py',26),
  ('declaration_l -> declaration','declaration_l',1,'p_declaration_l','main.py',27),
  ('declaration -> type var_declaration EOI','declaration',3,'p_declaration','main.py',31),
  ('declaration -> fun_declaration','declaration',1,'p_declaration','main.py',32),
  ('var_declaration -> var_declaration COMMA var_definition','var_declaration',3,'p_var_declaration','main.py',38),
  ('var_declaration -> var_definition','var_declaration',1,'p_var_declaration','main.py',39),
  ('var_definition -> ID','var_definition',1,'p_var_definition','main.py',43),
  ('var_definition -> ID ASSIGN simple_expression','var_definition',3,'p_var_definition','main.py',44),
  ('fun_declaration -> type ID LPAREN params RPAREN compound_stmt','fun_declaration',6,'p_fun_declaration','main.py',48),
  ('fun_declaration -> VOID ID LPAREN params RPAREN compound_stmt','fun_declaration',6,'p_fun_declaration','main.py',49),
  ('params -> params_l','params',1,'p_params','main.py',53),
  ('params -> VOID','params',1,'p_params','main.py',54),
  ('params -> empty','params',1,'p_params','main.py',55),
  ('params_l -> params_l COMMA param','params_l',3,'p_params_l','main.py',59),
  ('params_l -> param','params_l',1,'p_params_l','main.py',60),
  ('param -> type ID','param',2,'p_param','main.py',64),
  ('type -> INT','type',1,'p_type','main.py',67),
  ('type -> FLOAT','type',1,'p_type','main.py',68),
  ('type -> CHAR','type',1,'p_type','main.py',69),
  ('expression -> ID ASSIGN simple_expression','expression',3,'p_expression','main.py',75),
  ('expression -> simple_expression','expression',1,'p_expression','main.py',76),
  ('expression_stmt -> expression EOI','expression_stmt',2,'p_expression_stmt','main.py',80),
  ('expression_stmt -> EOI','expression_stmt',1,'p_expression_stmt','main.py',81),
  ('compound_stmt -> BLOCK_START local_instructions BLOCK_END','compound_stmt',3,'p_compound_stmt','main.py',85),
  ('local_instructions -> local_instructions type var_declaration EOI','local_instructions',4,'p_local_instructions','main.py',89),
  ('local_instructions -> local_instructions statement','local_instructions',2,'p_local_instructions','main.py',90),
  ('local_instructions -> empty','local_instructions',1,'p_local_instructions','main.py',91),
  ('statement -> expression_stmt','statement',1,'p_statement','main.py',95),
  ('statement -> compound_stmt','statement',1,'p_statement','main.py',96),
  ('statement -> if_stmt','statement',1,'p_statement','main.py',97),
  ('statement -> while_stmt','statement',1,'p_statement','main.py',98),
  ('statement -> return_stmt','statement',1,'p_statement','main.py',99),
  ('return_stmt -> RETURN EOI','return_stmt',2,'p_return_stmt','main.py',103),
  ('return_stmt -> RETURN expression EOI','return_stmt',3,'p_return_stmt','main.py',104),
  ('if_stmt -> IF LPAREN condition RPAREN statement','if_stmt',5,'p_if_stmt','main.py',108),
  ('if_stmt -> IF LPAREN condition RPAREN statement ELSE statement','if_stmt',7,'p_if_stmt','main.py',109),
  ('while_stmt -> WHILE LPAREN condition RPAREN statement','while_stmt',5,'p_while_stmt','main.py',113),
  ('condition -> NEGATION simple_expression','condition',2,'p_condition','main.py',119),
  ('condition -> condition LOGIC_OP simple_expression','condition',3,'p_condition','main.py',120),
  ('condition -> simple_expression','condition',1,'p_condition','main.py',121),
  ('simple_expression -> simple_expression RELATION_OP bit_operation','simple_expression',3,'p_simple_expression','main.py',127),
  ('simple_expression -> bit_operation','simple_expression',1,'p_simple_expression','main.py',128),
  ('bit_operation -> bit_operation BIT_OP additive_operation','bit_operation',3,'p_bit_operation','main.py',132),
  ('bit_operation -> additive_operation','bit_operation',1,'p_bit_operation','main.py',133),
  ('additive_operation -> additive_operation ARITMETIC_OP_ADD prod_operation','additive_operation',3,'p_additive_operation','main.py',137),
  ('additive_operation -> prod_operation','additive_operation',1,'p_additive_operation','main.py',138),
  ('prod_operation -> prod_operation ARITMETIC_OP_PROD factor','prod_operation',3,'p_prod_operation','main.py',142),
  ('prod_operation -> factor','prod_operation',1,'p_prod_operation','main.py',143),
  ('factor -> LPAREN simple_expression RPAREN','factor',3,'p_factor','main.py',147),
  ('factor -> call','factor',1,'p_factor','main.py',148),
  ('factor -> ID','factor',1,'p_factor','main.py',149),
  ('factor -> NUMBER','factor',1,'p_factor','main.py',150),
  ('factor -> CHARACTER','factor',1,'p_factor','main.py',151),
  ('call -> ID LPAREN args RPAREN','call',4,'p_call','main.py',157),
  ('args -> args_l','args',1,'p_args','main.py',160),
  ('args -> empty','args',1,'p_args','main.py',161),
  ('args_l -> args_l COMMA simple_expression','args_l',3,'p_args_l','main.py',165),
  ('args_l -> simple_expression','args_l',1,'p_args_l','main.py',166),
]
