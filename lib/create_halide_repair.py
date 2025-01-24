
from properties.EqClassEqualDepthV4 import EqClassEqualDepthV4
from sema.hexsemantics_new import semantics as hvx_semantics
from sema.hvx_swizzles_decomposed import hvx_swizzles_decomposed as hvx_swizzles
from sema.halide_sema import halide_semantics
from utils.CodeSynthesizerDesc import X86_SYNTH_DESC, HVX_SYNTH_DESC, HALIDE_HVX_SYNTH_DESC,ARM_SYNTH_DESC, create_synth_desc, HALIDE_SYNTH_DESC
from common.DSLParser import parse_dict
import json
import time
from sema.x86_swizzles_decomposed import x86_swizzles_decomposed as  x86_swizzles
from sema.x86SemanticsAllArgs import semantcs as x86_semantics
from sema.ARMSema import arm_semantics
from arm_swizzles_decomposed import arm_swizzles_decomposed as arm_swizzles
from utils.DSLInstructionUtils import *
import sys

from utils.RepairPostProcessUtils import create_repair_identity_map, create_repair_swizzle_map
from utils.SwizzleUtils import create_swizzle_identity_map

halide_dsl_list = parse_dict(halide_semantics)
x86_dsl_list = parse_dict(x86_semantics)
x86_swizzle_dsl_list = parse_dict(x86_swizzles)

hvx_dsl_list = parse_dict(hvx_semantics)
hvx_swizzle_dsl_list = parse_dict(hvx_swizzles)

arm_dsl_list = parse_dict(arm_semantics)
arm_swizzle_dsl_list = parse_dict(arm_swizzles)

test_dsl_list = []
test_swizzle_dsl_list = []

TARGET = "arm"

if TARGET == "x86":
    test_dsl_list = x86_dsl_list
    test_swizzle_dsl_list = x86_swizzle_dsl_list
elif TARGET == "hvx":
    test_dsl_list = hvx_dsl_list
    test_swizzle_dsl_list = hvx_swizzle_dsl_list
elif TARGET == "arm":
    test_dsl_list = arm_dsl_list
    test_swizzle_dsl_list = arm_swizzle_dsl_list

map_ = create_repair_swizzle_map(test_dsl_list, test_swizzle_dsl_list)

print(json.dumps(map_, indent = 4))

