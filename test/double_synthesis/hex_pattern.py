from common.DSLParser import parse_dict
from utils.ReadDSL import read_string_to_dsl, get_matching_context
from utils.DoubleGrammarSynthesisUtils import DoubleGrammarSynthesisUtils
from utils.DSLInstructionUtils import *
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

#file_name = sys.argv[1]
#expr_file = open(file_name)
#content = expr_file.readlines()  

#hvx_expr_str = content[1]
#halide_expr_str = content[0]

hvx_expr_str = sys.argv[2]
halide_expr_str = sys.argv[1]

#for i in hvx_dsl_list:
#    print(i)

#halide_expr_str = "(typed:unsigned-vec-shr (reg (bv #x01 8))  (reg (bv #x00 8))  16 1024)"
#hvx_expr_str = "(hexagon_V6_vlsrw_128B (reg (bv #x01 8)) (lit (bv #x00000000000000000000000000000000 (bitvector 32))) (reg (bv #x00 8))  1024 1024 0 1024 32 1 0)"

#hvx_expr_str = "(hexagon_V6_vminuh_128B (reg (bv #x00 8)) (hexagon_V6_vminuh_128B (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 0 0) 1024 1024 0 1024 16 0 0)"
#halide_expr_str = "(typed:unsigned-vec-min (reg (bv #x00 8)) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024) 16 1024)"

hvx_expr_ctx = read_string_to_dsl(hvx_expr_str, hvx_dsl_list)
halide_expr_ctx = read_string_to_dsl(halide_expr_str, halide_dsl_list)

print("="*5, "Pretty Printing Expressions", "="*5)
print(hvx_expr_ctx.emit_context_expr_string())
print("hvx Context concrete name: ", hvx_expr_ctx.name)
print(halide_expr_ctx.emit_context_expr_string())

synthesizer = DoubleGrammarSynthesisUtils(input_dsl_list = hvx_dsl_list,
                                          output_dsl_list = halide_dsl_list)





#print("hvx Context output size: ",hvx_expr_ctx.out_vectsize)
#print("Halide Context output size: ", halide_expr_ctx.out_vectsize)

#print("Halide Context concrete name: ",halide_expr_ctx.name)


#output_sizes = [32, 64, 128, 1024]
output_sizes = [128, 1024]

for output_size in output_sizes:
    #print("="*10, "Testing Output size", output_size ,"="*10)


    input_sizes = [output_size] * 2

    success, src_expr_str, dst_expr_str = synthesizer.double_grammar_synthesis(hvx_expr_ctx, halide_expr_ctx,
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
    else:
        print("FAILURE")
