from sema.arm_swizzles_decomposed import arm_swizzles_decomposed as arm_swizzles
from sema.ARMSema import arm_semantics
from sema.halide_sema import halide_semantics
from utils.CodeSynthesizerDesc import X86_SYNTH_DESC, HVX_SYNTH_DESC, HALIDE_HVX_SYNTH_DESC,ARM_SYNTH_DESC, create_synth_desc, HALIDE_SYNTH_DESC
from common.DSLParser import parse_dict
from properties.EnumeratePattern import EnumeratePattern
from properties.EqClassEqualDepthV4 import EqClassEqualDepthV4
from sema.hexsemantics_new import semantics as hvx_semantics
from sema.hvx_swizzles_decomposed import hvx_swizzles_decomposed as hvx_swizzles
from utils.ReadDSL import read_string_to_dsl
from utils.DSLInstructionUtils import *

import json

halide_dsl_list = parse_dict(halide_semantics)
hvx_dsl_list = parse_dict(hvx_semantics)
hvx_swizzles_dsl_list =  parse_dict(hvx_swizzles)

combined_list = halide_dsl_list + hvx_dsl_list + hvx_swizzles_dsl_list


def process_test_expr(expr_str):
    expr =  read_string_to_dsl(expr_str, combined_list)
    return  is_expression_constant(expr, combined_list)



test_expressions = [
    "(typed:cast-int (lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 512)) 8 1 64 16)",
    "(hexagon_V6_vmpyieoh_128B_dsl (lit (bv #x00000010 32)) (hexagon_V6_vmpyieoh_128B_dsl (lit (bv #x00000010 32)) (reg (bv #x01 8)) (reg (bv #x02 8)) 1024 1024 0 512 16 32 1 1 1 16 0) (hexagon_V6_vmpyieoh_128B_dsl (lit (bv #x00000010 32)) (reg (bv #x00 8)) (reg (bv #x03 8)) 1024 1024 0 512 16 32 1 1 1 16 0) 1024 1024 0 512 16 32 1 1 1 16 0)",
    "(typed:xBroadcast (reg (bv #x00 8)) 16 16 2)",
    "(hexagon_V6_interleave_2_128B_dsl (reg (bv #x00 8)) 16 32)",
]

results = [process_test_expr(expr) for expr in test_expressions]
print(results)


