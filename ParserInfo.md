| Token               | First                                                                        | Follow                                                                              |
| ------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| while_stmt          | { WHILE }                                                                    | { $ }                                                                               |
| statement           | { ID, LPAREN, NUMBER, CHARACTER, EOI } { BLOCK_START }                       | { $, INT, FLOAT, CHAR, BLOCK_START, ID, LPAREN, NUMBER, CHARACTER, EOI, BLOCK_END } |
| compound_stmt       | { BLOCK_START}                                                               | { $, INT, FLOAT, CHAR, BLOCK_START, ID, LPAREN, NUMBER, CHARACTER, EOI, BLOCK_END } |
| local_instructions  | { INT, FLOAT, CHAR, BLOCK_START, ID, LPAREN, NUMBER, CHARACTER, EOI, empty } | { BLOCK_END }                                                                       |
| local_instructions' | { INT, FLOAT, CHAR, BLOCK_START, ID, LPAREN, NUMBER, CHARACTER, EOI, empty } | { BLOCK_END }                                                                       |
| local_instruction   | { INT, FLOAT, CHAR, BLOCK_START, ID, LPAREN, NUMBER, CHARACTER, EOI }        | { INT, FLOAT, CHAR, BLOCK_START, ID, LPAREN, NUMBER, CHARACTER, EOI, BLOCK_END }    |
| expression_stmt     | { ID, LPAREN, NUMBER, CHARACTER, EOI }                                       | { $, INT, FLOAT, CHAR, BLOCK_START, ID, LPAREN, NUMBER, CHARACTER, EOI, BLOCK_END } |
| expression          | { ID, LPAREN, NUMBER, CHARACTER }                                            | { EOI }                                                                             |
| expression'         | { ID, empty }                                                                | { ID, LPAREN, NUMBER, CHARACTER }                                                   |
| var_declaration     | { ID }                                                                       | { EOI }                                                                             |
| var_declaration'    | { COMMA, empty }                                                             | { EOI }                                                                             |
| var_definition      | { ID }                                                                       | { COMMA, EOI }                                                                      |
| var_definition'     | { ASSIGN, empty }                                                            | { COMMA, EOI }                                                                      |
| type                | { INT, FLOAT, CHAR }                                                         | { ID }                                                                              |
| condition           | { NEGATION, ID, LPAREN, NUMBER, CHARACTER }                                  | { RPAREN }                                                                          |
| condition'          | { LOGIC_OP, empty }                                                          | { RPAREN }                                                                          |
| condition_member    | { NEGATION, ID, LPAREN, NUMBER, CHARACTER }                                  | { LOGIC_OP, RPAREN }                                                                          |
| simple_expression   | { ID, LPAREN, NUMBER, CHARACTER }                                            | { LOGIC_OP, RPAREN, EOI, COMMA }                                                              |
| simple_expression'  | { RELATION_OP, empty }                                                       | { LOGIC_OP, RPAREN, EOI, COMMA }                                                              |
| additive_operation  | { ID, LPAREN, NUMBER, CHARACTER }                                            | { RELATION_OP, LOGIC_OP, RPAREN, EOI, COMMA }                                                 |
| additive_operation' | { ARITMETIC_OP_ADD, empty }                                                  | { RELATION_OP, LOGIC_OP, RPAREN, EOI, COMMA }                                                 |
| prod_operation      | { ID, LPAREN, NUMBER, CHARACTER }                                            | { ARITMETIC_OP_ADD, RELATION_OP, LOGIC_OP, RPAREN, EOI, COMMA }                               |
| prod_operation'     | { ARITMETIC_OP_PROD, empty }                                                 | { ARITMETIC_OP_ADD, RELATION_OP, LOGIC_OP, RPAREN, EOI, COMMA }                               |
| factor              | { ID, LPAREN, NUMBER, CHARACTER }                                            | { ARITMETIC_OP_PROD, ARITMETIC_OP_ADD, RELATION_OP, LOGIC_OP, RPAREN, EOI, COMMA }            |

Tabla de parseo

| NT/T                | WHILE | LPAREN | RPAREN | BLOCK_START | BLOCK_END | EOI | ID  | ASSIGN | COMMA | INT | FLOAT | CHAR | NEGATION | RELATION_OP | ARITMETIC_OP_ADD | ARITMETIC_OP_PROD | LOGIC_OP | NUMBER | CHARACTER |
| ------------------- | ----- | ------ | ------ | ----------- | --------- | --- | --- | ------ | ----- | --- | ----- | ---- | -------- | ----------- | ---------------- | ----------------- | -------- | ------ | --------- |
| while_stmt          | 01    |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| statement           |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| compound_stmt       |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| local_instructions  |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| local_instructions' |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| local_instruction   |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| expression_stmt     |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| expression          |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| expression'         |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| var_declaration     |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| var_declaration'    |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| var_definition      |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| var_definition'     |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| type                |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| condition           |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| condition'          |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| simple_expression   |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| simple_expression'  |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| additive_operation  |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| additive_operation' |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| prod_operation      |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| prod_operation'     |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |
| factor              |       |        |        |             |           |     |     |        |       |     |       |      |          |             |                  |                   |          |        |           |