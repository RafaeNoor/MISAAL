from sema.x86_swizzles import x86_swizzles
from sema.x86_swizzles_decomposed import x86_swizzles_decomposed
from utils.SwizzleUtils import split_swizzle_eq_class_by_size_behavior
from common.DSLParser import parse_dict
from utils.DSLInstructionUtils import print_dsl_list_summary


x86_swizzle_dsl_list = parse_dict( x86_swizzles, keep_duplicate = True)
#decomposed_list = split_swizzle_eq_class_by_size_behavior(x86_swizzle_dsl_list, "x86_swizzles.py", "x86_swizzles_decomposed")

decomposed_list = parse_dict( x86_swizzles_decomposed, keep_duplicate = True)
print("Original")
print_dsl_list_summary(x86_swizzle_dsl_list)

print("After")
print_dsl_list_summary(decomposed_list)
