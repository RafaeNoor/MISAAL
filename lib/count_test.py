from common.DSLParser import parse_dict
from sema.hexsemantics_new import semantics as hvx_semantics
from sema.x86SemanticsAllArgs import semantcs as x86_semantics
from sema.halide_sema import halide_semantics
from sema.ARMSema import arm_semantics
from sema.repairs_sema import repair_semantics
from sema.halide_folded_full import halide_folded_full as halide_folded
from utils.CountUtils import *
import sys

IGNORE_MASK = False

halide_dsl_list = parse_dict(halide_semantics)
x86_dsl_list = parse_dict(x86_semantics)
repair_dsl_list = parse_dict(repair_semantics)

if  IGNORE_MASK:
    x86_dsl_list = [x for x in x86_dsl_list if 'mask' not in x.name]

arm_dsl_list = parse_dict(arm_semantics)
hvx_dsl_list = parse_dict(hvx_semantics)

halide_folded_dsl_list = parse_dict(halide_folded)

target_map = {
    "x86": x86_dsl_list,
    "arm": arm_dsl_list,
    "hvx": hvx_dsl_list,
    "halide": halide_dsl_list,
    "repair": repair_dsl_list,
    "halide_folded": halide_folded_dsl_list,
}

depth_range = [1,2]


for depth in depth_range:
    print("–*" * 30)
    for target in ["halide_folded"]:

        num_target_expr = count_num_expressions(target_map[target], depth)
        print("Target [{}]\t # Expressions at depth {}:\t\t{:.2e}".format(target, depth ,num_target_expr))

        num_target_eq_expr = count_num_expressions_eq_class(target_map[target], depth)
        print("Target [{}]\t # Eq Class Expressions at depth {}:\t\t{:.2e}".format(target, depth ,num_target_eq_expr))

        reduction = num_target_expr / num_target_eq_expr
        print("Target [{}]\t Enumeration reduction using Eq Classes at depth {}:\t{:.2e}".format(target,depth, reduction))

        print("")

sys.exit()

halide_subset_names = [
    "typed:vec-add",
    "typed:unsigned-vec-widen-mul",
    "typed:signed-vector_reduce_add",
    "typed:signed-vec-widen-mul",
    "typed:cast-uint",
    "typed:cast-int"
]

print("Subset results")
halide_subset = [d for d in halide_dsl_list if d.name in halide_subset_names]
num_target_eq_expr = count_num_expressions_eq_class(halide_subset, 2)

print("Target [{}]\t # Eq Class Expressions at depth {}:\t\t{:.2e}".format("SUBSET", 2 ,num_target_eq_expr))
