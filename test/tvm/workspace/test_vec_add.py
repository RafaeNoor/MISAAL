import tvm
from tvm import relax
from tvm.relax.frontend import nn
from tvm.ir.instrument import PrintAfterAll, PrintBeforeAll
from tvm import transform
from tvm.tir.build import codegen_build
from tvm.script import ir as I
from tvm.script import tir as T
from tvm.script import relax as R

import numpy as np
import pytest
import os

@I.ir_module
class Module:
    @T.prim_func(private=True)
    def vec_add(x: T.Buffer((T.int64(1), T.int64(128)), "int16"), y: T.Buffer((T.int64(1), T.int64(128)), "int16"), T_add_intermediate_1: T.Buffer((T.int64(1), T.int64(128)), "bool")):
        T.func_attr({"op_pattern": 0, "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_fused_0_ax0_ax1_fused_1_fused_0 in T.parallel(T.int64(32)):
            for ax0_ax1_fused_0_ax0_ax1_fused_1_fused_1 in T.vectorized(T.int64(4)):
                with T.block("T_add_1"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(4), ax0_ax1_fused_0_ax0_ax1_fused_1_fused_0 * T.int64(4) + ax0_ax1_fused_0_ax0_ax1_fused_1_fused_1)
                    T.reads(x[v_ax0, v_ax1], y[v_ax0, v_ax1])
                    T.writes(T_add_intermediate_1[v_ax0, v_ax1])
                    T_add_intermediate_1[v_ax0, v_ax1] = x[v_ax0, v_ax1] + y[v_ax0, v_ax1]

    @R.function
    def forward(x: R.Tensor((1, 128), dtype="int16"), y: R.Tensor((1, 128), dtype="int16")) -> R.Tensor((1, 128), dtype="bool"):
        R.func_attr({"num_input": 2})
        cls = Module
        with R.dataflow():
            gv = R.call_tir(cls.vec_add, (x, y), out_sinfo=R.Tensor((1, 128), dtype="bool"))
            R.output(gv)
        return gv


mod = Module
target = tvm.target.Target("llvm -mcpu=alderlake -mattr=+avx2 -num-cores=14")

file_name= __file__[:-3]
## with tvm.transform.PassContext(instruments=[], config={'codegen_debug':False, 'misaal':True,'misaal_s_exp_path':file_name} ):
with tvm.transform.PassContext(instruments=[], config={
    'codegen_debug':False, 
    'misaal':True,
    'misaal_benchmark_name':file_name,
    'misaal_ll_path':'test_vec_add_misaal_temp_file.legalize.ll'} ):
    ex = relax.build(mod, target)

device = tvm.cpu()
vm = relax.VirtualMachine(ex, device)

data_a = np.random.rand(1, 128).astype("int16")
data_b = np.random.rand(1, 128).astype("int16")
tvm_data_a = tvm.nd.array(data_a, device=device)
tvm_data_b = tvm.nd.array(data_b, device=device)
tvm_result = vm["forward"](tvm_data_a, tvm_data_b).numpy()
print(tvm_result)
# numpy_result = data_a + data_b

# print("tvm and numpy equality: ", np.array_equal(tvm_result,numpy_result))
