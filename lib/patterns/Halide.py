from compiler.HydrideCompiler import HydrideCompiler
from compiler.Pattern import Pattern, parse_pattern_from_string
from sema.halide_sema import halide_semantics
from common.DSLParser import parse_dict
from utils.ReadDSL import read_string_to_dsl
import os
import json

from patterns.PatternUtils import create_patterns, deduplicate_patterns

halide_dsl_list = parse_dict(halide_semantics)


combined_dsl_list = halide_dsl_list

test_files = [
    "/home/arnoor2/MISAAL/lib/EqClassEqualDepthV4_halide_intermediate_results.py",

              ]


props = [
]

for tf in test_files:
    with open(tf, "r") as ReadFile:
        props.append(json.load(ReadFile))

parsed_patterns = create_patterns(props, combined_dsl_list)





Halide_patterns =  parsed_patterns

print("Total Patterns Pre Deduplication:", len(Halide_patterns))
Halide_patterns = deduplicate_patterns(Halide_patterns)

print("Total Patterns Post Deduplication:", len(Halide_patterns))
