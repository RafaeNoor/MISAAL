from common.DSLParser import parse_dict
from utils.ReadDSL import read_string_to_dsl, get_matching_context
from utils.DoubleGrammarSynthesisUtils import DoubleGrammarSynthesisUtils
from utils.DSLInstructionUtils import *
from utils.ConcretizeUtils import get_valid_concretization
import os
import sys
from os import listdir
from os.path import isfile, join


# Python dictionaries for semantics
from sema.hexsemantics_new import semantics as hvx_semantics
from sema.halide_sema import halide_semantics

# Uncomment below line to keep intermediate racket files
# keep_temporary_files()

# Parse the dictionay into a list of DSLInstruction types
hvx_dsl_list = parse_dict(hvx_semantics)
halide_dsl_list = parse_dict(halide_semantics)



# This pattern should fail
fail_halide_expr_str = " (typed:unsigned-vec-shr (reg (bv #x00 8)) (reg (bv #x00 8)) 16 1024) "
fail_hvx_expr_str = " (hexagon_V6_vlsrwv_128B (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 (bitvector 16))) (reg (bv #x01 8)) 1024 1024 0 1024 16 1 0) "

tests_0 = (fail_hvx_expr_str, fail_halide_expr_str, False)


fail_halide_expr_str_1 = " (typed:unsigned-vec-shr (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024) "
fail_hvx_expr_str_1 = " (hexagon_V6_vlsrwv_128B (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 (bitvector 16))) (reg (bv #x01 8)) 1024 1024 0 1024 16 1 0) "

tests_1 = (fail_hvx_expr_str_1, fail_halide_expr_str_1, False)



fail_halide_expr_str_2 = " (typed:unsigned-vec-shr (reg (bv #x01 8)) (reg (bv #x00 8)) 16 1024) "
fail_hvx_expr_str_2 = " (hexagon_V6_vlsrwv_128B (reg (bv #x00 8)) (lit (bv #x00000000000000000000000000000000 (bitvector 16))) (reg (bv #x01 8)) 1024 1024 0 1024 16 1 0) "

tests_2 = (fail_hvx_expr_str_2, fail_halide_expr_str_2, True)

tests = [tests_0, tests_1, tests_2]





synthesizer = DoubleGrammarSynthesisUtils(input_dsl_list = hvx_dsl_list,
                                          output_dsl_list = halide_dsl_list,
                                          # Force all source expression to be used in the left hand side (i.e. src expression)
                                          force_contains_all_regs = True,
                                          use_any_reg = False
                                          )




def test_rule(hvx_expr_str, halide_expr_str):
    hvx_expr_ctx = read_string_to_dsl(hvx_expr_str, hvx_dsl_list)
    halide_expr_ctx = read_string_to_dsl(halide_expr_str, halide_dsl_list)
    print("=*="*20, "TEST RULE")

    print("="*5, "Pretty Printing Expressions", "="*5)
    print(hvx_expr_ctx.emit_context_expr_string())
    print("hvx Context concrete name: ", hvx_expr_ctx.name)
    print(halide_expr_ctx.emit_context_expr_string())

    output_sizes = [pow(2,i) for i in range(16)]

    for output_size in output_sizes:

        src_expression_hvx = get_valid_concretization(hvx_expr_ctx, output_size, hvx_dsl_list)

        if src_expression_hvx is None:
            print("No valid concretization at output size", output_size)
            continue

        regs = get_unique_context_registers(src_expression_hvx)


        input_sizes = [reg.size for reg in regs]

        success, src_expr_str, dst_expr_str = synthesizer.double_grammar_synthesis(src_expression_hvx,  # src expression
                                                                                   halide_expr_ctx,    # target expression
                                                                                   custom_src_output_size = output_size,
                                                                                   custom_dst_output_size = output_size,
                                                                                   custom_src_input_sizes = input_sizes,
                                                                                   custom_target_input_sizes = input_sizes
                                                                                   )




        if success:
            print("ENUMO_SUCC")
            print("SUCCESS at output size {}!".format(output_size))
            print("Corresponding hvx concretization:")
            print(src_expr_str)

            print("Corresponding Halide concretization:")
            print(dst_expr_str)
            return True
        else:
            print("FAILURE")

    return False


summary = []
for idx,(hvx_str, halide_str, expected_result) in enumerate(tests):
    result = test_rule(hvx_str, halide_str)

    summary.append(result == expected_result)

for idx,s in enumerate(summary):
    if s:
        print("Test",idx,"Passed!")
    else:
        print("Test",idx,"Failed!")


