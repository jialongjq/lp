# El doble intèrpret de JSBach
Aquesta pàgina descriu la implementació feta per la pràctica de GEI-LP (edició 2021-2022 Q2), el doble intèrpret de JSBach.

## Gramàtica

La gramàtica proposada consisteix en un conjunt de procediments com a arrel, on cada procediment és un conjunt d'instruccions.  

Cal diferenciar les regles que internament retornen un valor amb les que no en retornen cap. Aquelles que no retornen cap valor son considerades instruccions (`assignacio`, `lectura`, `escriptura`, `reproduccio`, `invocacio`, `condicional`, `iteracio`, `afegit` i `tall`). Les que sí en retornen un valor (`mida`, `consulta`, `enters`, `notes`, `transposicio`, `expressio`, `condicio`, `text`, `variable`, `enter` i `nota`) s'utilitzen per complementar les instruccions segons les necessitats de cadascuna, les quals s'explicaran més endavant. Els tokens s'han utilitzat principalment per permetre una millor llegibilitat de la gramàtica. Els que es consulten al visitador son els operadors aritmètics i relacionals.

Un tret que pot semblar confús és l'ús alternat de la regla `variable` i el token `VARIABLE` a les regles. La diferència clau és que el token `VARIABLE` s'utilitza quan no és necessari l'accés al valor d'una variable. A més a més, les regles `variable`, `enter`, `nota` i `text`, tot i semblar innecessaris perquè no són res més que un token, son realment molt útils a l'hora de fer resolucions perquè internament es poden fer visites directament sense importar els tipus de node, fet que permet estalviar molta lògica.

## Visitador

En relació al visitador és important comentar la seva funcionalitat interna (la resta, és a dir, com es visiten les diferents regles, s'assumeix que es sobreentèn amb les corresponents explicacions més endavant a l'apartat d'especificació de JSBach).   

El visitador disposa de tres diccionaris: `notaEnter`, `enterNota` i `notaOutput`. Els diccionaris `notaEnter` i `enterNota` permeten tractar les notes com a constants enteres i viceversa, facilitant la transposició de notes. El diccionari `notaOutput` permet fer una traducció de les notes a la notació que utilitza el programa extern LilyPond.  

Com a atributs privats té un booleà `executar`, un diccionari `bloc`, un diccionari `parametres`, una llista `pila`, un string `inici` i una llista `partitura`.  

Quan s'inicia l'intèrpret, el primer pas que ha de fer és el de guardar el context de tots els procediments presents al programa al diccionari `bloc`, de manera que es pugui fer una visita directa a qualsevol procediment del programa (fet que serà de gran ajuda per fer invocacions), a més dels paràmetres que rep al diccionari `parametres`. Com que això implica una primera visita a totes les regles `procediment`, però sense voler executar cap instrucció, l'atribut booleà `executar` s'inicialitza a `False`, i serveix com a un flag que determina si la visita d'una regla `procediment` és per inicialitzar el diccionari `bloc` o per executar les instruccions del seu context. Una vegada finalitzada la inicialització, el booleà `executar` passarà a ser `True` i es farà una visita al context del procediment indicat a l'string `inici`, que per defecte és `Main`. Abans de fer la invocació al procediment principal, però, s'afegeix un diccionari buit a la llista `pila`, representant el nivell del procediment al qual es crida, i servirà com a taula de símbols per aquest nivell. Quan l'execució d'un procediment finalitza, s'elimina el diccionari de la `pila`. S'aplica el mateix per les invocacions. Durant aquest procés, es poden produir errors quan: un procediment ja ha estat definit, el procediment inicial no s'ha definit, el procediment inicial s'ha definit amb paràmetres o hi ha noms de paràmetres formals repetits.  

La llista `partitura` es passa per referència des de l'intèrpret i serveix per guardar totes les notes ja traduïdes que es van reproduint durant l'execució del programa.

## Intèrpret

L'intèrpret s'invoca amb la comanda `python3 jsbach.py fitxer.jsb [Procediment]` (l'extensió dels fitxers per programes en JSBach és `.jsb`). Per defecte, si no s'especifica cap procediment inicial com a argument, el programa comença a executar-se pel procediment `Main`. El programa es llegeix amb el format UTF-8, per poder admetre caràcters especials de l'alfabet alemany. Un cop llegit es fa la invocació del visitador, el qual rep com a paràmetres el procediment inicial i una partitura, que no és res més que una llista a on el visitador anirà afegint les notes musicals (si n'hi ha) reproduïdes al programa. Finalment, quan l'execució del programa finalitza, es fan crides al sistema dels programes externs LilyPond, TiMidity++ i FFmpeg per generar els fitxers `.pdf`, `.midi`, `.wav` i `.mp3`. Els noms d'aquest fitxers coincideixen amb el nom del programa en JSBach introduit.

## Especificació de JSBach

### Comentaris

Els comentaris s'indiquen entre triple titlles (`~~~`). Per exemple, `~~~ Kleines Program in JSBach ~~~`.

### Enters

L'intèrpret JSBach només admet nombres enters. Els operadors amb enters suportats són els aritmètics (`+`, `-`, `*`, `/`, `%`), els quals tenen la mateixa prioritat que en C, i els relacionals (`=`, `/=`, `<`, `>`, `<=`, `>=`), que retornen zero per fals i u per cert. Com que el domini admès és el d'enters, la divisió també és entera. Les expressions amb enters també admeten parèntesis i expressions dins d'expressions.  
  
L'error que es pot produir a l'hora de treballar amb enters es la de divisó per zero.

A continuació es mostra un exemple d'un programa que implementa l'ús d'expressions amb enters, seguit de la seva sortida.
```
Main |:
    n <- 1 + 1
    <!> (((n * (20 - n) + 10) - 10) / 2) % 10
    b <- (n = 2) + 2 * (n < 5) + 0 /= 0
    <!> n b n >= b
:|
```
```
8
2 1 1
```

### Notes

JSBach proporciona uns noms que representen les notes blanques d'un piano, d'acord a la notació anglosaxona. Per tant, el rang de notes comença amb A0 i acaba amb C8 (les notes C, D, E, F, G, A, B (sense número) son sinònims de C4 (Do central), D4, E4, F4, G4, A4, B4). Admeten els operadors `+` i `-` per transposar cap amunt o cap avall segons el nombre de tons indicat. Tot i que la distància entre un Si i un Do i entre un Mi i un Fa és d'un semitò, per simplicitat, s'ha considerat una distancia d'una unitat.  

Internament, encara que les notes es tracten com a constants per a enters, aquestes es guarden com a cadenes de caràcters per poder mantenir coherència a l'hora de fer servir instruccions d'escriptura (no seria molt lògic assignar un C4 a una variable i que la seva escriptura fos 23!). Ara bé, la transposició d'una nota pot resultar en un valor fora del rang [0, 51] i, com a conseqüència, aquest valor passaria a ser considerat com a un enter sense poder tornar a convertir-se en una nota, encara que es torni a aplicar una transposició que el deixi dins del rang de notes (queda com a responsabilitat del programador evitar això).  
  
A continuació es mostra un exemple d'un programa que implementa l'ús de les notes, seguit de la seva sortida.
```
Main |:
    notes <- {C D E F G A B}
    <!> notes
    nota1 <- C4
    nota2 <- nota1 - 1
    nota3 <- nota1 + 1
    <!> nota2 nota1 nota3
    nota4 <- C8
    nota5 <- C8 + 1
    nota6 <- nota5 - 1
    <!> nota4 nota5 nota6
    nota6 <- A0
    nota7 <- nota6 - 1
    nota8 <- nota7 + 1
    <!> nota6 nota7 nota8
    <!> A0 + 7 A1 - 7
:|
```
```
{C4 D4 E4 F4 G4 A4 B4}
B3 C4 D4
C8 52 51
A0 -1 0
A1 A0
```

### Llistes

Les llistes s'escriuen entre claus, amb els seus elements separats per blancs. Poden ser llistes d'enters o de notes, sense poder contenir mai elements de tots dos tipus simultàniament (pel mateix motiu d'abans, tot i que les notes es tracten com a enters, es fa per mantenir coherència).  

Les operacions per a llistes suportades son els d'afegit `l << x`, tall `8< l[i]`, consulta `l[i]` i mida `#l`:
- L'operació  d'afegit `l << x` afegeix l'element `x` a la llista `l`. La llista `l` ha de ser una variable amb una llista. L'element `x` pot ser, en esencia, un enter o una nota, que o bé s'introdueix directament o bé deriva de l'avaluació d'una variable, una transposició, una expressió, una consulta o una mida. Es produeix un error quan: la variable a la qual es vol afegir l'element no és una llista, s'intenta afegir una llista a una altra llista, o bé s'intenta afegir una nota a una llista d'enters o un enter a una llista de notes.
- L'operació de tall `8< l[i]` elimina l'`i`-èsim element de la llista `l`. La llista `l` ha de ser una variable amb una llista. L'índex `i` ha de ser un enter dins el rang [1, `#l`], que o bé s'introdueix directament o bé deriva de l'avaluació d'una variable, una expressió, una mida o una consulta. Es produeix un error quan: s'intenta consultar un element d'una variable que no és una llista, l'índex indicat no és un enter o l'índex és fora de rang.
- L'operació de mida `#l` retorna la llargada de la llista `l`. La llista `l` ha de ser una variable amb una llista. Es produeix un error quan s'intenta  consultar la mida d'una variable que no és una llista.
- L'operació de consulta `l[i]` retorna l'`i`-èsim element de la llista `l`. La llista `l` ha de ser una variable amb una llista. L'índex `i` ha de ser un enter dins el rang [1, `#l`], que o bé s'introdueix directament o bé deriva de l'avaluació d'una variable, una expressió, una mida o una consulta. Es produeix un error quan: s'intenta consultar un element d'una variable que no és una llista, l'índex indicat no és un enter o l'índex és fora de rang.

```
Main |:
    l1 <- {1 2 3 4 5}
    l2 <- l1
    l3 <- {C}
    <!> l1 #l1 l1[#l1 - 2]
    8< l1[#l1]
    8< l1[1]
    l1 << 6
    <!> l1 l2 l1[1] + l2[2]
    <!> l3[1] + 5
:|
```
```
{1 2 3 4 5} 5 3
{2 3 4 6} {1 2 3 4 5} 4
A4
```


### Variables

Les variables començen amb una lletra minúscula. Admet l'alfabet alemany (https://unicode-table.com/en/alphabets/german/), números i el guió baix. Una variable pot contenir un enter, una nota o una llista. Quan es vol accedir a una variable, si aquesta no ha rebut cap valor, el seu valor és zero.  

A continuació es mostra un exemple d'un programa que utilitza variables amb la seva corresponent sortida.
```
Main |:
    b <- 10
    c <- A0
    d <- {1 2 3 4 5 6 7}
    e <- {C D E F G A B}
    <!> a b c d e
:|
```
```
0 10 A0 {1 2 3 4 5 6 7} {C4 D4 E4 F4 G4 A4 B4}
```

### Procediments

Els procediments, a diferència de les variables, començen amb una lletra majúscula. També admet l'alfabet alemany, números i el guió baix. Es poden definir amb paràmetres d'entrada (sense repetir noms formals) i no son res més que conjunts d'instruccions.

### Assignació

L'assignació `<-` permet fer una assignació de variables, enters, notes, llistes (d'enters o de notes), expressions i operadors de consulta per a llistes a una variable. Com en Python, el tipatge és dinàmic. L'assignació de llistes es fa amb còpies (sense fer aliasing).

### Lectura

La instrucció de lectura `<?>` llegeix un valor enter del canal d'entrada estàndard i l'enmagatzema a la variable especificada.

### Escriptura

La instrucció d'escriptura `<!>` admet variables, textos, enters, notes, llistes (d'enters o de notes), expressions i operadors de consulta per a llistes. Les llistes s'escriuen entre claus amb els elements separats entre espais. En el cas d'escriure múltiples paràmetres, s'escriuen a la mateixa línea separats per espais.

### Reproducció

La instrucció de reproducció `<:>` admet notes, llistes de notes, variables i operacions de transposició. Avalua l'expressió corresponent i les notes obtingudes s'afegeixen a la partitura amb el valor d'una negra.  

Es produeix un error quan s'intenta reproduir un valor que no és una nota.

### Invocació de procediments

Una invocació d'un procediment consisteix en l'identificador d'aquest procediment seguit dels paràmetres corresponents. Els procediments no retornen valors i es poden cridar recursivament.

Es produeix un error quan s'invoca un procediment no definit o el nombre de paràmetres donats no corresponen als declarats.

### Condicional `if` `else`

La instrucció condicional té la semàntica habitual `if condicio |: instruccions :| else |: instruccions :|`, on el bloc `else` és optatiu. Una condició admet comparacions entre enters i notes, que poden ser donats directament o derivats de l'avaluació d'una transposició, una variable o una expressió, i pot produir-se un error en el cas que s'intenti fer comparacions de valors amb un tipus diferent a aquests. 


### Iteració `while`

La instrucció iterativa té la semàntica habitual `while condicio |: instruccions :|`. La condició és igual a l'esmentada a l'apartat anterior.
