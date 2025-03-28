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

def test_vec_add_int64():
    vec_sizes = [2,4,8,16,32,64]
    for vs in vec_sizes:
        @I.ir_module
        class Module:
            @T.prim_func(private=True)
            def vec_add(x: T.Buffer((T.int64(1), T.int64(128)), "int64"), y: T.Buffer((T.int64(1), T.int64(128)), "int64"), T_add_intermediate_1: T.Buffer((T.int64(1), T.int64(128)), "int64")):
                T.func_attr({"op_pattern": 0, "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
                # with T.block("root"):
                for ax0_ax1_fused_0_ax0_ax1_fused_1_fused_0 in T.parallel(T.int64(3)):
                    for ax0_ax1_fused_0_ax0_ax1_fused_1_fused_1 in T.vectorized(T.int64(vs)):
                        with T.block("T_add_1"):
                            v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                            v_ax1 = T.axis.spatial(T.int64(128), ax0_ax1_fused_0_ax0_ax1_fused_1_fused_0 * T.int64(64) + ax0_ax1_fused_0_ax0_ax1_fused_1_fused_1)
                            T.reads(x[v_ax0, v_ax1], y[v_ax0, v_ax1])
                            T.writes(T_add_intermediate_1[v_ax0, v_ax1])
                            T_add_intermediate_1[v_ax0, v_ax1] = x[v_ax0, v_ax1] + y[v_ax0, v_ax1]

            @R.function
            def forward(x: R.Tensor((1, 128), dtype="int64"), y: R.Tensor((1, 128), dtype="int64")) -> R.Tensor((1, 128), dtype="int64"):
                R.func_attr({"num_input": 2})
                cls = Module
                with R.dataflow():
                    gv = R.call_tir(cls.vec_add, (x, y), out_sinfo=R.Tensor((1, 128), dtype="int64"))
                    R.output(gv)
                return gv
        mod = Module
        answer_str = f"""
==
misaal_func_0:
("vec-add"
arg_2
arg_1
64
{64*vs}
1)"""
        runner(Module, answer_str)