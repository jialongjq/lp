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
        token = jsbachParser.symbolicNames[l[2].getSymbol().type]
        self.pila[-1][l[0].getText()] = self.visit(l[2])
        print(self.pila)

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
            token = jsbachParser.symbolicNames[l[0].getSymbol().type]
            if token == 'ENTER':
                return int(l[0].getText())
            elif token == 'VARIABLE':
                if l[0].getText() in self.pila[-1]:
                    return self.pila[-1][l[0].getText()]
                self.pila[-1][l[0].getText()] = 0
                return 0
        else:  # len(l) == 3
            if l[0].getText() == '(':
                return self.visit(l[1])
            else:
                var1 = self.visit(l[0])
                var2 = self.visit(l[2])
                token = jsbachParser.symbolicNames[l[1].getSymbol().type]
                if token == 'SUMA':
                    #if type(var1) != type(var2):
                    #    raise Exception("Operador '+' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
                    return var1 + var2
                elif token == 'RESTA':
                    #if type(var1) != type(var2) or type(var1) == string:
                    #    raise Exception("Operador '-' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
                    return var1 - var2
                elif token == 'MULTIPLICACIO':
                    #if type(var1) == type(var2) and type(var1) == string:
                    #    raise Exception("Operador '*' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
                    return var1 * var2
                elif token == 'DIVISIO':
                    #if type(var1) != type(var2) or type(var1) == string:
                    #    raise Exception("Operador '/' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
                    return var1 / var2
                elif token == 'MODUL':
                    #if type(var1) != type(var2) or type(var1) == string:
                    #    raise Exception("Operador '%' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
                    return var1 % var2
                elif token == 'MAJOR':
                    #if type(var1) != type(var2):
                    #    raise Exception("Operador '>' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
                    return 1 if var1 > var2 else 0
                elif token == 'MAJORIGUAL':
                    if type(var1) != type(var2):
                        raise Exception("Operador '>=' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
                    return 1 if var1 >= var2 else 0
                elif token == 'MENOR':
                    if type(var1) != type(var2):
                        raise Exception("Operador '<' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
                    return 1 if var1 < var2 else 0
                elif token == 'MENORIGUAL':
                    if type(var1) != type(var2):
                        raise Exception("Operador '<=' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
                    return 1 if var1 <= var2 else 0
                elif token == 'IGUAL':
                    if type(var1) != type(var2):
                        raise Exception("Operador '=' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
                    return 1 if var1 == var2 else 0
                elif token == 'DIFERENT':
                    if type(var1) != type(var2):
                        raise Exception("Operador '/=' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
                    return 1 if var1 != var2 else 0
        
    def visitCondicio(self, ctx):
        l = list(ctx.getChildren())
        var1 = self.visit(l[0])
        var2 = self.visit(l[2])
        token = jsbachParser.symbolicNames[l[1].getSymbol().type]
        if token == 'MAJOR':
            if type(var1) != type(var2):
                raise Exception("Operador '>' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
            return 1 if var1 > var2 else 0
        elif token == 'MAJORIGUAL':
            if type(var1) != type(var2):
                raise Exception("Operador '>=' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
            return 1 if var1 >= var2 else 0
        elif token == 'MENOR':
            if type(var1) != type(var2):
                raise Exception("Operador '<' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
            return 1 if var1 < var2 else 0
        elif token == 'MENORIGUAL':
            if type(var1) != type(var2):
                raise Exception("Operador '<=' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
            return 1 if var1 <= var2 else 0
        elif token == 'IGUAL':
            if type(var1) != type(var2):
                raise Exception("Operador '=' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
            return 1 if var1 == var2 else 0
        elif token == 'DIFERENT':
            if type(var1) != type(var2):
                raise Exception("Operador '/=' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
            return 1 if var1 != var2 else 0
       
    def visitText(self, ctx):
        l = list(ctx.getChildren())
        return l[0].getText()[1:-1]
        
    def visitAfegit(self, ctx):
        l = list(ctx.getChildren())
        token = jsbachParser.symbolicNames[l[0].getSymbol().type]
        nom = l[0].getText()
        if not nom in self.pila[-1]:
            raise Exception("La variable %s no existeix!" % nom)
        llista = self.pila[-1][nom]
        if not type(llista) == list:
            raise Exception("La variable %s no és una llista!" % nom)
        val = self.visit(l[2])
        llista.append(val)
        self.pila[-1][l[0].getText()] = llista
            
        
    def visitLlista(self, ctx):
        l = list(ctx.getChildren())
        token = jsbachParser.symbolicNames[l[0].getSymbol().type]
        if token == 'VARIABLE':
            if l[0].getText() in self.pila[-1]:
                if type(self.pila[-1][l[0].getText()]) == list:
                    return self.pila[-1][l[0].getText()]
                raise Exception('La variable %s no és una llista!' % l[0].getText())
            raise Exception('La variable %s no existeix!' % l[0].getText())
        else:
            llista = []
            for i in range(1, len(l)-1):
                llista.append(int(l[i].getText()))
            return llista

