# Generated from jsbach.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jsbachParser import jsbachParser
else:
    from jsbachParser import jsbachParser

# This class defines a complete generic visitor for a parse tree produced by jsbachParser.

class jsbachVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by jsbachParser#root.
    def visitRoot(self, ctx:jsbachParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#instruccio.
    def visitInstruccio(self, ctx:jsbachParser.InstruccioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#procediment.
    def visitProcediment(self, ctx:jsbachParser.ProcedimentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#assignacio.
    def visitAssignacio(self, ctx:jsbachParser.AssignacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#escriptura.
    def visitEscriptura(self, ctx:jsbachParser.EscripturaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#reproduccio.
    def visitReproduccio(self, ctx:jsbachParser.ReproduccioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#lectura.
    def visitLectura(self, ctx:jsbachParser.LecturaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#expressio.
    def visitExpressio(self, ctx:jsbachParser.ExpressioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#invocacio.
    def visitInvocacio(self, ctx:jsbachParser.InvocacioContext):
        return self.visitChildren(ctx)



del jsbachParser