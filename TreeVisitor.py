if __name__ is not None and "." in __name__:
    from .jsbachParser import jsbachParser
    from .jsbachVisitor import jsbachVisitor
else:
    from jsbachParser import jsbachParser
    from jsbachVisitor import jsbachVisitor

notaEnter = {'A0': 0, 'B0': 1,
             'C1': 2, 'D1': 3, 'E1': 4, 'F1': 5, 'G1': 6, 'A1': 7, 'B1': 8,
             'C2': 9, 'D2': 10, 'E2': 11, 'F2': 12, 'G2': 13, 'A2': 14, 'B2': 15,
             'C3': 16, 'D3': 17, 'E3': 18, 'F3': 19, 'G3': 20, 'A3': 21, 'B3': 22,
             'C4': 23, 'D4': 24, 'E4': 25, 'F4': 26, 'G4': 27, 'A4': 28, 'B4': 29,
             'C5': 30, 'D5': 31, 'E5': 32, 'F5': 33, 'G5': 34, 'A5': 35, 'B5': 36,
             'C6': 37, 'D6': 38, 'E6': 39, 'F6': 40, 'G6': 41, 'A6': 42, 'B6': 43,
             'C7': 44, 'D7': 45, 'E7': 46, 'F7': 47, 'G7': 48, 'A7': 49, 'B7': 50,
             'C8': 51}

enterNota = {0: 'A0', 1: 'B0',
             2: 'C1', 3: 'D1', 4: 'E1', 5: 'F1', 6: 'G1', 7: 'A1', 8: 'B1',
             9: 'C2', 10: 'D2', 11: 'E2', 12: 'F2', 13: 'G2', 14: 'A2', 15: 'B2',
             16: 'C3', 17: 'D3', 18: 'E3', 19: 'F3', 20: 'G3', 21: 'A3', 22: 'B3',
             23: 'C4', 24: 'D4', 25: 'E4', 26: 'F4', 27: 'G4', 28: 'A4', 29: 'B4',
             30: 'C5', 31: 'D5', 32: 'E5', 33: 'F5', 34: 'G5', 35: 'A5', 36: 'B5',
             37: 'C6', 38: 'D6', 39: 'E6', 40: 'F6', 41: 'G6', 42: 'A6', 43: 'B6',
             44: 'C7', 45: 'D7', 46: 'E7', 47: 'F7', 48: 'G7', 49: 'A7', 50: 'B7',
             51: 'C8'}

notaOutput = {'A0': "a,,,", 'B0': 'b,,,',
              'C1': "c,,", 'D1': "d,,", 'E1': "e,,", 'F1': "f,,", 'G1': "g,,", 'A1': "a,,", 'B1': "b,,",
              'C2': "c,", 'D2': "d,", 'E2': "e,", 'F2': "f,", 'G2': "g,", 'A2': "a,", 'B2': "b,",
              'C3': 'c', 'D3': 'd', 'E3': 'e', 'F3': 'f', 'G3': 'g', 'A3': 'a', 'B3': 'b',
              'C4': "c'", 'D4': "d'", 'E4': "e'", 'F4': "f'", 'G4': "g'", 'A4': "a'", 'B4': "b'",
              'C5': "c''", 'D5': "d''", 'E5': "e''", 'F5': "f''", 'G5': "g''", 'A5': "a''", 'B5': "b''",
              'C6': "c'''", 'D6': "d'''", 'E6': "e'''", 'F6': "f'''", 'G6': "g'''", 'A6': "a'''", 'B6': "b'''",
              'C7': "c''''", 'D7': "d''''", 'E7': "e''''", 'F7': "f''''", 'G7': "g''''", 'A7': "a''''", 'B7': "b''''",
              'C8': "c'''''"}


class TreeVisitor(jsbachVisitor):
    def __init__(self, inici, partitura):
        self.executar = False
        self.bloc = {}
        self.parametres = {}
        self.pila = []
        self.inici = inici
        self.partitura = partitura

    def isNota(self, nota):
        return type(nota) == str and nota in notaEnter

    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        for procediment in l:
            self.visit(procediment)
        self.executar = True
        if self.inici not in self.bloc:
            raise Exception(
                "No s'ha definit el procediment '%s'!" % self.inici)
        if len(self.parametres[self.inici]) != 0:
            raise Exception("El procediment inicial no admet paràmetres!")
        self.pila.append({})
        self.visit(self.bloc[self.inici])
        self.pila.pop()

    def visitProcediment(self, ctx):
        if not self.executar:
            l = list(ctx.getChildren())
            nom = l[0].getText()
            if nom in self.bloc:
                raise Exception("El procediment %s ja està definit!" % nom)
            self.bloc[nom] = ctx
            self.parametres[nom] = []
            i = 1
            while l[i].getText() != '|:':
                if l[i].getText() in self.parametres[nom]:
                    raise Exception(
                        "No es poden repetir els noms dels paràmetres formals d'un procediment!")
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
        self.pila[-1][l[1].getText()] = int(input('<?> '))

    def visitEscriptura(self, ctx):
        l = list(ctx.getChildren())
        for i in range(1, len(l)):
            output = self.visit(l[i])
            if type(output) == list:
                print('{', end='')
                print(*output, sep=' ', end='')
                print('}', end='')
            else:
                print(output, end='')
            if i < len(l)-1:
                print(' ', end='')
        print('')

    def visitReproduccio(self, ctx):
        l = list(ctx.getChildren())
        notes = self.visit(l[1])
        if type(notes) == list:
            for n in notes:
                nota = n
                if not self.isNota(nota):
                    raise Exception(
                        "S'ha intentat reproduir un valor que no és una nota!")
                self.partitura.append(notaOutput[nota])
        elif self.isNota(notes):
            self.partitura.append(notaOutput[notes])
        else:
            raise Exception(
                "S'ha intentat reproduir un valor que no és una nota!")

    def visitInvocacio(self, ctx):
        l = list(ctx.getChildren())
        nom = l[0].getText()
        if nom not in self.bloc:
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

    def visitAfegit(self, ctx):
        l = list(ctx.getChildren())
        llista = self.visit(l[0])
        if not type(llista) == list:
            raise Exception("La variable %s no és una llista!" %
                            l[0].getText())
        val = self.visit(l[2])
        if type(val) == list:
            raise Exception("No es pot afegir una llista a una altra llista!")
        else:
            if len(llista) > 0:
                if type(llista[0]) == int and type(val) == str:
                    raise Exception(
                        "No es pot afegir una nota a una llista d'enters!")
                elif type(llista[0]) == str and type(val) == int:
                    raise Exception(
                        "No es pot afegir un enter a una llista de notes!")
            llista.append(val)
        self.pila[-1][l[0].getText()] = llista

    def visitTall(self, ctx):
        l = list(ctx.getChildren())
        llista = self.visit(l[1])
        if type(llista) != list:
            raise Exception(
                "La variable '%s' no és de tipus 'llista'!" % l[1].getText())
        index = self.visit(l[3])
        if type(index) != int:
            raise Exception("L'índex ha de ser un enter!")
        if index < 1 or index > len(llista):
            raise Exception("Índex fora de rang!")
        llista.pop(index-1)

    def visitMida(self, ctx):
        l = list(ctx.getChildren())
        llista = self.visit(l[1])
        if type(llista) != list:
            raise Exception(
                "La variable '%s' no és de tipus 'llista'!" % l[1].getText())
        return len(llista)

    def visitConsulta(self, ctx):
        l = list(ctx.getChildren())
        llista = self.visit(l[0])
        if type(llista) != list:
            raise Exception(
                "La variable '%s' no és de tipus 'llista'!" % l[0].getText())
        index = self.visit(l[2])
        if type(index) != int:
            raise Exception("L'índex ha de ser un enter!")
        if index < 1 or index > len(llista):
            raise Exception("Índex fora de rang!")
        return llista[index-1]

    def visitTransposicio(self, ctx):
        l = list(ctx.getChildren())
        var1 = self.visit(l[0])
        nota = False
        if self.isNota(var1):
            nota = True
            var1 = notaEnter[var1]
        var2 = self.visit(l[2])
        if type(var1) != int or (type(var2) != int):
            raise Exception("Operador '%s' no suportat entre variables de tipus %s i %s!" % (
                l[1].getText(), type(var1), type(var2)))
        token = jsbachParser.symbolicNames[l[1].getSymbol().type]
        ret = 0
        if token == 'SUMA':
            ret = var1 + var2
        elif token == 'RESTA':
            ret = var1 - var2
        if nota and ret >= 0 and ret <= 51:
            ret = enterNota[ret]
        return ret

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
                    raise Exception("Operador '%s' no suportat entre variables de tipus %s i %s" % (
                        l[1].getText(), type(var1), type(var2)))

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

    def visitCondicio(self, ctx):
        l = list(ctx.getChildren())
        var1 = self.visit(l[0])
        if var1 in notaEnter:
            var1 = notaEnter[var1]
        var2 = self.visit(l[2])
        if var2 in notaEnter:
            var2 = notaEnter[var2]
        if type(var1) != int or type(var2) != int:
            raise Exception("Operador '%s' no suportat entre variables de tipus %s i %s" % (
                l[1].getText(), type(var1), type(var2)))
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

    def visitEnters(self, ctx):
        l = list(ctx.getChildren())
        enters = []
        for i in range(1, len(l)-1):
            enters.append(self.visit(l[i]))
        return enters

    def visitNotes(self, ctx):
        l = list(ctx.getChildren())
        notes = []
        for i in range(1, len(l)-1):
            notes.append(self.visit(l[i]))
        return notes

    def visitVariable(self, ctx):
        l = list(ctx.getChildren())
        nom = l[0].getText()
        if nom not in self.pila[-1]:
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

    def visitText(self, ctx):
        l = list(ctx.getChildren())
        return l[0].getText()[1:-1]
