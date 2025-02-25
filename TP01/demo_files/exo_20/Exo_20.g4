grammar Exo_20;

full_expr: ab_sequence EOF;

ab_sequence: A ab_sequence B B | /* empty */;

A: 'a';
B: 'b';

LETTERS: ~[ab] -> skip;
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
