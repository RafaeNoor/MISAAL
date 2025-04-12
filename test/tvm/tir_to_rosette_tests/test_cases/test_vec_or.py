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
    def vec_add(x: T.Buffer((T.int64(1), T.int64(128)), "bool"), y: T.Buffer((T.int64(1), T.int64(128)), "bool"), T_add_intermediate_1: T.Buffer((T.int64(1), T.int64(128)), "bool")):
        T.func_attr({"op_pattern": 0, "tir.is_scheduled": T.bool(True), "tir.noalias": T.bool(True)})
        # with T.block("root"):
        for ax0_ax1_fused_0_ax0_ax1_fused_1_fused_0 in T.parallel(T.int64(2)):
            for ax0_ax1_fused_0_ax0_ax1_fused_1_fused_1 in T.vectorized(T.int64(64)):
                with T.block("T_add_1"):
                    v_ax0 = T.axis.spatial(T.int64(1), T.int64(0))
                    v_ax1 = T.axis.spatial(T.int64(128), ax0_ax1_fused_0_ax0_ax1_fused_1_fused_0 * T.int64(64) + ax0_ax1_fused_0_ax0_ax1_fused_1_fused_1)
                    T.reads(x[v_ax0, v_ax1], y[v_ax0, v_ax1])
                    T.writes(T_add_intermediate_1[v_ax0, v_ax1])
                    T_add_intermediate_1[v_ax0, v_ax1] = T.Or(x[v_ax0, v_ax1], y[v_ax0, v_ax1])

    @R.function
    def forward(x: R.Tensor((1, 128), dtype="bool"), y: R.Tensor((1, 128), dtype="bool")) -> R.Tensor((1, 128), dtype="bool"):
        R.func_attr({"num_input": 2})
        cls = Module
        with R.dataflow():
            gv = R.call_tir(cls.vec_add, (x, y), out_sinfo=R.Tensor((1, 128), dtype="bool"))
            R.output(gv)
        return gv

import pytest

@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    """Fixture to execute asserts before and after a test is run"""
    yield 

    file_name = __file__[:-3] + '_s_exp'
    os.remove(file_name)


def test_simple_vec_add():
    mod = Module
    target = tvm.target.Target("llvm -mcpu=alderlake -mattr=+avx2 -num-cores=14")

    file_name = __file__[:-3] + '_s_exp'
    with tvm.transform.PassContext(instruments=[], config={'codegen_debug':False, 'misaal':True,'misaal_s_exp_path':file_name} ):
        ex = relax.build(mod, target)

    f = open(file_name)
    answer_str = """
==
misaal_func_0:
("vec-or"
arg_2
arg_1
1
64)"""
    f_str = f.read().strip()
    f.close()
    assert f_str == answer_str.strip()