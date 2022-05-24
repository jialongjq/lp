grammar jsbach;
root : procediment * EOF ;

procediment : ID VARIABLE* '|:' instruccio* ':|';

instruccio : (assignacio | lectura | escriptura | reproduccio | invocacio | condicional | iteracio | afegit | tall) ;

assignacio : VARIABLE ASSIGNACIO (VARIABLE | expressio | llista | text | consulta | mida);

lectura : LECTURA VARIABLE ;

escriptura : ESCRIPTURA (VARIABLE | expressio | text | llista)+ ;

reproduccio : REPRODUCCIO '{' NOTA* '}' ;

invocacio : ID expressio* ;

condicional : 'if' condicio '|:' instruccio+ ':|' ('else' '|:' instruccio+ ':|')?;

iteracio : 'while' condicio '|:' instruccio+ ':|' ;

afegit : VARIABLE '<<' expressio;

tall : '8<' VARIABLE '[' expressio ']' ;

mida : '#' VARIABLE ;

consulta : VARIABLE '[' expressio ']' ;

llista : '{' ENTER* '}';

expressio : '(' expressio ')'
          | expressio (MULTIPLICACIO | DIVISIO | MODUL) expressio
          | expressio (SUMA | RESTA) expressio
          | expressio (MAJOR | MAJORIGUAL | MENOR | MENORIGUAL | IGUAL | DIFERENT) expressio
    	  | ENTER
    	  | VARIABLE
    	  ;
    	  
condicio : expressio (MAJOR | MAJORIGUAL | MENOR | MENORIGUAL | IGUAL | DIFERENT) expressio ;
    	  
text : TEXT ;

ESCRIPTURA : '<!>' ;
LECTURA : '<?>' ;
ASSIGNACIO : '<-' ;
REPRODUCCIO : '<:>' ;

NOTA : 'C' | 'D' | 'E' | 'F' | 'G' | 'A' | 'B' ;
ID : [A-Z] [a-zA-Z\u0080-\u00FF0-9]* ;
VARIABLE : [a-z] [a-z\u0080-\u00FF0-9]* ;
ENTER : '-'? NUMERO ;
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
