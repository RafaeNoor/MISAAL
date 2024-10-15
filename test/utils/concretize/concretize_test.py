from common.DSLParser import parse_dict
from utils.ReadDSL import read_string_to_dsl
from utils.ConcretizeUtils import *
import os
import sys

# Python dictionaries for semantics
from sema.x86SemanticsAllArgs import semantcs as x86_semantics

# Uncomment below line to keep intermediate racket files
keep_temporary_files()

# Parse the dictionay into a list of DSLInstruction types
x86_dsl_list = parse_dict(x86_semantics)


leaf_0_expr = "(_mm512_mulhi_epu16_dsl (reg (bv 0 8))   (reg (bv 1 8)) 64 64 0 64 16 16 0 32 0 0)"

leaf_1_expr = "(_mm512_mulhi_epu16_dsl (reg (bv 2 8))   (reg (bv 3 8)) 64 64 0 64 16 16 0 32 0 0)"

test_expr ="(_mm_add_pi8_dsl {} {} 64 64 0 64 8 -1 0)".format(leaf_0_expr, leaf_1_expr)


x86_expr = read_string_to_dsl(test_expr, x86_dsl_list)


print(x86_expr.emit_context_expr_string())


possible_output_sizes = [pow(2, i) for i in range(16)]


for size in possible_output_sizes:
    print("=*="*20)
    valid_concretization = get_valid_concretization(x86_expr, size, x86_dsl_list)
    print("Output Size:", size)

    if valid_concretization is None:
        print("None")
    else:
        input_regs = get_unique_context_registers(valid_concretization)
        print(valid_concretization.emit_context_expr_string())
        print('Input Sizes:', [arg.size for arg in input_regs])



