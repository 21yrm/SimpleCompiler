# Generated from Cgrammer.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CgrammerParser import CgrammerParser
else:
    from CgrammerParser import CgrammerParser

# This class defines a complete generic visitor for a parse tree produced by CgrammerParser.

class CgrammerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CgrammerParser#int.
    def visitInt(self, ctx:CgrammerParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#float.
    def visitFloat(self, ctx:CgrammerParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#char.
    def visitChar(self, ctx:CgrammerParser.CharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#bool.
    def visitBool(self, ctx:CgrammerParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#string.
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


    # Visit a parse tree produced by CgrammerParser#value_.
    def visitValue_(self, ctx:CgrammerParser.Value_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#content_of_.
    def visitContent_of_(self, ctx:CgrammerParser.Content_of_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#address_of_.
    def visitAddress_of_(self, ctx:CgrammerParser.Address_of_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#array_.
    def visitArray_(self, ctx:CgrammerParser.Array_Context):
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


    # Visit a parse tree produced by CgrammerParser#liecrese.
    def visitLiecrese(self, ctx:CgrammerParser.LiecreseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#ldecrease.
    def visitLdecrease(self, ctx:CgrammerParser.LdecreaseContext):
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


    # Visit a parse tree produced by CgrammerParser#next_2.
    def visitNext_2(self, ctx:CgrammerParser.Next_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#rincrease.
    def visitRincrease(self, ctx:CgrammerParser.RincreaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#dincrease.
    def visitDincrease(self, ctx:CgrammerParser.DincreaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#expr_l2.
    def visitExpr_l2(self, ctx:CgrammerParser.Expr_l2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#multiply_.
    def visitMultiply_(self, ctx:CgrammerParser.Multiply_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#divide_.
    def visitDivide_(self, ctx:CgrammerParser.Divide_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#modulo_.
    def visitModulo_(self, ctx:CgrammerParser.Modulo_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#expr_l3_s1.
    def visitExpr_l3_s1(self, ctx:CgrammerParser.Expr_l3_s1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#multiply.
    def visitMultiply(self, ctx:CgrammerParser.MultiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#divide.
    def visitDivide(self, ctx:CgrammerParser.DivideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#modulo.
    def visitModulo(self, ctx:CgrammerParser.ModuloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#expr_l3.
    def visitExpr_l3(self, ctx:CgrammerParser.Expr_l3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#add_.
    def visitAdd_(self, ctx:CgrammerParser.Add_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#subtract_.
    def visitSubtract_(self, ctx:CgrammerParser.Subtract_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#expr_l4_s1.
    def visitExpr_l4_s1(self, ctx:CgrammerParser.Expr_l4_s1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#add.
    def visitAdd(self, ctx:CgrammerParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#subtract.
    def visitSubtract(self, ctx:CgrammerParser.SubtractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#expr_l4.
    def visitExpr_l4(self, ctx:CgrammerParser.Expr_l4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#lshift_.
    def visitLshift_(self, ctx:CgrammerParser.Lshift_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#rshift_.
    def visitRshift_(self, ctx:CgrammerParser.Rshift_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#expr_l5_s1.
    def visitExpr_l5_s1(self, ctx:CgrammerParser.Expr_l5_s1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#lshift.
    def visitLshift(self, ctx:CgrammerParser.LshiftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#rshift.
    def visitRshift(self, ctx:CgrammerParser.RshiftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#expr_l5.
    def visitExpr_l5(self, ctx:CgrammerParser.Expr_l5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#equal_.
    def visitEqual_(self, ctx:CgrammerParser.Equal_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#nequal_.
    def visitNequal_(self, ctx:CgrammerParser.Nequal_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#expr_l6_s1.
    def visitExpr_l6_s1(self, ctx:CgrammerParser.Expr_l6_s1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#equal.
    def visitEqual(self, ctx:CgrammerParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#nequal.
    def visitNequal(self, ctx:CgrammerParser.NequalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#expr_l6.
    def visitExpr_l6(self, ctx:CgrammerParser.Expr_l6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#greater_.
    def visitGreater_(self, ctx:CgrammerParser.Greater_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#gequal_.
    def visitGequal_(self, ctx:CgrammerParser.Gequal_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#less_.
    def visitLess_(self, ctx:CgrammerParser.Less_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#leuqal_.
    def visitLeuqal_(self, ctx:CgrammerParser.Leuqal_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#expr_l7_s1.
    def visitExpr_l7_s1(self, ctx:CgrammerParser.Expr_l7_s1Context):
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


    # Visit a parse tree produced by CgrammerParser#expr_l7.
    def visitExpr_l7(self, ctx:CgrammerParser.Expr_l7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#bitnot__.
    def visitBitnot__(self, ctx:CgrammerParser.Bitnot__Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#next_81.
    def visitNext_81(self, ctx:CgrammerParser.Next_81Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#bitandd_.
    def visitBitandd_(self, ctx:CgrammerParser.Bitandd_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#bitor_.
    def visitBitor_(self, ctx:CgrammerParser.Bitor_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#bitnot_.
    def visitBitnot_(self, ctx:CgrammerParser.Bitnot_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#expr_l8_s2.
    def visitExpr_l8_s2(self, ctx:CgrammerParser.Expr_l8_s2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#bitandd.
    def visitBitandd(self, ctx:CgrammerParser.BitanddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#bitor.
    def visitBitor(self, ctx:CgrammerParser.BitorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#bitnot.
    def visitBitnot(self, ctx:CgrammerParser.BitnotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#expr_l8.
    def visitExpr_l8(self, ctx:CgrammerParser.Expr_l8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#and_.
    def visitAnd_(self, ctx:CgrammerParser.And_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#or_.
    def visitOr_(self, ctx:CgrammerParser.Or_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#expr_l9_s1.
    def visitExpr_l9_s1(self, ctx:CgrammerParser.Expr_l9_s1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#and.
    def visitAnd(self, ctx:CgrammerParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#or.
    def visitOr(self, ctx:CgrammerParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CgrammerParser#expr_l9.
    def visitExpr_l9(self, ctx:CgrammerParser.Expr_l9Context):
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



del CgrammerParser