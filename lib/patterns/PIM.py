from compiler.HydrideCompiler import HydrideCompiler
from compiler.Pattern import Pattern, parse_pattern_from_string
#from sema.halide_folded_full import halide_folded_full as halide_semantics
#from sema.bitserial_fused_sema import bitserial_fused_sema
#from sema.pim_extend_dsl import pim_extended_dsl as bitserial_fused_sema
from sema.halide_full_pim import  halide_semantics
from sema.bitserial_fused_sema_v2 import bitserial_fused_sema_v2 as bitserial_fused_sema
from common.DSLParser import parse_dict
from utils.ReadDSL import read_string_to_dsl
import os
import json
import pickle

from patterns.PatternUtils import create_patterns, deduplicate_patterns, PatternAbstractor, simplify_double_division, remove_invalid_patterns

halide_dsl_list = parse_dict(halide_semantics, keep_duplicate = True)
pim_dsl_list = parse_dict(bitserial_fused_sema)


MISAAL_ROOT = os.getenv('MISAAL_SRC')

combined_dsl_list = halide_dsl_list + pim_dsl_list


props = []

if False:

    test_files = [
        MISAAL_ROOT+"/targets/pim_fused/EnumeratePattern_pim_d1_pim_fused-enumerate_d1_intermediate_results.py",
        MISAAL_ROOT+"/targets/pim_fused/EnumeratePattern_pim_construction_pim_fused-enumerate_construction_intermediate_results.py",
        MISAAL_ROOT+"/targets/pim_fused/EnumeratePattern_pim_self_to_self_pim_fused-enumerate_self_intermediate_results.py",
        MISAAL_ROOT+"/targets/pim_fused/EnumeratePattern_pim_extra_construct_pim_fused-enumerate_self_intermediate_results.py",
    ]

    pickle_file_name = MISAAL_ROOT+ "/lib/patterns/bitserial_fused.pickle"
    abstract_pickle_file_name = MISAAL_ROOT+ "/lib/patterns/bitserial_fused_abstract.pickle"
    simplified_pickle_file_name = MISAAL_ROOT+ "/lib/patterns/bitserial_fused_abstract_simplified.pickle"

else:

    pim_dir = f"{MISAAL_ROOT}/targets/pim_fused/"

    test_files = [
        f"{pim_dir}/EnumeratePattern_pim_bi_map_v2_pim_fused-enumerate_self_intermediate_results.py",
        #f"{pim_dir}/EnumeratePattern_pim_construct_v2_pim_fused-enumerate_self_intermediate_results.py",
        f"{pim_dir}/EnumeratePattern_pim_self_to_self_v2_pim_fused-enumerate_self_intermediate_results.py",
        f"{pim_dir}/EnumeratePattern_pim_construction_v2_select_fix_pim_fused-enumerate_self_intermediate_results.py",
    ]

    pickle_file_name = MISAAL_ROOT+ "/lib/patterns/bitserial_fused_v2_fix.pickle"
    abstract_pickle_file_name = MISAAL_ROOT+ "/lib/patterns/bitserial_fused_abstract_v2_fix.pickle"
    simplified_pickle_file_name = MISAAL_ROOT+ "/lib/patterns/bitserial_fused_abstract_simplified_v2_fix.pickle"


    #pickle_file_name = MISAAL_ROOT+ "/lib/patterns/bitserial_fused_v2.pickle"
    #abstract_pickle_file_name = MISAAL_ROOT+ "/lib/patterns/bitserial_fused_abstract_v2.pickle"
    #simplified_pickle_file_name = MISAAL_ROOT+ "/lib/patterns/bitserial_fused_abstract_simplified_v2.pickle"







pim_patterns = []

if os.path.exists(simplified_pickle_file_name):
    print("Found existing pattern pickle file", simplified_pickle_file_name)
    with open(simplified_pickle_file_name, "rb") as handle:
        pim_patterns = pickle.load(handle)
    print("Read {} patterns".format(len(pim_patterns)))

elif os.path.exists(abstract_pickle_file_name):
    print("Found existing pattern pickle file", abstract_pickle_file_name)
    with open(abstract_pickle_file_name, "rb") as handle:
        pim_patterns = pickle.load(handle)
    print("Read {} patterns".format(len(pim_patterns)))
    if False:
        for pat in pim_patterns:
            pat.print_pattern()
elif os.path.exists(pickle_file_name):
    print("Found existing pattern pickle file", pickle_file_name)
    with open(pickle_file_name, "rb") as handle:
        pim_patterns = pickle.load(handle)
    print("Read {} patterns".format(len(pim_patterns)))

    print("Abstracting patterns!")

    abstractor = PatternAbstractor(pim_patterns, combined_dsl_list, examples_limit = 16, target = "pim")
    abstracted_patterns = abstractor.abstract_patterns(pim_patterns, combined_dsl_list)
    with open(abstract_pickle_file_name, "wb") as handle:
        pickle.dump(abstracted_patterns, handle, protocol=pickle.HIGHEST_PROTOCOL)
else:
    print("Creating new pattern files")
    for tf in test_files:
        with open(tf, "r") as ReadFile:
            props.append(json.load(ReadFile))

    parsed_patterns = create_patterns(props, combined_dsl_list)
    pim_patterns =  parsed_patterns

    print("Total Patterns Pre Deduplication:", len(pim_patterns))
    pim_patterns = deduplicate_patterns(pim_patterns)

    print("Total Patterns Post Deduplication:", len(pim_patterns))

    with open(pickle_file_name, "wb") as handle:
        pickle.dump(pim_patterns, handle, protocol=pickle.HIGHEST_PROTOCOL)




SIMPLIFY=False

if SIMPLIFY:
    pim_patterns = simplify_double_division(pim_patterns)
    pim_patterns = remove_invalid_patterns(pim_patterns)
    with open(simplified_pickle_file_name, "wb") as handle:
        pickle.dump(pim_patterns, handle, protocol=pickle.HIGHEST_PROTOCOL)

