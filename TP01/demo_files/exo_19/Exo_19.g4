grammar Exo_19;

full_expr: par_expression EOF;

par_expression: LPAR par_expression RPAR 
    | '[' par_expression ']' 
    | /* Empty */;
    
LPAR: '(';
RPAR: ')';

CHARS: ~[()[\]] -> skip;
// WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

/*
    
 */