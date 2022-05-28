if __name__ is not None and "." in __name__:
    from .jsbachParser import jsbachParser
    from .jsbachVisitor import jsbachVisitor
else:
    from jsbachParser import jsbachParser
    from jsbachVisitor import jsbachVisitor

notaEnter = {'A0' : 0, 'B0' : 1,
'C1' : 2, 'D1' : 3, 'E1' : 4, 'F1' : 5, 'G1' : 6, 'A1' : 7, 'B1' : 8, 
'C2' : 9, 'D2' : 10, 'E2' : 11, 'F2' : 12, 'G2' : 13, 'A2' : 14, 'B2' : 15, 
'C3' : 16, 'D3' : 17, 'E3' : 18, 'F3' : 19, 'G3' : 20, 'A3' : 21, 'B3' : 22, 
'C4' : 23, 'D4' : 24, 'E4' : 25, 'F4' : 26, 'G4' : 27, 'A4' : 28, 'B4' : 29, 
'C5' : 30, 'D5' : 31, 'E5' : 32, 'F5' : 33, 'G5' : 34, 'A5' : 35, 'B5' : 36, 
'C6' : 37, 'D6' : 38, 'E6' : 39, 'F6' : 40, 'G6' : 41, 'A6' : 42, 'B6' : 43, 
'C7' : 44, 'D7' : 45, 'E7' : 46, 'F7' : 47, 'G7' : 48, 'A7' : 49, 'B7' : 50, 
'C8' : 51}

enterNota = {0: 'A0', 1: 'B0',
2: 'C1', 3: 'D1', 4: 'E1', 5: 'F1', 6: 'G1', 7: 'A1', 8: 'B1',
9: 'C2', 10: 'D2', 11: 'E2', 12: 'F2', 13: 'G2', 14: 'A2', 15: 'B2',
16: 'C3', 17: 'D3', 18: 'E3', 19: 'F3', 20: 'G3', 21: 'A3', 22: 'B3',
23: 'C4', 24: 'D4', 25: 'E4', 26: 'F4', 27: 'G4', 28: 'A4', 29: 'B4',
30: 'C5', 31: 'D5', 32: 'E5', 33: 'F5', 34: 'G5', 35: 'A5', 36: 'B5',
37: 'C6', 38: 'D6', 39: 'E6', 40: 'F6', 41: 'G6', 42: 'A6', 43: 'B6',
44: 'C7', 45: 'D7', 46: 'E7', 47: 'F7', 48: 'G7', 49: 'A7', 50: 'B7',
51: 'C8'}

enterOutput = {0: "a,,,", 1: 'b,,,',
2: "c,,", 3: "d,,", 4: "e,,", 5: "f,,", 6: "g,,", 7: "a,,", 8: "b,,",
9: "c,", 10: "d,", 11: "e,", 12: "f,", 13: "g,", 14: "a,", 15: "b,",
16: 'c', 17: 'd', 18: 'e', 19: 'f', 20: 'g', 21: 'a', 22: 'b',
23: "c'", 24: "d'", 25: "e'", 26: "f'", 27: "g'", 28: "a'", 29: "b'",
30: "c''", 31: "d''", 32: "e''", 33: "f''", 34: "g''", 35: "a''", 36: "b''",
37: "c'''", 38: "d'''", 39: "e'''", 40: "f'''", 41: "g'''", 42: "a'''", 43: "b'''",
44: "c''''", 45: "d''''", 46: "e''''", 47: "f''''", 48: "g''''", 49: "a''''", 50: "b''''",
51: "c'''''"}

class TreeVisitor(jsbachVisitor):
    def __init__(self, inici, partitura):
        self.executar = False
        self.bloc = {}
        self.parametres = {}
        self.pila = []
        self.inici = inici
        print(self.inici)
        self.partitura = partitura

    def isNota(self, nota):
        return type(nota) == str and nota in notaEnter

    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        for procediment in l:
            self.visit(procediment)
        self.executar = True
        if not self.inici in self.bloc:
            raise Exception("No s'ha definit el procediment '%s'!" % self.inici)
        self.pila.append({})
        self.visit(self.bloc[self.inici])
        self.pila.pop()

    def visitProcediment(self, ctx):
        if not self.executar:
            l = list(ctx.getChildren())
            nom = l[0].getText()
            self.bloc[nom] = ctx
            self.parametres[nom] = []
            i = 1
            while l[i].getText() != '|:':
                self.parametres[nom].append(l[i].getText())
                i += 1
        else:
            l = list(ctx.getChildren())
            for i in range(1, len(l)):
                if l[i].getText() == '|:':
                    for j in range(i+1, len(l)-1):
                        self.visit(l[j])
                    break
                
    def visitInstruccio(self, ctx):
        l = list(ctx.getChildren())
        self.visit(l[0])        

    def visitAssignacio(self, ctx):
        l = list(ctx.getChildren())
        key = l[0].getText()
        assig = self.visit(l[2])
        if type(assig) == list:
            self.pila[-1][key] = assig.copy()
        else:
            self.pila[-1][key] = assig

    def visitLectura(self, ctx):
        l = list(ctx.getChildren())
        self.pila[-1][l[1].getText()] = int(input('? '))

    def visitEscriptura(self, ctx):
        l = list(ctx.getChildren())
        for i in range(1, len(l)):
            output = self.visit(l[i])
            if type(output) == list:
                print('{', end = '')
                print(*output, sep=' ', end = '')
                print('}', end = '')
            else:
                print(output, end = '')
            if i < len(l)-1:
                print(' ', end = '')
        print('')
            
    def visitReproduccio(self, ctx):
        l = list(ctx.getChildren())
        notes = self.visit(l[1])
        if type(notes) == list:
            for n in notes:
                nota = n
                if not self.isNota(nota):
                    raise Exception("S'ha intentat reproduir un valor que no és una nota!")
                self.partitura.append(enterOutput[notaEnter[nota]])
        elif self.isNota(notes):
            self.partitura.append(enterOutput[notaEnter[notes]])
        else:
            raise Exception("S'ha intentat reproduir un valor que no és una nota!")
            
    def visitInvocacio(self, ctx):
        l = list(ctx.getChildren())
        nom = l[0].getText()
        if not nom in self.bloc:
            raise Exception('El procediment %s no esta definit!' % nom)
        if len(l)-1 != len(self.parametres[nom]):
            raise Exception('El nombre de parametres no coincideix!')
        diccionari = {}
        for i in range(1, len(l)):
            diccionari[self.parametres[nom][i-1]] = self.visit(l[i])
        self.pila.append(diccionari)
        self.visit(self.bloc[nom])
        self.pila.pop()
        
    def visitCondicional(self, ctx):
        l = list(ctx.getChildren())
        indexelse = -1
        indexendif = len(l)-1
        for i in range(len(l)):
            if l[i].getText() == 'else':
                indexelse = i
                indexendif = indexelse-1
                break
        if self.visit(l[1]) == 1:
            for i in range(3, indexendif):
                self.visit(l[i])
        elif indexelse != -1:
            for i in range(indexelse+2, len(l)-1):
                self.visit(l[i])
        
    def visitIteracio(self, ctx):
        l = list(ctx.getChildren())
        while self.visit(l[1]) == 1:
            for i in range(3, len(l)-1):
                self.visit(l[i])
        
    def visitExpressio(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
            return self.visit(l[0])
        else:
            if l[0].getText() == '(':
                return self.visit(l[1])
            else:
                var1 = self.visit(l[0])
                var2 = self.visit(l[2])
                if type(var1) != int or (type(var2) != int):
                    raise Exception("Operador '%s' no suportat entre variables de tipus %s i %s" % (l[1].getText(), type(var1), type(var2)))
                
                token = jsbachParser.symbolicNames[l[1].getSymbol().type]
                if token == 'SUMA':
                    return var1 + var2
                elif token == 'RESTA':
                    return var1 - var2
                elif token == 'MULTIPLICACIO':
                    return var1 * var2
                elif token == 'DIVISIO':
                    if var2 == 0:
                        raise Exception("Divisió per zero!")
                    return var1 // var2
                elif token == 'MODUL':
                    if var2 == 0:
                        raise Exception("Divisió per zero!")
                    return var1 % var2
                elif token == 'MAJOR':
                    return 1 if var1 > var2 else 0
                elif token == 'MAJORIGUAL':
                    return 1 if var1 >= var2 else 0
                elif token == 'MENOR':
                    return 1 if var1 < var2 else 0
                elif token == 'MENORIGUAL':
                    return 1 if var1 <= var2 else 0
                elif token == 'IGUAL':
                    return 1 if var1 == var2 else 0
                elif token == 'DIFERENT':
                    return 1 if var1 != var2 else 0

    def visitTransposicio(self, ctx):
        l = list(ctx.getChildren())
        var1 = self.visit(l[0])
        nota = False
        if type(var1) == str:
            if len(var1) == 1:
                var1 = var1 + '4'
            if var1 in notaEnter:
                nota = True
                var1 = notaEnter[var1]
        var2 = self.visit(l[2])
        if type(var1) != int or (type(var2) != int):
            raise Exception("Operador '%s' no suportat entre variables de tipus %s i %s!" % (l[1].getText(), type(var1), type(var2)))
        token = jsbachParser.symbolicNames[l[1].getSymbol().type]
        ret = 0
        if token == 'SUMA':
            ret = var1 + var2
        elif token == 'RESTA':
            ret = var1 - var2
        if nota and ret >= 0 and ret <= 51:
            ret = enterNota[ret]
        return ret

    def visitCondicio(self, ctx):
        l = list(ctx.getChildren())
        var1 = self.visit(l[0])
        if var1 in notaEnter:
            var1 = notaEnter[var1]
        var2 = self.visit(l[2])
        if var2 in notaEnter:
            var2 = notaEnter[var2]
        if type(var1) != int or type(var2) != int:
            raise Exception("Operador '%s' no suportat entre variables de tipus %s i %s" % (l[1].getText(), type(var1), type(var2)))
        token = jsbachParser.symbolicNames[l[1].getSymbol().type]
        if token == 'MAJOR':
            return 1 if var1 > var2 else 0
        elif token == 'MAJORIGUAL':
            return 1 if var1 >= var2 else 0
        elif token == 'MENOR':
            return 1 if var1 < var2 else 0
        elif token == 'MENORIGUAL':
            return 1 if var1 <= var2 else 0
        elif token == 'IGUAL':
            return 1 if var1 == var2 else 0
        elif token == 'DIFERENT':
            return 1 if var1 != var2 else 0
       
    def visitText(self, ctx):
        l = list(ctx.getChildren())
        return l[0].getText()[1:-1]
        
    def visitAfegit(self, ctx):
        l = list(ctx.getChildren())
        nom = l[0].getText()
        if not nom in self.pila[-1]:
            raise Exception("La variable %s no existeix!" % nom)
        llista = self.pila[-1][nom]
        if not type(llista) == list:
            raise Exception("La variable %s no és una llista!" % nom)
        val = self.visit(l[2])
        llista.append(val)
        self.pila[-1][l[0].getText()] = llista

    def visitTall(self, ctx):
        l = list(ctx.getChildren())  
        llista = self.visit(l[1])
        if type(llista) != list:
            raise Exception("La variable '%s' no és de tipus 'llista'!" % l[1].getText())
        index = self.visit(l[3])
        if index < 1 or index > len(llista):
            raise Exception("Índex fora de rang!")
        llista.pop(index-1)          

    def visitMida(self, ctx):
        l = list(ctx.getChildren())  
        llista = self.visit(l[1])
        if type(llista) != list:
            raise Exception("La variable '%s' no és de tipus 'llista'!" % l[1].getText())
        return len(llista)

    def visitConsulta(self, ctx):
        l = list(ctx.getChildren())  
        llista = self.visit(l[0])
        if type(llista) != list:
            raise Exception("La variable '%s' no és de tipus 'llista'!" % l[0].getText())
        index = self.visit(l[2])
        if index < 1 or index > len(llista):
            raise Exception("Índex fora de rang!")
        return llista[index-1]       

    def visitEnters(self, ctx):
        l = list(ctx.getChildren())
        enters = []
        for i in range(1, len(l)-1):
            enters.append(int(l[i].getText()))
        return enters

    def visitNotes(self, ctx):
        l = list(ctx.getChildren())
        notes = []
        for i in range(1, len(l)-1):
            nota = l[i].getText()
            if len(nota) == 1:
                nota += '4'
            notes.append(nota)
        return notes

    def visitVariable(self, ctx):
        l = list(ctx.getChildren())
        nom = l[0].getText()
        if not nom in self.pila[-1]:
            self.pila[-1][nom] = 0
            return 0
        return self.pila[-1][nom]

    def visitEnter(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())

    def visitNota(self, ctx):
        l = list(ctx.getChildren())
        nota = l[0].getText()
        if len(nota) == 1:
            nota += '4'
        return nota