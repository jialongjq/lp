grammar jsbach;
root : procediment * EOF ;

instruccio : (assignacio | escriptura | lectura | reproduccio | invocacio) ;

procediment : ID VARIABLE* '|:' instruccio* ':|';

assignacio : VARIABLE ASSIGNACIO expressio ;

escriptura : ESCRIPTURA expressio ;

reproduccio : REPRODUCCIO '{' NOTA* '}' ;

lectura : LECTURA VARIABLE ;

expressio : '(' expressio ')'
          | expressio (MULTIPLICACIO | DIVISIO | MODUL) expressio
          | expressio (SUMA | RESTA) expressio
          | expressio (MAJOR | MAJORIGUAL | MENOR | MENORIGUAL | IGUAL | DIFERENT) expressio
    	  | NUMERO | VARIABLE | TEXT
    	  ;

invocacio : ID expressio* ;

ESCRIPTURA : '<!>' ;
LECTURA : '<?>' ;
ASSIGNACIO : '<-' ;
REPRODUCCIO : '<:>' ;

NOTA : 'C' | 'D' | 'E' | 'F' | 'G' | 'A' | 'B' ;
ID : [A-Z] [a-zA-Z\u0080-\u00FF]* ;
VARIABLE : [a-z]+ ;
NUMERO : [0-9]+ ;
TEXT : '"' .*? '"' ;

MULTIPLICACIO : '*' ;
DIVISIO : '/' ;
MODUL : '%' ;
SUMA : '+' ;
RESTA : '-' ;
MAJOR : '>' ;
MENOR : '<' ;
MAJORIGUAL : '>=' ;
MENORIGUAL : '<=' ;
IGUAL : '=' ;
DIFERENT : '/=' ;

COMENTARI : '~~~' .*? '~~~' -> skip;
WS : [ \n]+ -> skip ;
