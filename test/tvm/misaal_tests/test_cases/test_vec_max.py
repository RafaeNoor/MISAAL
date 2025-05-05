import tvm
from tvm import relax
from tvm.relax.frontend import nn
from tvm.ir.instrument import PrintAfterAll, PrintBeforeAll
from tvm import transform
from tvm.tir.build import codegen_build
from tvm.script import ir as I
from tvm.script import tir as T
from tvm.script import relax as R

from runner import simple_op

import numpy as np
import os

dtype = "int32"
buffer_size = 128
vector_size = 8
numpy_op = lambda x,y : np.max([x, y], axis=0)


@I.ir_module
class Module:
    @T.prim_func(private=True)
    def vec_compute(x: T.Buffer((T.int64(1), T.int64(buffer_size)), dtype), y: T.Buffer((T.int64(1), T.int64(buffer_size)), dtype), T_add_intermediate_1: T.Buffer((T.int64(1), T.int64(buffer_size)), dtype)):
        T.func_attr({"op_pattern": 0, "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_fused_0_ax0_ax1_fused_1_fused_0 in T.parallel(T.int64(buffer_size/vector_size)):
            for ax0_ax1_fused_0_ax0_ax1_fused_1_fused_1 in T.vectorized(T.int64(vector_size)):
                with T.block("T_add_1"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(vector_size), ax0_ax1_fused_0_ax0_ax1_fused_1_fused_0 * T.int64(vector_size) + ax0_ax1_fused_0_ax0_ax1_fused_1_fused_1)
                    T.reads(x[v_ax0, v_ax1], y[v_ax0, v_ax1])
                    T.writes(T_add_intermediate_1[v_ax0, v_ax1])
                    T_add_intermediate_1[v_ax0, v_ax1] = T.Max(x[v_ax0, v_ax1], y[v_ax0, v_ax1])

    @R.function
    def forward(x: R.Tensor((1, buffer_size), dtype=dtype), y: R.Tensor((1, buffer_size), dtype=dtype)) -> R.Tensor((1, buffer_size), dtype=dtype):
        R.func_attr({"num_input": 2})
        cls = Module
        with R.dataflow():
            gv = R.call_tir(cls.vec_compute, (x, y), out_sinfo=R.Tensor((1, buffer_size), dtype=dtype))
            R.output(gv)
        return gv

def test_simple_vec_max():
    simple_op(file_name = __file__[:-3], dtype=dtype, buffer_size=buffer_size, vector_size=vector_size, Module=Module, numpy_op= numpy_op, print_result=False)


if __name__ == "__main__":
    simple_op(file_name = __file__[:-3], dtype=dtype, buffer_size=buffer_size, vector_size=vector_size, Module=Module, numpy_op= numpy_op, print_result=True)