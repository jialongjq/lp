grammar jsbach;
root : procediment * EOF ;

procediment : ID VARIABLE* '|:' instruccio* ':|';

instruccio : (assignacio | lectura | escriptura | reproduccio | invocacio | condicional | iteracio | afegit | tall) ;

assignacio : VARIABLE ASSIGNACIO (variable | expressio | llista | text | consulta | mida);

lectura : LECTURA VARIABLE ;

escriptura : ESCRIPTURA (variable | expressio | text | llista | mida | consulta)+ ;

reproduccio : REPRODUCCIO notes ;

invocacio : ID expressio* ;

condicional : 'if' condicio '|:' instruccio+ ':|' ('else' '|:' instruccio+ ':|')?;

iteracio : 'while' condicio '|:' instruccio+ ':|' ;

afegit : variable '<<' expressio;

tall : '8<' variable '[' expressio ']' ;

mida : '#' variable ;

consulta : variable '[' expressio ']' ;

llista : '{' ENTER* '}';

notes : '{' NOTA* '}';

expressio : '(' expressio ')'
          | expressio (MULTIPLICACIO | DIVISIO | MODUL) expressio
          | expressio (SUMA | RESTA) expressio
          | expressio (MAJOR | MAJORIGUAL | MENOR | MENORIGUAL | IGUAL | DIFERENT) expressio
    	  | enter
    	  | variable
    	  ;
    	  
condicio : expressio (MAJOR | MAJORIGUAL | MENOR | MENORIGUAL | IGUAL | DIFERENT) expressio ;
    	  
text : TEXT ;

variable : VARIABLE ;

enter : ENTER ;

ESCRIPTURA : '<!>' ;
LECTURA : '<?>' ;
ASSIGNACIO : '<-' ;
REPRODUCCIO : '<:>' ;

NOTA : [A-B] '0' | [A-G] [1-7] | 'C' '8' | [A-G];
ID : [A-Z] [a-zA-Z\u0080-\u00FF0-9_]* ;
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
