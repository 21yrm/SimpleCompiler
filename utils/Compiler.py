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
    生成器类，用于进行�??义分析并且转化为LLVM
    """

    def __init__(self):
        super(CgrammerVisitor, self).__init__()

        # 控制llvm生成
        self.Module = ir.Module()
        self.Module.triple = "x86_64-pc-windows-msvc"
        self.Module.data_layout = "e-m:w-i64:64-f80:128-n8:16:32:64-S128"

        # �??句块
        self.Blocks = []

        # 待生成的llvm�??句块
        self.Builders = []

        # 函数列表
        self.Functions = dict()

        # 当前所在函�??
        self.CurrentFunction = ''
        self.Constants = 0

        # 这个变量�??否需要加�??
        self.WhetherNeedLoad = True

        # endif�??
        self.EndifBlock = None

        # 符号�??
        self.SymbolTable = SymbolTable()

    # 入口符号 Program
    def visitProgram(self, ctx: CgrammerParser.CodeContext):
        for i in range(ctx.getChildCount()):
            self.visit(ctx.getChild(i))
        return

    # 代码入口 code
    def visitCode(self, ctx: CgrammerParser.CodeContext):
        for i in range(ctx.getChildCount()):
            self.visit(ctx.getChild(i))
        return

    def visitDomained_code(self, ctx: CgrammerParser.Domained_codeContext):
        self.visit(ctx.getChild(1))
        return

    def visitSimple_code(self, ctx: CgrammerParser.Simple_codeContext):
        self.visit(ctx.getChild(0))
        return

    # 代码�? Block，可能为if、while、for、switch、function和line
    def visitBlock(self, ctx: CgrammerParser.BlockContext):
        self.visit(ctx.getChild(0))
        return None

    # TODO:条件�?�?
    def visitCondition(self, ctx: CgrammerParser.ConditionContext):
        result = self.visit(ctx.getChild(0))
        return self.toBoolean(result, notFlag=False)

    # 具体代码块：if
    def visitIf_block(self, ctx: CgrammerParser.If_blockContext):
        # 增加两个block，�?�应If的内�? �? If结束后的内�??
        curBuilder = self.Builders[-1]
        IfBlock = curBuilder.append_basic_block()
        EndifBlock = curBuilder.append_basic_block()
        curBuilder.branch(IfBlock)

        # 纳入if
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(IfBlock)
        self.Builders.append(ir.IRBuilder(IfBlock))

        tmpBlock = self.EndifBlock
        self.EndifBlock = EndifBlock
        Length = ctx.getChildCount()
        for i in range(Length):
            self.visit(ctx.getChild(i))  # 分别处理每个if ,elseif, else�?
        self.EndifBlock = tmpBlock

        # 结束后�?�向EndIf�?
        tmpBlock = self.Blocks.pop()
        tmpBuilder = self.Builders.pop()
        if not tmpBlock.is_terminated:
            tmpBuilder.branch(EndifBlock)

        self.Blocks.append(EndifBlock)
        self.Builders.append(ir.IRBuilder(EndifBlock))
        return

    # if子块：�?�个if
    def visitPure_if_block(self, ctx: CgrammerParser.Pure_if_blockContext):
        # 创建真块与假�?
        self.SymbolTable.EnterScope()
        curBuilder = self.Builders[-1]
        TrueBlock = curBuilder.append_basic_block()
        FalseBlock = curBuilder.append_basic_block()

        # 由condition选择跳转
        result = self.visit(ctx.getChild(2))
        curBuilder.cbranch(result['name'], TrueBlock, FalseBlock)

        # 处理TrueBlock，�?�应code
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(TrueBlock)
        self.Builders.append(ir.IRBuilder(TrueBlock))
        self.visit(ctx.getChild(4))

        if not self.Blocks[-1].is_terminated:
            self.Builders[-1].branch(self.EndifBlock)

        # 处理FlaseBlock，�?�应后续操作
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(FalseBlock)
        self.Builders.append(ir.IRBuilder(FalseBlock))
        self.SymbolTable.QuitScope()
        return

    # if子块：elif
    def visitElif_block(self, ctx: CgrammerParser.IntContext):
        # 创建真块与假�?
        self.SymbolTable.EnterScope()
        curBuilder = self.Builders[-1]
        TrueBlock = curBuilder.append_basic_block()
        FalseBlock = curBuilder.append_basic_block()

        # 由condition选择跳转
        result = self.visit(ctx.getChild(2))
        curBuilder.cbranch(result['name'], TrueBlock, FalseBlock)

        # 处理TrueBlock，�?�应code
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(TrueBlock)
        self.Builders.append(ir.IRBuilder(TrueBlock))
        self.visit(ctx.getChild(4))

        if not self.Blocks[-1].is_terminated:
            self.Builders[-1].branch(self.EndifBlock)

        # 处理FlaseBlock，�?�应后续操作
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(FalseBlock)
        self.Builders.append(ir.IRBuilder(FalseBlock))
        self.SymbolTable.QuitScope()
        return

    # if子块：else
    def visitElse_block(self, ctx: CgrammerParser.Else_blockContext):
        # 直接生成
        self.SymbolTable.EnterScope()
        self.visit(ctx.getChild(2))  # body
        self.SymbolTable.QuitScope()

    # 具体代码块：while
    def visitWhile_block(self, ctx: CgrammerParser.While_blockContext):
        # 创建条件块，执�?�块与跳出块
        self.SymbolTable.EnterScope()
        curBuilder = self.Builders[-1]
        condBlock = curBuilder.append_basic_block()
        doBlock = curBuilder.append_basic_block()
        endBlock = curBuilder.append_basic_block()

        # 处理condBlock，�?�应expression
        curBuilder.branch(condBlock)
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(condBlock)
        self.Builders.append(ir.IRBuildercondBlock)
        result = self.visit(ctx.getChild(2))
        self.Builders[-1].cbranch(result['name'], doBlock, endBlock)

        # 处理doBlock，�?�应code
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(doBlock)
        self.Builders.append(ir.IRBuilder(doBlock))
        self.visit(ctx.getChild(4))  # body

        # do后跳�?回条件判�?
        if not self.Blocks[-1].is_terminated:
            self.Builders[-1].branch(condBlock)

        # 处理endBlock，�?�应后续操作
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(endBlock)
        self.Builders.append(ir.IRBuilder(endBlock))
        self.SymbolTable.QuitScope()
        return

    # 具体代码块：for
    def visitFor_block(self, ctx: CgrammerParser.For_blockContext):
        self.SymbolTable.EnterScope()

        # 创建条件块，执�?�块和跳出块
        curBuilder = self.Builders[-1]
        varBlock = curBuilder.append_basic_block()
        condBlock = curBuilder.append_basic_block()
        doBlock = curBuilder.append_basic_block()
        endBlock = curBuilder.append_basic_block()

        # 首先处理for_var
        curBuilder.branch(varBlock)
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(varBlock)
        self.Builders.append(ir.IRBuilder(varBlock))
        self.visit(ctx.getChild(2))

        # 处理condBlock，跳�?条件
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(condBlock)
        self.Builders.append(ir.IRBuilder(condBlock))

        result = self.visit(ctx.getChild(4))  # condition block
        self.Builders[-1].cbranch(result['name'], doBlock, endBlock)

        # 处理doblock，�?�应code与iter两部�?
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(doBlock)
        self.Builders.append(ir.IRBuilder(doBlock))
        self.visit(ctx.getChild(7))  # code
        self.visit(ctx.getChild(5))  # iter

        # do后跳�?回条件判�?
        if not self.Blocks[-1].is_terminated:
            self.Builders[-1].branch(condBlock)

        # 处理endBlock，�?�应后续操作
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(endBlock)
        self.Builders.append(ir.IRBuilder(endBlock))
        self.SymbolTable.QuitScope()
        return

    # for子块：for_var
    def visitFor_var(self, ctx: CgrammerParser.For_varContext):
        Length = ctx.getChildCount()
        if Length == 0:
            return

        self.visit(ctx.getChild(0))
        return

    # for子块：for_iter
    def visitFor_iter(self, ctx: CgrammerParser.FloatContext):
        Length = ctx.getChildCount()
        if Length == 0:
            return

        self.visit(ctx.getChild(0))
        return

    # TODO：具体代码块：switch
    def visitSwitch_block(self, ctx: CgrammerParser.Switch_blockContext):
        return self.visitChildren(ctx)

    # 入口符号 Program
    def visitProgram(self, ctx:CgrammerParser.CodeContext):
        for i in range(ctx.getChildCount()):
            self.visit(ctx.getChild(i))
        return
    
    # 代码入口 code
    def visitCode(self, ctx:CgrammerParser.CodeContext):
        for i in range(ctx.getChildCount()):
            self.visit(ctx.getChild(i))
        return

    def visitDomained_code(self, ctx:CgrammerParser.Domained_codeContext):
        self.visit(ctx.getChild(1))
        return

    def visitSimple_code(self, ctx: CgrammerParser.Simple_codeContext):
        self.visit(ctx.getChild(0))
        return

    # 代码�? Block，可能为if、while、for、switch、function和line
    def visitBlock(self, ctx:CgrammerParser.BlockContext):
        self.visit(ctx.getChild(0))
        return None

    # TODO:条件�?�?
    def visitCondition(self, ctx:CgrammerParser.ConditionContext):
        result = self.visit(ctx.getChild(0))
        return self.toBoolean(result, notFlag=False)

    # 具体代码块：if
    def visitIf_block(self, ctx:CgrammerParser.If_blockContext):
        # 增加两个block，�?�应If的内�? �? If结束后的内�??
        curBuilder = self.Builders[-1] 
        IfBlock = curBuilder.append_basic_block()
        EndifBlock = curBuilder.append_basic_block()
        curBuilder.branch(IfBlock)

        # 纳入if
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(IfBlock)
        self.Builders.append(ir.IRBuilder(IfBlock))

        tmpBlock = self.EndifBlock
        self.EndifBlock = EndifBlock
        Length = ctx.getChildCount()
        for i in range(Length):
            self.visit(ctx.getChild(i))  # 分别处理每个if ,elseif, else�?
        self.EndifBlock = tmpBlock

        # 结束后�?�向EndIf�?
        tmpBlock = self.Blocks.pop()
        tmpBuilder = self.Builders.pop()
        if not tmpBlock.is_terminated:
            tmpBuilder.branch(EndifBlock)

        self.Blocks.append(EndifBlock)
        self.Builders.append(ir.IRBuilder(EndifBlock))
        return

    # if子块：�?�个if
    def visitPure_if_block(self, ctx:CgrammerParser.Pure_if_blockContext):
        # 创建真块与假�?
        self.SymbolTable.EnterScope()
        curBuilder = self.Builders[-1]
        TrueBlock = curBuilder.append_basic_block()
        FalseBlock = curBuilder.append_basic_block()

        # 由condition选择跳转
        result = self.visit(ctx.getChild(2))
        curBuilder.cbranch(result['name'], TrueBlock, FalseBlock)

        # 处理TrueBlock，�?�应code
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(TrueBlock)
        self.Builders.append(ir.IRBuilder(TrueBlock))
        self.visit(ctx.getChild(4))

        if not self.Blocks[-1].is_terminated:
            self.Builders[-1].branch(self.EndifBlock)

        # 处理FlaseBlock，�?�应后续操作
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(FalseBlock)
        self.Builders.append(ir.IRBuilder(FalseBlock))
        self.SymbolTable.QuitScope()
        return

    # if子块：elif
    def visitElif_block(self, ctx:CgrammerParser.IntContext):
        # 创建真块与假�?
        self.SymbolTable.EnterScope()
        curBuilder = self.Builders[-1]
        TrueBlock = curBuilder.append_basic_block()
        FalseBlock = curBuilder.append_basic_block()

        # 由condition选择跳转
        result = self.visit(ctx.getChild(2))
        curBuilder.cbranch(result['name'], TrueBlock, FalseBlock)
        
        # 处理TrueBlock，�?�应code
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(TrueBlock)
        self.Builders.append(ir.IRBuilder(TrueBlock))
        self.visit(ctx.getChild(4))

        if not self.Blocks[-1].is_terminated:
            self.Builders[-1].branch(self.EndifBlock)
        
        # 处理FlaseBlock，�?�应后续操作
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(FalseBlock)
        self.Builders.append(ir.IRBuilder(FalseBlock))
        self.SymbolTable.QuitScope()
        return

    # if子块：else
    def visitElse_block(self, ctx:CgrammerParser.Else_blockContext):
        # 直接生成
        self.SymbolTable.EnterScope()
        self.visit(ctx.getChild(2)) # body
        self.SymbolTable.QuitScope()

    # 具体代码块：while
    def visitWhile_block(self, ctx:CgrammerParser.While_blockContext):
        # 创建条件块，执�?�块与跳出块
        self.SymbolTable.EnterScope()
        curBuilder = self.Builders[-1]
        condBlock = curBuilder.append_basic_block()
        doBlock = curBuilder.append_basic_block()
        endBlock = curBuilder.append_basic_block()

        # 处理condBlock，�?�应expression
        curBuilder.branch(condBlock)
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(condBlock)
        self.Builders.append(ir.IRBuildercondBlock)
        result = self.visit(ctx.getChild(2))
        self.Builders[-1].cbranch(result['name'], doBlock, endBlock)

        # 处理doBlock，�?�应code
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(doBlock)
        self.Builders.append(ir.IRBuilder(doBlock))
        self.visit(ctx.getChild(4)) # body

        # do后跳�?回条件判�?
        if not self.Blocks[-1].is_terminated:
            self.Builders[-1].branch(condBlock)

        # 处理endBlock，�?�应后续操作
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(endBlock)
        self.Builders.append(ir.IRBuilder(endBlock))
        self.SymbolTable.QuitScope()
        return
    
    # 具体代码块：for
    def visitFor_block(self, ctx:CgrammerParser.For_blockContext):
        self.SymbolTable.EnterScope()

        # 创建条件块，执�?�块和跳出块
        curBuilder = self.Builders[-1]
        varBlock = curBuilder.append_basic_block()
        condBlock = curBuilder.append_basic_block()
        doBlock = curBuilder.append_basic_block()
        endBlock = curBuilder.append_basic_block()
       
        # 首先处理for_var
        curBuilder.branch(varBlock)
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(varBlock)
        self.Builders.append(ir.IRBuilder(varBlock))
        self.visit(ctx.getChild(2))
                
        # 处理condBlock，跳�?条件
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(condBlock)
        self.Builders.append(ir.IRBuilder(condBlock))

        result = self.visit(ctx.getChild(4)) # condition block
        self.Builders[-1].cbranch(result['name'], doBlock, endBlock)

        # 处理doblock，�?�应code与iter两部�?
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(doBlock)
        self.Builders.append(ir.IRBuilder(doBlock))
        self.visit(ctx.getChild(7)) # code
        self.visit(ctx.getChild(5)) # iter

         # do后跳�?回条件判�?
        if not self.Blocks[-1].is_terminated:
            self.Builders[-1].branch(condBlock)

        # 处理endBlock，�?�应后续操作
        self.Blocks.pop()
        self.Builders.pop()
        self.Blocks.append(endBlock)
        self.Builders.append(ir.IRBuilder(endBlock))
        self.SymbolTable.QuitScope()
        return
    
    # for子块：for_var
    def visitFor_var(self, ctx:CgrammerParser.For_varContext):
        Length = ctx.getChildCount()
        if Length == 0:
            return

        self.visit(ctx.getChild(0))
        return

    # for子块：for_iter
    def visitFor_iter(self, ctx:CgrammerParser.FloatContext):
        Length = ctx.getChildCount()
        if Length == 0:
            return

        self.visit(ctx.getChild(0))
        return

    # TODO：具体代码块：switch
    def visitSwitch_block(self, ctx: CgrammerParser.Switch_blockContext):
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by CgrammerParser#pointer_flag.
    def visitPointer_flag(self, ctx: CgrammerParser.Pointer_flagContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#originalType.
    def visitOriginalType(self, ctx: CgrammerParser.OriginalTypeContext):
        token_type = ctx.start.type
        if token_type == CgrammerParser.INT:
            return int32
        elif token_type == CgrammerParser.FLOAT:
            return float32
        elif token_type == CgrammerParser.CHAR:
            return int8
        elif token_type == CgrammerParser.BOOL:
            return int1

    # Visit a parse tree produced by CgrammerParser#pointer.
    def visitPointer(self, ctx: CgrammerParser.PointerContext):
        token_type = ctx.start.type
        if token_type == CgrammerParser.INT:
            return int32_pointer
        elif token_type == CgrammerParser.FLOAT:
            return float32_pointer
        elif token_type == CgrammerParser.CHAR:
            return int8_pointer
        elif token_type == CgrammerParser.BOOL:
            return int1_pointer

    # Visit a parse tree produced by CgrammerParser#index.
    def visitIndex(self, ctx: CgrammerParser.IndexContext):
        return self.visit(ctx.getChild(1))

    # Visit a parse tree produced by CgrammerParser#memset.
    def visitMemset(self, ctx: CgrammerParser.MemsetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#strlen.
    def visitStrlen(self, ctx: CgrammerParser.StrlenContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#printf.
    def visitPrintf(self, ctx: CgrammerParser.PrintfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#scanf.
    def visitScanf(self, ctx: CgrammerParser.ScanfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#variable_declaration.
    def visitVariable_declaration(self, ctx: CgrammerParser.Variable_declarationContext):
        if ctx.getChildCount() <= 2:
            variable_type = self.visit(ctx.getChild(0))
        else:
            basic_type = self.visit(ctx.getChild(0))
            count = self.visit(ctx.getChild(2))
            variable_type = ir.ArrayType(basic_type, count)
        variable_name = ctx.getChild(1).getText()
        result = {'type': variable_type, 'name': variable_name}
        return result

    # Visit a parse tree produced by CgrammerParser#params.
    def visitParams(self, ctx: CgrammerParser.ParamsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#params_definition.
    def visitParams_definition(self, ctx: CgrammerParser.Params_definitionContext):
        length = ctx.getChildCount()
        parameter_list = []
        i = 0
        while i < length:
            parameter = self.visit(ctx.getChild(i))
            parameter_list.append(parameter)
            i += 2
        return parameter_list

    # Visit a parse tree produced by CgrammerParser#function_call.
    def visitFunction_call(self, ctx: CgrammerParser.Function_callContext):
        function_name = ctx.getChild(0)
        if function_name.getText() == 'printf':
            if 'printf' in self.Functions:
                printf = self.Functions['printf']
            else:
                printfType = ir.FunctionType(int32, [ir.PointerType(int8)], var_arg=True)
                printf = ir.Function(self.Module, printfType, name="printf")
                self.Functions['printf'] = printf

            theBuilder = self.Builders[-1]
            zero = ir.Constant(int32, 0)

            # 就一�?变量
            if ctx.getChildCount() == 4:
                ParameterInfo = self.visit(ctx.getChild(2))
                Argument = theBuilder.gep(ParameterInfo['name'], [zero, zero], inbounds=True)
                ReturnVariableName = theBuilder.call(printf, [Argument])
            else:
                ParameterInfo = self.visit(ctx.getChild(2))
                Arguments = [theBuilder.gep(ParameterInfo['name'], [zero, zero], inbounds=True)]

                Length = ctx.getChildCount()
                i = 4
                while i < Length - 1:
                    OneParameter = self.visit(ctx.getChild(i))
                    Arguments.append(OneParameter['name'])
                    i += 2
                ReturnVariableName = theBuilder.call(printf, Arguments)
            result = {'type': int32, 'name': ReturnVariableName}
            return result
        elif function_name.getText() == 'scanf':
            if 'scanf' in self.Functions:
                scanf = self.Functions['scanf']
            else:
                scanfType = ir.FunctionType(int32, [ir.PointerType(int8)], var_arg=True)
                scanf = ir.Function(self.Module, scanfType, name="scanf")
                self.Functions['scanf'] = scanf

            theBuilder = self.Builders[-1]
            zero = ir.Constant(int32, 0)
            ParameterList = self.visit(ctx.getChild(2))  # MString
            Arguments = [theBuilder.gep(ParameterList['name'], [zero, zero], inbounds=True)]

            Length = ctx.getChildCount()
            i = 4
            while i < Length - 1:
                if ctx.getChild(i).getText() == '&':
                    # 读取变量
                    PreviousNeedLoad = self.WhetherNeedLoad
                    self.WhetherNeedLoad = False
                    theParameter = self.visit(ctx.getChild(i + 1))
                    self.WhetherNeedLoad = PreviousNeedLoad
                    Arguments.append(theParameter['name'])
                    i += 3
                else:
                    PreviousNeedLoad = self.WhetherNeedLoad
                    self.WhetherNeedLoad = True
                    theParameter = self.visit(ctx.getChild(i))
                    self.WhetherNeedLoad = PreviousNeedLoad
                    Arguments.append(theParameter['name'])
                    i += 2

            ReturnVariableName = theBuilder.call(scanf, Arguments)
            result = {'type': int32, 'name': ReturnVariableName}
            return result
        elif function_name.getText() == 'strlen':
            if 'strlen' in self.Functions:
                strlen = self.Functions['strlen']
            else:
                strlenType = ir.FunctionType(int32, [ir.PointerType(int8)], var_arg=False)
                strlen = ir.Function(self.Module, strlenType, name="strlen")
                self.Functions['strlen'] = strlen

            theBuilder = self.Builders[-1]
            zero = ir.Constant(int32, 0)

            # 加载变量
            PreviousNeedLoad = self.WhetherNeedLoad
            self.WhetherNeedLoad = False
            res = self.visit(ctx.getChild(2))
            self.WhetherNeedLoad = PreviousNeedLoad

            Arguments = theBuilder.gep(res['name'], [zero, zero], inbounds=True)
            ReturnVariableName = theBuilder.call(strlen, [Arguments])

            result = {'type': int32, 'name': ReturnVariableName}
            return result
        elif function_name.getText() == 'memset':
            if 'memset' in self.Functions:
                memset = self.Functions['memset']
            else:
                memsetType = ir.FunctionType(int32, [ir.PointerType(int8)], var_arg=False)
                memset = ir.Function(self.Module, memsetType, name="memset")
                self.Functions['strlen'] = memset

            theBuilder = self.Builders[-1]

            # 加载变量
            PreviousNeedLoad = self.WhetherNeedLoad
            self.WhetherNeedLoad = False
            res = self.visit(ctx.getChild(2))
            self.WhetherNeedLoad = PreviousNeedLoad
            zero = ir.Constant(int32, 0)

            Arguments = theBuilder.gep(res['name'], [zero, zero], inbounds=True)
            i = 2
            while i <= 6:
                PreviousNeedLoad = self.WhetherNeedLoad
                self.WhetherNeedLoad = True
                theParameter = self.visit(ctx.getChild(i))
                self.WhetherNeedLoad = PreviousNeedLoad
                Arguments.append(theParameter['name'])
                i += 2
            ReturnVariableName = theBuilder.call(theBuilder, [Arguments])

            Result = {'type': int32, 'name': ReturnVariableName}
            return Result
        else:
            theBuilder = self.Builders[-1]
            FunctionName = ctx.getChild(0).getText()  # func name
            if FunctionName in self.Functions:
                TheFunction = self.Functions[FunctionName]

                Length = ctx.getChildCount()
                ParameterList = []
                i = 2
                while i < Length - 1:
                    TheParameter = self.visit(ctx.getChild(i))
                    TheParameter = self.assignConvert(TheParameter, TheFunction.args[i // 2 - 1].type)
                    ParameterList.append(TheParameter['name'])
                    i += 2
                ReturnVariableName = theBuilder.call(TheFunction, ParameterList)
                Result = {'type': TheFunction.function_type.return_type, 'name': ReturnVariableName}
                return Result
            else:
                raise SemanticError(ctx=ctx, msg="函数�?定义�?")

    # Visit a parse tree produced by CgrammerParser#id.
    def visitId(self, ctx: CgrammerParser.IdContext):
        name = ctx.getChild(0).getText()
        if self.SymbolTable.JudgeExist(name):
            builder = self.Builders[-1]
            item = self.SymbolTable.GetItem(name)
            if item is not None:
                return builder.load(item["type"], item["entry"])

    # Visit a parse tree produced by CgrammerParser#int_value.
    def visitInt_value(self, ctx: CgrammerParser.Int_valueContext):
        return int(ctx.getChild(0).getText())

    # Visit a parse tree produced by CgrammerParser#float_value.
    def visitFloat_value(self, ctx: CgrammerParser.Float_valueContext):
        return float(ctx.getChild(0).getText())

    # Visit a parse tree produced by CgrammerParser#char_value.
    def visitChar_value(self, ctx: CgrammerParser.Char_valueContext):
        return ctx.getChild(0).getText()

    # Visit a parse tree produced by CgrammerParser#string_value.
    def visitString_value(self, ctx: CgrammerParser.String_valueContext):
        return ctx.getChild(0).getText()

    # Visit a parse tree produced by CgrammerParser#bool_value.
    def visitBool_value(self, ctx: CgrammerParser.Bool_valueContext):
        return ctx.getChild(0).getText()

    # Visit a parse tree produced by CgrammerParser#function_call_.
    def visitFunction_call_(self, ctx: CgrammerParser.Function_call_Context):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by CgrammerParser#round.
    def visitRound(self, ctx: CgrammerParser.RoundContext):
        return self.visit(ctx.getChild(1))

    # Visit a parse tree produced by CgrammerParser#expr_value.
    def visitExpr_value(self, ctx: CgrammerParser.Expr_valueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#content_of.
    def visitContent_of(self, ctx: CgrammerParser.Content_ofContext):
        Index = self.visit(ctx.getChild(1))
        Builder = self.Builders[-1]
        RealReturnValue = Builder.load(Index['name'])
        return {
            'type': Index['type'].pointee,
            'name': RealReturnValue
        }

    # Visit a parse tree produced by CgrammerParser#address_of.
    def visitAddress_of(self, ctx: CgrammerParser.Address_ofContext):
        Index = self.visit(ctx.getChild(1))
        Builder = self.Builders[-1]
        RealReturnValue = Builder.gep(Index['name'], [ir.Constant(ir.IntType(32), 0)])
        return {
            'type': ir.PointerType(Index['type']),
            'name': RealReturnValue
        }

    # Visit a parse tree produced by CgrammerParser#array.
    def visitArray(self, ctx: CgrammerParser.ArrayContext):
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
            raise SemanticError(ctx=ctx, msg="类型错�??")

    # Visit a parse tree produced by CgrammerParser#unit.
    def visitUnit(self, ctx: CgrammerParser.UnitContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#lincrese.
    def visitLincrese(self, ctx: CgrammerParser.LincreseContext):
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
    def visitRincrease(self, ctx: CgrammerParser.RincreaseContext):
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
    def visitLdecrease(self, ctx: CgrammerParser.LdecreaseContext):
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
    def visitRdecrease(self, ctx: CgrammerParser.RdecreaseContext):
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
    def visitNot(self, ctx: CgrammerParser.NotContext):
        RealReturnValue = self.visit(ctx.getChild(1))
        return self.toBoolean(RealReturnValue, notFlag=True)

    # Visit a parse tree produced by CgrammerParser#positive.
    def visitPositive(self, ctx: CgrammerParser.PositiveContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#negative.
    def visitNegative(self, ctx: CgrammerParser.NegativeContext):
        IndexMid = self.visit(ctx.getChild(1))
        Builder = self.Builders[-1]
        RealReturnValue = Builder.neg(IndexMid['name'])
        return {
            'type': IndexMid['type'],
            'name': RealReturnValue
        }

    # Visit a parse tree produced by CgrammerParser#addr.
    def visitAddr(self, ctx: CgrammerParser.AddrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#divide.
    def visitDivide(self, ctx: CgrammerParser.DivideContext):
        Builder = self.Builders[-1]
        Index1 = self.visit(ctx.getChild(0))
        Index2 = self.visit(ctx.getChild(2))
        Index1, Index2 = self.exprConvert(ctx, Index1, Index2)
        RealReturnValue = Builder.sdiv(Index1['name'], Index2['name'])
        return {
            'type': Index1['type'],
            'name': RealReturnValue
        }

    # Visit a parse tree produced by CgrammerParser#unary.
    def visitUnary(self, ctx: CgrammerParser.UnaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#multiply.
    def visitMultiply(self, ctx: CgrammerParser.MultiplyContext):
        Builder = self.Builders[-1]
        Index1 = self.visit(ctx.getChild(0))
        Index2 = self.visit(ctx.getChild(2))
        Index1, Index2 = self.exprConvert(ctx, Index1, Index2)
        RealReturnValue = Builder.mul(Index1['name'], Index2['name'])
        return {
            'type': Index1['type'],
            'name': RealReturnValue
        }

    # Visit a parse tree produced by CgrammerParser#modulo.
    def visitModulo(self, ctx: CgrammerParser.ModuloContext):
        Builder = self.Builders[-1]
        Index1 = self.visit(ctx.getChild(0))
        Index2 = self.visit(ctx.getChild(2))
        Index1, Index2 = self.exprConvert(ctx, Index1, Index2)
        RealReturnValue = Builder.srem(Index1['name'], Index2['name'])
        return {
            'type': Index1['type'],
            'name': RealReturnValue
        }

    # Visit a parse tree produced by CgrammerParser#add.
    def visitAdd(self, ctx: CgrammerParser.AddContext):
        Builder = self.Builders[-1]
        Index1 = self.visit(ctx.getChild(0))
        Index2 = self.visit(ctx.getChild(2))
        Index1, Index2 = self.exprConvert(ctx, Index1, Index2)
        RealReturnValue = Builder.add(Index1['name'], Index2['name'])
        return {
            'type': Index1['type'],
            'name': RealReturnValue
        }

    # Visit a parse tree produced by CgrammerParser#subtract.
    def visitSubtract(self, ctx: CgrammerParser.SubtractContext):
        Builder = self.Builders[-1]
        Index1 = self.visit(ctx.getChild(0))
        Index2 = self.visit(ctx.getChild(2))
        Index1, Index2 = self.exprConvert(ctx, Index1, Index2)
        RealReturnValue = Builder.sub(Index1['name'], Index2['name'])
        return {
            'type': Index1['type'],
            'name': RealReturnValue
        }

    # Visit a parse tree produced by CgrammerParser#calc1.
    def visitCalc1(self, ctx: CgrammerParser.Calc1Context):
        return self.visitChildren(ctx)

    def visitJudge(self, ctx):
        Builder = self.Builders[-1]
        Index1 = self.visit(ctx.getChild(0))
        Index2 = self.visit(ctx.getChild(2))
        Index1, Index2 = self.exprConvert(ctx, Index1, Index2)
        OperationChar = ctx.getChild(1).getText()
        if Index1['type'] == float32:
            RealReturnValue = Builder.fcmp_ordered(OperationChar, Index1['name'], Index2['name'])
        elif self.isInteger(Index1['type']):
            RealReturnValue = Builder.icmp_signed(OperationChar, Index1['name'], Index2['name'])
        return {
            'type': int1,
            'name': RealReturnValue
        }

    # Visit a parse tree produced by CgrammerParser#equal.
    def visitEqual(self, ctx: CgrammerParser.EqualContext):
        return self.visitJudge(self, ctx)

    # Visit a parse tree produced by CgrammerParser#nequal.
    def visitNequal(self, ctx: CgrammerParser.NequalContext):
        return self.visitJudge(self, ctx)

    # Visit a parse tree produced by CgrammerParser#calc2.
    def visitCalc2(self, ctx: CgrammerParser.Calc2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#greater.
    def visitGreater(self, ctx: CgrammerParser.GreaterContext):
        return self.visitJudge(self, ctx)

    # Visit a parse tree produced by CgrammerParser#gequal.
    def visitGequal(self, ctx: CgrammerParser.GequalContext):
        return self.visitJudge(self, ctx)

    # Visit a parse tree produced by CgrammerParser#less.
    def visitLess(self, ctx: CgrammerParser.LessContext):
        return self.visitJudge(self, ctx)

    # Visit a parse tree produced by CgrammerParser#leuqal.
    def visitLeuqal(self, ctx: CgrammerParser.LeuqalContext):
        return self.visitJudge(self, ctx)

    # Visit a parse tree produced by CgrammerParser#rop1.
    def visitRop1(self, ctx: CgrammerParser.Rop1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#or.
    def visitOr(self, ctx: CgrammerParser.OrContext):
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
    def visitAnd(self, ctx: CgrammerParser.AndContext):
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
    def visitRop2(self, ctx: CgrammerParser.Rop2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#expression.
    def visitExpression(self, ctx: CgrammerParser.ExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#assign.
    def visitAssign(self, ctx: CgrammerParser.AssignContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#addeqaul.
    def visitAddeqaul(self, ctx: CgrammerParser.AddeqaulContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#suvequal.
    def visitSuvequal(self, ctx: CgrammerParser.SuvequalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#multiplyequal.
    def visitMultiplyequal(self, ctx: CgrammerParser.MultiplyequalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#divideequal.
    def visitDivideequal(self, ctx: CgrammerParser.DivideequalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#moduloequal.
    def visitModuloequal(self, ctx: CgrammerParser.ModuloequalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#assignment.
    def visitAssignment(self, ctx: CgrammerParser.AssignmentContext):
        return self.visitChildren(ctx)

    def isInteger(self, typ):
        ReturnValue = 'width'
        return hasattr(typ, ReturnValue)

    def exprConvert(self, ctx, Index1, Index2):
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
        elif self.isInteger(Index1['type']) and Index2['type'] == float32:
            Index1 = self.convertIDS(Index1, Index2['type'])
        elif self.isInteger(Index2['type']) and Index1['type'] == float32:
            Index2 = self.convertIDS(Index2, Index1['type'])
        else:
            raise SemanticError(ctx=ctx, msg="类型不匹�??")
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
        ConfirmedVal = Builder.sitofp(CalcIndex['name'], float32)
        return {
            'type': float32,
            'name': ConfirmedVal
        }

    def convertIDU(self, CalcIndex):
        Builder = self.Builders[-1]
        ConfirmedVal = Builder.uitofp(CalcIndex['name'], float32)
        return {
            'type': float32,
            'name': ConfirmedVal
        }

    def toBoolean(self, ManipulateIndex, notFlag=True):
        Builder = self.Builders[-1]
        if notFlag:
            OperationChar = '=='
        else:
            OperationChar = '!='
        if ManipulateIndex['type'] == int8 or ManipulateIndex['type'] == int32:
            RealReturnValue = Builder.icmp_signed(OperationChar, ManipulateIndex['name'],
                                                  ir.Constant(ManipulateIndex['type'], 0))
            return {
                'tpye': int1,
                'name': RealReturnValue
            }
        elif ManipulateIndex['type'] == float32:
            RealReturnValue = Builder.fcmp_ordered(OperationChar, ManipulateIndex['name'], ir.Constant(float32, 0))
            return {
                'tpye': int1,
                'name': RealReturnValue
            }
        return ManipulateIndex

    # Visit a parse tree produced by CgrammerParser#variable_definition.
    def visitVariable_definition(self, ctx: CgrammerParser.Variable_definitionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CgrammerParser#memest_announce.
    def visitMemest_announce(self, ctx: CgrammerParser.Memest_announceContext):
        return

    # Visit a parse tree produced by CgrammerParser#strlen_announce.
    def visitStrlen_announce(self, ctx: CgrammerParser.Strlen_announceContext):
        return

    # Visit a parse tree produced by CgrammerParser#printf_announce.
    def visitPrintf_announce(self, ctx: CgrammerParser.Printf_announceContext):
        return

    # Visit a parse tree produced by CgrammerParser#scanf_annouce.
    def visitScanf_annouce(self, ctx: CgrammerParser.Scanf_annouceContext):
        return

    # Visit a parse tree produced by CgrammerParser#function_definition.
    def visitFunction_definition(self, ctx: CgrammerParser.Function_definitionContext):
        # function_definition: ( type | VOID ) IDENTIFIER LROUND params_definition? RROUND LCURLY code RCURLY;
        # 获取返回值类�??
        if ctx.start.type == CgrammerParser.VOID:
            return_type = void
        else:
            return_type = self.visit(ctx.getChild(0))

        # 获取函数名称
        function_name = ctx.getChild(1).getText()

        # 获取参数列表
        if ctx.getChildCount() < 8:
            parameter_list = []
        else:
            parameter_list = self.visit(ctx.getChild(3))

        # 生成llvm函数
        parameter_type_list = []
        for i in range(len(parameter_list)):
            parameter_type_list.append(parameter_type_list[i]['type'])
        function_type = ir.FunctionType(return_type, parameter_type_list)
        function = ir.Function(self.Module, function_type, name=function_name)

        # 设置形参名称
        for i in range(len(parameter_list)):
            function.args[i].name = parameter_list[i]['name']

        # 为函数添加基�?�?
        block = function.append_basic_block(name=function_name + '_entry')
        self.Blocks.append(block)

        # 为函数添加指令工�?
        builder = ir.IRBuilder(block)
        self.Builders.append(builder)

        # 为�?�理函数体做准�??
        self.CurrentFunction = function_name
        self.SymbolTable.EnterScope()

        # 为形参分配空间并在�?�号表里建立表项
        for i in range(len(parameter_list)):
            # 创建一个alloca指令，用于在栈上分配内存，返回一�?指向分配内存的指�?
            address = builder.alloca(parameter_list[i]['type'])
            # 创建一个load指令，用于加载指针所指的�?
            builder.store(function.args[i], address)
            # 在�?�号表里建立表项
            item = {"type": parameter_list[i]['type'], "entry": address}
            result = self.SymbolTable.AddItem(parameter_list[i]['name'], item)
            if result["result"] != "success":
                raise SemanticError(ctx=ctx, msg=result["reason"])

        # 处理函数�?
        if ctx.getChildCount() < 8:
            self.visit(ctx.getChild(5))
        else:
            self.visit(ctx.getChild(6))

        # 处理完毕，退一�?
        self.CurrentFunction = ''
        self.Blocks.pop()
        self.Builders.pop()
        self.SymbolTable.QuitScope()

    def save(self, filename):
        with open(filename, "w") as f:
            f.write(repr(self.Module))


class Compiler:
    # 遍历�?
    visitor = Visitor()
    
    def compile(self, input_filename, output_filename):
        lexer = CgrammerLexer(FileStream(input_filename))
        stream = CommonTokenStream(lexer)
        parser = CgrammerParser(stream)
        self.visitor.visit(parser.code())
        self.visitor.save(output_filename)
