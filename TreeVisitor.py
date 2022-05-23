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
        for funcio in l:
            self.visit(funcio)
        self.executar = True
        if not 'Main' in self.bloc:
            raise Exception("No s'ha definit el procediment 'Main'!")
        self.visit(self.bloc['Main'])

    def visitProcediment(self, ctx):
        if not self.executar:
            l = list(ctx.getChildren())
            nom = l[0].getText()
            self.bloc[nom] = ctx
            self.parametres[nom] = []
            i = 1
            while l[i].getText() != '|:':
                self.parametres[nom].append(l[i].getText())
                
            
        else:
            self.pila.append({})
            l = list(ctx.getChildren())
            for i in range(1, len(l)):
                if l[i].getText() == '|:':
                    for j in range(i+1, len(l)-1):
                        self.visit(l[j])
                    break
            self.pila.pop()
                

    def visitInstruccio(self, ctx):
        l = list(ctx.getChildren())
        self.visit(l[0])
        

    def visitAssignacio(self, ctx):
        l = list(ctx.getChildren())
        self.pila[-1][l[0].getText()] = self.visit(l[2])

    def visitEscriptura(self, ctx):
        l = list(ctx.getChildren())
        print(self.visit(l[1]))

    def visitLectura(self, ctx):
        l = list(ctx.getChildren())
        self.pila[-1][l[1].getText()] = input('? ')
        
    def visitExpressio(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
            token = jsbachParser.symbolicNames[l[0].getSymbol().type]
            if token == 'NUMERO':
                return int(l[0].getText())
            elif token == 'VARIABLE':
                return self.pila[-1][l[0].getText()]
            elif token == 'TEXT':
                return l[0].getText()[1:-1]
        else:  # len(l) == 3
            if l[0].getText() == '(':
                return self.visit(l[1])
            else:
                var1 = self.visit(l[0])
                var2 = self.visit(l[2])
                token = jsbachParser.symbolicNames[l[1].getSymbol().type]
                if token == 'SUMA':
                    if type(var1) != type(var2):
                        raise Exception("Operador '+' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
                    return var1 + var2
                elif token == 'RESTA':
                    if type(var1) != type(var2) or type(var1) == string:
                        raise Exception("Operador '-' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
                    return var1 - var2
                elif token == 'MULTIPLICACIO':
                    if type(var1) == type(var2) and type(var1) == string:
                        raise Exception("Operador '*' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
                    return var1 * var2
                elif token == 'DIVISIO':
                    if type(var1) != type(var2) or type(var1) == string:
                        raise Exception("Operador '/' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
                    return var1 / var2
                elif token == 'MODUL':
                    if type(var1) != type(var2) or type(var1) == string:
                        raise Exception("Operador '%' no suportat entre variables de tipus %s i %s" % (type(var1), type(var2)))
                    return var1 % var2
                elif token == 'MAJOR':
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
                

    def visitInvocacio(self, ctx):
        l = list(ctx.getChildren())
        nom = l[0].getText()
        if not nom in self.bloc:
            raise Exception('El procediment %s no esta definit!' % nom)
        diccionari = {}
        if len(l)-1 != len(self.parametres[nom]):
            raise Exception('El nombre de parametres no coincideix!')
        for i in range(1, len(l)):
            diccionari[self.parametres[nom][i-1]]= self.visit(l[i])
        self.pila.append(diccionari)
        self.visit(self.bloc[nom])


