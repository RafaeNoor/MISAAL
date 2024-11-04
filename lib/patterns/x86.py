from compiler.HydrideCompiler import HydrideCompiler
from compiler.Pattern import Pattern, parse_pattern_from_string
from sema.hexsemantics_new import semantics as hvx_semantics
#from sema.halide_sema import halide_semantics
from sema.halide_decomposed import halide_decomposed as halide_semantics
from sema.x86_swizzles_decomposed import x86_swizzles_decomposed as x86_swizzles
from sema.x86SemanticsAllArgs import semantcs as x86_semantics
from common.DSLParser import parse_dict
from utils.ReadDSL import read_string_to_dsl
import os
import json
import pickle

from patterns.PatternUtils import create_patterns, deduplicate_patterns
from EqClassEqualDepthV4_hvx_results import hvx_EqClassEqualDepthV4

halide_dsl_list = parse_dict(halide_semantics)
x86_dsl_list = parse_dict(x86_semantics)
x86_swizzles_dsl_list = parse_dict(x86_swizzles)


MISAAL_ROOT = os.getenv('MISAAL_SRC')

combined_dsl_list = halide_dsl_list +x86_dsl_list + x86_swizzles_dsl_list

test_files = [
    "/home/arnoor2/MISAAL/targets/x86/EnumeratePattern_x86-enumerate_intermediate_results.py",
    "/home/arnoor2/MISAAL/targets/x86/EnumeratePattern_broadcasts_x86-enumerate_intermediate_results.py",
    "/home/arnoor2/MISAAL/targets/x86/EnumeratePattern_x86-casts_intermediate_results.py",
    MISAAL_ROOT+"/targets/x86/EnumeratePattern_x86-divs_intermediate_results.py",
    MISAAL_ROOT+"/targets/x86/EnumeratePattern_assoc_x86-enumerate_intermediate_results.py",
]


props = [
]



pickle_file_name = "/home/arnoor2/MISAAL/lib/patterns/x86.pickle"

x86_patterns = []

if os.path.exists(pickle_file_name):
    print("Found existing pattern pickle file", pickle_file_name)
    with open(pickle_file_name, "rb") as handle:
        x86_patterns = pickle.load(handle)
    print("Read {} patterns".format(len(x86_patterns)))
else:
    print("Creating new pattern files")
    for tf in test_files:
        with open(tf, "r") as ReadFile:
            props.append(json.load(ReadFile))

    parsed_patterns = create_patterns(props, combined_dsl_list)
    x86_patterns =  parsed_patterns

    print("Total Patterns Pre Deduplication:", len(x86_patterns))
    x86_patterns = deduplicate_patterns(x86_patterns)

    print("Total Patterns Post Deduplication:", len(x86_patterns))

    with open(pickle_file_name, "wb") as handle:
        pickle.dump(x86_patterns, handle, protocol=pickle.HIGHEST_PROTOCOL)
