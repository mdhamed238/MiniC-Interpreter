grammar Exo_20;

full_expr: ab_saquence EOF;

ab_saquence: A B
        | A ab_saquence B;

A: 'a';
B: 'bb';

LETTERS: ~[ab] -> skip;
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
