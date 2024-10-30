from compiler.HydrideCompiler import HydrideCompiler
from compiler.Pattern import Pattern, parse_pattern_from_string
from sema.hexsemantics_new import semantics as hvx_semantics
#from sema.halide_sema import halide_semantics
from sema.halide_decomposed import halide_decomposed as halide_semantics
from sema.hex_swizzles import hvx_swizzles
from common.DSLParser import parse_dict
from utils.ReadDSL import read_string_to_dsl
import os
import json

from patterns.PatternUtils import create_patterns, deduplicate_patterns
from EqClassEqualDepthV4_hvx_results import hvx_EqClassEqualDepthV4

halide_dsl_list = parse_dict(halide_semantics)
hvx_dsl_list = parse_dict(hvx_semantics)
hvx_swizzles_dsl_list = parse_dict(hvx_swizzles)


combined_dsl_list = halide_dsl_list + hvx_dsl_list + hvx_swizzles_dsl_list

test_files = [
    #"/home/arnoor2/MISAAL/lib/EnumeratePattern_hvx_intermediate_results.py",
    "/home/arnoor2/MISAAL/lib/EnumeratePattern_hvx-swizzles_intermediate_results.py",
    "/home/arnoor2/MISAAL/test/property/eq_class_enumeration/hvx/tempEnumxHVX_hvx_intermediate_results.py",
]


props = [
    #hvx_EqClassEqualDepthV4
]

for tf in test_files:
    with open(tf, "r") as ReadFile:
        props.append(json.load(ReadFile))

parsed_patterns = create_patterns(props, combined_dsl_list)


pattern_str_from = """
(typed:vec-add
(reg (bv 0 4))
(reg (bv 1 4))
32
2048
)
"""


pattern_str_to = """
(hexagon_V6_vaddhsat_128B_dsl
(reg (bv 0 4))
(reg (bv 1 4))
2048
2048
0
2048
32
-1
0
)

"""



pattern = parse_pattern_from_string(pattern_str_from, pattern_str_to, halide_dsl_list, hvx_dsl_list, src_language = "halide", target_language = "hvx")
HVX_patterns = [pattern] + parsed_patterns

print("Total Patterns Pre Deduplication:", len(HVX_patterns))
HVX_patterns = deduplicate_patterns(HVX_patterns)

print("Total Patterns Post Deduplication:", len(HVX_patterns))
