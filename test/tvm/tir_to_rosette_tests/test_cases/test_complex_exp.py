import tvm
from tvm import relax
from tvm.relax.frontend import nn
from tvm.ir.instrument import PrintAfterAll, PrintBeforeAll
from tvm import transform
from tvm.tir.build import codegen_build
from tvm.script import ir as I
from tvm.script import tir as T
from tvm.script import relax as R

from utils import runner

def test_complex_function():
    @I.ir_module
    class Module:
        @T.prim_func(private=True)
        def fused_multiply_subtract_multiply_subtract_add_multiply_add(x: T.Buffer((T.int64(1), T.int64(1024)), "uint32"), y: T.Buffer((T.int64(1), T.int64(1024)), "uint32"), T_add_intermediate_1: T.Buffer((T.int64(1), T.int64(1024)), "uint32")):
            T.func_attr({"tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
            # with T.block("root"):
            for ax0_ax1_fused_0 in T.parallel(T.int64(8)):
                for ax0_ax1_fused_1 in T.vectorized(T.int64(128)):
                    with T.block("T_add_1"):
                        v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                        v_ax1 = T.axis.spatial(T.int64(1024), ax0_ax1_fused_0 * T.int64(128) + ax0_ax1_fused_1)
                        T.reads(x[v_ax0, v_ax1], y[v_ax0, v_ax1])
                        T.writes(T_add_intermediate_1[v_ax0, v_ax1])
                        T_add_intermediate_1[v_ax0, v_ax1] = (x[v_ax0, v_ax1] * y[v_ax0, v_ax1] - y[v_ax0, v_ax1]) * y[v_ax0, v_ax1] + (x[v_ax0, v_ax1] * y[v_ax0, v_ax1] - y[v_ax0, v_ax1] - y[v_ax0, v_ax1]) * (x[v_ax0, v_ax1] * y[v_ax0, v_ax1] - y[v_ax0, v_ax1] + y[v_ax0, v_ax1])

        @R.function
        def forward(x: R.Tensor((1, 1024), dtype="uint32"), y: R.Tensor((1, 1024), dtype="uint32")) -> R.Tensor((1, 1024), dtype="uint32"):
            R.func_attr({"num_input": 2})
            cls = Module
            with R.dataflow():
                gv = R.call_tir(cls.fused_multiply_subtract_multiply_subtract_add_multiply_add, (x, y), out_sinfo=R.Tensor((1, 1024), dtype="uint32"))
                R.output(gv)
            return gv
    answer_str = """
==
misaal_func_0:
("vec-add"
("vec-mul"
("vec-sub"
("vec-mul"
arg_12
arg_11
32
4096
0)
arg_10
32
4096
0)
arg_9
32
4096
0)
("vec-mul"
("vec-sub"
("vec-sub"
("vec-mul"
arg_8
arg_7
32
4096
0)
arg_6
32
4096
0)
arg_5
32
4096
0)
("vec-add"
("vec-sub"
("vec-mul"
arg_4
arg_3
32
4096
0)
arg_2
32
4096
0)
arg_1
32
4096
0)
32
4096
0)
32
4096
0)"""
    runner(Module, answer_str)