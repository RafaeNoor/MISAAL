from sema.arm_swizzles_decomposed import arm_swizzles_decomposed as arm_swizzles
from sema.ARMSema import arm_semantics
from sema.halide_sema import halide_semantics
from utils.CodeSynthesizerDesc import X86_SYNTH_DESC, HVX_SYNTH_DESC, HALIDE_HVX_SYNTH_DESC,ARM_SYNTH_DESC, create_synth_desc, HALIDE_SYNTH_DESC
from common.DSLParser import parse_dict
from properties.EnumeratePattern import EnumeratePattern

import json

halide_dsl_list = parse_dict(halide_semantics)
arm_dsl_list = parse_dict(arm_semantics)
arm_swizzle_dsl_list = parse_dict(arm_swizzles, keep_duplicate=True)

combined_dsl_list = halide_dsl_list + arm_dsl_list + arm_swizzle_dsl_list

pattern_file_path = "arm_test_patterns.json"

with open(pattern_file_path, "r") as PatternFile:
    input_patterns = json.load(PatternFile)

prop = EnumeratePattern(dsl_list = combined_dsl_list,  input_patterns_dict = input_patterns)

prop.parallel = False
prop.POOL_SIZE = 2
prop.BATCH_SIZE = 16
prop.notify_enabled = False


property_map = prop.get_property()
