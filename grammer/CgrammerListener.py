# Generated from Cgrammer.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CgrammerParser import CgrammerParser
else:
    from CgrammerParser import CgrammerParser

# This class defines a complete listener for a parse tree produced by CgrammerParser.
class CgrammerListener(ParseTreeListener):

    # Enter a parse tree produced by CgrammerParser#int.
    def enterInt(self, ctx:CgrammerParser.IntContext):
        pass

    # Exit a parse tree produced by CgrammerParser#int.
    def exitInt(self, ctx:CgrammerParser.IntContext):
        pass


    # Enter a parse tree produced by CgrammerParser#float.
    def enterFloat(self, ctx:CgrammerParser.FloatContext):
        pass

    # Exit a parse tree produced by CgrammerParser#float.
    def exitFloat(self, ctx:CgrammerParser.FloatContext):
        pass


    # Enter a parse tree produced by CgrammerParser#char.
    def enterChar(self, ctx:CgrammerParser.CharContext):
        pass

    # Exit a parse tree produced by CgrammerParser#char.
    def exitChar(self, ctx:CgrammerParser.CharContext):
        pass


    # Enter a parse tree produced by CgrammerParser#bool.
    def enterBool(self, ctx:CgrammerParser.BoolContext):
        pass

    # Exit a parse tree produced by CgrammerParser#bool.
    def exitBool(self, ctx:CgrammerParser.BoolContext):
        pass


    # Enter a parse tree produced by CgrammerParser#pointer_flag.
    def enterPointer_flag(self, ctx:CgrammerParser.Pointer_flagContext):
        pass

    # Exit a parse tree produced by CgrammerParser#pointer_flag.
    def exitPointer_flag(self, ctx:CgrammerParser.Pointer_flagContext):
        pass


    # Enter a parse tree produced by CgrammerParser#originalType.
    def enterOriginalType(self, ctx:CgrammerParser.OriginalTypeContext):
        pass

    # Exit a parse tree produced by CgrammerParser#originalType.
    def exitOriginalType(self, ctx:CgrammerParser.OriginalTypeContext):
        pass


    # Enter a parse tree produced by CgrammerParser#pointer.
    def enterPointer(self, ctx:CgrammerParser.PointerContext):
        pass

    # Exit a parse tree produced by CgrammerParser#pointer.
    def exitPointer(self, ctx:CgrammerParser.PointerContext):
        pass


    # Enter a parse tree produced by CgrammerParser#index.
    def enterIndex(self, ctx:CgrammerParser.IndexContext):
        pass

    # Exit a parse tree produced by CgrammerParser#index.
    def exitIndex(self, ctx:CgrammerParser.IndexContext):
        pass


    # Enter a parse tree produced by CgrammerParser#memset.
    def enterMemset(self, ctx:CgrammerParser.MemsetContext):
        pass

    # Exit a parse tree produced by CgrammerParser#memset.
    def exitMemset(self, ctx:CgrammerParser.MemsetContext):
        pass


    # Enter a parse tree produced by CgrammerParser#strlen.
    def enterStrlen(self, ctx:CgrammerParser.StrlenContext):
        pass

    # Exit a parse tree produced by CgrammerParser#strlen.
    def exitStrlen(self, ctx:CgrammerParser.StrlenContext):
        pass


    # Enter a parse tree produced by CgrammerParser#printf.
    def enterPrintf(self, ctx:CgrammerParser.PrintfContext):
        pass

    # Exit a parse tree produced by CgrammerParser#printf.
    def exitPrintf(self, ctx:CgrammerParser.PrintfContext):
        pass


    # Enter a parse tree produced by CgrammerParser#scanf.
    def enterScanf(self, ctx:CgrammerParser.ScanfContext):
        pass

    # Exit a parse tree produced by CgrammerParser#scanf.
    def exitScanf(self, ctx:CgrammerParser.ScanfContext):
        pass


    # Enter a parse tree produced by CgrammerParser#variable_declaration.
    def enterVariable_declaration(self, ctx:CgrammerParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by CgrammerParser#variable_declaration.
    def exitVariable_declaration(self, ctx:CgrammerParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by CgrammerParser#params.
    def enterParams(self, ctx:CgrammerParser.ParamsContext):
        pass

    # Exit a parse tree produced by CgrammerParser#params.
    def exitParams(self, ctx:CgrammerParser.ParamsContext):
        pass


    # Enter a parse tree produced by CgrammerParser#params_definition.
    def enterParams_definition(self, ctx:CgrammerParser.Params_definitionContext):
        pass

    # Exit a parse tree produced by CgrammerParser#params_definition.
    def exitParams_definition(self, ctx:CgrammerParser.Params_definitionContext):
        pass


    # Enter a parse tree produced by CgrammerParser#function_call.
    def enterFunction_call(self, ctx:CgrammerParser.Function_callContext):
        pass

    # Exit a parse tree produced by CgrammerParser#function_call.
    def exitFunction_call(self, ctx:CgrammerParser.Function_callContext):
        pass


    # Enter a parse tree produced by CgrammerParser#id.
    def enterId(self, ctx:CgrammerParser.IdContext):
        pass

    # Exit a parse tree produced by CgrammerParser#id.
    def exitId(self, ctx:CgrammerParser.IdContext):
        pass


    # Enter a parse tree produced by CgrammerParser#int_value.
    def enterInt_value(self, ctx:CgrammerParser.Int_valueContext):
        pass

    # Exit a parse tree produced by CgrammerParser#int_value.
    def exitInt_value(self, ctx:CgrammerParser.Int_valueContext):
        pass


    # Enter a parse tree produced by CgrammerParser#float_value.
    def enterFloat_value(self, ctx:CgrammerParser.Float_valueContext):
        pass

    # Exit a parse tree produced by CgrammerParser#float_value.
    def exitFloat_value(self, ctx:CgrammerParser.Float_valueContext):
        pass


    # Enter a parse tree produced by CgrammerParser#char_value.
    def enterChar_value(self, ctx:CgrammerParser.Char_valueContext):
        pass

    # Exit a parse tree produced by CgrammerParser#char_value.
    def exitChar_value(self, ctx:CgrammerParser.Char_valueContext):
        pass


    # Enter a parse tree produced by CgrammerParser#string_value.
    def enterString_value(self, ctx:CgrammerParser.String_valueContext):
        pass

    # Exit a parse tree produced by CgrammerParser#string_value.
    def exitString_value(self, ctx:CgrammerParser.String_valueContext):
        pass


    # Enter a parse tree produced by CgrammerParser#bool_value.
    def enterBool_value(self, ctx:CgrammerParser.Bool_valueContext):
        pass

    # Exit a parse tree produced by CgrammerParser#bool_value.
    def exitBool_value(self, ctx:CgrammerParser.Bool_valueContext):
        pass


    # Enter a parse tree produced by CgrammerParser#function_call_.
    def enterFunction_call_(self, ctx:CgrammerParser.Function_call_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#function_call_.
    def exitFunction_call_(self, ctx:CgrammerParser.Function_call_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#round.
    def enterRound(self, ctx:CgrammerParser.RoundContext):
        pass

    # Exit a parse tree produced by CgrammerParser#round.
    def exitRound(self, ctx:CgrammerParser.RoundContext):
        pass


    # Enter a parse tree produced by CgrammerParser#expr_value.
    def enterExpr_value(self, ctx:CgrammerParser.Expr_valueContext):
        pass

    # Exit a parse tree produced by CgrammerParser#expr_value.
    def exitExpr_value(self, ctx:CgrammerParser.Expr_valueContext):
        pass


    # Enter a parse tree produced by CgrammerParser#content_of.
    def enterContent_of(self, ctx:CgrammerParser.Content_ofContext):
        pass

    # Exit a parse tree produced by CgrammerParser#content_of.
    def exitContent_of(self, ctx:CgrammerParser.Content_ofContext):
        pass


    # Enter a parse tree produced by CgrammerParser#address_of.
    def enterAddress_of(self, ctx:CgrammerParser.Address_ofContext):
        pass

    # Exit a parse tree produced by CgrammerParser#address_of.
    def exitAddress_of(self, ctx:CgrammerParser.Address_ofContext):
        pass


    # Enter a parse tree produced by CgrammerParser#array.
    def enterArray(self, ctx:CgrammerParser.ArrayContext):
        pass

    # Exit a parse tree produced by CgrammerParser#array.
    def exitArray(self, ctx:CgrammerParser.ArrayContext):
        pass


    # Enter a parse tree produced by CgrammerParser#unit.
    def enterUnit(self, ctx:CgrammerParser.UnitContext):
        pass

    # Exit a parse tree produced by CgrammerParser#unit.
    def exitUnit(self, ctx:CgrammerParser.UnitContext):
        pass


    # Enter a parse tree produced by CgrammerParser#lincrese.
    def enterLincrese(self, ctx:CgrammerParser.LincreseContext):
        pass

    # Exit a parse tree produced by CgrammerParser#lincrese.
    def exitLincrese(self, ctx:CgrammerParser.LincreseContext):
        pass


    # Enter a parse tree produced by CgrammerParser#rincrease.
    def enterRincrease(self, ctx:CgrammerParser.RincreaseContext):
        pass

    # Exit a parse tree produced by CgrammerParser#rincrease.
    def exitRincrease(self, ctx:CgrammerParser.RincreaseContext):
        pass


    # Enter a parse tree produced by CgrammerParser#ldecrease.
    def enterLdecrease(self, ctx:CgrammerParser.LdecreaseContext):
        pass

    # Exit a parse tree produced by CgrammerParser#ldecrease.
    def exitLdecrease(self, ctx:CgrammerParser.LdecreaseContext):
        pass


    # Enter a parse tree produced by CgrammerParser#rdecrease.
    def enterRdecrease(self, ctx:CgrammerParser.RdecreaseContext):
        pass

    # Exit a parse tree produced by CgrammerParser#rdecrease.
    def exitRdecrease(self, ctx:CgrammerParser.RdecreaseContext):
        pass


    # Enter a parse tree produced by CgrammerParser#not.
    def enterNot(self, ctx:CgrammerParser.NotContext):
        pass

    # Exit a parse tree produced by CgrammerParser#not.
    def exitNot(self, ctx:CgrammerParser.NotContext):
        pass


    # Enter a parse tree produced by CgrammerParser#positive.
    def enterPositive(self, ctx:CgrammerParser.PositiveContext):
        pass

    # Exit a parse tree produced by CgrammerParser#positive.
    def exitPositive(self, ctx:CgrammerParser.PositiveContext):
        pass


    # Enter a parse tree produced by CgrammerParser#negative.
    def enterNegative(self, ctx:CgrammerParser.NegativeContext):
        pass

    # Exit a parse tree produced by CgrammerParser#negative.
    def exitNegative(self, ctx:CgrammerParser.NegativeContext):
        pass


    # Enter a parse tree produced by CgrammerParser#addr.
    def enterAddr(self, ctx:CgrammerParser.AddrContext):
        pass

    # Exit a parse tree produced by CgrammerParser#addr.
    def exitAddr(self, ctx:CgrammerParser.AddrContext):
        pass


    # Enter a parse tree produced by CgrammerParser#divide.
    def enterDivide(self, ctx:CgrammerParser.DivideContext):
        pass

    # Exit a parse tree produced by CgrammerParser#divide.
    def exitDivide(self, ctx:CgrammerParser.DivideContext):
        pass


    # Enter a parse tree produced by CgrammerParser#unary.
    def enterUnary(self, ctx:CgrammerParser.UnaryContext):
        pass

    # Exit a parse tree produced by CgrammerParser#unary.
    def exitUnary(self, ctx:CgrammerParser.UnaryContext):
        pass


    # Enter a parse tree produced by CgrammerParser#multiply.
    def enterMultiply(self, ctx:CgrammerParser.MultiplyContext):
        pass

    # Exit a parse tree produced by CgrammerParser#multiply.
    def exitMultiply(self, ctx:CgrammerParser.MultiplyContext):
        pass


    # Enter a parse tree produced by CgrammerParser#modulo.
    def enterModulo(self, ctx:CgrammerParser.ModuloContext):
        pass

    # Exit a parse tree produced by CgrammerParser#modulo.
    def exitModulo(self, ctx:CgrammerParser.ModuloContext):
        pass


    # Enter a parse tree produced by CgrammerParser#add.
    def enterAdd(self, ctx:CgrammerParser.AddContext):
        pass

    # Exit a parse tree produced by CgrammerParser#add.
    def exitAdd(self, ctx:CgrammerParser.AddContext):
        pass


    # Enter a parse tree produced by CgrammerParser#subtract.
    def enterSubtract(self, ctx:CgrammerParser.SubtractContext):
        pass

    # Exit a parse tree produced by CgrammerParser#subtract.
    def exitSubtract(self, ctx:CgrammerParser.SubtractContext):
        pass


    # Enter a parse tree produced by CgrammerParser#calc1.
    def enterCalc1(self, ctx:CgrammerParser.Calc1Context):
        pass

    # Exit a parse tree produced by CgrammerParser#calc1.
    def exitCalc1(self, ctx:CgrammerParser.Calc1Context):
        pass


    # Enter a parse tree produced by CgrammerParser#equal.
    def enterEqual(self, ctx:CgrammerParser.EqualContext):
        pass

    # Exit a parse tree produced by CgrammerParser#equal.
    def exitEqual(self, ctx:CgrammerParser.EqualContext):
        pass


    # Enter a parse tree produced by CgrammerParser#nequal.
    def enterNequal(self, ctx:CgrammerParser.NequalContext):
        pass

    # Exit a parse tree produced by CgrammerParser#nequal.
    def exitNequal(self, ctx:CgrammerParser.NequalContext):
        pass


    # Enter a parse tree produced by CgrammerParser#calc2.
    def enterCalc2(self, ctx:CgrammerParser.Calc2Context):
        pass

    # Exit a parse tree produced by CgrammerParser#calc2.
    def exitCalc2(self, ctx:CgrammerParser.Calc2Context):
        pass


    # Enter a parse tree produced by CgrammerParser#greater.
    def enterGreater(self, ctx:CgrammerParser.GreaterContext):
        pass

    # Exit a parse tree produced by CgrammerParser#greater.
    def exitGreater(self, ctx:CgrammerParser.GreaterContext):
        pass


    # Enter a parse tree produced by CgrammerParser#gequal.
    def enterGequal(self, ctx:CgrammerParser.GequalContext):
        pass

    # Exit a parse tree produced by CgrammerParser#gequal.
    def exitGequal(self, ctx:CgrammerParser.GequalContext):
        pass


    # Enter a parse tree produced by CgrammerParser#less.
    def enterLess(self, ctx:CgrammerParser.LessContext):
        pass

    # Exit a parse tree produced by CgrammerParser#less.
    def exitLess(self, ctx:CgrammerParser.LessContext):
        pass


    # Enter a parse tree produced by CgrammerParser#leuqal.
    def enterLeuqal(self, ctx:CgrammerParser.LeuqalContext):
        pass

    # Exit a parse tree produced by CgrammerParser#leuqal.
    def exitLeuqal(self, ctx:CgrammerParser.LeuqalContext):
        pass


    # Enter a parse tree produced by CgrammerParser#rop1.
    def enterRop1(self, ctx:CgrammerParser.Rop1Context):
        pass

    # Exit a parse tree produced by CgrammerParser#rop1.
    def exitRop1(self, ctx:CgrammerParser.Rop1Context):
        pass


    # Enter a parse tree produced by CgrammerParser#or.
    def enterOr(self, ctx:CgrammerParser.OrContext):
        pass

    # Exit a parse tree produced by CgrammerParser#or.
    def exitOr(self, ctx:CgrammerParser.OrContext):
        pass


    # Enter a parse tree produced by CgrammerParser#and.
    def enterAnd(self, ctx:CgrammerParser.AndContext):
        pass

    # Exit a parse tree produced by CgrammerParser#and.
    def exitAnd(self, ctx:CgrammerParser.AndContext):
        pass


    # Enter a parse tree produced by CgrammerParser#rop2.
    def enterRop2(self, ctx:CgrammerParser.Rop2Context):
        pass

    # Exit a parse tree produced by CgrammerParser#rop2.
    def exitRop2(self, ctx:CgrammerParser.Rop2Context):
        pass


    # Enter a parse tree produced by CgrammerParser#expression.
    def enterExpression(self, ctx:CgrammerParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CgrammerParser#expression.
    def exitExpression(self, ctx:CgrammerParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CgrammerParser#assign.
    def enterAssign(self, ctx:CgrammerParser.AssignContext):
        pass

    # Exit a parse tree produced by CgrammerParser#assign.
    def exitAssign(self, ctx:CgrammerParser.AssignContext):
        pass


    # Enter a parse tree produced by CgrammerParser#addeqaul.
    def enterAddeqaul(self, ctx:CgrammerParser.AddeqaulContext):
        pass

    # Exit a parse tree produced by CgrammerParser#addeqaul.
    def exitAddeqaul(self, ctx:CgrammerParser.AddeqaulContext):
        pass


    # Enter a parse tree produced by CgrammerParser#suvequal.
    def enterSuvequal(self, ctx:CgrammerParser.SuvequalContext):
        pass

    # Exit a parse tree produced by CgrammerParser#suvequal.
    def exitSuvequal(self, ctx:CgrammerParser.SuvequalContext):
        pass


    # Enter a parse tree produced by CgrammerParser#multiplyequal.
    def enterMultiplyequal(self, ctx:CgrammerParser.MultiplyequalContext):
        pass

    # Exit a parse tree produced by CgrammerParser#multiplyequal.
    def exitMultiplyequal(self, ctx:CgrammerParser.MultiplyequalContext):
        pass


    # Enter a parse tree produced by CgrammerParser#divideequal.
    def enterDivideequal(self, ctx:CgrammerParser.DivideequalContext):
        pass

    # Exit a parse tree produced by CgrammerParser#divideequal.
    def exitDivideequal(self, ctx:CgrammerParser.DivideequalContext):
        pass


    # Enter a parse tree produced by CgrammerParser#moduloequal.
    def enterModuloequal(self, ctx:CgrammerParser.ModuloequalContext):
        pass

    # Exit a parse tree produced by CgrammerParser#moduloequal.
    def exitModuloequal(self, ctx:CgrammerParser.ModuloequalContext):
        pass


    # Enter a parse tree produced by CgrammerParser#assignment.
    def enterAssignment(self, ctx:CgrammerParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CgrammerParser#assignment.
    def exitAssignment(self, ctx:CgrammerParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CgrammerParser#variable_definition.
    def enterVariable_definition(self, ctx:CgrammerParser.Variable_definitionContext):
        pass

    # Exit a parse tree produced by CgrammerParser#variable_definition.
    def exitVariable_definition(self, ctx:CgrammerParser.Variable_definitionContext):
        pass


    # Enter a parse tree produced by CgrammerParser#memest_announce.
    def enterMemest_announce(self, ctx:CgrammerParser.Memest_announceContext):
        pass

    # Exit a parse tree produced by CgrammerParser#memest_announce.
    def exitMemest_announce(self, ctx:CgrammerParser.Memest_announceContext):
        pass


    # Enter a parse tree produced by CgrammerParser#strlen_announce.
    def enterStrlen_announce(self, ctx:CgrammerParser.Strlen_announceContext):
        pass

    # Exit a parse tree produced by CgrammerParser#strlen_announce.
    def exitStrlen_announce(self, ctx:CgrammerParser.Strlen_announceContext):
        pass


    # Enter a parse tree produced by CgrammerParser#printf_announce.
    def enterPrintf_announce(self, ctx:CgrammerParser.Printf_announceContext):
        pass

    # Exit a parse tree produced by CgrammerParser#printf_announce.
    def exitPrintf_announce(self, ctx:CgrammerParser.Printf_announceContext):
        pass


    # Enter a parse tree produced by CgrammerParser#scanf_annouce.
    def enterScanf_annouce(self, ctx:CgrammerParser.Scanf_annouceContext):
        pass

    # Exit a parse tree produced by CgrammerParser#scanf_annouce.
    def exitScanf_annouce(self, ctx:CgrammerParser.Scanf_annouceContext):
        pass


    # Enter a parse tree produced by CgrammerParser#function_definition.
    def enterFunction_definition(self, ctx:CgrammerParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by CgrammerParser#function_definition.
    def exitFunction_definition(self, ctx:CgrammerParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by CgrammerParser#if_block.
    def enterIf_block(self, ctx:CgrammerParser.If_blockContext):
        pass

    # Exit a parse tree produced by CgrammerParser#if_block.
    def exitIf_block(self, ctx:CgrammerParser.If_blockContext):
        pass


    # Enter a parse tree produced by CgrammerParser#while_block.
    def enterWhile_block(self, ctx:CgrammerParser.While_blockContext):
        pass

    # Exit a parse tree produced by CgrammerParser#while_block.
    def exitWhile_block(self, ctx:CgrammerParser.While_blockContext):
        pass


    # Enter a parse tree produced by CgrammerParser#for_block.
    def enterFor_block(self, ctx:CgrammerParser.For_blockContext):
        pass

    # Exit a parse tree produced by CgrammerParser#for_block.
    def exitFor_block(self, ctx:CgrammerParser.For_blockContext):
        pass


    # Enter a parse tree produced by CgrammerParser#switch_block.
    def enterSwitch_block(self, ctx:CgrammerParser.Switch_blockContext):
        pass

    # Exit a parse tree produced by CgrammerParser#switch_block.
    def exitSwitch_block(self, ctx:CgrammerParser.Switch_blockContext):
        pass


    # Enter a parse tree produced by CgrammerParser#declaration.
    def enterDeclaration(self, ctx:CgrammerParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CgrammerParser#declaration.
    def exitDeclaration(self, ctx:CgrammerParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CgrammerParser#definition.
    def enterDefinition(self, ctx:CgrammerParser.DefinitionContext):
        pass

    # Exit a parse tree produced by CgrammerParser#definition.
    def exitDefinition(self, ctx:CgrammerParser.DefinitionContext):
        pass


    # Enter a parse tree produced by CgrammerParser#assign_state.
    def enterAssign_state(self, ctx:CgrammerParser.Assign_stateContext):
        pass

    # Exit a parse tree produced by CgrammerParser#assign_state.
    def exitAssign_state(self, ctx:CgrammerParser.Assign_stateContext):
        pass


    # Enter a parse tree produced by CgrammerParser#expr.
    def enterExpr(self, ctx:CgrammerParser.ExprContext):
        pass

    # Exit a parse tree produced by CgrammerParser#expr.
    def exitExpr(self, ctx:CgrammerParser.ExprContext):
        pass


    # Enter a parse tree produced by CgrammerParser#lib_func.
    def enterLib_func(self, ctx:CgrammerParser.Lib_funcContext):
        pass

    # Exit a parse tree produced by CgrammerParser#lib_func.
    def exitLib_func(self, ctx:CgrammerParser.Lib_funcContext):
        pass


    # Enter a parse tree produced by CgrammerParser#break.
    def enterBreak(self, ctx:CgrammerParser.BreakContext):
        pass

    # Exit a parse tree produced by CgrammerParser#break.
    def exitBreak(self, ctx:CgrammerParser.BreakContext):
        pass


    # Enter a parse tree produced by CgrammerParser#continue.
    def enterContinue(self, ctx:CgrammerParser.ContinueContext):
        pass

    # Exit a parse tree produced by CgrammerParser#continue.
    def exitContinue(self, ctx:CgrammerParser.ContinueContext):
        pass


    # Enter a parse tree produced by CgrammerParser#return.
    def enterReturn(self, ctx:CgrammerParser.ReturnContext):
        pass

    # Exit a parse tree produced by CgrammerParser#return.
    def exitReturn(self, ctx:CgrammerParser.ReturnContext):
        pass


    # Enter a parse tree produced by CgrammerParser#line.
    def enterLine(self, ctx:CgrammerParser.LineContext):
        pass

    # Exit a parse tree produced by CgrammerParser#line.
    def exitLine(self, ctx:CgrammerParser.LineContext):
        pass


    # Enter a parse tree produced by CgrammerParser#if.
    def enterIf(self, ctx:CgrammerParser.IfContext):
        pass

    # Exit a parse tree produced by CgrammerParser#if.
    def exitIf(self, ctx:CgrammerParser.IfContext):
        pass


    # Enter a parse tree produced by CgrammerParser#while.
    def enterWhile(self, ctx:CgrammerParser.WhileContext):
        pass

    # Exit a parse tree produced by CgrammerParser#while.
    def exitWhile(self, ctx:CgrammerParser.WhileContext):
        pass


    # Enter a parse tree produced by CgrammerParser#for.
    def enterFor(self, ctx:CgrammerParser.ForContext):
        pass

    # Exit a parse tree produced by CgrammerParser#for.
    def exitFor(self, ctx:CgrammerParser.ForContext):
        pass


    # Enter a parse tree produced by CgrammerParser#switch.
    def enterSwitch(self, ctx:CgrammerParser.SwitchContext):
        pass

    # Exit a parse tree produced by CgrammerParser#switch.
    def exitSwitch(self, ctx:CgrammerParser.SwitchContext):
        pass


    # Enter a parse tree produced by CgrammerParser#single.
    def enterSingle(self, ctx:CgrammerParser.SingleContext):
        pass

    # Exit a parse tree produced by CgrammerParser#single.
    def exitSingle(self, ctx:CgrammerParser.SingleContext):
        pass


    # Enter a parse tree produced by CgrammerParser#function.
    def enterFunction(self, ctx:CgrammerParser.FunctionContext):
        pass

    # Exit a parse tree produced by CgrammerParser#function.
    def exitFunction(self, ctx:CgrammerParser.FunctionContext):
        pass


    # Enter a parse tree produced by CgrammerParser#simple_code.
    def enterSimple_code(self, ctx:CgrammerParser.Simple_codeContext):
        pass

    # Exit a parse tree produced by CgrammerParser#simple_code.
    def exitSimple_code(self, ctx:CgrammerParser.Simple_codeContext):
        pass


    # Enter a parse tree produced by CgrammerParser#domained_code.
    def enterDomained_code(self, ctx:CgrammerParser.Domained_codeContext):
        pass

    # Exit a parse tree produced by CgrammerParser#domained_code.
    def exitDomained_code(self, ctx:CgrammerParser.Domained_codeContext):
        pass


    # Enter a parse tree produced by CgrammerParser#code.
    def enterCode(self, ctx:CgrammerParser.CodeContext):
        pass

    # Exit a parse tree produced by CgrammerParser#code.
    def exitCode(self, ctx:CgrammerParser.CodeContext):
        pass



del CgrammerParser