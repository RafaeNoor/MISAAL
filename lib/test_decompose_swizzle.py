from sema.x86_swizzles import x86_swizzles
from sema.arm_swizzles import arm_swizzles
from sema.hex_swizzles import hvx_swizzles as hvx_swizzles
from sema.halide_sema import halide_semantics
from utils.SwizzleUtils import split_swizzle_eq_class_by_size_behavior
from common.DSLParser import parse_dict
from utils.DSLInstructionUtils import print_dsl_list_summary


hvx_swizzle_dsl_list = parse_dict( hvx_swizzles, keep_duplicate = True)
halide_dsl_list = parse_dict(halide_semantics)

test_list = hvx_swizzle_dsl_list
test_name = "hvx_swizzles"

decomposed_list = split_swizzle_eq_class_by_size_behavior(test_list, test_name +"_decomposed.py", test_name+"_decomposed")

print("Original")
print_dsl_list_summary(test_list)

print("After")
print_dsl_list_summary(decomposed_list)
