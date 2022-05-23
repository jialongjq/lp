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
        4,1,28,101,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,5,2,36,8,2,10,2,12,2,39,9,2,1,2,
        1,2,5,2,43,8,2,10,2,12,2,46,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,
        1,4,1,5,1,5,1,5,5,5,60,8,5,10,5,12,5,63,9,5,1,5,1,5,1,6,1,6,1,6,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,78,8,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,5,7,89,8,7,10,7,12,7,92,9,7,1,8,1,8,5,8,96,8,8,10,
        8,12,8,99,9,8,1,8,0,1,14,9,0,2,4,6,8,10,12,14,16,0,3,1,0,16,18,1,
        0,19,20,1,0,21,26,106,0,21,1,0,0,0,2,31,1,0,0,0,4,33,1,0,0,0,6,49,
        1,0,0,0,8,53,1,0,0,0,10,56,1,0,0,0,12,66,1,0,0,0,14,77,1,0,0,0,16,
        93,1,0,0,0,18,20,3,4,2,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,
        0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,0,0,1,25,1,1,
        0,0,0,26,32,3,6,3,0,27,32,3,8,4,0,28,32,3,12,6,0,29,32,3,10,5,0,
        30,32,3,16,8,0,31,26,1,0,0,0,31,27,1,0,0,0,31,28,1,0,0,0,31,29,1,
        0,0,0,31,30,1,0,0,0,32,3,1,0,0,0,33,37,5,12,0,0,34,36,5,13,0,0,35,
        34,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,
        0,39,37,1,0,0,0,40,44,5,1,0,0,41,43,3,2,1,0,42,41,1,0,0,0,43,46,
        1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,44,1,0,0,0,
        47,48,5,2,0,0,48,5,1,0,0,0,49,50,5,13,0,0,50,51,5,9,0,0,51,52,3,
        14,7,0,52,7,1,0,0,0,53,54,5,7,0,0,54,55,3,14,7,0,55,9,1,0,0,0,56,
        57,5,10,0,0,57,61,5,3,0,0,58,60,5,11,0,0,59,58,1,0,0,0,60,63,1,0,
        0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,61,1,0,0,0,64,65,
        5,4,0,0,65,11,1,0,0,0,66,67,5,8,0,0,67,68,5,13,0,0,68,13,1,0,0,0,
        69,70,6,7,-1,0,70,71,5,5,0,0,71,72,3,14,7,0,72,73,5,6,0,0,73,78,
        1,0,0,0,74,78,5,14,0,0,75,78,5,13,0,0,76,78,5,15,0,0,77,69,1,0,0,
        0,77,74,1,0,0,0,77,75,1,0,0,0,77,76,1,0,0,0,78,90,1,0,0,0,79,80,
        10,6,0,0,80,81,7,0,0,0,81,89,3,14,7,7,82,83,10,5,0,0,83,84,7,1,0,
        0,84,89,3,14,7,6,85,86,10,4,0,0,86,87,7,2,0,0,87,89,3,14,7,5,88,
        79,1,0,0,0,88,82,1,0,0,0,88,85,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,
        0,90,91,1,0,0,0,91,15,1,0,0,0,92,90,1,0,0,0,93,97,5,12,0,0,94,96,
        3,14,7,0,95,94,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,
        98,17,1,0,0,0,99,97,1,0,0,0,9,21,31,37,44,61,77,88,90,97
    ]

class jsbachParser ( Parser ):

    grammarFileName = "jsbach.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|:'", "':|'", "'{'", "'}'", "'('", "')'", 
                     "'<!>'", "'<?>'", "'<-'", "'<:>'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'*'", "'/'", 
                     "'%'", "'+'", "'-'", "'>'", "'<'", "'>='", "'<='", 
                     "'='", "'/='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ESCRIPTURA", 
                      "LECTURA", "ASSIGNACIO", "REPRODUCCIO", "NOTA", "ID", 
                      "VARIABLE", "NUMERO", "TEXT", "MULTIPLICACIO", "DIVISIO", 
                      "MODUL", "SUMA", "RESTA", "MAJOR", "MENOR", "MAJORIGUAL", 
                      "MENORIGUAL", "IGUAL", "DIFERENT", "COMENTARI", "WS" ]

    RULE_root = 0
    RULE_instruccio = 1
    RULE_procediment = 2
    RULE_assignacio = 3
    RULE_escriptura = 4
    RULE_reproduccio = 5
    RULE_lectura = 6
    RULE_expressio = 7
    RULE_invocacio = 8

    ruleNames =  [ "root", "instruccio", "procediment", "assignacio", "escriptura", 
                   "reproduccio", "lectura", "expressio", "invocacio" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    ESCRIPTURA=7
    LECTURA=8
    ASSIGNACIO=9
    REPRODUCCIO=10
    NOTA=11
    ID=12
    VARIABLE=13
    NUMERO=14
    TEXT=15
    MULTIPLICACIO=16
    DIVISIO=17
    MODUL=18
    SUMA=19
    RESTA=20
    MAJOR=21
    MENOR=22
    MAJORIGUAL=23
    MENORIGUAL=24
    IGUAL=25
    DIFERENT=26
    COMENTARI=27
    WS=28

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
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.ID:
                self.state = 18
                self.procediment()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(jsbachParser.EOF)
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


        def escriptura(self):
            return self.getTypedRuleContext(jsbachParser.EscripturaContext,0)


        def lectura(self):
            return self.getTypedRuleContext(jsbachParser.LecturaContext,0)


        def reproduccio(self):
            return self.getTypedRuleContext(jsbachParser.ReproduccioContext,0)


        def invocacio(self):
            return self.getTypedRuleContext(jsbachParser.InvocacioContext,0)


        def getRuleIndex(self):
            return jsbachParser.RULE_instruccio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccio" ):
                return visitor.visitInstruccio(self)
            else:
                return visitor.visitChildren(self)




    def instruccio(self):

        localctx = jsbachParser.InstruccioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [jsbachParser.VARIABLE]:
                self.state = 26
                self.assignacio()
                pass
            elif token in [jsbachParser.ESCRIPTURA]:
                self.state = 27
                self.escriptura()
                pass
            elif token in [jsbachParser.LECTURA]:
                self.state = 28
                self.lectura()
                pass
            elif token in [jsbachParser.REPRODUCCIO]:
                self.state = 29
                self.reproduccio()
                pass
            elif token in [jsbachParser.ID]:
                self.state = 30
                self.invocacio()
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
        self.enterRule(localctx, 4, self.RULE_procediment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(jsbachParser.ID)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.VARIABLE:
                self.state = 34
                self.match(jsbachParser.VARIABLE)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(jsbachParser.T__0)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.ESCRIPTURA) | (1 << jsbachParser.LECTURA) | (1 << jsbachParser.REPRODUCCIO) | (1 << jsbachParser.ID) | (1 << jsbachParser.VARIABLE))) != 0):
                self.state = 41
                self.instruccio()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 47
            self.match(jsbachParser.T__1)
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

        def expressio(self):
            return self.getTypedRuleContext(jsbachParser.ExpressioContext,0)


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
            self.state = 49
            self.match(jsbachParser.VARIABLE)
            self.state = 50
            self.match(jsbachParser.ASSIGNACIO)
            self.state = 51
            self.expressio(0)
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

        def expressio(self):
            return self.getTypedRuleContext(jsbachParser.ExpressioContext,0)


        def getRuleIndex(self):
            return jsbachParser.RULE_escriptura

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscriptura" ):
                return visitor.visitEscriptura(self)
            else:
                return visitor.visitChildren(self)




    def escriptura(self):

        localctx = jsbachParser.EscripturaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_escriptura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(jsbachParser.ESCRIPTURA)
            self.state = 54
            self.expressio(0)
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
        self.enterRule(localctx, 10, self.RULE_reproduccio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(jsbachParser.REPRODUCCIO)
            self.state = 57
            self.match(jsbachParser.T__2)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.NOTA:
                self.state = 58
                self.match(jsbachParser.NOTA)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(jsbachParser.T__3)
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
        self.enterRule(localctx, 12, self.RULE_lectura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(jsbachParser.LECTURA)
            self.state = 67
            self.match(jsbachParser.VARIABLE)
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


        def NUMERO(self):
            return self.getToken(jsbachParser.NUMERO, 0)

        def VARIABLE(self):
            return self.getToken(jsbachParser.VARIABLE, 0)

        def TEXT(self):
            return self.getToken(jsbachParser.TEXT, 0)

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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expressio, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [jsbachParser.T__4]:
                self.state = 70
                self.match(jsbachParser.T__4)
                self.state = 71
                self.expressio(0)
                self.state = 72
                self.match(jsbachParser.T__5)
                pass
            elif token in [jsbachParser.NUMERO]:
                self.state = 74
                self.match(jsbachParser.NUMERO)
                pass
            elif token in [jsbachParser.VARIABLE]:
                self.state = 75
                self.match(jsbachParser.VARIABLE)
                pass
            elif token in [jsbachParser.TEXT]:
                self.state = 76
                self.match(jsbachParser.TEXT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 88
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = jsbachParser.ExpressioContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressio)
                        self.state = 79
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 80
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.MULTIPLICACIO) | (1 << jsbachParser.DIVISIO) | (1 << jsbachParser.MODUL))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 81
                        self.expressio(7)
                        pass

                    elif la_ == 2:
                        localctx = jsbachParser.ExpressioContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressio)
                        self.state = 82
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 83
                        _la = self._input.LA(1)
                        if not(_la==jsbachParser.SUMA or _la==jsbachParser.RESTA):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 84
                        self.expressio(6)
                        pass

                    elif la_ == 3:
                        localctx = jsbachParser.ExpressioContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressio)
                        self.state = 85
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 86
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.MAJOR) | (1 << jsbachParser.MENOR) | (1 << jsbachParser.MAJORIGUAL) | (1 << jsbachParser.MENORIGUAL) | (1 << jsbachParser.IGUAL) | (1 << jsbachParser.DIFERENT))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 87
                        self.expressio(5)
                        pass

             
                self.state = 92
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 16, self.RULE_invocacio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(jsbachParser.ID)
            self.state = 97
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 94
                    self.expressio(0) 
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
        self._predicates[7] = self.expressio_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expressio_sempred(self, localctx:ExpressioContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




