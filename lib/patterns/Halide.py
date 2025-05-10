from compiler.HydrideCompiler import HydrideCompiler
from utils.egg_config import EGG_PKG_PATH
from compiler.Pattern import Pattern, parse_pattern_from_string
#from sema.halide_sema import halide_semantics
from sema.halide_decomposed import halide_decomposed as  halide_semantics
from common.DSLParser import parse_dict
from utils.ReadDSL import read_string_to_dsl
import os
import json
import pickle


from patterns.PatternUtils import create_patterns, deduplicate_patterns, prune_redundant_patterns, deduplicate_patterns_parallel, PatternAbstractor

halide_dsl_list = parse_dict(halide_semantics)


combined_dsl_list = halide_dsl_list

MISAAL_ROOT = os.getenv('MISAAL_SRC')

test_files = [
    MISAAL_ROOT+ "/targets/halide/tmpHalideEnum_halide-swizzles_intermediate_results.py",
    MISAAL_ROOT+"/targets/halide/EnumeratePattern_halide-enumerate_intermediate_results.py",
    MISAAL_ROOT+"/targets/halide/EnumeratePattern_double_broadcast_halide-enumerate_intermediate_results.py",
]


props = [
]

print("Loading Halide json files..")
for tf in test_files:
    with open(tf, "r") as ReadFile:
        props.append(json.load(ReadFile))

pickle_file_name = MISAAL_ROOT+"/lib/patterns/halide.pickle"
#abstract_pickle_file_name = MISAAL_ROOT+"/lib/patterns/halide_abstract.pickle"
abstract_pickle_file_name = MISAAL_ROOT+"/lib/patterns/halide.pickle"

Halide_patterns = []
halide_patterns_intermediate_pickle_file = MISAAL_ROOT+"/lib/patterns/halide_patterns_intermediate.pickle"


if os.path.exists(abstract_pickle_file_name):
    with open(abstract_pickle_file_name, "rb") as handle:
        Halide_patterns = pickle.load(handle)
    print("Found existing pattern pickle file", pickle_file_name)
    print("Read {} patterns".format(len(Halide_patterns)))
elif os.path.exists(pickle_file_name):
    with open(pickle_file_name, "rb") as handle:
        Halide_patterns = pickle.load(handle)
    print("Found existing pattern pickle file", pickle_file_name)
    print("Read {} patterns".format(len(Halide_patterns)))
    abstractor = PatternAbstractor(Halide_patterns, halide_dsl_list, examples_limit = None)
    abstracted_patterns = abstractor.abstract_patterns(Halide_patterns, halide_dsl_list)

    with open(abstract_pickle_file_name, "wb") as handle:
        pickle.dump(abstracted_patterns, handle, protocol=pickle.HIGHEST_PROTOCOL)
else:
    if os.path.exists(halide_patterns_intermediate_pickle_file):
        print("Loading patterns from intermediate pickle file")
        with open(halide_patterns_intermediate_pickle_file, "rb") as handle:
            Halide_patterns = pickle.load(handle)
    else:
        print("Creating patterns..")
        parsed_patterns = create_patterns(props, combined_dsl_list)
        print("Done creating patterns")
        Halide_patterns =  parsed_patterns
        with open(halide_patterns_intermediate_pickle_file, "wb") as handle:
            pickle.dump(Halide_patterns, handle, protocol=pickle.HIGHEST_PROTOCOL)

    print("Total Patterns Pre Deduplication:", len(Halide_patterns))
    Halide_patterns = prune_redundant_patterns(Halide_patterns, combined_dsl_list)
    print("Total Patterns After Removing redundant patterns:", len(Halide_patterns))
    Halide_patterns = deduplicate_patterns(Halide_patterns)

    print("Total Patterns Post Deduplication:", len(Halide_patterns))

    with open(pickle_file_name, "wb") as handle:
        pickle.dump(Halide_patterns, handle, protocol=pickle.HIGHEST_PROTOCOL)
