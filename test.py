import llvmlite.ir as ir
import llvmlite.binding as llvm
import ctypes

# åå?å LLVM
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

# åå»º LLVM ä¸ä¸æåæ¨¡å
context = ir.Context()
module = ir.Module(name="my_module")

# åå»ºä¸»å½æ°ç±»å?
main_type = ir.FunctionType(ir.IntType(32), [])
main_func = ir.Function(module, main_type, name="main")

# åå»ºä¸»å½æ°çåºæ¬å?
entry_block = main_func.append_basic_block(name="entry")

# ä½¿ç¨æä»¤çæå¨å¨åºæ¬åä¸­æå¥æä»¤
builder = ir.IRBuilder(entry_block)

# åå»ºåéaï¼bï¼c
a = builder.alloca(ir.IntType(32), name="a")
b = builder.alloca(ir.IntType(32), name="b")
c = builder.alloca(ir.IntType(32), name="c")

# åå?ååéaåb
builder.store(ir.Constant(ir.IntType(32), 5), a)
builder.store(ir.Constant(ir.IntType(32), 10), b)

# è®¡ç®c = a + b
a_value = builder.load(a)
b_value = builder.load(b)
c_value = builder.add(a_value, b_value)
builder.store(c_value, c)

# è°ç¨printfæå°ç»æ
printf_type = ir.FunctionType(ir.IntType(32), [ir.IntType(8).as_pointer(), ir.IntType(32)])
printf_func = ir.Function(module, printf_type, name="printf")
builder.call(printf_func, [format_string, builder.load(c)])

# è¿å0
builder.ret(ir.Constant(ir.IntType(32), 0))

# åå»ºå¼æåç¼è¯å¨
target = llvm.Target.from_default_triple()
target_machine = target.create_target_machine()
backing_mod = llvm.parse_assembly("")
engine = llvm.create_mcjit_compiler(backing_mod, target_machine)

# ç¼è¯æ¨¡å
llvm_ir = str(module)
mod = llvm.parse_assembly(llvm_ir)
mod.verify()
engine.add_module(mod)
engine.finalize_object()
engine.run_static_constructors()

# è·åä¸»å½æ°æéå¹¶æ§è??
func_ptr = engine.get_function_address("main")
c_func = ctypes.CFUNCTYPE(ctypes.c_int)(func_ptr)
result = c_func()

print("Result:", result)
