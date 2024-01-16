from antlr4.error.ErrorListener import ErrorListener
from antlr4 import *


class SemanticError(Exception):
    """�?义错�?基类"""

    def __init__(self, msg, ctx=None):
        super().__init__()
        if ctx:
            self.line = ctx.start.line  # 错�??出现位置
            self.column = ctx.start.column
        else:
            self.line = 0
            self.column = 0
        self.msg = msg

    def __str__(self):
        return "SemanticError: " + str(self.line) + ":" + str(self.column) + " " + self.msg


# �?法错�?检查与反�??
class SyntaxErrorListener(ErrorListener):

    # 打印�?法错�?
    def syntaxError(self, recognizer, offending_symbol, row, column, msg, e):
        exception = "(row:" + str(row) + ",column:" + str(column) + ") " + msg
        print('SyntaxError: ' + exception)
