| Token               | First                                                                   | Follow                                                                             |
| ------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| while_stmt          | { WHILE }                                                               | { $ }                                                                              |
| statement           | { BLOCK_START, ID, LPAREN, NUMBER, CHARACTER }                          | { $, INT, FLOAT, CHAR, BLOCK_START, ID, LPAREN, NUMBER, CHARACTER, BLOCK_END }     |
| compound_stmt       | { BLOCK_START}                                                          | { $, INT, FLOAT, CHAR, BLOCK_START, ID, LPAREN, NUMBER, CHARACTER, BLOCK_END }     |
| local_instructions  | { empty }                                                               | { BLOCK_END }                                                                      |
| local_instructions' | { INT, FLOAT, CHAR, BLOCK_START, ID, LPAREN, NUMBER, CHARACTER, empty } | { BLOCK_END }                                                                      |
| local_instruction   | { INT, FLOAT, CHAR, BLOCK_START, ID, LPAREN, NUMBER, CHARACTER }        | { INT, FLOAT, CHAR, BLOCK_START, ID, LPAREN, NUMBER, CHARACTER, BLOCK_END }        |
| expression_stmt     | { EOI, ID, LPAREN, NUMBER, CHARACTER }                                  | { $, INT, FLOAT, CHAR, BLOCK_START, ID, LPAREN, NUMBER, CHARACTER, BLOCK_END }     |
| expression          | { ID, LPAREN, NUMBER, CHARACTER }                                       | { EOI }                                                                            |
| var_declaration     | { ID }                                                                  | { EOI }                                                                            |
| var_declaration'    | { COMMA, empty }                                                        | { EOI }                                                                            |
| var_definition      | { ID }                                                                  | { COMMA, EOI }                                                                     |
| type                | { INT, FLOAT, CHAR }                                                    | { ID }                                                                             |
| condition           | { NEGATION, ID, LPAREN, NUMBER, CHARACTER }                             | { RPAREN }                                                                         |
| simple_expression   | { ID, LPAREN, NUMBER, CHARACTER }                                       | { RPAREN, EOI, COMMA, LOGIC_OP }                                                   |
| simple_expression'  | { RELATION_OP, empty }                                                  | { RPAREN, EOI, COMMA, LOGIC_OP }                                                   |
| additive_operation  | { ID, LPAREN, NUMBER, CHARACTER }                                       | { RELATION_OP, RPAREN, EOI, COMMA, LOGIC_OP }                                      |
| additive_operation' | { ARITMETIC_OP_ADD, empty }                                             | { RELATION_OP, RPAREN, EOI, COMMA, LOGIC_OP }                                      |
| prod_operation      | { ID, LPAREN, NUMBER, CHARACTER }                                       | { ARITMETIC_OP_ADD, RELATION_OP, RPAREN, EOI, COMMA, LOGIC_OP }                    |
| prod_operation'     | { ARITMETIC_OP_PROD, empty }                                            | { ARITMETIC_OP_ADD, RELATION_OP, RPAREN, EOI, COMMA, LOGIC_OP }                    |
| factor              | { ID, LPAREN, NUMBER, CHARACTER }                                       | { ARITMETIC_OP_PROD, ARITMETIC_OP_ADD, RELATION_OP, RPAREN, EOI, COMMA, LOGIC_OP } |