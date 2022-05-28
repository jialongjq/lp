# Especificació de JSBach
Aquesta pàgina descriu la implementació feta per la pràctica de GEI-LP (edició 2021-2022 Q2), el doble intèrpret de JSBach.

# Característiques bàsiques

## Enters
L'intèrpret JSBach només admet nombres enters. Els operadors amb enters suportats són els aritmètics (`+`, `-`, `*`, `/`, `%`), els quals tenen la mateixa prioritat que en C, i els relacionals (`=`, `/=`, `<`, `>`, `<=`, `>=`), que retornen zero per fals i u per cert. Com que el domini admès és el d'enters, la divisió també és entera.  
  
L'error que es pot produir a l'hora de treballar amb enters es la de divisó per zero.

## Notes
JSBach proporciona uns noms que representen les notes blanques d'un piano, d'acord a la notació anglosaxona. Per tant, el rang de notes comença amb A0 i acaba amb C8 (les notes C, D, E, F, G, A, B (sense número) son sinónims de C4 (Do central), D4, E4, F4, G4, A4, B4). Admeten els operadors `+` i `-` per transposar cap amunt o cap avall segons el nombre de tons indicat.  

Internament, encara que les notes es tracten com a constants per a enters, aquestes es guarden com a cadenes de caràcters per poder mantenir coherència a l'hora de fer servir instruccions d'escriptura (no seria molt lògic assignar un C4 a una variable i que la seva escriptura fos [NUMERO]!). Ara bé, la transposició d'una nota pot
  
Per exemple, 
```

```

## Variables
Les variables començen amb una lletra minúscula. Admet l'alfabet alemany, números i el guió baix. Una variable pot contenir un enter, una nota o una llista. Quan es vol accedir a una variable, si aquesta no ha rebut cap valor, el seu valor és zero.

# Instruccions

## Escriptura
La instrucció d'escriptura `<!>` admet variables, textos, enters, notes, llistes (d'enters o de notes), expressions i operadors de consulta per a llistes.
