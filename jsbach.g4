grammar jsbach;
root : procediment * EOF ;

procediment : ID VARIABLE* '|:' instruccio* ':|';

instruccio : (assignacio | lectura | escriptura | reproduccio | invocacio | condicional | iteracio | afegit | tall) ;

assignacio : VARIABLE ASSIGNACIO (variable | enter | nota | enters | notes | transposicio | expressio | mida | consulta);

lectura : LECTURA VARIABLE ;

escriptura : ESCRIPTURA (text | variable | enter | nota | enters | notes | transposicio | expressio | mida | consulta)+ ;

reproduccio : REPRODUCCIO (nota | notes | variable) ;

invocacio : ID (variable | enter | expressio | mida | consulta)* ;

condicional : 'if' condicio '|:' instruccio+ ':|' ('else' '|:' instruccio+ ':|')?;

iteracio : 'while' condicio '|:' instruccio+ ':|' ;

afegit : variable '<<' expressio;

tall : '8<' variable '[' (variable | enter | expressio | mida | consulta) ']' ;

mida : '#' variable ;

consulta : variable '[' (variable | enter | expressio | mida | consulta) ']' ;

enters : '{' ENTER* '}' ;

notes : '{' NOTA* '}' ;

transposicio : (nota | variable) (SUMA | RESTA) enter ;

expressio : '(' expressio ')'
          | expressio (MULTIPLICACIO | DIVISIO | MODUL) expressio
          | expressio (SUMA | RESTA) expressio
          | expressio (MAJOR | MAJORIGUAL | MENOR | MENORIGUAL | IGUAL | DIFERENT) expressio
    	  | enter
    	  | variable
    	  ;
    	  
condicio : (nota | variable) (MAJOR | MAJORIGUAL | MENOR | MENORIGUAL | IGUAL | DIFERENT) (nota | variable)
         | expressio (MAJOR | MAJORIGUAL | MENOR | MENORIGUAL | IGUAL | DIFERENT) expressio
         ;
    	  
text : TEXT ;

variable : VARIABLE ;

enter : ENTER ;

nota : NOTA ;

ESCRIPTURA : '<!>' ;
LECTURA : '<?>' ;
ASSIGNACIO : '<-' ;
REPRODUCCIO : '<:>' ;

NOTA : [A-B] '0' | [A-G] [1-7] | 'C' '8' | [A-G];
ID : [A-Z\u00C4\u00D6\u00DC\u1E9E] [a-z\u00E4\u00F6\u00FC\u00DFA-Z\u00C4\u00D6\u00DC\u1E9E0-9_]* ;
VARIABLE : [a-z\u00E4\u00F6\u00FC\u00DF] [a-z\u00E4\u00F6\u00FC\u00DFA-Z\u00C4\u00D6\u00DC\u1E9E0-9_]* ;
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
