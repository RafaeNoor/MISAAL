import tvm
import os
from tvm import relax

def runner(module_class, expected_output, target=None):
    mod = module_class
    if not target:
        target = tvm.target.Target("llvm -mcpu=skylake -mattr=+avx,+avx512f -num-cores=16")

    file_name = __file__[:-3] + '_s_exp'
    with tvm.transform.PassContext(instruments=[], config={'codegen_debug':False, 'misaal':True,'misaal_s_exp_path':file_name} ):
        ex = relax.build(mod, target)

    f = open(file_name)
    f_str = f.read().strip()
    f.close()
    os.remove(file_name)
    assert f_str == expected_output.strip()


