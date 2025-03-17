from compiler.HydrideCompiler import HydrideCompiler
from compiler.Pattern import Pattern, parse_pattern_from_string
from sema.hexsemantics_new import semantics as hvx_semantics
#from sema.halide_sema import halide_semantics
from sema.halide_decomposed import halide_decomposed as halide_semantics
from sema.hex_swizzles import hvx_swizzles
from common.DSLParser import parse_dict
from utils.ReadDSL import read_string_to_dsl
from utils.DSLInstructionUtils import parse_dict_with_bounded
import os
import json
import pickle

from patterns.PatternUtils import create_patterns, deduplicate_patterns, prune_redundant_patterns, deduplicate_patterns_parallel, PatternAbstractor
from EqClassEqualDepthV4_hvx_results import hvx_EqClassEqualDepthV4

halide_dsl_list = parse_dict(halide_semantics)
hvx_dsl_list = parse_dict_with_bounded(hvx_semantics)
hvx_swizzles_dsl_list = parse_dict(hvx_swizzles)


combined_dsl_list = halide_dsl_list + hvx_dsl_list + hvx_swizzles_dsl_list

test_files = [
    #"/home/arnoor2/MISAAL/lib/EnumeratePattern_hvx-swizzles_intermediate_results.py",
    "/home/arnoor2/MISAAL/targets/hvx/EnumeratePattern_hvx_acc_hvx-enumerate_intermediate_results.py",
    "/home/arnoor2/MISAAL/targets/hvx/EnumeratePattern_hvx_vmpyh_hvx-enumerate_intermediate_results.py",
    "/home/arnoor2/MISAAL/targets/hvx/EnumeratePatternhvx_swizzle_transfer_hvx-enumerate_intermediate_results.py",
    "/home/arnoor2/MISAAL/targets/hvx/EnumeratePatternhvx_rmpy_hvx-enumerate_intermediate_results.py",
    "/home/arnoor2/MISAAL/targets/hvx/RoundMulShiftRightPatterns.py",
    "/home/arnoor2/MISAAL/targets/hvx/LowerSwizzles_filtered_hvx_intermediate_results.py",
    "/home/arnoor2/MISAAL/test/property/eq_class_enumeration/hvx/tempEnumxHVX_hvx_intermediate_results.py",
    "/home/arnoor2/MISAAL/targets/hvx/EnumeratePattern_hvx-enumerate_intermediate_results.py",
    "/home/arnoor2/MISAAL/targets/hvx/EnumeratePattern_scalar_widen_hvx-enumerate_intermediate_results.py",
    "/home/arnoor2/MISAAL/targets/hvx/EnumeratePattern_shift_right_hvx-enumerate_intermediate_results.py",
    "/home/arnoor2/MISAAL/targets/hvx/EnumeratePattern_shift_right_w_hvx-enumerate_intermediate_results.py",
    "/home/arnoor2/MISAAL/targets/hvx/EnumeratePattern_hvx-enumerate-absd_intermediate_results.py",
    "/home/arnoor2/MISAAL/targets/hvx/EnumeratePattern_avgrnd_hvx-enumerate-absd_intermediate_results.py",
    "/home/arnoor2/MISAAL/targets/hvx/LowerSwizzles_hvx_swizzle_hvx_intermediate_results_addon.py",
    "/home/arnoor2/MISAAL/targets/hvx/EqClassEqualDepthV4_hvx_combine_simpl_hvx_intermediate_results.py",
    "/home/arnoor2/MISAAL/targets/hvx/EnumeratePattern_shift_left_scalar_hvx-enumerate-absd_intermediate_results.py",
    "/home/arnoor2/MISAAL/targets/hvx/EnumeratePattern_shift_left_acc_hvx-enumerate-absd_intermediate_results.py",
    "/home/arnoor2/MISAAL/targets/hvx/EnumeratePattern_hvx_sat_hvx-enumerate_intermediate_results.py",
    "/home/arnoor2/MISAAL/targets/hvx/EqClassEqualDepthV4_asrh_acc_hvx_intermediate_results.py",
    "/home/arnoor2/MISAAL/targets/hvx/EqClassEqualDepthV4_interleave_2_hvx_intermediate_results.py",
]

props = [
]



pickle_file_name = "/home/arnoor2/MISAAL/lib/patterns/hvx.pickle"
#abstract_pickle_file_name = "/home/arnoor2/MISAAL/lib/patterns/hvx_abstract.pickle"
abstract_pickle_file_name = "/home/arnoor2/MISAAL/lib/patterns/hvx.pickle"

HVX_patterns = []

if os.path.exists(abstract_pickle_file_name):
    print("Found existing abstract pattern pickle file", abstract_pickle_file_name)
    with open(abstract_pickle_file_name, "rb") as handle:
        HVX_patterns = pickle.load(handle)
    print("Read {} patterns".format(len(HVX_patterns)))

elif os.path.exists(pickle_file_name):
    print("Found existing pattern pickle file", pickle_file_name)
    with open(pickle_file_name, "rb") as handle:
        HVX_patterns = pickle.load(handle)
    print("Read {} patterns".format(len(HVX_patterns)))

    abstractor = PatternAbstractor(HVX_patterns, combined_dsl_list, examples_limit = 16, target = "hvx")
    abstracted_patterns = abstractor.abstract_patterns(HVX_patterns, combined_dsl_list)
    with open(abstract_pickle_file_name, "wb") as handle:
        pickle.dump(abstracted_patterns, handle, protocol=pickle.HIGHEST_PROTOCOL)
else:
    for tf in test_files:
        print(tf)
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

    HVX_patterns = prune_redundant_patterns(HVX_patterns, combined_dsl_list)
    print("Total Patterns After Removing redundant patterns:", len(HVX_patterns))
    HVX_patterns = deduplicate_patterns(HVX_patterns)

    print("Total Patterns Post Deduplication:", len(HVX_patterns))

    with open(pickle_file_name, "wb") as handle:
        pickle.dump(HVX_patterns, handle, protocol=pickle.HIGHEST_PROTOCOL)
