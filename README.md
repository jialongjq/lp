# JSBach
Aquesta pàgina descriu la implementació feta per la pràctica de GEI-LP (edició 2021-2022 Q2), el doble intèrpret de JSBach.

## Gramàtica ANTLR

La gramàtica proposada consisteix en un conjunt de procediments com a arrel, on cada procediment és un conjunt d'instruccions.  

Cal diferenciar les regles que internament retornen un valor amb les que no en retornen cap. Aquelles que no retornen cap valor son considerades instruccions (`assignacio`, `lectura`, `escriptura`, `reproduccio`, `invocacio`, `condicional`, `iteracio`, `afegit` i `tall`). Les que sí en retornen un valor (`mida`, `consulta`, `enters`, `notes`, `transposicio`, `expressio`, `condicio`, `text`, `variable`, `enter` i `nota`) s'utilitzen per complementar les instruccions segons les necessitats de cadascuna, les quals s'explicaran més endavant.  

Els tokens s'han utilitzat principalment per permetre una millor llegibilitat de la gramàtica. Els que es consulten al visitador son els operadors aritmètics i relacionals.

Un tret que pot semblar confús és l'ús alternat de la regla `variable` i el token `VARIABLE` a les regles. La diferència clau és que el token `VARIABLE` s'utilitza quan no és necessari l'accés al valor d'una variable. A més a més, les regles `variable`, `enter`, `nota` i `text`, tot i semblar innecessaris perquè no són res més que un token, son realment molt útils a l'hora de fer resolucions perquè internament es poden fer visites directament sense importar els tipus de node, fet que permet estalviar molta lògica.

## Visitador

## Intèrpret

L'intèrpret s'invoca amb la comanda `python3 jsbach.py fitxer.jsb [Procediment]` (l'extensió dels fitxers per programes en JSBach és `.jsb`). Per defecte, si no s'especifica cap procediment inicial com a argument, el programa comença a executar-se pel procediment `Main`. El programa es llegeix amb el format UTF-8, per poder admetre caràcters especials de l'alfabet alemany. Un cop llegit es fa la invocació del visitador, el qual rep com a paràmetres el procediment inicial i una partitura, que no és res més que una llista a on el visitador anirà afegint les notes musicals (si n'hi ha) reproduïdes al programa. Finalment, quan l'execució del programa finalitza, es fan crides al sistema dels programes externs LilyPond, TiMidity++ i ffmpeg per generar els arxius `.pdf`, `.midi`, `.wav` i `.mp3`, i es reprodueix aquest últim arxiu `.mp3` amb la instrucció `playsound('fitxer.mp3')` importada de la llibreria `playsound`. Els noms d'aquest fitxers coincideixen amb el nom del programa en JSBach introduit.

# Especificació de JSBach

## Comentaris

Els comentaris s'indiquen entre triple titlles (`~~~`). Per exemple, `~~~ Kleines Program in JSBach ~~~`.

## Enters

L'intèrpret JSBach només admet nombres enters. Els operadors amb enters suportats són els aritmètics (`+`, `-`, `*`, `/`, `%`), els quals tenen la mateixa prioritat que en C, i els relacionals (`=`, `/=`, `<`, `>`, `<=`, `>=`), que retornen zero per fals i u per cert. Com que el domini admès és el d'enters, la divisió també és entera.  
  
L'error que es pot produir a l'hora de treballar amb enters es la de divisó per zero.

## Notes

JSBach proporciona uns noms que representen les notes blanques d'un piano, d'acord a la notació anglosaxona. Per tant, el rang de notes comença amb A0 i acaba amb C8 (les notes C, D, E, F, G, A, B (sense número) son sinònims de C4 (Do central), D4, E4, F4, G4, A4, B4). Admeten els operadors `+` i `-` per transposar cap amunt o cap avall segons el nombre de tons indicat. Tot i que la distància entre un Si i un Do i entre un Mi i un Fa és d'un semitò, per simplicitat, s'ha considerat una distancia d'una unitat.  

Internament, encara que les notes es tracten com a constants per a enters, aquestes es guarden com a cadenes de caràcters per poder mantenir coherència a l'hora de fer servir instruccions d'escriptura (no seria molt lògic assignar un C4 a una variable i que la seva escriptura fos 23!). Ara bé, la transposició d'una nota pot resultar en un valor fora del rang [0, 51] i, com a conseqüència, aquest valor passaria a ser considerat com a un enter sense poder tornar a convertir-se en una nota, encara que es torni a aplicar una transposició que el deixi dins del rang de notes (queda com a responsabilitat del programador evitar això).  
  
En aquest exemple, les quatre instruccions d'escriptura tenen com a sortida `{C4 D4 E4 F4 G4 A4 B4}`, `B3 C4 D4`, `C8 52 51` i `A0 -1 0`, respectivament.
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
:|
```

## Llistes

Les llistes s'escriuen entre claus, amb els seus elements separats per blancs. Poden ser llistes d'enters o de notes, sense poder contenir mai elements de tots dos tipus simultàniament (pel mateix motiu d'abans, tot i que les notes es tracten com a enters, es fa per mantenir coherència).  

Les operacions per a llistes suportades son els d'afegit `l << x`, tall `8< l[i]`, consulta `l[i]` i mida `#l`:
- L'operació  d'afegit `l << x` afegeix l'element `x` a la llista `l`. La llista `l` ha de ser una variable amb una llista. L'element `x` pot ser, en esencia, un enter o una nota, que o bé s'introdueix directament o bé deriva de l'avaluació d'una variable, una transposició, una expressió, una consulta o una mida. Es produeix un error quan: la variable a la qual es vol afegir l'element no és una llista, s'intenta afegir una llista a una altra llista, o bé s'intenta afegir una nota a una llista d'enters o un enter a una llista de notes.
- L'operació de tall `8< l[i]` elimina l'`i`-èsim element de la llista `l`. La llista `l` ha de ser una variable amb una llista. L'índex `i` ha de ser un enter dins el rang [1, `#l`], que o bé s'introdueix directament o bé deriva de l'avaluació d'una variable, una expressió, una mida o una consulta. Es produeix un error quan: s'intenta consultar un element d'una variable que no és una llista, l'índex indicat no és un enter o l'índex és fora de rang.
- L'operació de mida `#l` retorna la llargada de la llista `l`. La llista `l` ha de ser una variable amb una llista. Es produeix un error quan s'intenta  consultar la mida d'una variable que no és una llista.
- L'operació de consulta `l[i]` retorna l'`i`-èsim element de la llista `l`. La llista `l` ha de ser una variable amb una llista. L'índex `i` ha de ser un enter dins el rang [1, `#l`], que o bé s'introdueix directament o bé deriva de l'avaluació d'una variable, una expressió, una mida o una consulta. Es produeix un error quan: s'intenta consultar un element d'una variable que no és una llista, l'índex indicat no és un enter o l'índex és fora de rang.


## Variables

Les variables començen amb una lletra minúscula. Admet l'alfabet alemany (https://unicode-table.com/en/alphabets/german/), números i el guió baix. Una variable pot contenir un enter, una nota o una llista. Quan es vol accedir a una variable, si aquesta no ha rebut cap valor, el seu valor és zero.  

Per exemple, la sortida d'aquest programa seria `0`.
```
Main |:
    <!> x
:|
```

## Procediments

Els procediments, a diferència de les variables, començen amb una lletra majúscula. També admet l'alfabet alemany, números i el guió baix. Es poden definir amb paràmetres d'entrada i no son res més que conjunts d'instruccions.

## Escriptura
La instrucció d'escriptura `<!>` admet variables, textos, enters, notes, llistes (d'enters o de notes), expressions i operadors de consulta per a llistes.
