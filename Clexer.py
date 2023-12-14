# Generated from Clexer.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,11,68,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,5,0,26,8,0,10,0,
        12,0,29,9,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,
        1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,4,9,54,8,9,11,9,12,9,55,
        1,9,1,9,1,10,1,10,1,10,1,10,5,10,64,8,10,10,10,12,10,67,9,10,0,0,
        11,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,1,0,4,3,0,
        65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,3,0,9,10,13,13,32,
        32,2,0,10,10,13,13,70,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,
        0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,
        0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,1,23,1,0,0,0,3,30,1,0,0,0,5,33,1,
        0,0,0,7,38,1,0,0,0,9,42,1,0,0,0,11,44,1,0,0,0,13,46,1,0,0,0,15,48,
        1,0,0,0,17,50,1,0,0,0,19,53,1,0,0,0,21,59,1,0,0,0,23,27,7,0,0,0,
        24,26,7,1,0,0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,
        0,0,0,28,2,1,0,0,0,29,27,1,0,0,0,30,31,5,105,0,0,31,32,5,102,0,0,
        32,4,1,0,0,0,33,34,5,101,0,0,34,35,5,108,0,0,35,36,5,115,0,0,36,
        37,5,101,0,0,37,6,1,0,0,0,38,39,5,102,0,0,39,40,5,111,0,0,40,41,
        5,114,0,0,41,8,1,0,0,0,42,43,5,61,0,0,43,10,1,0,0,0,44,45,5,43,0,
        0,45,12,1,0,0,0,46,47,5,45,0,0,47,14,1,0,0,0,48,49,5,59,0,0,49,16,
        1,0,0,0,50,51,5,44,0,0,51,18,1,0,0,0,52,54,7,2,0,0,53,52,1,0,0,0,
        54,55,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,57,1,0,0,0,57,58,6,
        9,0,0,58,20,1,0,0,0,59,60,5,47,0,0,60,61,5,47,0,0,61,65,1,0,0,0,
        62,64,8,3,0,0,63,62,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,
        0,0,0,66,22,1,0,0,0,67,65,1,0,0,0,4,0,27,55,65,1,6,0,0
    ]

class Clexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IDENTIFIER = 1
    IF = 2
    ELSE = 3
    FOR = 4
    ASSIGN = 5
    PLUS = 6
    MINUS = 7
    SEMICOLON = 8
    COMMA = 9
    WS = 10
    COMMENT = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'='", "'+'", "'-'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "IF", "ELSE", "FOR", "ASSIGN", "PLUS", "MINUS", 
            "SEMICOLON", "COMMA", "WS", "COMMENT" ]

    ruleNames = [ "IDENTIFIER", "IF", "ELSE", "FOR", "ASSIGN", "PLUS", "MINUS", 
                  "SEMICOLON", "COMMA", "WS", "COMMENT" ]

    grammarFileName = "Clexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


