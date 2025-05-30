grammar AnB2n;
// Rappel : Grammaire combinée lexicographie + syntaxe.
// Non-terminaux en minuscule, terminaux (lexico) en MAJUSCULE.

start: anb2n EOF;

anb2n: A B B
    |A anb2n B B ;


A: 'a';
B: 'b';
// Ne pas modifier, cette règle est nécessaire pour les tests
COMMENT
 : '//' ~[\r\n]* -> skip
 ;

WS : [\t\r\n]+ -> skip ; // skip spaces, tabs, newlines
