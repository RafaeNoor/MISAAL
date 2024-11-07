from compiler.HydrideCompiler import HydrideCompiler
from compiler.Pattern import Pattern, parse_pattern_from_string
from sema.ARMSema import arm_semantics as arm_semantics
#from sema.halide_sema import halide_semantics
from sema.halide_decomposed import halide_decomposed as halide_semantics
from sema.arm_swizzles_decomposed import arm_swizzles_decomposed as arm_swizzles
from common.DSLParser import parse_dict
from utils.ReadDSL import read_string_to_dsl
import os
import json
import pickle

from patterns.PatternUtils import create_patterns, deduplicate_patterns

halide_dsl_list = parse_dict(halide_semantics)
arm_dsl_list = parse_dict(arm_semantics)
arm_swizzles_dsl_list = parse_dict(arm_swizzles)


MISAAL_ROOT = os.getenv('MISAAL_SRC')

combined_dsl_list = halide_dsl_list +arm_dsl_list + arm_swizzles_dsl_list

test_files = [
    MISAAL_ROOT+"/targets/arm/EnumeratePattern_arm-enumerate_intermediate_results.py",
]


props = [
]



pickle_file_name = MISAAL_ROOT+ "/lib/patterns/arm.pickle"

arm_patterns = []

if os.path.exists(pickle_file_name):
    print("Found existing pattern pickle file", pickle_file_name)
    with open(pickle_file_name, "rb") as handle:
        arm_patterns = pickle.load(handle)
    print("Read {} patterns".format(len(arm_patterns)))
else:
    print("Creating new pattern files")
    for tf in test_files:
        with open(tf, "r") as ReadFile:
            props.append(json.load(ReadFile))

    parsed_patterns = create_patterns(props, combined_dsl_list)
    arm_patterns =  parsed_patterns

    print("Total Patterns Pre Deduplication:", len(arm_patterns))
    arm_patterns = deduplicate_patterns(arm_patterns)

    print("Total Patterns Post Deduplication:", len(arm_patterns))

    with open(pickle_file_name, "wb") as handle:
        pickle.dump(arm_patterns, handle, protocol=pickle.HIGHEST_PROTOCOL)