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


    # Enter a parse tree produced by CgrammerParser#string.
    def enterString(self, ctx:CgrammerParser.StringContext):
        pass

    # Exit a parse tree produced by CgrammerParser#string.
    def exitString(self, ctx:CgrammerParser.StringContext):
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


    # Enter a parse tree produced by CgrammerParser#value_.
    def enterValue_(self, ctx:CgrammerParser.Value_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#value_.
    def exitValue_(self, ctx:CgrammerParser.Value_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#content_of_.
    def enterContent_of_(self, ctx:CgrammerParser.Content_of_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#content_of_.
    def exitContent_of_(self, ctx:CgrammerParser.Content_of_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#address_of_.
    def enterAddress_of_(self, ctx:CgrammerParser.Address_of_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#address_of_.
    def exitAddress_of_(self, ctx:CgrammerParser.Address_of_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#array_.
    def enterArray_(self, ctx:CgrammerParser.Array_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#array_.
    def exitArray_(self, ctx:CgrammerParser.Array_Context):
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


    # Enter a parse tree produced by CgrammerParser#liecrese.
    def enterLiecrese(self, ctx:CgrammerParser.LiecreseContext):
        pass

    # Exit a parse tree produced by CgrammerParser#liecrese.
    def exitLiecrese(self, ctx:CgrammerParser.LiecreseContext):
        pass


    # Enter a parse tree produced by CgrammerParser#ldecrease.
    def enterLdecrease(self, ctx:CgrammerParser.LdecreaseContext):
        pass

    # Exit a parse tree produced by CgrammerParser#ldecrease.
    def exitLdecrease(self, ctx:CgrammerParser.LdecreaseContext):
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


    # Enter a parse tree produced by CgrammerParser#next_2.
    def enterNext_2(self, ctx:CgrammerParser.Next_2Context):
        pass

    # Exit a parse tree produced by CgrammerParser#next_2.
    def exitNext_2(self, ctx:CgrammerParser.Next_2Context):
        pass


    # Enter a parse tree produced by CgrammerParser#rincrease.
    def enterRincrease(self, ctx:CgrammerParser.RincreaseContext):
        pass

    # Exit a parse tree produced by CgrammerParser#rincrease.
    def exitRincrease(self, ctx:CgrammerParser.RincreaseContext):
        pass


    # Enter a parse tree produced by CgrammerParser#dincrease.
    def enterDincrease(self, ctx:CgrammerParser.DincreaseContext):
        pass

    # Exit a parse tree produced by CgrammerParser#dincrease.
    def exitDincrease(self, ctx:CgrammerParser.DincreaseContext):
        pass


    # Enter a parse tree produced by CgrammerParser#expr_l2.
    def enterExpr_l2(self, ctx:CgrammerParser.Expr_l2Context):
        pass

    # Exit a parse tree produced by CgrammerParser#expr_l2.
    def exitExpr_l2(self, ctx:CgrammerParser.Expr_l2Context):
        pass


    # Enter a parse tree produced by CgrammerParser#multiply_.
    def enterMultiply_(self, ctx:CgrammerParser.Multiply_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#multiply_.
    def exitMultiply_(self, ctx:CgrammerParser.Multiply_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#divide_.
    def enterDivide_(self, ctx:CgrammerParser.Divide_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#divide_.
    def exitDivide_(self, ctx:CgrammerParser.Divide_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#modulo_.
    def enterModulo_(self, ctx:CgrammerParser.Modulo_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#modulo_.
    def exitModulo_(self, ctx:CgrammerParser.Modulo_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#expr_l3_s1.
    def enterExpr_l3_s1(self, ctx:CgrammerParser.Expr_l3_s1Context):
        pass

    # Exit a parse tree produced by CgrammerParser#expr_l3_s1.
    def exitExpr_l3_s1(self, ctx:CgrammerParser.Expr_l3_s1Context):
        pass


    # Enter a parse tree produced by CgrammerParser#multiply.
    def enterMultiply(self, ctx:CgrammerParser.MultiplyContext):
        pass

    # Exit a parse tree produced by CgrammerParser#multiply.
    def exitMultiply(self, ctx:CgrammerParser.MultiplyContext):
        pass


    # Enter a parse tree produced by CgrammerParser#divide.
    def enterDivide(self, ctx:CgrammerParser.DivideContext):
        pass

    # Exit a parse tree produced by CgrammerParser#divide.
    def exitDivide(self, ctx:CgrammerParser.DivideContext):
        pass


    # Enter a parse tree produced by CgrammerParser#modulo.
    def enterModulo(self, ctx:CgrammerParser.ModuloContext):
        pass

    # Exit a parse tree produced by CgrammerParser#modulo.
    def exitModulo(self, ctx:CgrammerParser.ModuloContext):
        pass


    # Enter a parse tree produced by CgrammerParser#expr_l3.
    def enterExpr_l3(self, ctx:CgrammerParser.Expr_l3Context):
        pass

    # Exit a parse tree produced by CgrammerParser#expr_l3.
    def exitExpr_l3(self, ctx:CgrammerParser.Expr_l3Context):
        pass


    # Enter a parse tree produced by CgrammerParser#add_.
    def enterAdd_(self, ctx:CgrammerParser.Add_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#add_.
    def exitAdd_(self, ctx:CgrammerParser.Add_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#subtract_.
    def enterSubtract_(self, ctx:CgrammerParser.Subtract_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#subtract_.
    def exitSubtract_(self, ctx:CgrammerParser.Subtract_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#expr_l4_s1.
    def enterExpr_l4_s1(self, ctx:CgrammerParser.Expr_l4_s1Context):
        pass

    # Exit a parse tree produced by CgrammerParser#expr_l4_s1.
    def exitExpr_l4_s1(self, ctx:CgrammerParser.Expr_l4_s1Context):
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


    # Enter a parse tree produced by CgrammerParser#expr_l4.
    def enterExpr_l4(self, ctx:CgrammerParser.Expr_l4Context):
        pass

    # Exit a parse tree produced by CgrammerParser#expr_l4.
    def exitExpr_l4(self, ctx:CgrammerParser.Expr_l4Context):
        pass


    # Enter a parse tree produced by CgrammerParser#lshift_.
    def enterLshift_(self, ctx:CgrammerParser.Lshift_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#lshift_.
    def exitLshift_(self, ctx:CgrammerParser.Lshift_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#rshift_.
    def enterRshift_(self, ctx:CgrammerParser.Rshift_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#rshift_.
    def exitRshift_(self, ctx:CgrammerParser.Rshift_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#expr_l5_s1.
    def enterExpr_l5_s1(self, ctx:CgrammerParser.Expr_l5_s1Context):
        pass

    # Exit a parse tree produced by CgrammerParser#expr_l5_s1.
    def exitExpr_l5_s1(self, ctx:CgrammerParser.Expr_l5_s1Context):
        pass


    # Enter a parse tree produced by CgrammerParser#lshift.
    def enterLshift(self, ctx:CgrammerParser.LshiftContext):
        pass

    # Exit a parse tree produced by CgrammerParser#lshift.
    def exitLshift(self, ctx:CgrammerParser.LshiftContext):
        pass


    # Enter a parse tree produced by CgrammerParser#rshift.
    def enterRshift(self, ctx:CgrammerParser.RshiftContext):
        pass

    # Exit a parse tree produced by CgrammerParser#rshift.
    def exitRshift(self, ctx:CgrammerParser.RshiftContext):
        pass


    # Enter a parse tree produced by CgrammerParser#expr_l5.
    def enterExpr_l5(self, ctx:CgrammerParser.Expr_l5Context):
        pass

    # Exit a parse tree produced by CgrammerParser#expr_l5.
    def exitExpr_l5(self, ctx:CgrammerParser.Expr_l5Context):
        pass


    # Enter a parse tree produced by CgrammerParser#equal_.
    def enterEqual_(self, ctx:CgrammerParser.Equal_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#equal_.
    def exitEqual_(self, ctx:CgrammerParser.Equal_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#nequal_.
    def enterNequal_(self, ctx:CgrammerParser.Nequal_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#nequal_.
    def exitNequal_(self, ctx:CgrammerParser.Nequal_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#expr_l6_s1.
    def enterExpr_l6_s1(self, ctx:CgrammerParser.Expr_l6_s1Context):
        pass

    # Exit a parse tree produced by CgrammerParser#expr_l6_s1.
    def exitExpr_l6_s1(self, ctx:CgrammerParser.Expr_l6_s1Context):
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


    # Enter a parse tree produced by CgrammerParser#expr_l6.
    def enterExpr_l6(self, ctx:CgrammerParser.Expr_l6Context):
        pass

    # Exit a parse tree produced by CgrammerParser#expr_l6.
    def exitExpr_l6(self, ctx:CgrammerParser.Expr_l6Context):
        pass


    # Enter a parse tree produced by CgrammerParser#greater_.
    def enterGreater_(self, ctx:CgrammerParser.Greater_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#greater_.
    def exitGreater_(self, ctx:CgrammerParser.Greater_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#gequal_.
    def enterGequal_(self, ctx:CgrammerParser.Gequal_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#gequal_.
    def exitGequal_(self, ctx:CgrammerParser.Gequal_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#less_.
    def enterLess_(self, ctx:CgrammerParser.Less_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#less_.
    def exitLess_(self, ctx:CgrammerParser.Less_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#leuqal_.
    def enterLeuqal_(self, ctx:CgrammerParser.Leuqal_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#leuqal_.
    def exitLeuqal_(self, ctx:CgrammerParser.Leuqal_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#expr_l7_s1.
    def enterExpr_l7_s1(self, ctx:CgrammerParser.Expr_l7_s1Context):
        pass

    # Exit a parse tree produced by CgrammerParser#expr_l7_s1.
    def exitExpr_l7_s1(self, ctx:CgrammerParser.Expr_l7_s1Context):
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


    # Enter a parse tree produced by CgrammerParser#expr_l7.
    def enterExpr_l7(self, ctx:CgrammerParser.Expr_l7Context):
        pass

    # Exit a parse tree produced by CgrammerParser#expr_l7.
    def exitExpr_l7(self, ctx:CgrammerParser.Expr_l7Context):
        pass


    # Enter a parse tree produced by CgrammerParser#bitnot__.
    def enterBitnot__(self, ctx:CgrammerParser.Bitnot__Context):
        pass

    # Exit a parse tree produced by CgrammerParser#bitnot__.
    def exitBitnot__(self, ctx:CgrammerParser.Bitnot__Context):
        pass


    # Enter a parse tree produced by CgrammerParser#next_81.
    def enterNext_81(self, ctx:CgrammerParser.Next_81Context):
        pass

    # Exit a parse tree produced by CgrammerParser#next_81.
    def exitNext_81(self, ctx:CgrammerParser.Next_81Context):
        pass


    # Enter a parse tree produced by CgrammerParser#bitandd_.
    def enterBitandd_(self, ctx:CgrammerParser.Bitandd_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#bitandd_.
    def exitBitandd_(self, ctx:CgrammerParser.Bitandd_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#bitor_.
    def enterBitor_(self, ctx:CgrammerParser.Bitor_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#bitor_.
    def exitBitor_(self, ctx:CgrammerParser.Bitor_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#bitnot_.
    def enterBitnot_(self, ctx:CgrammerParser.Bitnot_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#bitnot_.
    def exitBitnot_(self, ctx:CgrammerParser.Bitnot_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#expr_l8_s2.
    def enterExpr_l8_s2(self, ctx:CgrammerParser.Expr_l8_s2Context):
        pass

    # Exit a parse tree produced by CgrammerParser#expr_l8_s2.
    def exitExpr_l8_s2(self, ctx:CgrammerParser.Expr_l8_s2Context):
        pass


    # Enter a parse tree produced by CgrammerParser#bitandd.
    def enterBitandd(self, ctx:CgrammerParser.BitanddContext):
        pass

    # Exit a parse tree produced by CgrammerParser#bitandd.
    def exitBitandd(self, ctx:CgrammerParser.BitanddContext):
        pass


    # Enter a parse tree produced by CgrammerParser#bitor.
    def enterBitor(self, ctx:CgrammerParser.BitorContext):
        pass

    # Exit a parse tree produced by CgrammerParser#bitor.
    def exitBitor(self, ctx:CgrammerParser.BitorContext):
        pass


    # Enter a parse tree produced by CgrammerParser#bitnot.
    def enterBitnot(self, ctx:CgrammerParser.BitnotContext):
        pass

    # Exit a parse tree produced by CgrammerParser#bitnot.
    def exitBitnot(self, ctx:CgrammerParser.BitnotContext):
        pass


    # Enter a parse tree produced by CgrammerParser#expr_l8.
    def enterExpr_l8(self, ctx:CgrammerParser.Expr_l8Context):
        pass

    # Exit a parse tree produced by CgrammerParser#expr_l8.
    def exitExpr_l8(self, ctx:CgrammerParser.Expr_l8Context):
        pass


    # Enter a parse tree produced by CgrammerParser#and_.
    def enterAnd_(self, ctx:CgrammerParser.And_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#and_.
    def exitAnd_(self, ctx:CgrammerParser.And_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#or_.
    def enterOr_(self, ctx:CgrammerParser.Or_Context):
        pass

    # Exit a parse tree produced by CgrammerParser#or_.
    def exitOr_(self, ctx:CgrammerParser.Or_Context):
        pass


    # Enter a parse tree produced by CgrammerParser#expr_l9_s1.
    def enterExpr_l9_s1(self, ctx:CgrammerParser.Expr_l9_s1Context):
        pass

    # Exit a parse tree produced by CgrammerParser#expr_l9_s1.
    def exitExpr_l9_s1(self, ctx:CgrammerParser.Expr_l9_s1Context):
        pass


    # Enter a parse tree produced by CgrammerParser#and.
    def enterAnd(self, ctx:CgrammerParser.AndContext):
        pass

    # Exit a parse tree produced by CgrammerParser#and.
    def exitAnd(self, ctx:CgrammerParser.AndContext):
        pass


    # Enter a parse tree produced by CgrammerParser#or.
    def enterOr(self, ctx:CgrammerParser.OrContext):
        pass

    # Exit a parse tree produced by CgrammerParser#or.
    def exitOr(self, ctx:CgrammerParser.OrContext):
        pass


    # Enter a parse tree produced by CgrammerParser#expr_l9.
    def enterExpr_l9(self, ctx:CgrammerParser.Expr_l9Context):
        pass

    # Exit a parse tree produced by CgrammerParser#expr_l9.
    def exitExpr_l9(self, ctx:CgrammerParser.Expr_l9Context):
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