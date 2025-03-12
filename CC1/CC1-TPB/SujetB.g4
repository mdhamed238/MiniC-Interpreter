grammar SujetB;
// Rappel : Grammaire combinée lexicographie + syntaxe.
// Non-terminaux en minuscule, terminaux (lexico) en MAJUSCULE.

// Ne pas modifier le nom 'start' (axiome de la grammaire)
start: EOF;
EQ: '=';

// Ne pas modifier, cette règle est nécessaire pour les tests
COMMENT
 : '//' ~[\r\n]* -> skip
 ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
