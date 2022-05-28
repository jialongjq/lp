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
        4,1,37,261,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,1,0,
        1,1,1,1,5,1,57,8,1,10,1,12,1,60,9,1,1,1,1,1,5,1,64,8,1,10,1,12,1,
        67,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,80,8,2,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,93,8,3,1,4,1,4,1,4,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,4,5,109,8,5,11,5,12,
        5,110,1,6,1,6,1,6,1,6,3,6,117,8,6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,125,
        8,7,10,7,12,7,128,9,7,1,8,1,8,1,8,1,8,4,8,134,8,8,11,8,12,8,135,
        1,8,1,8,1,8,1,8,4,8,142,8,8,11,8,12,8,143,1,8,1,8,3,8,148,8,8,1,
        9,1,9,1,9,1,9,4,9,154,8,9,11,9,12,9,155,1,9,1,9,1,10,1,10,1,10,1,
        10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,172,8,11,1,11,1,
        11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,186,8,
        13,1,13,1,13,1,14,1,14,5,14,192,8,14,10,14,12,14,195,9,14,1,14,1,
        14,1,15,1,15,5,15,201,8,15,10,15,12,15,204,9,15,1,15,1,15,1,16,1,
        16,3,16,210,8,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,3,17,222,8,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,5,
        17,233,8,17,10,17,12,17,236,9,17,1,18,1,18,3,18,240,8,18,1,18,1,
        18,1,18,3,18,245,8,18,1,18,1,18,1,18,1,18,3,18,251,8,18,1,19,1,19,
        1,20,1,20,1,21,1,21,1,22,1,22,1,22,0,1,34,23,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,0,3,1,0,28,29,1,0,25,
        27,1,0,30,35,296,0,49,1,0,0,0,2,54,1,0,0,0,4,79,1,0,0,0,6,81,1,0,
        0,0,8,94,1,0,0,0,10,97,1,0,0,0,12,112,1,0,0,0,14,118,1,0,0,0,16,
        129,1,0,0,0,18,149,1,0,0,0,20,159,1,0,0,0,22,163,1,0,0,0,24,175,
        1,0,0,0,26,178,1,0,0,0,28,189,1,0,0,0,30,198,1,0,0,0,32,209,1,0,
        0,0,34,221,1,0,0,0,36,250,1,0,0,0,38,252,1,0,0,0,40,254,1,0,0,0,
        42,256,1,0,0,0,44,258,1,0,0,0,46,48,3,2,1,0,47,46,1,0,0,0,48,51,
        1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,49,1,0,0,0,
        52,53,5,0,0,1,53,1,1,0,0,0,54,58,5,20,0,0,55,57,5,21,0,0,56,55,1,
        0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,61,1,0,0,0,60,
        58,1,0,0,0,61,65,5,1,0,0,62,64,3,4,2,0,63,62,1,0,0,0,64,67,1,0,0,
        0,65,63,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,65,1,0,0,0,68,69,
        5,2,0,0,69,3,1,0,0,0,70,80,3,6,3,0,71,80,3,8,4,0,72,80,3,10,5,0,
        73,80,3,12,6,0,74,80,3,14,7,0,75,80,3,16,8,0,76,80,3,18,9,0,77,80,
        3,20,10,0,78,80,3,22,11,0,79,70,1,0,0,0,79,71,1,0,0,0,79,72,1,0,
        0,0,79,73,1,0,0,0,79,74,1,0,0,0,79,75,1,0,0,0,79,76,1,0,0,0,79,77,
        1,0,0,0,79,78,1,0,0,0,80,5,1,0,0,0,81,82,5,21,0,0,82,92,5,17,0,0,
        83,93,3,40,20,0,84,93,3,42,21,0,85,93,3,44,22,0,86,93,3,28,14,0,
        87,93,3,30,15,0,88,93,3,32,16,0,89,93,3,34,17,0,90,93,3,24,12,0,
        91,93,3,26,13,0,92,83,1,0,0,0,92,84,1,0,0,0,92,85,1,0,0,0,92,86,
        1,0,0,0,92,87,1,0,0,0,92,88,1,0,0,0,92,89,1,0,0,0,92,90,1,0,0,0,
        92,91,1,0,0,0,93,7,1,0,0,0,94,95,5,16,0,0,95,96,5,21,0,0,96,9,1,
        0,0,0,97,108,5,15,0,0,98,109,3,38,19,0,99,109,3,40,20,0,100,109,
        3,42,21,0,101,109,3,44,22,0,102,109,3,28,14,0,103,109,3,30,15,0,
        104,109,3,32,16,0,105,109,3,34,17,0,106,109,3,24,12,0,107,109,3,
        26,13,0,108,98,1,0,0,0,108,99,1,0,0,0,108,100,1,0,0,0,108,101,1,
        0,0,0,108,102,1,0,0,0,108,103,1,0,0,0,108,104,1,0,0,0,108,105,1,
        0,0,0,108,106,1,0,0,0,108,107,1,0,0,0,109,110,1,0,0,0,110,108,1,
        0,0,0,110,111,1,0,0,0,111,11,1,0,0,0,112,116,5,18,0,0,113,117,3,
        44,22,0,114,117,3,30,15,0,115,117,3,40,20,0,116,113,1,0,0,0,116,
        114,1,0,0,0,116,115,1,0,0,0,117,13,1,0,0,0,118,126,5,20,0,0,119,
        125,3,40,20,0,120,125,3,42,21,0,121,125,3,34,17,0,122,125,3,24,12,
        0,123,125,3,26,13,0,124,119,1,0,0,0,124,120,1,0,0,0,124,121,1,0,
        0,0,124,122,1,0,0,0,124,123,1,0,0,0,125,128,1,0,0,0,126,124,1,0,
        0,0,126,127,1,0,0,0,127,15,1,0,0,0,128,126,1,0,0,0,129,130,5,3,0,
        0,130,131,3,36,18,0,131,133,5,1,0,0,132,134,3,4,2,0,133,132,1,0,
        0,0,134,135,1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,137,1,0,
        0,0,137,147,5,2,0,0,138,139,5,4,0,0,139,141,5,1,0,0,140,142,3,4,
        2,0,141,140,1,0,0,0,142,143,1,0,0,0,143,141,1,0,0,0,143,144,1,0,
        0,0,144,145,1,0,0,0,145,146,5,2,0,0,146,148,1,0,0,0,147,138,1,0,
        0,0,147,148,1,0,0,0,148,17,1,0,0,0,149,150,5,5,0,0,150,151,3,36,
        18,0,151,153,5,1,0,0,152,154,3,4,2,0,153,152,1,0,0,0,154,155,1,0,
        0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,157,1,0,0,0,157,158,5,2,
        0,0,158,19,1,0,0,0,159,160,3,40,20,0,160,161,5,6,0,0,161,162,3,34,
        17,0,162,21,1,0,0,0,163,164,5,7,0,0,164,165,3,40,20,0,165,171,5,
        8,0,0,166,172,3,40,20,0,167,172,3,42,21,0,168,172,3,34,17,0,169,
        172,3,24,12,0,170,172,3,26,13,0,171,166,1,0,0,0,171,167,1,0,0,0,
        171,168,1,0,0,0,171,169,1,0,0,0,171,170,1,0,0,0,172,173,1,0,0,0,
        173,174,5,9,0,0,174,23,1,0,0,0,175,176,5,10,0,0,176,177,3,40,20,
        0,177,25,1,0,0,0,178,179,3,40,20,0,179,185,5,8,0,0,180,186,3,40,
        20,0,181,186,3,42,21,0,182,186,3,34,17,0,183,186,3,24,12,0,184,186,
        3,26,13,0,185,180,1,0,0,0,185,181,1,0,0,0,185,182,1,0,0,0,185,183,
        1,0,0,0,185,184,1,0,0,0,186,187,1,0,0,0,187,188,5,9,0,0,188,27,1,
        0,0,0,189,193,5,11,0,0,190,192,5,22,0,0,191,190,1,0,0,0,192,195,
        1,0,0,0,193,191,1,0,0,0,193,194,1,0,0,0,194,196,1,0,0,0,195,193,
        1,0,0,0,196,197,5,12,0,0,197,29,1,0,0,0,198,202,5,11,0,0,199,201,
        5,19,0,0,200,199,1,0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,203,
        1,0,0,0,203,205,1,0,0,0,204,202,1,0,0,0,205,206,5,12,0,0,206,31,
        1,0,0,0,207,210,3,44,22,0,208,210,3,40,20,0,209,207,1,0,0,0,209,
        208,1,0,0,0,210,211,1,0,0,0,211,212,7,0,0,0,212,213,3,42,21,0,213,
        33,1,0,0,0,214,215,6,17,-1,0,215,216,5,13,0,0,216,217,3,34,17,0,
        217,218,5,14,0,0,218,222,1,0,0,0,219,222,3,42,21,0,220,222,3,40,
        20,0,221,214,1,0,0,0,221,219,1,0,0,0,221,220,1,0,0,0,222,234,1,0,
        0,0,223,224,10,5,0,0,224,225,7,1,0,0,225,233,3,34,17,6,226,227,10,
        4,0,0,227,228,7,0,0,0,228,233,3,34,17,5,229,230,10,3,0,0,230,231,
        7,2,0,0,231,233,3,34,17,4,232,223,1,0,0,0,232,226,1,0,0,0,232,229,
        1,0,0,0,233,236,1,0,0,0,234,232,1,0,0,0,234,235,1,0,0,0,235,35,1,
        0,0,0,236,234,1,0,0,0,237,240,3,44,22,0,238,240,3,40,20,0,239,237,
        1,0,0,0,239,238,1,0,0,0,240,241,1,0,0,0,241,244,7,2,0,0,242,245,
        3,44,22,0,243,245,3,40,20,0,244,242,1,0,0,0,244,243,1,0,0,0,245,
        251,1,0,0,0,246,247,3,34,17,0,247,248,7,2,0,0,248,249,3,34,17,0,
        249,251,1,0,0,0,250,239,1,0,0,0,250,246,1,0,0,0,251,37,1,0,0,0,252,
        253,5,24,0,0,253,39,1,0,0,0,254,255,5,21,0,0,255,41,1,0,0,0,256,
        257,5,22,0,0,257,43,1,0,0,0,258,259,5,19,0,0,259,45,1,0,0,0,25,49,
        58,65,79,92,108,110,116,124,126,135,143,147,155,171,185,193,202,
        209,221,232,234,239,244,250
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
    RULE_enters = 14
    RULE_notes = 15
    RULE_transposicio = 16
    RULE_expressio = 17
    RULE_condicio = 18
    RULE_text = 19
    RULE_variable = 20
    RULE_enter = 21
    RULE_nota = 22

    ruleNames =  [ "root", "procediment", "instruccio", "assignacio", "lectura", 
                   "escriptura", "reproduccio", "invocacio", "condicional", 
                   "iteracio", "afegit", "tall", "mida", "consulta", "enters", 
                   "notes", "transposicio", "expressio", "condicio", "text", 
                   "variable", "enter", "nota" ]

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
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.ID:
                self.state = 46
                self.procediment()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
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
            self.state = 54
            self.match(jsbachParser.ID)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.VARIABLE:
                self.state = 55
                self.match(jsbachParser.VARIABLE)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.match(jsbachParser.T__0)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.T__2) | (1 << jsbachParser.T__4) | (1 << jsbachParser.T__6) | (1 << jsbachParser.ESCRIPTURA) | (1 << jsbachParser.LECTURA) | (1 << jsbachParser.REPRODUCCIO) | (1 << jsbachParser.ID) | (1 << jsbachParser.VARIABLE))) != 0):
                self.state = 62
                self.instruccio()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
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
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 70
                self.assignacio()
                pass

            elif la_ == 2:
                self.state = 71
                self.lectura()
                pass

            elif la_ == 3:
                self.state = 72
                self.escriptura()
                pass

            elif la_ == 4:
                self.state = 73
                self.reproduccio()
                pass

            elif la_ == 5:
                self.state = 74
                self.invocacio()
                pass

            elif la_ == 6:
                self.state = 75
                self.condicional()
                pass

            elif la_ == 7:
                self.state = 76
                self.iteracio()
                pass

            elif la_ == 8:
                self.state = 77
                self.afegit()
                pass

            elif la_ == 9:
                self.state = 78
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


        def enter(self):
            return self.getTypedRuleContext(jsbachParser.EnterContext,0)


        def nota(self):
            return self.getTypedRuleContext(jsbachParser.NotaContext,0)


        def enters(self):
            return self.getTypedRuleContext(jsbachParser.EntersContext,0)


        def notes(self):
            return self.getTypedRuleContext(jsbachParser.NotesContext,0)


        def transposicio(self):
            return self.getTypedRuleContext(jsbachParser.TransposicioContext,0)


        def expressio(self):
            return self.getTypedRuleContext(jsbachParser.ExpressioContext,0)


        def mida(self):
            return self.getTypedRuleContext(jsbachParser.MidaContext,0)


        def consulta(self):
            return self.getTypedRuleContext(jsbachParser.ConsultaContext,0)


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
            self.state = 81
            self.match(jsbachParser.VARIABLE)
            self.state = 82
            self.match(jsbachParser.ASSIGNACIO)
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 83
                self.variable()
                pass

            elif la_ == 2:
                self.state = 84
                self.enter()
                pass

            elif la_ == 3:
                self.state = 85
                self.nota()
                pass

            elif la_ == 4:
                self.state = 86
                self.enters()
                pass

            elif la_ == 5:
                self.state = 87
                self.notes()
                pass

            elif la_ == 6:
                self.state = 88
                self.transposicio()
                pass

            elif la_ == 7:
                self.state = 89
                self.expressio(0)
                pass

            elif la_ == 8:
                self.state = 90
                self.mida()
                pass

            elif la_ == 9:
                self.state = 91
                self.consulta()
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
            self.state = 94
            self.match(jsbachParser.LECTURA)
            self.state = 95
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

        def text(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.TextContext)
            else:
                return self.getTypedRuleContext(jsbachParser.TextContext,i)


        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.VariableContext)
            else:
                return self.getTypedRuleContext(jsbachParser.VariableContext,i)


        def enter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.EnterContext)
            else:
                return self.getTypedRuleContext(jsbachParser.EnterContext,i)


        def nota(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.NotaContext)
            else:
                return self.getTypedRuleContext(jsbachParser.NotaContext,i)


        def enters(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.EntersContext)
            else:
                return self.getTypedRuleContext(jsbachParser.EntersContext,i)


        def notes(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.NotesContext)
            else:
                return self.getTypedRuleContext(jsbachParser.NotesContext,i)


        def transposicio(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.TransposicioContext)
            else:
                return self.getTypedRuleContext(jsbachParser.TransposicioContext,i)


        def expressio(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExpressioContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExpressioContext,i)


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
            self.state = 97
            self.match(jsbachParser.ESCRIPTURA)
            self.state = 108 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 108
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        self.state = 98
                        self.text()
                        pass

                    elif la_ == 2:
                        self.state = 99
                        self.variable()
                        pass

                    elif la_ == 3:
                        self.state = 100
                        self.enter()
                        pass

                    elif la_ == 4:
                        self.state = 101
                        self.nota()
                        pass

                    elif la_ == 5:
                        self.state = 102
                        self.enters()
                        pass

                    elif la_ == 6:
                        self.state = 103
                        self.notes()
                        pass

                    elif la_ == 7:
                        self.state = 104
                        self.transposicio()
                        pass

                    elif la_ == 8:
                        self.state = 105
                        self.expressio(0)
                        pass

                    elif la_ == 9:
                        self.state = 106
                        self.mida()
                        pass

                    elif la_ == 10:
                        self.state = 107
                        self.consulta()
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 110 
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

        def nota(self):
            return self.getTypedRuleContext(jsbachParser.NotaContext,0)


        def notes(self):
            return self.getTypedRuleContext(jsbachParser.NotesContext,0)


        def variable(self):
            return self.getTypedRuleContext(jsbachParser.VariableContext,0)


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
            self.state = 112
            self.match(jsbachParser.REPRODUCCIO)
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [jsbachParser.NOTA]:
                self.state = 113
                self.nota()
                pass
            elif token in [jsbachParser.T__10]:
                self.state = 114
                self.notes()
                pass
            elif token in [jsbachParser.VARIABLE]:
                self.state = 115
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

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

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.VariableContext)
            else:
                return self.getTypedRuleContext(jsbachParser.VariableContext,i)


        def enter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.EnterContext)
            else:
                return self.getTypedRuleContext(jsbachParser.EnterContext,i)


        def expressio(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExpressioContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExpressioContext,i)


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
            self.state = 118
            self.match(jsbachParser.ID)
            self.state = 126
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 124
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        self.state = 119
                        self.variable()
                        pass

                    elif la_ == 2:
                        self.state = 120
                        self.enter()
                        pass

                    elif la_ == 3:
                        self.state = 121
                        self.expressio(0)
                        pass

                    elif la_ == 4:
                        self.state = 122
                        self.mida()
                        pass

                    elif la_ == 5:
                        self.state = 123
                        self.consulta()
                        pass

             
                self.state = 128
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
            self.state = 129
            self.match(jsbachParser.T__2)
            self.state = 130
            self.condicio()
            self.state = 131
            self.match(jsbachParser.T__0)
            self.state = 133 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 132
                self.instruccio()
                self.state = 135 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.T__2) | (1 << jsbachParser.T__4) | (1 << jsbachParser.T__6) | (1 << jsbachParser.ESCRIPTURA) | (1 << jsbachParser.LECTURA) | (1 << jsbachParser.REPRODUCCIO) | (1 << jsbachParser.ID) | (1 << jsbachParser.VARIABLE))) != 0)):
                    break

            self.state = 137
            self.match(jsbachParser.T__1)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==jsbachParser.T__3:
                self.state = 138
                self.match(jsbachParser.T__3)
                self.state = 139
                self.match(jsbachParser.T__0)
                self.state = 141 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 140
                    self.instruccio()
                    self.state = 143 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.T__2) | (1 << jsbachParser.T__4) | (1 << jsbachParser.T__6) | (1 << jsbachParser.ESCRIPTURA) | (1 << jsbachParser.LECTURA) | (1 << jsbachParser.REPRODUCCIO) | (1 << jsbachParser.ID) | (1 << jsbachParser.VARIABLE))) != 0)):
                        break

                self.state = 145
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
            self.state = 149
            self.match(jsbachParser.T__4)
            self.state = 150
            self.condicio()
            self.state = 151
            self.match(jsbachParser.T__0)
            self.state = 153 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 152
                self.instruccio()
                self.state = 155 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.T__2) | (1 << jsbachParser.T__4) | (1 << jsbachParser.T__6) | (1 << jsbachParser.ESCRIPTURA) | (1 << jsbachParser.LECTURA) | (1 << jsbachParser.REPRODUCCIO) | (1 << jsbachParser.ID) | (1 << jsbachParser.VARIABLE))) != 0)):
                    break

            self.state = 157
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
            self.state = 159
            self.variable()
            self.state = 160
            self.match(jsbachParser.T__5)
            self.state = 161
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

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.VariableContext)
            else:
                return self.getTypedRuleContext(jsbachParser.VariableContext,i)


        def enter(self):
            return self.getTypedRuleContext(jsbachParser.EnterContext,0)


        def expressio(self):
            return self.getTypedRuleContext(jsbachParser.ExpressioContext,0)


        def mida(self):
            return self.getTypedRuleContext(jsbachParser.MidaContext,0)


        def consulta(self):
            return self.getTypedRuleContext(jsbachParser.ConsultaContext,0)


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
            self.state = 163
            self.match(jsbachParser.T__6)
            self.state = 164
            self.variable()
            self.state = 165
            self.match(jsbachParser.T__7)
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 166
                self.variable()
                pass

            elif la_ == 2:
                self.state = 167
                self.enter()
                pass

            elif la_ == 3:
                self.state = 168
                self.expressio(0)
                pass

            elif la_ == 4:
                self.state = 169
                self.mida()
                pass

            elif la_ == 5:
                self.state = 170
                self.consulta()
                pass


            self.state = 173
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
            self.state = 175
            self.match(jsbachParser.T__9)
            self.state = 176
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

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.VariableContext)
            else:
                return self.getTypedRuleContext(jsbachParser.VariableContext,i)


        def enter(self):
            return self.getTypedRuleContext(jsbachParser.EnterContext,0)


        def expressio(self):
            return self.getTypedRuleContext(jsbachParser.ExpressioContext,0)


        def mida(self):
            return self.getTypedRuleContext(jsbachParser.MidaContext,0)


        def consulta(self):
            return self.getTypedRuleContext(jsbachParser.ConsultaContext,0)


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
            self.state = 178
            self.variable()
            self.state = 179
            self.match(jsbachParser.T__7)
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 180
                self.variable()
                pass

            elif la_ == 2:
                self.state = 181
                self.enter()
                pass

            elif la_ == 3:
                self.state = 182
                self.expressio(0)
                pass

            elif la_ == 4:
                self.state = 183
                self.mida()
                pass

            elif la_ == 5:
                self.state = 184
                self.consulta()
                pass


            self.state = 187
            self.match(jsbachParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntersContext(ParserRuleContext):
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
            return jsbachParser.RULE_enters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnters" ):
                return visitor.visitEnters(self)
            else:
                return visitor.visitChildren(self)




    def enters(self):

        localctx = jsbachParser.EntersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_enters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(jsbachParser.T__10)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.ENTER:
                self.state = 190
                self.match(jsbachParser.ENTER)
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 196
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
            self.state = 198
            self.match(jsbachParser.T__10)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.NOTA:
                self.state = 199
                self.match(jsbachParser.NOTA)
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 205
            self.match(jsbachParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransposicioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enter(self):
            return self.getTypedRuleContext(jsbachParser.EnterContext,0)


        def SUMA(self):
            return self.getToken(jsbachParser.SUMA, 0)

        def RESTA(self):
            return self.getToken(jsbachParser.RESTA, 0)

        def nota(self):
            return self.getTypedRuleContext(jsbachParser.NotaContext,0)


        def variable(self):
            return self.getTypedRuleContext(jsbachParser.VariableContext,0)


        def getRuleIndex(self):
            return jsbachParser.RULE_transposicio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransposicio" ):
                return visitor.visitTransposicio(self)
            else:
                return visitor.visitChildren(self)




    def transposicio(self):

        localctx = jsbachParser.TransposicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_transposicio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [jsbachParser.NOTA]:
                self.state = 207
                self.nota()
                pass
            elif token in [jsbachParser.VARIABLE]:
                self.state = 208
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 211
            _la = self._input.LA(1)
            if not(_la==jsbachParser.SUMA or _la==jsbachParser.RESTA):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 212
            self.enter()
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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expressio, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [jsbachParser.T__12]:
                self.state = 215
                self.match(jsbachParser.T__12)
                self.state = 216
                self.expressio(0)
                self.state = 217
                self.match(jsbachParser.T__13)
                pass
            elif token in [jsbachParser.ENTER]:
                self.state = 219
                self.enter()
                pass
            elif token in [jsbachParser.VARIABLE]:
                self.state = 220
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 234
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 232
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = jsbachParser.ExpressioContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressio)
                        self.state = 223
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 224
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.MULTIPLICACIO) | (1 << jsbachParser.DIVISIO) | (1 << jsbachParser.MODUL))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 225
                        self.expressio(6)
                        pass

                    elif la_ == 2:
                        localctx = jsbachParser.ExpressioContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressio)
                        self.state = 226
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 227
                        _la = self._input.LA(1)
                        if not(_la==jsbachParser.SUMA or _la==jsbachParser.RESTA):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 228
                        self.expressio(5)
                        pass

                    elif la_ == 3:
                        localctx = jsbachParser.ExpressioContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressio)
                        self.state = 229
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 230
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.MAJOR) | (1 << jsbachParser.MENOR) | (1 << jsbachParser.MAJORIGUAL) | (1 << jsbachParser.MENORIGUAL) | (1 << jsbachParser.IGUAL) | (1 << jsbachParser.DIFERENT))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 231
                        self.expressio(4)
                        pass

             
                self.state = 236
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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

        def nota(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.NotaContext)
            else:
                return self.getTypedRuleContext(jsbachParser.NotaContext,i)


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


        def getRuleIndex(self):
            return jsbachParser.RULE_condicio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicio" ):
                return visitor.visitCondicio(self)
            else:
                return visitor.visitChildren(self)




    def condicio(self):

        localctx = jsbachParser.CondicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_condicio)
        self._la = 0 # Token type
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [jsbachParser.NOTA]:
                    self.state = 237
                    self.nota()
                    pass
                elif token in [jsbachParser.VARIABLE]:
                    self.state = 238
                    self.variable()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 241
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.MAJOR) | (1 << jsbachParser.MENOR) | (1 << jsbachParser.MAJORIGUAL) | (1 << jsbachParser.MENORIGUAL) | (1 << jsbachParser.IGUAL) | (1 << jsbachParser.DIFERENT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 244
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [jsbachParser.NOTA]:
                    self.state = 242
                    self.nota()
                    pass
                elif token in [jsbachParser.VARIABLE]:
                    self.state = 243
                    self.variable()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.expressio(0)
                self.state = 247
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.MAJOR) | (1 << jsbachParser.MENOR) | (1 << jsbachParser.MAJORIGUAL) | (1 << jsbachParser.MENORIGUAL) | (1 << jsbachParser.IGUAL) | (1 << jsbachParser.DIFERENT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 248
                self.expressio(0)
                pass


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
        self.enterRule(localctx, 38, self.RULE_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
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
        self.enterRule(localctx, 40, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
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
        self.enterRule(localctx, 42, self.RULE_enter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(jsbachParser.ENTER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NotaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOTA(self):
            return self.getToken(jsbachParser.NOTA, 0)

        def getRuleIndex(self):
            return jsbachParser.RULE_nota

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNota" ):
                return visitor.visitNota(self)
            else:
                return visitor.visitChildren(self)




    def nota(self):

        localctx = jsbachParser.NotaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_nota)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(jsbachParser.NOTA)
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
        self._predicates[17] = self.expressio_sempred
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
         




