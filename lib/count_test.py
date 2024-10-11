from common.DSLParser import parse_dict
from sema.hexsemantics_new import semantics as hvx_semantics
from sema.x86SemanticsAllArgs import semantcs as x86_semantics
from sema.halide_sema import halide_semantics
from sema.ARMSema import arm_semantics

from utils.CountUtils import *


halide_dsl_list = parse_dict(halide_semantics)
x86_dsl_list = parse_dict(x86_semantics)
arm_dsl_list = parse_dict(arm_semantics)
hvx_dsl_list = parse_dict(hvx_semantics)

target_map = {
    "x86": x86_dsl_list,
    "arm": arm_dsl_list,
    "hvx": hvx_dsl_list,
    "halide": halide_dsl_list,
}

depth_range = [1,2,3,4]


for depth in depth_range:
    print("–*" * 30)
    for target in target_map:
        num_target_expr = count_num_expressions(target_map[target], depth)
        print("Target [{}]\t # Expressions at depth {}:\t\t{:.2e}".format(target, depth ,num_target_expr))

        num_target_eq_expr = count_num_expressions_eq_class(target_map[target], depth)
        print("Target [{}]\t # Eq Class Expressions at depth {}:\t\t{:.2e}".format(target, depth ,num_target_eq_expr))

        reduction = num_target_expr // num_target_eq_expr
        print("Target [{}]\t Enumeration reduction using Eq Classes at depth {}:\t{:.2e}".format(target,depth, reduction))

        print("")

