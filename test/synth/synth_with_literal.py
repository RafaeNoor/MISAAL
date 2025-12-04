import argparse
from common.Types import *
import json
import sys
import os

from common.DSLParser import parse_dict
from utils.CodeSynthesizerDesc import X86_SYNTH_DESC, HVX_SYNTH_DESC, HALIDE_HVX_SYNTH_DESC,ARM_SYNTH_DESC, create_synth_desc, HALIDE_SYNTH_DESC, HALIDE_X86_SYNTH_DESC
from sema.halide_decomposed import halide_decomposed  as halide_semantics

from properties.EqClassEqualDepthV4Full import EqClassEqualDepthV4Full
from properties.EnumeratePattern import EnumeratePattern
from utils.EnumerateUtils import create_exhaustive_expressions_generator_v2
from utils.EggLogUtils import emit_expr_to_egg
from utils.LiteralHole import legalize_concrete_literal_holes, LiteralHole

from compiler.Pattern import Pattern, parse_pattern_from_string
from compiler.HydrideCompiler import HydrideCompiler
from patterns.PatternUtils import create_patterns, deduplicate_patterns, PatternAbstractor


halide_dsl_list = parse_dict(halide_semantics)

# Focus on halide subset
halide_subset = ["shl", "unsigned-vec-mul"]
halide_dsl_list = [d for d in halide_dsl_list if any([substr in d.name for substr in halide_subset])]

expr_gen = create_exhaustive_expressions_generator_v2(halide_dsl_list, 1, output_size = 128)

for e in expr_gen:
    if isinstance(e, Reg):
        continue

    print(e.emit_context_expr_string())
    pass




target_swizzles = []
swizzle_forward_path = None
forward_path_name = None
commutative_path = "./commutative_map.json"
synthesizer_desc = HALIDE_HVX_SYNTH_DESC


if True:
    PropertyInstance = EqClassEqualDepthV4Full(dsl_list = halide_dsl_list, source_synth_desc = synthesizer_desc, target_synth_desc = HALIDE_HVX_SYNTH_DESC, target_dsl_list = halide_dsl_list, output_depth = 1,input_depth = 1,  forward_map_path = forward_path_name, swizzle_dsl_list = target_swizzles, swizzle_map_path = swizzle_forward_path, commutative_map_path=  commutative_path, depth_range = True , use_canon_map = False, include_lit_holes = True)

    PropertyInstance.parallel = False
    PropertyInstance.POOL_SIZE = 8
    PropertyInstance.BATCH_SIZE = 1024

    property_map = PropertyInstance.get_property()


if False:

    pattern_file = "./EqClassEqualDepthV4Full_halide_intermediate_results.py"

    with open(pattern_file, "r") as PatternFile:
        input_patterns = json.load(PatternFile)

    print("Number of AutoLLVM IR pattern", input_patterns)
    PropertyInstance = EnumeratePattern(dsl_list = halide_dsl_list, synth_desc = HALIDE_HVX_SYNTH_DESC, input_patterns_dict = input_patterns )

    PropertyInstance.parallel = True
    PropertyInstance.POOL_SIZE = 8
    PropertyInstance.BATCH_SIZE = 1024

    property_map = PropertyInstance.get_property()


if False:
    enum_file = "./EnumeratePattern_halide_intermediate_results.py"
    with open(enum_file, "r") as ReadFile:
        props = [json.load(ReadFile)]

    parsed_patterns = create_patterns(props, halide_dsl_list)

    parsed_patterns = deduplicate_patterns(parsed_patterns)

    abstractor = PatternAbstractor(parsed_patterns, halide_dsl_list, examples_limit = 16, target = "halide")
    abstracted_patterns = abstractor.abstract_patterns(parsed_patterns, halide_dsl_list)

    for idx, pattern in enumerate(abstracted_patterns):
        print("Pattern Number", idx+1)
        pattern.print_pattern()

        print("SRC EXPR")
        print(emit_expr_to_egg(pattern.src_expr))

        print("TARGET EXPR")
        print(emit_expr_to_egg(pattern.target_expr))


    tests = []
    test_expr = "(typed:vec-shl (reg (bv #x00 8)) (LiteralHole (lit (bv #x01 8)) 8 512) 8 512)"
    test_name = "test_shift_left"

    tests.append((test_name ,test_expr ))

    egg_compiler = HydrideCompiler(abstracted_patterns, src_dsl_list = halide_dsl_list, run_iterations = 5, egg_pkg_path = "/home/arnoor2/egglogs/egg_log_2025/egglog",  parallel = False, tests = tests, skip_axioms = True)

    egg_compiler.compile_hydride()
    egg_compiler.run_llvm_legalizer()
    egg_compiler.print_stats()







