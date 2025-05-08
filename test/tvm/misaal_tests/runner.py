import tvm
from tvm import relax
from tvm.relax.frontend import nn
from tvm.ir.instrument import PrintAfterAll, PrintBeforeAll
from tvm import transform
from tvm.tir.build import codegen_build
from tvm.script import ir as I
from tvm.script import tir as T
from tvm.script import relax as R

import os, glob
import numpy as np

def cleanup(file_name):
    to_remove = ['test_cases/'+file_name+'_misaal.py',
                 file_name+'_misaal.py',
                 'test_cases/'+file_name+'_s_exp',
                 file_name+'_s_exp',
                 'test_cases/'+file_name+'_misaal_temp_file.ll',
                 file_name+'_misaal_temp_file.ll',
                 'test_cases/'+file_name+'_misaal_temp_file.linked.bc',
                 file_name+'_misaal_temp_file.linked.bc',
                 'test_cases/'+file_name+'_misaal_temp_file.linked.ll',
                 file_name+'_misaal_temp_file.linked.ll',
                 'test_cases/'+file_name+'_misaal_temp_file.legalize.ll',
                 file_name+'_misaal_temp_file.legalize.ll,'
                 'test.out']
    for name in to_remove:
        if os.path.exists(name):
            os.remove(name)
    for file in glob.glob("test_cases/*misaal*"):
        os.remove(file)
    for file in glob.glob("*misaal*"):
        os.remove(file)
    for file in glob.glob("test_cases/*egg*"):
        os.remove(file)
    for file in glob.glob("*egg*"):
        os.remove(file)

def simple_op(file_name, dtype, buffer_size, vector_size, Module, numpy_op, print_result, do_cleanup=True):
    mod = Module
    # target = tvm.target.Target("llvm -mcpu=alderlake -mattr=+avx2 -num-cores=14")
    target = tvm.target.Target("llvm -mcpu=skylake-avx512 -mattr=+avx512f,+avx512dq,+avx512cd,+avx512bw,+avx512vl -num-cores=64")

    # with tvm.transform.PassContext(instruments=[], config={'codegen_debug':False, 'misaal':True,'misaal_s_exp_path':file_name} ):
    misaal_ll_path = file_name+'_misaal_temp_file.legalize.ll'
    with tvm.transform.PassContext(instruments=[], config={
        'codegen_debug':False, 
        'misaal':True,
        'disable_misaal_compile': False,
        'misaal_benchmark_name':file_name,
        'misaal_ll_path':misaal_ll_path} ):
        ex = relax.build(mod, target)

    device = tvm.cpu()
    vm = relax.VirtualMachine(ex, device)

    max_val = np.iinfo(np.dtype(dtype)).max
    min_val = np.iinfo(np.dtype(dtype)).min
    data_a = np.random.randint(min_val,max_val,(1, buffer_size)).astype(dtype)
    data_b = np.random.randint(min_val,max_val,(1, buffer_size)).astype(dtype)
    tvm_data_a = tvm.nd.array(data_a, device=device)
    tvm_data_b = tvm.nd.array(data_b, device=device)
    tvm_result = vm["forward"](tvm_data_a, tvm_data_b).numpy()
    numpy_result = numpy_op(data_a, data_b)

    if (print_result):
        print("data_a")
        print(data_a)
        print("data_b")
        print(data_b)
        print("numpy_result")
        print(numpy_result)
        print("tvm_result")
        print(tvm_result)
        print("tvm and numpy equality: ", np.array_equal(tvm_result,numpy_result))

    if do_cleanup:
        cleanup(file_name)
    assert np.array_equal(tvm_result, numpy_result)

def cast_op(file_name, input_dtype, output_dtype, buffer_size, vector_size, Module, numpy_op, print_result, do_cleanup=True):
    mod = Module
    # target = tvm.target.Target("llvm -mcpu=alderlake -mattr=+avx2 -num-cores=14")
    target = tvm.target.Target("llvm -mcpu=skylake-avx512 -mattr=+avx512f,+avx512dq,+avx512cd,+avx512bw,+avx512vl -num-cores=64")

    # with tvm.transform.PassContext(instruments=[], config={'codegen_debug':False, 'misaal':True,'misaal_s_exp_path':file_name} ):
    misaal_ll_path = file_name+'_misaal_temp_file.legalize.ll'
    with tvm.transform.PassContext(instruments=[], config={
        'codegen_debug':False, 
        'misaal':True,
        'disable_misaal_compile': False,
        'misaal_benchmark_name':file_name,
        'misaal_ll_path':misaal_ll_path} ):
        ex = relax.build(mod, target)

    device = tvm.cpu()
    vm = relax.VirtualMachine(ex, device)

    max_val = np.iinfo(np.dtype(input_dtype)).max
    min_val = np.iinfo(np.dtype(input_dtype)).min
    data_a = np.random.randint(min_val,max_val,(1, buffer_size)).astype(input_dtype)
    tvm_data_a = tvm.nd.array(data_a, device=device)
    tvm_result = vm["forward"](tvm_data_a).numpy()
    numpy_result = numpy_op(data_a)

    if (print_result):
        print("data_a")
        print(data_a)
        print("numpy_result")
        print(numpy_result)
        print("tvm_result")
        print(tvm_result)
        print("tvm and numpy equality: ", np.array_equal(tvm_result,numpy_result))

    if do_cleanup:
        cleanup(file_name)
    assert np.array_equal(tvm_result, numpy_result)