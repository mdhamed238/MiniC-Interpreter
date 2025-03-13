grammar SujetA;
// Rappel : Grammaire combinée lexicographie + syntaxe.
// Non-terminaux en minuscule, terminaux (lexico) en MAJUSCULE.

// Ne pas modifier le nom 'start' (axiome de la grammaire)
start: expr EOF;

expr: LET ID EQ INT SEMI;

SEMI: ';';
EQ: '=';
LET: 'let';
ID: [a-zA-Z] [a-zA-Z_0-9]*;
INT: [1-9] [0-9]*;

// Ne pas modifier, cette règle est nécessaire pour les tests
COMMENT
 : '//' ~[\r\n]* -> skip
 ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
