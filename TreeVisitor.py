if __name__ is not None and "." in __name__:
    from .jsbachParser import jsbachParser
    from .jsbachVisitor import jsbachVisitor
else:
    from jsbachParser import jsbachParser
    from jsbachVisitor import jsbachVisitor

class TreeVisitor(jsbachVisitor):
    def __init__(self):
        self.executar = False
        self.bloc = {}
        self.parametres = {}
        self.pila = []

    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        for procediment in l:
            self.visit(procediment)
        self.executar = True
        if not 'Main' in self.bloc:
            raise Exception("No s'ha definit el procediment 'Main'!")
        self.pila.append({})
        self.visit(self.bloc['Main'])
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
        print('REPRODUCCIO')
            
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
                if type(var1) != int or type(var2) != int:
                    raise Exception("Operador '%s' no suportat entre variables de tipus %s i %s" % (l[1].getText(), type(var1), type(var2)))
                token = jsbachParser.symbolicNames[l[1].getSymbol().type]
                if token == 'SUMA':
                    return var1 + var2
                elif token == 'RESTA':
                    return var1 - var2
                elif token == 'MULTIPLICACIO':
                    return var1 * var2
                elif token == 'DIVISIO':
                    return var1 / var2
                elif token == 'MODUL':
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
        var2 = self.visit(l[2])
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

    def visitLlista(self, ctx):
        l = list(ctx.getChildren())
        llista = []
        for i in range(1, len(l)-1):
            llista.append(int(l[i].getText()))
        return llista

    # Funcio que facilita l'acces a una variable
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