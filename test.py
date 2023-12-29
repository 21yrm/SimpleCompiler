from llvmlite import ir
from llvmlite import binding as llvm


def create_ir_function():
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()

    # 创建一个LLVM模块
    module = ir.Module(name='my_module')

    # 创建一个LLVM函数类型
    function_type = ir.FunctionType(ir.IntType(32), [], False)

    # 创建一个LLVM函数
    function = ir.Function(module, function_type, name='my_function')

    # 创建一个LLVM基本块
    block = function.append_basic_block(name='entry')

    # 在基本块中创建LLVM指令
    builder = ir.IRBuilder(block)
    constant = ir.Constant(ir.IntType(32), 42)
    return_value = builder.ret(constant)

    # 打印生成的LLVM IR代码
    print(module)

    # 创建一个LLVM执行引擎
    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    backing_mod = llvm.parse_assembly("")
    engine = llvm.create_mcjit_compiler(backing_mod, target_machine)

    # 使用LLVM执行引擎运行LLVM IR函数
    engine.add_module(module)
    engine.finalize_object()
    engine.run_static_constructors()
    result = engine.get_function_address('my_function')()

    # 打印结果
    print('Result:', result)


if __name__ == '__main__':
    create_ir_function()