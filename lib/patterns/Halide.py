from compiler.HydrideCompiler import HydrideCompiler
from compiler.Pattern import Pattern, parse_pattern_from_string
#from sema.halide_sema import halide_semantics
from sema.halide_decomposed import halide_decomposed as  halide_semantics
from common.DSLParser import parse_dict
from utils.ReadDSL import read_string_to_dsl
import os
import json
import pickle


from patterns.PatternUtils import create_patterns, deduplicate_patterns, prune_redundant_patterns, deduplicate_patterns_parallel

halide_dsl_list = parse_dict(halide_semantics)


combined_dsl_list = halide_dsl_list

test_files = [
    "/home/arnoor2/MISAAL/targets/halide/tmpHalideEnum_halide-swizzles_intermediate_results.py",
    "/home/arnoor2/MISAAL/targets/halide/EnumeratePattern_halide-enumerate_intermediate_results.py",
]


props = [
]

for tf in test_files:
    with open(tf, "r") as ReadFile:
        props.append(json.load(ReadFile))

pickle_file_name = "/home/arnoor2/MISAAL/lib/patterns/halide.pickle"

Halide_patterns = []

if os.path.exists(pickle_file_name):
    with open(pickle_file_name, "rb") as handle:
        Halide_patterns = pickle.load(handle)
    print("Found existing pattern pickle file", pickle_file_name)
    print("Read {} patterns".format(len(Halide_patterns)))
else:
    parsed_patterns = create_patterns(props, combined_dsl_list)
    Halide_patterns =  parsed_patterns

    print("Total Patterns Pre Deduplication:", len(Halide_patterns))
    Halide_patterns = prune_redundant_patterns(Halide_patterns, combined_dsl_list)
    print("Total Patterns After Removing redundant patterns:", len(Halide_patterns))
    Halide_patterns = deduplicate_patterns(Halide_patterns)

    print("Total Patterns Post Deduplication:", len(Halide_patterns))

    with open(pickle_file_name, "wb") as handle:
        pickle.dump(Halide_patterns, handle, protocol=pickle.HIGHEST_PROTOCOL)
