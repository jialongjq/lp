# Generated from jsbach.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,197,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,5,0,38,8,0,10,0,12,0,
        41,9,0,1,0,1,0,1,1,1,1,5,1,47,8,1,10,1,12,1,50,9,1,1,1,1,1,5,1,54,
        8,1,10,1,12,1,57,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,70,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,80,8,3,1,4,1,4,1,
        4,1,5,1,5,1,5,1,5,1,5,4,5,90,8,5,11,5,12,5,91,1,6,1,6,1,6,5,6,97,
        8,6,10,6,12,6,100,9,6,1,6,1,6,1,7,1,7,5,7,106,8,7,10,7,12,7,109,
        9,7,1,8,1,8,1,8,1,8,4,8,115,8,8,11,8,12,8,116,1,8,1,8,1,8,1,8,4,
        8,123,8,8,11,8,12,8,124,1,8,1,8,3,8,129,8,8,1,9,1,9,1,9,1,9,4,9,
        135,8,9,11,9,12,9,136,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,
        5,14,161,8,14,10,14,12,14,164,9,14,1,14,1,14,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,3,15,175,8,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,5,15,186,8,15,10,15,12,15,189,9,15,1,16,1,16,1,16,1,16,
        1,17,1,17,1,17,0,1,30,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,0,3,1,0,25,27,1,0,28,29,1,0,30,35,210,0,39,1,0,0,0,2,44,
        1,0,0,0,4,69,1,0,0,0,6,71,1,0,0,0,8,81,1,0,0,0,10,84,1,0,0,0,12,
        93,1,0,0,0,14,103,1,0,0,0,16,110,1,0,0,0,18,130,1,0,0,0,20,140,1,
        0,0,0,22,144,1,0,0,0,24,150,1,0,0,0,26,153,1,0,0,0,28,158,1,0,0,
        0,30,174,1,0,0,0,32,190,1,0,0,0,34,194,1,0,0,0,36,38,3,2,1,0,37,
        36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,1,0,0,
        0,41,39,1,0,0,0,42,43,5,0,0,1,43,1,1,0,0,0,44,48,5,20,0,0,45,47,
        5,21,0,0,46,45,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,
        49,51,1,0,0,0,50,48,1,0,0,0,51,55,5,1,0,0,52,54,3,4,2,0,53,52,1,
        0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,58,1,0,0,0,57,
        55,1,0,0,0,58,59,5,2,0,0,59,3,1,0,0,0,60,70,3,6,3,0,61,70,3,8,4,
        0,62,70,3,10,5,0,63,70,3,12,6,0,64,70,3,14,7,0,65,70,3,16,8,0,66,
        70,3,18,9,0,67,70,3,20,10,0,68,70,3,22,11,0,69,60,1,0,0,0,69,61,
        1,0,0,0,69,62,1,0,0,0,69,63,1,0,0,0,69,64,1,0,0,0,69,65,1,0,0,0,
        69,66,1,0,0,0,69,67,1,0,0,0,69,68,1,0,0,0,70,5,1,0,0,0,71,72,5,21,
        0,0,72,79,5,17,0,0,73,80,5,21,0,0,74,80,3,30,15,0,75,80,3,28,14,
        0,76,80,3,34,17,0,77,80,3,26,13,0,78,80,3,24,12,0,79,73,1,0,0,0,
        79,74,1,0,0,0,79,75,1,0,0,0,79,76,1,0,0,0,79,77,1,0,0,0,79,78,1,
        0,0,0,80,7,1,0,0,0,81,82,5,16,0,0,82,83,5,21,0,0,83,9,1,0,0,0,84,
        89,5,15,0,0,85,90,5,21,0,0,86,90,3,30,15,0,87,90,3,34,17,0,88,90,
        3,28,14,0,89,85,1,0,0,0,89,86,1,0,0,0,89,87,1,0,0,0,89,88,1,0,0,
        0,90,91,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,11,1,0,0,0,93,94,
        5,18,0,0,94,98,5,3,0,0,95,97,5,19,0,0,96,95,1,0,0,0,97,100,1,0,0,
        0,98,96,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,98,1,0,0,0,101,
        102,5,4,0,0,102,13,1,0,0,0,103,107,5,20,0,0,104,106,3,30,15,0,105,
        104,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,
        15,1,0,0,0,109,107,1,0,0,0,110,111,5,5,0,0,111,112,3,32,16,0,112,
        114,5,1,0,0,113,115,3,4,2,0,114,113,1,0,0,0,115,116,1,0,0,0,116,
        114,1,0,0,0,116,117,1,0,0,0,117,118,1,0,0,0,118,128,5,2,0,0,119,
        120,5,6,0,0,120,122,5,1,0,0,121,123,3,4,2,0,122,121,1,0,0,0,123,
        124,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,126,1,0,0,0,126,
        127,5,2,0,0,127,129,1,0,0,0,128,119,1,0,0,0,128,129,1,0,0,0,129,
        17,1,0,0,0,130,131,5,7,0,0,131,132,3,32,16,0,132,134,5,1,0,0,133,
        135,3,4,2,0,134,133,1,0,0,0,135,136,1,0,0,0,136,134,1,0,0,0,136,
        137,1,0,0,0,137,138,1,0,0,0,138,139,5,2,0,0,139,19,1,0,0,0,140,141,
        5,21,0,0,141,142,5,8,0,0,142,143,3,30,15,0,143,21,1,0,0,0,144,145,
        5,9,0,0,145,146,5,21,0,0,146,147,5,10,0,0,147,148,3,30,15,0,148,
        149,5,11,0,0,149,23,1,0,0,0,150,151,5,12,0,0,151,152,5,21,0,0,152,
        25,1,0,0,0,153,154,5,21,0,0,154,155,5,10,0,0,155,156,3,30,15,0,156,
        157,5,11,0,0,157,27,1,0,0,0,158,162,5,3,0,0,159,161,5,22,0,0,160,
        159,1,0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,
        165,1,0,0,0,164,162,1,0,0,0,165,166,5,4,0,0,166,29,1,0,0,0,167,168,
        6,15,-1,0,168,169,5,13,0,0,169,170,3,30,15,0,170,171,5,14,0,0,171,
        175,1,0,0,0,172,175,5,22,0,0,173,175,5,21,0,0,174,167,1,0,0,0,174,
        172,1,0,0,0,174,173,1,0,0,0,175,187,1,0,0,0,176,177,10,5,0,0,177,
        178,7,0,0,0,178,186,3,30,15,6,179,180,10,4,0,0,180,181,7,1,0,0,181,
        186,3,30,15,5,182,183,10,3,0,0,183,184,7,2,0,0,184,186,3,30,15,4,
        185,176,1,0,0,0,185,179,1,0,0,0,185,182,1,0,0,0,186,189,1,0,0,0,
        187,185,1,0,0,0,187,188,1,0,0,0,188,31,1,0,0,0,189,187,1,0,0,0,190,
        191,3,30,15,0,191,192,7,2,0,0,192,193,3,30,15,0,193,33,1,0,0,0,194,
        195,5,24,0,0,195,35,1,0,0,0,17,39,48,55,69,79,89,91,98,107,116,124,
        128,136,162,174,185,187
    ]

class jsbachParser ( Parser ):

    grammarFileName = "jsbach.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|:'", "':|'", "'{'", "'}'", "'if'", 
                     "'else'", "'while'", "'<<'", "'8<'", "'['", "']'", 
                     "'#'", "'('", "')'", "'<!>'", "'<?>'", "'<-'", "'<:>'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'*'", "'/'", "'%'", "'+'", 
                     "'-'", "'>'", "'<'", "'>='", "'<='", "'='", "'/='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ESCRIPTURA", 
                      "LECTURA", "ASSIGNACIO", "REPRODUCCIO", "NOTA", "ID", 
                      "VARIABLE", "ENTER", "NUMERO", "TEXT", "MULTIPLICACIO", 
                      "DIVISIO", "MODUL", "SUMA", "RESTA", "MAJOR", "MENOR", 
                      "MAJORIGUAL", "MENORIGUAL", "IGUAL", "DIFERENT", "COMENTARI", 
                      "WS" ]

    RULE_root = 0
    RULE_procediment = 1
    RULE_instruccio = 2
    RULE_assignacio = 3
    RULE_lectura = 4
    RULE_escriptura = 5
    RULE_reproduccio = 6
    RULE_invocacio = 7
    RULE_condicional = 8
    RULE_iteracio = 9
    RULE_afegit = 10
    RULE_tall = 11
    RULE_mida = 12
    RULE_consulta = 13
    RULE_llista = 14
    RULE_expressio = 15
    RULE_condicio = 16
    RULE_text = 17

    ruleNames =  [ "root", "procediment", "instruccio", "assignacio", "lectura", 
                   "escriptura", "reproduccio", "invocacio", "condicional", 
                   "iteracio", "afegit", "tall", "mida", "consulta", "llista", 
                   "expressio", "condicio", "text" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    ESCRIPTURA=15
    LECTURA=16
    ASSIGNACIO=17
    REPRODUCCIO=18
    NOTA=19
    ID=20
    VARIABLE=21
    ENTER=22
    NUMERO=23
    TEXT=24
    MULTIPLICACIO=25
    DIVISIO=26
    MODUL=27
    SUMA=28
    RESTA=29
    MAJOR=30
    MENOR=31
    MAJORIGUAL=32
    MENORIGUAL=33
    IGUAL=34
    DIFERENT=35
    COMENTARI=36
    WS=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(jsbachParser.EOF, 0)

        def procediment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ProcedimentContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ProcedimentContext,i)


        def getRuleIndex(self):
            return jsbachParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = jsbachParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.ID:
                self.state = 36
                self.procediment()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self.match(jsbachParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedimentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(jsbachParser.ID, 0)

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(jsbachParser.VARIABLE)
            else:
                return self.getToken(jsbachParser.VARIABLE, i)

        def instruccio(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.InstruccioContext)
            else:
                return self.getTypedRuleContext(jsbachParser.InstruccioContext,i)


        def getRuleIndex(self):
            return jsbachParser.RULE_procediment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcediment" ):
                return visitor.visitProcediment(self)
            else:
                return visitor.visitChildren(self)




    def procediment(self):

        localctx = jsbachParser.ProcedimentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_procediment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(jsbachParser.ID)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.VARIABLE:
                self.state = 45
                self.match(jsbachParser.VARIABLE)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self.match(jsbachParser.T__0)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.T__4) | (1 << jsbachParser.T__6) | (1 << jsbachParser.T__8) | (1 << jsbachParser.ESCRIPTURA) | (1 << jsbachParser.LECTURA) | (1 << jsbachParser.REPRODUCCIO) | (1 << jsbachParser.ID) | (1 << jsbachParser.VARIABLE))) != 0):
                self.state = 52
                self.instruccio()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
            self.match(jsbachParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignacio(self):
            return self.getTypedRuleContext(jsbachParser.AssignacioContext,0)


        def lectura(self):
            return self.getTypedRuleContext(jsbachParser.LecturaContext,0)


        def escriptura(self):
            return self.getTypedRuleContext(jsbachParser.EscripturaContext,0)


        def reproduccio(self):
            return self.getTypedRuleContext(jsbachParser.ReproduccioContext,0)


        def invocacio(self):
            return self.getTypedRuleContext(jsbachParser.InvocacioContext,0)


        def condicional(self):
            return self.getTypedRuleContext(jsbachParser.CondicionalContext,0)


        def iteracio(self):
            return self.getTypedRuleContext(jsbachParser.IteracioContext,0)


        def afegit(self):
            return self.getTypedRuleContext(jsbachParser.AfegitContext,0)


        def tall(self):
            return self.getTypedRuleContext(jsbachParser.TallContext,0)


        def getRuleIndex(self):
            return jsbachParser.RULE_instruccio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccio" ):
                return visitor.visitInstruccio(self)
            else:
                return visitor.visitChildren(self)




    def instruccio(self):

        localctx = jsbachParser.InstruccioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruccio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 60
                self.assignacio()
                pass

            elif la_ == 2:
                self.state = 61
                self.lectura()
                pass

            elif la_ == 3:
                self.state = 62
                self.escriptura()
                pass

            elif la_ == 4:
                self.state = 63
                self.reproduccio()
                pass

            elif la_ == 5:
                self.state = 64
                self.invocacio()
                pass

            elif la_ == 6:
                self.state = 65
                self.condicional()
                pass

            elif la_ == 7:
                self.state = 66
                self.iteracio()
                pass

            elif la_ == 8:
                self.state = 67
                self.afegit()
                pass

            elif la_ == 9:
                self.state = 68
                self.tall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignacioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(jsbachParser.VARIABLE)
            else:
                return self.getToken(jsbachParser.VARIABLE, i)

        def ASSIGNACIO(self):
            return self.getToken(jsbachParser.ASSIGNACIO, 0)

        def expressio(self):
            return self.getTypedRuleContext(jsbachParser.ExpressioContext,0)


        def llista(self):
            return self.getTypedRuleContext(jsbachParser.LlistaContext,0)


        def text(self):
            return self.getTypedRuleContext(jsbachParser.TextContext,0)


        def consulta(self):
            return self.getTypedRuleContext(jsbachParser.ConsultaContext,0)


        def mida(self):
            return self.getTypedRuleContext(jsbachParser.MidaContext,0)


        def getRuleIndex(self):
            return jsbachParser.RULE_assignacio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignacio" ):
                return visitor.visitAssignacio(self)
            else:
                return visitor.visitChildren(self)




    def assignacio(self):

        localctx = jsbachParser.AssignacioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignacio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(jsbachParser.VARIABLE)
            self.state = 72
            self.match(jsbachParser.ASSIGNACIO)
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 73
                self.match(jsbachParser.VARIABLE)
                pass

            elif la_ == 2:
                self.state = 74
                self.expressio(0)
                pass

            elif la_ == 3:
                self.state = 75
                self.llista()
                pass

            elif la_ == 4:
                self.state = 76
                self.text()
                pass

            elif la_ == 5:
                self.state = 77
                self.consulta()
                pass

            elif la_ == 6:
                self.state = 78
                self.mida()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LecturaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LECTURA(self):
            return self.getToken(jsbachParser.LECTURA, 0)

        def VARIABLE(self):
            return self.getToken(jsbachParser.VARIABLE, 0)

        def getRuleIndex(self):
            return jsbachParser.RULE_lectura

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLectura" ):
                return visitor.visitLectura(self)
            else:
                return visitor.visitChildren(self)




    def lectura(self):

        localctx = jsbachParser.LecturaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_lectura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(jsbachParser.LECTURA)
            self.state = 82
            self.match(jsbachParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EscripturaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESCRIPTURA(self):
            return self.getToken(jsbachParser.ESCRIPTURA, 0)

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(jsbachParser.VARIABLE)
            else:
                return self.getToken(jsbachParser.VARIABLE, i)

        def expressio(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExpressioContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExpressioContext,i)


        def text(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.TextContext)
            else:
                return self.getTypedRuleContext(jsbachParser.TextContext,i)


        def llista(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.LlistaContext)
            else:
                return self.getTypedRuleContext(jsbachParser.LlistaContext,i)


        def getRuleIndex(self):
            return jsbachParser.RULE_escriptura

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscriptura" ):
                return visitor.visitEscriptura(self)
            else:
                return visitor.visitChildren(self)




    def escriptura(self):

        localctx = jsbachParser.EscripturaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_escriptura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(jsbachParser.ESCRIPTURA)
            self.state = 89 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 89
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        self.state = 85
                        self.match(jsbachParser.VARIABLE)
                        pass

                    elif la_ == 2:
                        self.state = 86
                        self.expressio(0)
                        pass

                    elif la_ == 3:
                        self.state = 87
                        self.text()
                        pass

                    elif la_ == 4:
                        self.state = 88
                        self.llista()
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 91 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReproduccioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPRODUCCIO(self):
            return self.getToken(jsbachParser.REPRODUCCIO, 0)

        def NOTA(self, i:int=None):
            if i is None:
                return self.getTokens(jsbachParser.NOTA)
            else:
                return self.getToken(jsbachParser.NOTA, i)

        def getRuleIndex(self):
            return jsbachParser.RULE_reproduccio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReproduccio" ):
                return visitor.visitReproduccio(self)
            else:
                return visitor.visitChildren(self)




    def reproduccio(self):

        localctx = jsbachParser.ReproduccioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_reproduccio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(jsbachParser.REPRODUCCIO)
            self.state = 94
            self.match(jsbachParser.T__2)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.NOTA:
                self.state = 95
                self.match(jsbachParser.NOTA)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
            self.match(jsbachParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvocacioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(jsbachParser.ID, 0)

        def expressio(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExpressioContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExpressioContext,i)


        def getRuleIndex(self):
            return jsbachParser.RULE_invocacio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvocacio" ):
                return visitor.visitInvocacio(self)
            else:
                return visitor.visitChildren(self)




    def invocacio(self):

        localctx = jsbachParser.InvocacioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_invocacio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(jsbachParser.ID)
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 104
                    self.expressio(0) 
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicio(self):
            return self.getTypedRuleContext(jsbachParser.CondicioContext,0)


        def instruccio(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.InstruccioContext)
            else:
                return self.getTypedRuleContext(jsbachParser.InstruccioContext,i)


        def getRuleIndex(self):
            return jsbachParser.RULE_condicional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = jsbachParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(jsbachParser.T__4)
            self.state = 111
            self.condicio()
            self.state = 112
            self.match(jsbachParser.T__0)
            self.state = 114 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 113
                self.instruccio()
                self.state = 116 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.T__4) | (1 << jsbachParser.T__6) | (1 << jsbachParser.T__8) | (1 << jsbachParser.ESCRIPTURA) | (1 << jsbachParser.LECTURA) | (1 << jsbachParser.REPRODUCCIO) | (1 << jsbachParser.ID) | (1 << jsbachParser.VARIABLE))) != 0)):
                    break

            self.state = 118
            self.match(jsbachParser.T__1)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==jsbachParser.T__5:
                self.state = 119
                self.match(jsbachParser.T__5)
                self.state = 120
                self.match(jsbachParser.T__0)
                self.state = 122 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 121
                    self.instruccio()
                    self.state = 124 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.T__4) | (1 << jsbachParser.T__6) | (1 << jsbachParser.T__8) | (1 << jsbachParser.ESCRIPTURA) | (1 << jsbachParser.LECTURA) | (1 << jsbachParser.REPRODUCCIO) | (1 << jsbachParser.ID) | (1 << jsbachParser.VARIABLE))) != 0)):
                        break

                self.state = 126
                self.match(jsbachParser.T__1)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IteracioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicio(self):
            return self.getTypedRuleContext(jsbachParser.CondicioContext,0)


        def instruccio(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.InstruccioContext)
            else:
                return self.getTypedRuleContext(jsbachParser.InstruccioContext,i)


        def getRuleIndex(self):
            return jsbachParser.RULE_iteracio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIteracio" ):
                return visitor.visitIteracio(self)
            else:
                return visitor.visitChildren(self)




    def iteracio(self):

        localctx = jsbachParser.IteracioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_iteracio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(jsbachParser.T__6)
            self.state = 131
            self.condicio()
            self.state = 132
            self.match(jsbachParser.T__0)
            self.state = 134 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 133
                self.instruccio()
                self.state = 136 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.T__4) | (1 << jsbachParser.T__6) | (1 << jsbachParser.T__8) | (1 << jsbachParser.ESCRIPTURA) | (1 << jsbachParser.LECTURA) | (1 << jsbachParser.REPRODUCCIO) | (1 << jsbachParser.ID) | (1 << jsbachParser.VARIABLE))) != 0)):
                    break

            self.state = 138
            self.match(jsbachParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AfegitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(jsbachParser.VARIABLE, 0)

        def expressio(self):
            return self.getTypedRuleContext(jsbachParser.ExpressioContext,0)


        def getRuleIndex(self):
            return jsbachParser.RULE_afegit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAfegit" ):
                return visitor.visitAfegit(self)
            else:
                return visitor.visitChildren(self)




    def afegit(self):

        localctx = jsbachParser.AfegitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_afegit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(jsbachParser.VARIABLE)
            self.state = 141
            self.match(jsbachParser.T__7)
            self.state = 142
            self.expressio(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(jsbachParser.VARIABLE, 0)

        def expressio(self):
            return self.getTypedRuleContext(jsbachParser.ExpressioContext,0)


        def getRuleIndex(self):
            return jsbachParser.RULE_tall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTall" ):
                return visitor.visitTall(self)
            else:
                return visitor.visitChildren(self)




    def tall(self):

        localctx = jsbachParser.TallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_tall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(jsbachParser.T__8)
            self.state = 145
            self.match(jsbachParser.VARIABLE)
            self.state = 146
            self.match(jsbachParser.T__9)
            self.state = 147
            self.expressio(0)
            self.state = 148
            self.match(jsbachParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MidaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(jsbachParser.VARIABLE, 0)

        def getRuleIndex(self):
            return jsbachParser.RULE_mida

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMida" ):
                return visitor.visitMida(self)
            else:
                return visitor.visitChildren(self)




    def mida(self):

        localctx = jsbachParser.MidaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_mida)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(jsbachParser.T__11)
            self.state = 151
            self.match(jsbachParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConsultaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(jsbachParser.VARIABLE, 0)

        def expressio(self):
            return self.getTypedRuleContext(jsbachParser.ExpressioContext,0)


        def getRuleIndex(self):
            return jsbachParser.RULE_consulta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConsulta" ):
                return visitor.visitConsulta(self)
            else:
                return visitor.visitChildren(self)




    def consulta(self):

        localctx = jsbachParser.ConsultaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_consulta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(jsbachParser.VARIABLE)
            self.state = 154
            self.match(jsbachParser.T__9)
            self.state = 155
            self.expressio(0)
            self.state = 156
            self.match(jsbachParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlistaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTER(self, i:int=None):
            if i is None:
                return self.getTokens(jsbachParser.ENTER)
            else:
                return self.getToken(jsbachParser.ENTER, i)

        def getRuleIndex(self):
            return jsbachParser.RULE_llista

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlista" ):
                return visitor.visitLlista(self)
            else:
                return visitor.visitChildren(self)




    def llista(self):

        localctx = jsbachParser.LlistaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_llista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(jsbachParser.T__2)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.ENTER:
                self.state = 159
                self.match(jsbachParser.ENTER)
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 165
            self.match(jsbachParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressio(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExpressioContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExpressioContext,i)


        def ENTER(self):
            return self.getToken(jsbachParser.ENTER, 0)

        def VARIABLE(self):
            return self.getToken(jsbachParser.VARIABLE, 0)

        def MULTIPLICACIO(self):
            return self.getToken(jsbachParser.MULTIPLICACIO, 0)

        def DIVISIO(self):
            return self.getToken(jsbachParser.DIVISIO, 0)

        def MODUL(self):
            return self.getToken(jsbachParser.MODUL, 0)

        def SUMA(self):
            return self.getToken(jsbachParser.SUMA, 0)

        def RESTA(self):
            return self.getToken(jsbachParser.RESTA, 0)

        def MAJOR(self):
            return self.getToken(jsbachParser.MAJOR, 0)

        def MAJORIGUAL(self):
            return self.getToken(jsbachParser.MAJORIGUAL, 0)

        def MENOR(self):
            return self.getToken(jsbachParser.MENOR, 0)

        def MENORIGUAL(self):
            return self.getToken(jsbachParser.MENORIGUAL, 0)

        def IGUAL(self):
            return self.getToken(jsbachParser.IGUAL, 0)

        def DIFERENT(self):
            return self.getToken(jsbachParser.DIFERENT, 0)

        def getRuleIndex(self):
            return jsbachParser.RULE_expressio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressio" ):
                return visitor.visitExpressio(self)
            else:
                return visitor.visitChildren(self)



    def expressio(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = jsbachParser.ExpressioContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expressio, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [jsbachParser.T__12]:
                self.state = 168
                self.match(jsbachParser.T__12)
                self.state = 169
                self.expressio(0)
                self.state = 170
                self.match(jsbachParser.T__13)
                pass
            elif token in [jsbachParser.ENTER]:
                self.state = 172
                self.match(jsbachParser.ENTER)
                pass
            elif token in [jsbachParser.VARIABLE]:
                self.state = 173
                self.match(jsbachParser.VARIABLE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 187
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 185
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = jsbachParser.ExpressioContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressio)
                        self.state = 176
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 177
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.MULTIPLICACIO) | (1 << jsbachParser.DIVISIO) | (1 << jsbachParser.MODUL))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 178
                        self.expressio(6)
                        pass

                    elif la_ == 2:
                        localctx = jsbachParser.ExpressioContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressio)
                        self.state = 179
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 180
                        _la = self._input.LA(1)
                        if not(_la==jsbachParser.SUMA or _la==jsbachParser.RESTA):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 181
                        self.expressio(5)
                        pass

                    elif la_ == 3:
                        localctx = jsbachParser.ExpressioContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressio)
                        self.state = 182
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 183
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.MAJOR) | (1 << jsbachParser.MENOR) | (1 << jsbachParser.MAJORIGUAL) | (1 << jsbachParser.MENORIGUAL) | (1 << jsbachParser.IGUAL) | (1 << jsbachParser.DIFERENT))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 184
                        self.expressio(4)
                        pass

             
                self.state = 189
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CondicioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressio(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExpressioContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExpressioContext,i)


        def MAJOR(self):
            return self.getToken(jsbachParser.MAJOR, 0)

        def MAJORIGUAL(self):
            return self.getToken(jsbachParser.MAJORIGUAL, 0)

        def MENOR(self):
            return self.getToken(jsbachParser.MENOR, 0)

        def MENORIGUAL(self):
            return self.getToken(jsbachParser.MENORIGUAL, 0)

        def IGUAL(self):
            return self.getToken(jsbachParser.IGUAL, 0)

        def DIFERENT(self):
            return self.getToken(jsbachParser.DIFERENT, 0)

        def getRuleIndex(self):
            return jsbachParser.RULE_condicio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicio" ):
                return visitor.visitCondicio(self)
            else:
                return visitor.visitChildren(self)




    def condicio(self):

        localctx = jsbachParser.CondicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_condicio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.expressio(0)
            self.state = 191
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.MAJOR) | (1 << jsbachParser.MENOR) | (1 << jsbachParser.MAJORIGUAL) | (1 << jsbachParser.MENORIGUAL) | (1 << jsbachParser.IGUAL) | (1 << jsbachParser.DIFERENT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 192
            self.expressio(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(jsbachParser.TEXT, 0)

        def getRuleIndex(self):
            return jsbachParser.RULE_text

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitText" ):
                return visitor.visitText(self)
            else:
                return visitor.visitChildren(self)




    def text(self):

        localctx = jsbachParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(jsbachParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.expressio_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expressio_sempred(self, localctx:ExpressioContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




