from compiler.HydrideCompiler import HydrideCompiler
from utils.egg_config import EGG_PKG_PATH
from compiler.Pattern import Pattern, parse_pattern_from_string
#from sema.halide_sema import halide_semantics
# from sema.halide_decomposed import halide_decomposed as  halide_semantics
from sema.tvm_folded import tvm_folded as tvm_semantics
from sema.x86_swizzles_decomposed import x86_swizzles_decomposed as x86_swizzles
from sema.x86SemanticsAllArgs import semantcs as x86_semantics
from common.DSLParser import parse_dict
from utils.ReadDSL import read_string_to_dsl
import os
import json
import pickle


from patterns.PatternUtils import create_patterns, deduplicate_patterns, prune_redundant_patterns, deduplicate_patterns_parallel, PatternAbstractor

tvm_dsl_list = parse_dict(tvm_semantics)
x86_dsl_list = parse_dict(x86_semantics)
x86_swizzles_dsl_list = parse_dict(x86_swizzles)

combined_dsl_list = tvm_dsl_list + x86_dsl_list + x86_swizzles_dsl_list

MISAAL_ROOT = os.getenv('MISAAL_SRC')

test_files = [
    MISAAL_ROOT+ "/targets/tvm/depth_2_new_seman/EnumeratePattern_x86-swizzles_intermediate_results.py",
]


props = [
]

for tf in test_files:
    with open(tf, "r") as ReadFile:
        props.append(json.load(ReadFile))

pickle_file_name = MISAAL_ROOT+"/lib/patterns/tvm.pickle"
# abstract_pickle_file_name = MISAAL_ROOT+"/lib/patterns/halide_abstract.pickle"
# abstract_pickle_file_name = MISAAL_ROOT+"/lib/patterns/tvm_abstract.pickle"
# Don't use the abstract pickle for now, it has errors
abstract_pickle_file_name = MISAAL_ROOT+"/lib/patterns/tvm.pickle"

TVM_patterns = []


if os.path.exists(abstract_pickle_file_name):
    with open(abstract_pickle_file_name, "rb") as handle:
        TVM_patterns = pickle.load(handle)
    print("Found existing pattern pickle file", pickle_file_name)
    print("Read {} patterns".format(len(TVM_patterns)))
elif os.path.exists(pickle_file_name):
    with open(pickle_file_name, "rb") as handle:
        TVM_patterns = pickle.load(handle)
    print("Found existing pattern pickle file", pickle_file_name)
    print("Read {} patterns".format(len(TVM_patterns)))
    abstractor = PatternAbstractor(TVM_patterns, tvm_dsl_list, examples_limit = None)
    abstracted_patterns = abstractor.abstract_patterns(TVM_patterns, tvm_dsl_list)

    with open(abstract_pickle_file_name, "wb") as handle:
        pickle.dump(abstracted_patterns, handle, protocol=pickle.HIGHEST_PROTOCOL)
else:
    parsed_patterns = create_patterns(props, combined_dsl_list)
    TVM_patterns =  parsed_patterns

    print("Total Patterns Pre Deduplication:", len(TVM_patterns))
    TVM_patterns = prune_redundant_patterns(TVM_patterns, combined_dsl_list)
    print("Total Patterns After Removing redundant patterns:", len(TVM_patterns))
    TVM_patterns = deduplicate_patterns(TVM_patterns)

    print("Total Patterns Post Deduplication:", len(TVM_patterns))

    with open(pickle_file_name, "wb") as handle:
        pickle.dump(TVM_patterns, handle, protocol=pickle.HIGHEST_PROTOCOL)

# with open(pickle_file_name, "rb") as handle:
#     TVM_patterns = pickle.load(handle)