grammar AnB2n;

start: EOF;

// Ne pas modifier, cette règle est nécessaire pour les tests
COMMENT
 : '//' ~[\r\n]* -> skip
 ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
