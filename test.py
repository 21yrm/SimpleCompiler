import llvmlite.ir as ir
import llvmlite.binding as llvm
import ctypes

# 初�?�化 LLVM
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

# 创建 LLVM 上下文和模块
context = ir.Context()
module = ir.Module(name="my_module")

# 创建主函数类�?
main_type = ir.FunctionType(ir.IntType(32), [])
main_func = ir.Function(module, main_type, name="main")

# 创建主函数的基本�?
entry_block = main_func.append_basic_block(name="entry")

# 使用指令生成器在基本块中插入指令
builder = ir.IRBuilder(entry_block)

# 创建变量a，b，c
a = builder.alloca(ir.IntType(32), name="a")
b = builder.alloca(ir.IntType(32), name="b")
c = builder.alloca(ir.IntType(32), name="c")

# 初�?�化变量a和b
builder.store(ir.Constant(ir.IntType(32), 5), a)
builder.store(ir.Constant(ir.IntType(32), 10), b)

# 计算c = a + b
a_value = builder.load(a)
b_value = builder.load(b)
c_value = builder.add(a_value, b_value)
builder.store(c_value, c)

# 调用printf打印结果
printf_type = ir.FunctionType(ir.IntType(32), [ir.IntType(8).as_pointer(), ir.IntType(32)])
printf_func = ir.Function(module, printf_type, name="printf")
builder.call(printf_func, [format_string, builder.load(c)])

# 返回0
builder.ret(ir.Constant(ir.IntType(32), 0))

# 创建引擎和编译器
target = llvm.Target.from_default_triple()
target_machine = target.create_target_machine()
backing_mod = llvm.parse_assembly("")
engine = llvm.create_mcjit_compiler(backing_mod, target_machine)

# 编译模块
llvm_ir = str(module)
mod = llvm.parse_assembly(llvm_ir)
mod.verify()
engine.add_module(mod)
engine.finalize_object()
engine.run_static_constructors()

# 获取主函数指针并执�??
func_ptr = engine.get_function_address("main")
c_func = ctypes.CFUNCTYPE(ctypes.c_int)(func_ptr)
result = c_func()

print("Result:", result)
