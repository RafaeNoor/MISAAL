from common.DSLParser import parse_dict
from utils.ReadDSL import read_string_to_dsl
from utils.DoubleGrammarSynthesisUtils import DoubleGrammarSynthesisUtils
from utils.DSLInstructionUtils import keep_temporary_files
import os
import sys

# Python dictionaries for semantics
from sema.ARMSema import arm_semantics
from sema.halide_sema import halide_semantics

# Uncomment below line to keep intermediate racket files
#keep_temporary_files()

# Parse the dictionay into a list of DSLInstruction types
arm_dsl_list = parse_dict(arm_semantics)
halide_dsl_list = parse_dict(halide_semantics)


arm_expr_str = "(vhadd_s32_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64 0 64 8 1 -1 0 16 0 16)"
halide_expr_str = "(typed:unsigned-vec-halving_add (reg (bv #x01 8)) (reg (bv #x00 8)) 8 32)"

arm_expr_ctx = read_string_to_dsl(arm_expr_str, arm_dsl_list)
halide_expr_ctx = read_string_to_dsl(halide_expr_str, halide_dsl_list)

print("="*5, "Pretty Printing Expressions", "="*5)
print(arm_expr_ctx.emit_context_expr_string())
print(halide_expr_ctx.emit_context_expr_string())


synthesizer = DoubleGrammarSynthesisUtils(input_dsl_list = arm_dsl_list,
                                          output_dsl_list = halide_dsl_list)





print("Arm Context output size: ",arm_expr_ctx.out_vectsize)
print("Halide Context output size: ", halide_expr_ctx.out_vectsize)

print("Arm Context concrete name: ",arm_expr_ctx.name)
print("Halide Context concrete name: ",halide_expr_ctx.name)



output_sizes = [32, 64, 128]

for output_size in output_sizes:
    print("="*10, "Testing Output size", output_size ,"="*10)


    input_sizes = [output_size] * 2

    success, src_expr_str, dst_expr_str = synthesizer.double_grammar_synthesis(arm_expr_ctx, halide_expr_ctx,
                                                                               custom_src_output_size = output_size,
                                                                               custom_dst_output_size = output_size,
                                                                               custom_src_input_sizes = input_sizes,
                                                                               custom_target_input_sizes = input_sizes
                                                                               )




    if success:
        print("SUCCESS at output size {}!".format(output_size))
        print("Corresponding ARM concretization:")
        print(src_expr_str)

        print("Corresponding Halide concretization:")
        print(dst_expr_str)
    else:
        print("FAILURE!")
