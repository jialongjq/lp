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
        4,1,37,211,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,1,0,1,1,1,1,5,1,53,8,1,
        10,1,12,1,56,9,1,1,1,1,1,5,1,60,8,1,10,1,12,1,63,9,1,1,1,1,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,76,8,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,3,3,86,8,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,4,5,
        98,8,5,11,5,12,5,99,1,6,1,6,1,6,1,7,1,7,5,7,107,8,7,10,7,12,7,110,
        9,7,1,8,1,8,1,8,1,8,4,8,116,8,8,11,8,12,8,117,1,8,1,8,1,8,1,8,4,
        8,124,8,8,11,8,12,8,125,1,8,1,8,3,8,130,8,8,1,9,1,9,1,9,1,9,4,9,
        136,8,9,11,9,12,9,137,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,
        5,14,162,8,14,10,14,12,14,165,9,14,1,14,1,14,1,15,1,15,5,15,171,
        8,15,10,15,12,15,174,9,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,3,16,185,8,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        5,16,196,8,16,10,16,12,16,199,9,16,1,17,1,17,1,17,1,17,1,18,1,18,
        1,19,1,19,1,20,1,20,1,20,0,1,32,21,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,0,3,1,0,25,27,1,0,28,29,1,0,30,35,223,
        0,45,1,0,0,0,2,50,1,0,0,0,4,75,1,0,0,0,6,77,1,0,0,0,8,87,1,0,0,0,
        10,90,1,0,0,0,12,101,1,0,0,0,14,104,1,0,0,0,16,111,1,0,0,0,18,131,
        1,0,0,0,20,141,1,0,0,0,22,145,1,0,0,0,24,151,1,0,0,0,26,154,1,0,
        0,0,28,159,1,0,0,0,30,168,1,0,0,0,32,184,1,0,0,0,34,200,1,0,0,0,
        36,204,1,0,0,0,38,206,1,0,0,0,40,208,1,0,0,0,42,44,3,2,1,0,43,42,
        1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,0,
        47,45,1,0,0,0,48,49,5,0,0,1,49,1,1,0,0,0,50,54,5,20,0,0,51,53,5,
        21,0,0,52,51,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,
        57,1,0,0,0,56,54,1,0,0,0,57,61,5,1,0,0,58,60,3,4,2,0,59,58,1,0,0,
        0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,61,
        1,0,0,0,64,65,5,2,0,0,65,3,1,0,0,0,66,76,3,6,3,0,67,76,3,8,4,0,68,
        76,3,10,5,0,69,76,3,12,6,0,70,76,3,14,7,0,71,76,3,16,8,0,72,76,3,
        18,9,0,73,76,3,20,10,0,74,76,3,22,11,0,75,66,1,0,0,0,75,67,1,0,0,
        0,75,68,1,0,0,0,75,69,1,0,0,0,75,70,1,0,0,0,75,71,1,0,0,0,75,72,
        1,0,0,0,75,73,1,0,0,0,75,74,1,0,0,0,76,5,1,0,0,0,77,78,5,21,0,0,
        78,85,5,17,0,0,79,86,3,38,19,0,80,86,3,32,16,0,81,86,3,28,14,0,82,
        86,3,36,18,0,83,86,3,26,13,0,84,86,3,24,12,0,85,79,1,0,0,0,85,80,
        1,0,0,0,85,81,1,0,0,0,85,82,1,0,0,0,85,83,1,0,0,0,85,84,1,0,0,0,
        86,7,1,0,0,0,87,88,5,16,0,0,88,89,5,21,0,0,89,9,1,0,0,0,90,97,5,
        15,0,0,91,98,3,38,19,0,92,98,3,32,16,0,93,98,3,36,18,0,94,98,3,28,
        14,0,95,98,3,24,12,0,96,98,3,26,13,0,97,91,1,0,0,0,97,92,1,0,0,0,
        97,93,1,0,0,0,97,94,1,0,0,0,97,95,1,0,0,0,97,96,1,0,0,0,98,99,1,
        0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,11,1,0,0,0,101,102,5,18,0,
        0,102,103,3,30,15,0,103,13,1,0,0,0,104,108,5,20,0,0,105,107,3,32,
        16,0,106,105,1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,109,1,0,
        0,0,109,15,1,0,0,0,110,108,1,0,0,0,111,112,5,3,0,0,112,113,3,34,
        17,0,113,115,5,1,0,0,114,116,3,4,2,0,115,114,1,0,0,0,116,117,1,0,
        0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,119,1,0,0,0,119,129,5,2,
        0,0,120,121,5,4,0,0,121,123,5,1,0,0,122,124,3,4,2,0,123,122,1,0,
        0,0,124,125,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,127,1,0,
        0,0,127,128,5,2,0,0,128,130,1,0,0,0,129,120,1,0,0,0,129,130,1,0,
        0,0,130,17,1,0,0,0,131,132,5,5,0,0,132,133,3,34,17,0,133,135,5,1,
        0,0,134,136,3,4,2,0,135,134,1,0,0,0,136,137,1,0,0,0,137,135,1,0,
        0,0,137,138,1,0,0,0,138,139,1,0,0,0,139,140,5,2,0,0,140,19,1,0,0,
        0,141,142,3,38,19,0,142,143,5,6,0,0,143,144,3,32,16,0,144,21,1,0,
        0,0,145,146,5,7,0,0,146,147,3,38,19,0,147,148,5,8,0,0,148,149,3,
        32,16,0,149,150,5,9,0,0,150,23,1,0,0,0,151,152,5,10,0,0,152,153,
        3,38,19,0,153,25,1,0,0,0,154,155,3,38,19,0,155,156,5,8,0,0,156,157,
        3,32,16,0,157,158,5,9,0,0,158,27,1,0,0,0,159,163,5,11,0,0,160,162,
        5,22,0,0,161,160,1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,164,
        1,0,0,0,164,166,1,0,0,0,165,163,1,0,0,0,166,167,5,12,0,0,167,29,
        1,0,0,0,168,172,5,11,0,0,169,171,5,19,0,0,170,169,1,0,0,0,171,174,
        1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,175,1,0,0,0,174,172,
        1,0,0,0,175,176,5,12,0,0,176,31,1,0,0,0,177,178,6,16,-1,0,178,179,
        5,13,0,0,179,180,3,32,16,0,180,181,5,14,0,0,181,185,1,0,0,0,182,
        185,3,40,20,0,183,185,3,38,19,0,184,177,1,0,0,0,184,182,1,0,0,0,
        184,183,1,0,0,0,185,197,1,0,0,0,186,187,10,5,0,0,187,188,7,0,0,0,
        188,196,3,32,16,6,189,190,10,4,0,0,190,191,7,1,0,0,191,196,3,32,
        16,5,192,193,10,3,0,0,193,194,7,2,0,0,194,196,3,32,16,4,195,186,
        1,0,0,0,195,189,1,0,0,0,195,192,1,0,0,0,196,199,1,0,0,0,197,195,
        1,0,0,0,197,198,1,0,0,0,198,33,1,0,0,0,199,197,1,0,0,0,200,201,3,
        32,16,0,201,202,7,2,0,0,202,203,3,32,16,0,203,35,1,0,0,0,204,205,
        5,24,0,0,205,37,1,0,0,0,206,207,5,21,0,0,207,39,1,0,0,0,208,209,
        5,22,0,0,209,41,1,0,0,0,17,45,54,61,75,85,97,99,108,117,125,129,
        137,163,172,184,195,197
    ]

class jsbachParser ( Parser ):

    grammarFileName = "jsbach.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|:'", "':|'", "'if'", "'else'", "'while'", 
                     "'<<'", "'8<'", "'['", "']'", "'#'", "'{'", "'}'", 
                     "'('", "')'", "'<!>'", "'<?>'", "'<-'", "'<:>'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'*'", "'/'", "'%'", "'+'", "'-'", "'>'", 
                     "'<'", "'>='", "'<='", "'='", "'/='" ]

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
    RULE_notes = 15
    RULE_expressio = 16
    RULE_condicio = 17
    RULE_text = 18
    RULE_variable = 19
    RULE_enter = 20

    ruleNames =  [ "root", "procediment", "instruccio", "assignacio", "lectura", 
                   "escriptura", "reproduccio", "invocacio", "condicional", 
                   "iteracio", "afegit", "tall", "mida", "consulta", "llista", 
                   "notes", "expressio", "condicio", "text", "variable", 
                   "enter" ]

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
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.ID:
                self.state = 42
                self.procediment()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
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
            self.state = 50
            self.match(jsbachParser.ID)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.VARIABLE:
                self.state = 51
                self.match(jsbachParser.VARIABLE)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
            self.match(jsbachParser.T__0)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.T__2) | (1 << jsbachParser.T__4) | (1 << jsbachParser.T__6) | (1 << jsbachParser.ESCRIPTURA) | (1 << jsbachParser.LECTURA) | (1 << jsbachParser.REPRODUCCIO) | (1 << jsbachParser.ID) | (1 << jsbachParser.VARIABLE))) != 0):
                self.state = 58
                self.instruccio()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
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
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 66
                self.assignacio()
                pass

            elif la_ == 2:
                self.state = 67
                self.lectura()
                pass

            elif la_ == 3:
                self.state = 68
                self.escriptura()
                pass

            elif la_ == 4:
                self.state = 69
                self.reproduccio()
                pass

            elif la_ == 5:
                self.state = 70
                self.invocacio()
                pass

            elif la_ == 6:
                self.state = 71
                self.condicional()
                pass

            elif la_ == 7:
                self.state = 72
                self.iteracio()
                pass

            elif la_ == 8:
                self.state = 73
                self.afegit()
                pass

            elif la_ == 9:
                self.state = 74
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

        def VARIABLE(self):
            return self.getToken(jsbachParser.VARIABLE, 0)

        def ASSIGNACIO(self):
            return self.getToken(jsbachParser.ASSIGNACIO, 0)

        def variable(self):
            return self.getTypedRuleContext(jsbachParser.VariableContext,0)


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
            self.state = 77
            self.match(jsbachParser.VARIABLE)
            self.state = 78
            self.match(jsbachParser.ASSIGNACIO)
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 79
                self.variable()
                pass

            elif la_ == 2:
                self.state = 80
                self.expressio(0)
                pass

            elif la_ == 3:
                self.state = 81
                self.llista()
                pass

            elif la_ == 4:
                self.state = 82
                self.text()
                pass

            elif la_ == 5:
                self.state = 83
                self.consulta()
                pass

            elif la_ == 6:
                self.state = 84
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
            self.state = 87
            self.match(jsbachParser.LECTURA)
            self.state = 88
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

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.VariableContext)
            else:
                return self.getTypedRuleContext(jsbachParser.VariableContext,i)


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


        def mida(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.MidaContext)
            else:
                return self.getTypedRuleContext(jsbachParser.MidaContext,i)


        def consulta(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ConsultaContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ConsultaContext,i)


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
            self.state = 90
            self.match(jsbachParser.ESCRIPTURA)
            self.state = 97 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 97
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        self.state = 91
                        self.variable()
                        pass

                    elif la_ == 2:
                        self.state = 92
                        self.expressio(0)
                        pass

                    elif la_ == 3:
                        self.state = 93
                        self.text()
                        pass

                    elif la_ == 4:
                        self.state = 94
                        self.llista()
                        pass

                    elif la_ == 5:
                        self.state = 95
                        self.mida()
                        pass

                    elif la_ == 6:
                        self.state = 96
                        self.consulta()
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 99 
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

        def notes(self):
            return self.getTypedRuleContext(jsbachParser.NotesContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(jsbachParser.REPRODUCCIO)
            self.state = 102
            self.notes()
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
            self.state = 104
            self.match(jsbachParser.ID)
            self.state = 108
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 105
                    self.expressio(0) 
                self.state = 110
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
            self.state = 111
            self.match(jsbachParser.T__2)
            self.state = 112
            self.condicio()
            self.state = 113
            self.match(jsbachParser.T__0)
            self.state = 115 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 114
                self.instruccio()
                self.state = 117 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.T__2) | (1 << jsbachParser.T__4) | (1 << jsbachParser.T__6) | (1 << jsbachParser.ESCRIPTURA) | (1 << jsbachParser.LECTURA) | (1 << jsbachParser.REPRODUCCIO) | (1 << jsbachParser.ID) | (1 << jsbachParser.VARIABLE))) != 0)):
                    break

            self.state = 119
            self.match(jsbachParser.T__1)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==jsbachParser.T__3:
                self.state = 120
                self.match(jsbachParser.T__3)
                self.state = 121
                self.match(jsbachParser.T__0)
                self.state = 123 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 122
                    self.instruccio()
                    self.state = 125 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.T__2) | (1 << jsbachParser.T__4) | (1 << jsbachParser.T__6) | (1 << jsbachParser.ESCRIPTURA) | (1 << jsbachParser.LECTURA) | (1 << jsbachParser.REPRODUCCIO) | (1 << jsbachParser.ID) | (1 << jsbachParser.VARIABLE))) != 0)):
                        break

                self.state = 127
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
            self.state = 131
            self.match(jsbachParser.T__4)
            self.state = 132
            self.condicio()
            self.state = 133
            self.match(jsbachParser.T__0)
            self.state = 135 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 134
                self.instruccio()
                self.state = 137 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.T__2) | (1 << jsbachParser.T__4) | (1 << jsbachParser.T__6) | (1 << jsbachParser.ESCRIPTURA) | (1 << jsbachParser.LECTURA) | (1 << jsbachParser.REPRODUCCIO) | (1 << jsbachParser.ID) | (1 << jsbachParser.VARIABLE))) != 0)):
                    break

            self.state = 139
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

        def variable(self):
            return self.getTypedRuleContext(jsbachParser.VariableContext,0)


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
            self.state = 141
            self.variable()
            self.state = 142
            self.match(jsbachParser.T__5)
            self.state = 143
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

        def variable(self):
            return self.getTypedRuleContext(jsbachParser.VariableContext,0)


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
            self.state = 145
            self.match(jsbachParser.T__6)
            self.state = 146
            self.variable()
            self.state = 147
            self.match(jsbachParser.T__7)
            self.state = 148
            self.expressio(0)
            self.state = 149
            self.match(jsbachParser.T__8)
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

        def variable(self):
            return self.getTypedRuleContext(jsbachParser.VariableContext,0)


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
            self.state = 151
            self.match(jsbachParser.T__9)
            self.state = 152
            self.variable()
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

        def variable(self):
            return self.getTypedRuleContext(jsbachParser.VariableContext,0)


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
            self.state = 154
            self.variable()
            self.state = 155
            self.match(jsbachParser.T__7)
            self.state = 156
            self.expressio(0)
            self.state = 157
            self.match(jsbachParser.T__8)
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
            self.state = 159
            self.match(jsbachParser.T__10)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.ENTER:
                self.state = 160
                self.match(jsbachParser.ENTER)
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 166
            self.match(jsbachParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NotesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOTA(self, i:int=None):
            if i is None:
                return self.getTokens(jsbachParser.NOTA)
            else:
                return self.getToken(jsbachParser.NOTA, i)

        def getRuleIndex(self):
            return jsbachParser.RULE_notes

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotes" ):
                return visitor.visitNotes(self)
            else:
                return visitor.visitChildren(self)




    def notes(self):

        localctx = jsbachParser.NotesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_notes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(jsbachParser.T__10)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.NOTA:
                self.state = 169
                self.match(jsbachParser.NOTA)
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 175
            self.match(jsbachParser.T__11)
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


        def enter(self):
            return self.getTypedRuleContext(jsbachParser.EnterContext,0)


        def variable(self):
            return self.getTypedRuleContext(jsbachParser.VariableContext,0)


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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expressio, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [jsbachParser.T__12]:
                self.state = 178
                self.match(jsbachParser.T__12)
                self.state = 179
                self.expressio(0)
                self.state = 180
                self.match(jsbachParser.T__13)
                pass
            elif token in [jsbachParser.ENTER]:
                self.state = 182
                self.enter()
                pass
            elif token in [jsbachParser.VARIABLE]:
                self.state = 183
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 197
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 195
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = jsbachParser.ExpressioContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressio)
                        self.state = 186
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 187
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.MULTIPLICACIO) | (1 << jsbachParser.DIVISIO) | (1 << jsbachParser.MODUL))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 188
                        self.expressio(6)
                        pass

                    elif la_ == 2:
                        localctx = jsbachParser.ExpressioContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressio)
                        self.state = 189
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 190
                        _la = self._input.LA(1)
                        if not(_la==jsbachParser.SUMA or _la==jsbachParser.RESTA):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 191
                        self.expressio(5)
                        pass

                    elif la_ == 3:
                        localctx = jsbachParser.ExpressioContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressio)
                        self.state = 192
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 193
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.MAJOR) | (1 << jsbachParser.MENOR) | (1 << jsbachParser.MAJORIGUAL) | (1 << jsbachParser.MENORIGUAL) | (1 << jsbachParser.IGUAL) | (1 << jsbachParser.DIFERENT))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 194
                        self.expressio(4)
                        pass

             
                self.state = 199
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
        self.enterRule(localctx, 34, self.RULE_condicio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.expressio(0)
            self.state = 201
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.MAJOR) | (1 << jsbachParser.MENOR) | (1 << jsbachParser.MAJORIGUAL) | (1 << jsbachParser.MENORIGUAL) | (1 << jsbachParser.IGUAL) | (1 << jsbachParser.DIFERENT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 202
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
        self.enterRule(localctx, 36, self.RULE_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(jsbachParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(jsbachParser.VARIABLE, 0)

        def getRuleIndex(self):
            return jsbachParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = jsbachParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(jsbachParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTER(self):
            return self.getToken(jsbachParser.ENTER, 0)

        def getRuleIndex(self):
            return jsbachParser.RULE_enter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnter" ):
                return visitor.visitEnter(self)
            else:
                return visitor.visitChildren(self)




    def enter(self):

        localctx = jsbachParser.EnterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_enter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(jsbachParser.ENTER)
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
        self._predicates[16] = self.expressio_sempred
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
         




