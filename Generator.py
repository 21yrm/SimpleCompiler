from llvmlite import ir
from antlr4 import *
from CgrammerLexer import CgrammerLexer
from CgrammerParser import CgrammerParser
from CgrammerVisitor import CgrammerVisitor
from SymbolTable import SymbolTable, Structure

# from Generator.ErrorListener import syntaxErrorListener
# from Generator.ErrorListener import SemanticError

double = ir.DoubleType()
int1 = ir.IntType(1)
int32 = ir.IntType(32)
int8 = ir.IntType(8)
void = ir.VoidType()


class Visitor(CgrammerVisitor):
    """
    生成器类，用于进行语义分析并且转化为LLVM
    """

    def __init__(self):
        super(CgrammerVisitor, self).__init__()

        # 控制llvm生成
        self.Module = ir.Module()
        self.Module.triple = "x86_64-pc-windows-msvc"
        self.Module.data_layout = "e-m:w-i64:64-f80:128-n8:16:32:64-S128"

        # 语句块
        self.Blocks = []

        # 待生成的llvm语句块
        self.Builders = []

        # 函数列表
        self.Functions = dict()

        # 结构体列表
        self.Structure = Structure()

        # 当前所在函数
        self.CurrentFunction = ''
        self.Constants = 0

        # 这个变量是否需要加载
        self.WhetherNeedLoad = True

        # endif块
        self.EndifBlock = None

        # 符号表
        self.SymbolTable = SymbolTable()

    def visitCode(self, ctx: CgrammerParser.CodeContext):
        for i in range(ctx.getChildCount()):
            self.visit(ctx.getChild(i))

    def visitIf(self, ctx: CgrammerParser.IfContext):
        self.visitChildren(ctx)

    def visitWhile(self, ctx: CgrammerParser.WhileContext):
        self.visitChildren(ctx)

    def visitFor(self, ctx: CgrammerParser.ForContext):
        self.visitChildren(ctx)

    def visitSwitch(self, ctx: CgrammerParser.SwitchContext):
        self.visitChildren(ctx)

    def visitSingle(self, ctx: CgrammerParser.SingleContext):
        self.visitChildren(ctx)

    def visitFunction(self, ctx: CgrammerParser.FunctionContext):
        self.visitChildren(ctx)

    def visitIf_block(self, ctx: CgrammerParser.If_blockContext):
        self.block

    def save(self, filename):
        """
        保存到文件
        描述：文件名含后缀
        返回：无
        """
        with open(filename, "w") as f:
            f.write(repr(self.Module))


def generate(input_filename, output_filename):
    """
    将C代码文件转成IR代码文件
    :param input_filename: C代码文件
    :param output_filename: IR代码文件
    :return: 生成是否成功
    """
    lexer = CgrammerLexer(FileStream(input_filename))
    stream = CommonTokenStream(lexer)
    parser = CgrammerParser(stream)
    # parser.removeErrorListeners()
    # errorListener = syntaxErrorListener()
    # parser.addErrorListener(errorListener)
    visitor = Visitor()
    visitor.visit(parser.code())
    visitor.save(output_filename)
