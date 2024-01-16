from llvmlite import ir
from antlr4 import *
from grammer.CgrammerLexer import CgrammerLexer
from grammer.CgrammerParser import CgrammerParser
from grammer.CgrammerVisitor import CgrammerVisitor
from SymbolTable import SymbolTable, Structure

# from Generator.ErrorListener import syntaxErrorListener
from ErrorListener import SemanticError

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
        return self.visit(ctx.getChild(1))


    # Visit a parse tree produced by CgrammerParser#expr_value.
    def visitExpr_value(self, ctx:CgrammerParser.Expr_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#content_of.
    def visitContent_of(self, ctx:CgrammerParser.Content_ofContext):
        Index = self.visit(ctx.getChild(1))
        Builder = self.Builders[-1]
        RealReturnValue = Builder.load(Index['name'])
        return {
            'type': Index['type'].pointee,
            'name': RealReturnValue
        }


    # Visit a parse tree produced by CgrammerParser#address_of.
    def visitAddress_of(self, ctx:CgrammerParser.Address_ofContext):
        Index = self.visit(ctx.getChild(1))
        Builder = self.Builders[-1]
        RealReturnValue = Builder.gep(Index['name'], [ir.Constant(ir.IntType(32), 0)])
        return {
            'type': ir.PointerType(Index['type']),
            'name': RealReturnValue
        }


    # Visit a parse tree produced by CgrammerParser#array.
    def visitArray(self, ctx:CgrammerParser.ArrayContext):
        TempRequireLoad = self.WhetherNeedLoad
        self.WhetherNeedLoad = False
        res = self.visit(ctx.getChild(0))  # mID
        self.WhetherNeedLoad = TempRequireLoad

        if isinstance(res['type'], ir.types.ArrayType):
            Builder = self.Builders[-1]

            TempRequireLoad = self.WhetherNeedLoad
            self.WhetherNeedLoad = True
            IndexRe1 = self.visit(ctx.getChild(2))  # subscript
            self.WhetherNeedLoad = TempRequireLoad

            Int32Zero = ir.Constant(int32, 0)
            RealReturnValue = Builder.gep(res['name'], [Int32Zero, IndexRe1['name']], inbounds=True)
            if self.WhetherNeedLoad:
                RealReturnValue = Builder.load(RealReturnValue)
            return {
                'type': res['type'].element,
                'name': RealReturnValue,
            }
        else:  # error!
            raise SemanticError(ctx=ctx, msg="类型错误")


    # Visit a parse tree produced by CgrammerParser#unit.
    def visitUnit(self, ctx:CgrammerParser.UnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#lincrese.
    def visitLincrese(self, ctx:CgrammerParser.LincreseContext):
        Index = self.visit(ctx.getChild(1))
        Builder = self.Builders[-1]
        OriginalValue = Builder.load(Index['name'])
        RealReturnValue = Builder.add(OriginalValue, ir.Constant(ir.IntType(32), 1))
        Builder.store(RealReturnValue, Index['name'])
        return {
            'type': Index['type'],
            'name': RealReturnValue
        }


    # Visit a parse tree produced by CgrammerParser#rincrease.
    def visitRincrease(self, ctx:CgrammerParser.RincreaseContext):
        Index = self.visit(ctx.getChild(0))
        Builder = self.Builders[-1]
        OriginalValue = Builder.load(Index['name'])
        RealReturnValue = Builder.add(OriginalValue, ir.Constant(ir.IntType(32), 1))
        Builder.store(RealReturnValue, Index['name'])
        return {
            'type': Index['type'],
            'name': OriginalValue
        }


    # Visit a parse tree produced by CgrammerParser#ldecrease.
    def visitLdecrease(self, ctx:CgrammerParser.LdecreaseContext):
        Index = self.visit(ctx.getChild(1))
        Builder = self.Builders[-1]
        OriginalValue = Builder.load(Index['name'])
        RealReturnValue = Builder.sub(OriginalValue, ir.Constant(ir.IntType(32), 1))
        Builder.store(RealReturnValue, Index['name'])
        return {
            'type': Index['type'],
            'name': RealReturnValue
        }


    # Visit a parse tree produced by CgrammerParser#rdecrease.
    def visitRdecrease(self, ctx:CgrammerParser.RdecreaseContext):
        Index = self.visit(ctx.getChild(0))
        Builder = self.Builders[-1]
        OriginalValue = Builder.load(Index['name'])
        RealReturnValue = Builder.sub(OriginalValue, ir.Constant(ir.IntType(32), 1))
        Builder.store(RealReturnValue, Index['name'])
        return {
            'type': Index['type'],
            'name': OriginalValue
        }


    # Visit a parse tree produced by CgrammerParser#not.
    def visitNot(self, ctx:CgrammerParser.NotContext):
        RealReturnValue = self.visit(ctx.getChild(1))
        return self.toBoolean(RealReturnValue, notFlag=True)


    # Visit a parse tree produced by CgrammerParser#positive.
    def visitPositive(self, ctx:CgrammerParser.PositiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#negative.
    def visitNegative(self, ctx:CgrammerParser.NegativeContext):
        IndexMid = self.visit(ctx.getChild(1))
        Builder = self.Builders[-1]
        RealReturnValue = Builder.neg(IndexMid['name'])
        return {
            'type': IndexMid['type'],
            'name': RealReturnValue
        }


    # Visit a parse tree produced by CgrammerParser#addr.
    def visitAddr(self, ctx:CgrammerParser.AddrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#divide.
    def visitDivide(self, ctx:CgrammerParser.DivideContext):
        Builder = self.Builders[-1]
        Index1 = self.visit(ctx.getChild(0))
        Index2 = self.visit(ctx.getChild(2))
        Index1, Index2 = self.exprConvert(Index1, Index2)
        RealReturnValue = Builder.sdiv(Index1['name'], Index2['name'])
        return {
            'type': Index1['type'],
            'name': RealReturnValue
        }


    # Visit a parse tree produced by CgrammerParser#unary.
    def visitUnary(self, ctx:CgrammerParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#multiply.
    def visitMultiply(self, ctx:CgrammerParser.MultiplyContext):
        Builder = self.Builders[-1]
        Index1 = self.visit(ctx.getChild(0))
        Index2 = self.visit(ctx.getChild(2))
        Index1, Index2 = self.exprConvert(Index1, Index2)
        RealReturnValue = Builder.mul(Index1['name'], Index2['name'])
        return {
            'type': Index1['type'],
            'name': RealReturnValue
        }


    # Visit a parse tree produced by CgrammerParser#modulo.
    def visitModulo(self, ctx:CgrammerParser.ModuloContext):
        Builder = self.Builders[-1]
        Index1 = self.visit(ctx.getChild(0))
        Index2 = self.visit(ctx.getChild(2))
        Index1, Index2 = self.exprConvert(Index1, Index2)
        RealReturnValue = Builder.srem(Index1['name'], Index2['name'])
        return {
            'type': Index1['type'],
            'name': RealReturnValue
        }


    # Visit a parse tree produced by CgrammerParser#add.
    def visitAdd(self, ctx:CgrammerParser.AddContext):
        Builder = self.Builders[-1]
        Index1 = self.visit(ctx.getChild(0))
        Index2 = self.visit(ctx.getChild(2))
        Index1, Index2 = self.exprConvert(Index1, Index2)
        RealReturnValue = Builder.add(Index1['name'], Index2['name'])
        return {
            'type': Index1['type'],
            'name': RealReturnValue
        }


    # Visit a parse tree produced by CgrammerParser#subtract.
    def visitSubtract(self, ctx:CgrammerParser.SubtractContext):
        Builder = self.Builders[-1]
        Index1 = self.visit(ctx.getChild(0))
        Index2 = self.visit(ctx.getChild(2))
        Index1, Index2 = self.exprConvert(Index1, Index2)
        RealReturnValue = Builder.sub(Index1['name'], Index2['name'])
        return {
            'type': Index1['type'],
            'name': RealReturnValue
        }


    # Visit a parse tree produced by CgrammerParser#calc1.
    def visitCalc1(self, ctx:CgrammerParser.Calc1Context):
        return self.visitChildren(ctx)

    def visitJudge(self, ctx):
        Builder = self.Builders[-1]
        Index1 = self.visit(ctx.getChild(0))
        Index2 = self.visit(ctx.getChild(2))
        Index1, Index2 = self.exprConvert(Index1, Index2)
        OperationChar = ctx.getChild(1).getText()
        if Index1['type'] == double:
            RealReturnValue = Builder.fcmp_ordered(OperationChar, Index1['name'], Index2['name'])
        elif self.isInteger(Index1['type']):
            RealReturnValue = Builder.icmp_signed(OperationChar, Index1['name'], Index2['name'])
        return {
            'type': int1,
            'name': RealReturnValue
        }

    # Visit a parse tree produced by CgrammerParser#equal.
    def visitEqual(self, ctx:CgrammerParser.EqualContext):
        return self.visitJudge(self, ctx)


    # Visit a parse tree produced by CgrammerParser#nequal.
    def visitNequal(self, ctx:CgrammerParser.NequalContext):
        return self.visitJudge(self, ctx)


    # Visit a parse tree produced by CgrammerParser#calc2.
    def visitCalc2(self, ctx:CgrammerParser.Calc2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#greater.
    def visitGreater(self, ctx:CgrammerParser.GreaterContext):
        return self.visitJudge(self, ctx)


    # Visit a parse tree produced by CgrammerParser#gequal.
    def visitGequal(self, ctx:CgrammerParser.GequalContext):
        return self.visitJudge(self, ctx)


    # Visit a parse tree produced by CgrammerParser#less.
    def visitLess(self, ctx:CgrammerParser.LessContext):
        return self.visitJudge(self, ctx)


    # Visit a parse tree produced by CgrammerParser#leuqal.
    def visitLeuqal(self, ctx:CgrammerParser.LeuqalContext):
        return self.visitJudge(self, ctx)


    # Visit a parse tree produced by CgrammerParser#rop1.
    def visitRop1(self, ctx:CgrammerParser.Rop1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#or.
    def visitOr(self, ctx:CgrammerParser.OrContext):
        Index1 = self.visit(ctx.getChild(0))
        Index1 = self.toBoolean(Index1, notFlag=False)
        Index2 = self.visit(ctx.getChild(2))
        Index2 = self.toBoolean(Index2, notFlag=False)
        Builder = self.Builders[-1]
        RealReturnValue = Builder.or_(Index1['name'], Index2['name'])
        return {
            'type': Index1['type'],
            'name': RealReturnValue
        }


    # Visit a parse tree produced by CgrammerParser#and.
    def visitAnd(self, ctx:CgrammerParser.AndContext):
        Index1 = self.visit(ctx.getChild(0))
        Index1 = self.toBoolean(Index1, notFlag=False)
        Index2 = self.visit(ctx.getChild(2))
        Index2 = self.toBoolean(Index2, notFlag=False)
        Builder = self.Builders[-1]
        RealReturnValue = Builder.and_(Index1['name'], Index2['name'])
        return {
            'type': Index1['type'],
            'name': RealReturnValue
        }


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

    def isInteger(self, typ):
        ReturnValue = 'width'
        return hasattr(typ, ReturnValue)

    def exprConvert(self, Index1, Index2):
        if Index1['type'] == Index2['type']:
            return Index1, Index2
        if self.isInteger(Index1['type']) and self.isInteger(Index2['type']):
            if Index1['type'].width < Index2['type'].width:
                if Index1['type'].width == 1:
                    Index1 = self.convertIIZ(Index1, Index2['type'])
                else:
                    Index1 = self.convertIIS(Index1, Index2['type'])
            else:
                if Index2['type'].width == 1:
                    Index2 = self.convertIIZ(Index2, Index1['type'])
                else:
                    Index2 = self.convertIIS(Index2, Index1['type'])
        elif self.isInteger(Index1['type']) and Index2['type'] == double:
            Index1 = self.convertIDS(Index1, Index2['type'])
        elif self.isInteger(Index2['type']) and Index1['type'] == double:
            Index2 = self.convertIDS(Index2, Index1['type'])
        else:
            raise SemanticError(ctx=ctx,msg="类型不匹配")
        return Index1, Index2

    def convertIIZ(self, CalcIndex, DType):
        Builder = self.Builders[-1]
        ConfirmedVal = Builder.zext(CalcIndex['name'], DType)
        return {
                'type': DType,
                'name': ConfirmedVal
        }

    def convertIIS(self, CalcIndex, DType):
        Builder = self.Builders[-1]
        ConfirmedVal = Builder.sext(CalcIndex['name'], DType)
        return {
                'type': DType,
                'name': ConfirmedVal
        }

    def convertDIS(self, CalcIndex, DType):
        Builder = self.Builders[-1]
        ConfirmedVal = Builder.fptosi(CalcIndex['name'], DType)
        return {
                'type': DType,
                'name': ConfirmedVal
        }

    def convertDIU(self, CalcIndex, DType):
        Builder = self.Builders[-1]
        ConfirmedVal = Builder.fptoui(CalcIndex['name'], DType)
        return {
                'type': DType,
                'name': ConfirmedVal
        }

    def convertIDS(self, CalcIndex):
        Builder = self.Builders[-1]
        ConfirmedVal = Builder.sitofp(CalcIndex['name'], double)
        return {
                'type': double,
                'name': ConfirmedVal
        }

    def convertIDU(self, CalcIndex):
        Builder = self.Builders[-1]
        ConfirmedVal = Builder.uitofp(CalcIndex['name'], double)
        return {
                'type': double,
                'name': ConfirmedVal
        }

    def toBoolean(self, ManipulateIndex, notFlag = True):
        Builder = self.Builders[-1]
        if notFlag:
            OperationChar = '=='
        else:
            OperationChar = '!='
        if ManipulateIndex['type'] == int8 or ManipulateIndex['type'] == int32:
            RealReturnValue = Builder.icmp_signed(OperationChar, ManipulateIndex['name'], ir.Constant(ManipulateIndex['type'], 0))
            return {
                    'tpye': int1,
                    'name': RealReturnValue
            }
        elif ManipulateIndex['type'] == double:
            RealReturnValue = Builder.fcmp_ordered(OperationChar, ManipulateIndex['name'], ir.Constant(double, 0))
            return {
                    'tpye': int1,
                    'name': RealReturnValue
            }
        return ManipulateIndex

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
