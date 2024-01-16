from llvmlite import ir
from antlr4 import *
from grammer.CgrammerLexer import CgrammerLexer
from grammer.CgrammerParser import CgrammerParser
from grammer.CgrammerVisitor import CgrammerVisitor
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

        # 当前所在函数
        self.CurrentFunction = ''
        self.Constants = 0

        # 这个变量是否需要加载
        self.WhetherNeedLoad = True

        # endif块
        self.EndifBlock = None

        # 符号表
        self.st = SymbolTable()

        # Visit a parse tree produced by CgrammerParser#int.


    def visitInt(self, ctx:CgrammerParser.IntContext):
        return self.visitChildren(ctx)


    def visitFloat(self, ctx:CgrammerParser.FloatContext):
        return self.visitChildren(ctx)


    def visitChar(self, ctx:CgrammerParser.CharContext):
        return self.visitChildren(ctx)


    def visitBool(self, ctx:CgrammerParser.BoolContext):
        return self.visitChildren(ctx)


    def visitString(self, ctx:CgrammerParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#pointer_flag.
    def visitPointer_flag(self, ctx:CgrammerParser.Pointer_flagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#originalType.
    def visitOriginalType(self, ctx:CgrammerParser.OriginalTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#pointer.
    def visitPointer(self, ctx:CgrammerParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#index.
    def visitIndex(self, ctx:CgrammerParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#memset.
    def visitMemset(self, ctx:CgrammerParser.MemsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#strlen.
    def visitStrlen(self, ctx:CgrammerParser.StrlenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#printf.
    def visitPrintf(self, ctx:CgrammerParser.PrintfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#scanf.
    def visitScanf(self, ctx:CgrammerParser.ScanfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#variable_declaration.
    def visitVariable_declaration(self, ctx:CgrammerParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#params.
    def visitParams(self, ctx:CgrammerParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#params_definition.
    def visitParams_definition(self, ctx:CgrammerParser.Params_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#function_call.
    def visitFunction_call(self, ctx:CgrammerParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#id.
    def visitId(self, ctx:CgrammerParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#int_value.
    def visitInt_value(self, ctx:CgrammerParser.Int_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#float_value.
    def visitFloat_value(self, ctx:CgrammerParser.Float_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#char_value.
    def visitChar_value(self, ctx:CgrammerParser.Char_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#string_value.
    def visitString_value(self, ctx:CgrammerParser.String_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#bool_value.
    def visitBool_value(self, ctx:CgrammerParser.Bool_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#function_call_.
    def visitFunction_call_(self, ctx:CgrammerParser.Function_call_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#round.
    def visitRound(self, ctx:CgrammerParser.RoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#expr_value.
    def visitExpr_value(self, ctx:CgrammerParser.Expr_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#content_of.
    def visitContent_of(self, ctx:CgrammerParser.Content_ofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#address_of.
    def visitAddress_of(self, ctx:CgrammerParser.Address_ofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#array.
    def visitArray(self, ctx:CgrammerParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#unit.
    def visitUnit(self, ctx:CgrammerParser.UnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#lincrese.
    def visitLincrese(self, ctx:CgrammerParser.LincreseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#rincrease.
    def visitRincrease(self, ctx:CgrammerParser.RincreaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#ldecrease.
    def visitLdecrease(self, ctx:CgrammerParser.LdecreaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#rdecrease.
    def visitRdecrease(self, ctx:CgrammerParser.RdecreaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#not.
    def visitNot(self, ctx:CgrammerParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#positive.
    def visitPositive(self, ctx:CgrammerParser.PositiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#negative.
    def visitNegative(self, ctx:CgrammerParser.NegativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#addr.
    def visitAddr(self, ctx:CgrammerParser.AddrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#divide.
    def visitDivide(self, ctx:CgrammerParser.DivideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#unary.
    def visitUnary(self, ctx:CgrammerParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#multiply.
    def visitMultiply(self, ctx:CgrammerParser.MultiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#modulo.
    def visitModulo(self, ctx:CgrammerParser.ModuloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#add.
    def visitAdd(self, ctx:CgrammerParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#subtract.
    def visitSubtract(self, ctx:CgrammerParser.SubtractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#calc1.
    def visitCalc1(self, ctx:CgrammerParser.Calc1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#equal.
    def visitEqual(self, ctx:CgrammerParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#nequal.
    def visitNequal(self, ctx:CgrammerParser.NequalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#calc2.
    def visitCalc2(self, ctx:CgrammerParser.Calc2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#greater.
    def visitGreater(self, ctx:CgrammerParser.GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#gequal.
    def visitGequal(self, ctx:CgrammerParser.GequalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#less.
    def visitLess(self, ctx:CgrammerParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#leuqal.
    def visitLeuqal(self, ctx:CgrammerParser.LeuqalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#rop1.
    def visitRop1(self, ctx:CgrammerParser.Rop1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#or.
    def visitOr(self, ctx:CgrammerParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#and.
    def visitAnd(self, ctx:CgrammerParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#rop2.
    def visitRop2(self, ctx:CgrammerParser.Rop2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#expression.
    def visitExpression(self, ctx:CgrammerParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#assign.
    def visitAssign(self, ctx:CgrammerParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#addeqaul.
    def visitAddeqaul(self, ctx:CgrammerParser.AddeqaulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#suvequal.
    def visitSuvequal(self, ctx:CgrammerParser.SuvequalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#multiplyequal.
    def visitMultiplyequal(self, ctx:CgrammerParser.MultiplyequalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#divideequal.
    def visitDivideequal(self, ctx:CgrammerParser.DivideequalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#moduloequal.
    def visitModuloequal(self, ctx:CgrammerParser.ModuloequalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#assignment.
    def visitAssignment(self, ctx:CgrammerParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#variable_definition.
    def visitVariable_definition(self, ctx:CgrammerParser.Variable_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#memest_announce.
    def visitMemest_announce(self, ctx:CgrammerParser.Memest_announceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#strlen_announce.
    def visitStrlen_announce(self, ctx:CgrammerParser.Strlen_announceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#printf_announce.
    def visitPrintf_announce(self, ctx:CgrammerParser.Printf_announceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#scanf_annouce.
    def visitScanf_annouce(self, ctx:CgrammerParser.Scanf_annouceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#function_definition.
    def visitFunction_definition(self, ctx:CgrammerParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#if_block.
    def visitIf_block(self, ctx:CgrammerParser.If_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#while_block.
    def visitWhile_block(self, ctx:CgrammerParser.While_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#for_block.
    def visitFor_block(self, ctx:CgrammerParser.For_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#switch_block.
    def visitSwitch_block(self, ctx:CgrammerParser.Switch_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#line.
    def visitLine(self, ctx:CgrammerParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#if.
    def visitIf(self, ctx:CgrammerParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#while.
    def visitWhile(self, ctx:CgrammerParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#for.
    def visitFor(self, ctx:CgrammerParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#switch.
    def visitSwitch(self, ctx:CgrammerParser.SwitchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#single.
    def visitSingle(self, ctx:CgrammerParser.SingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#function.
    def visitFunction(self, ctx:CgrammerParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#simple_code.
    def visitSimple_code(self, ctx:CgrammerParser.Simple_codeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#domained_code.
    def visitDomained_code(self, ctx:CgrammerParser.Domained_codeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#code.
    def visitCode(self, ctx:CgrammerParser.CodeContext):
        return self.visitChildren(ctx)

    def save(self, filename):
        with open(filename, "w") as f:
            f.write(repr(self.Module))


class Compiler:
    # 遍历器
    visitor = Visitor()
    
    def compile(self, input_filename, output_filename):
        lexer = CgrammerLexer(FileStream(input_filename))
        stream = CommonTokenStream(lexer)
        parser = CgrammerParser(stream)
        self.visitor.visit(parser.code())
        self.visitor.save(output_filename)
