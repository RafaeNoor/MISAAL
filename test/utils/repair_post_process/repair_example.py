from common.DSLParser import parse_dict
from common.StructDef import StructDef
from utils.ReadDSL import read_string_to_dsl
from utils.DSLInstructionUtils import *
from utils.RepairPostProcessUtils import  RepairPostProcessUtils
from utils.CodeSynthesizerDesc import create_synth_desc
import os
import sys

# Python dictionaries for semantics
from sema.x86SemanticsAllArgs import semantcs as x86_semantics
from sema.repairs_sema import repair_semantics
from sema.halide_sema import halide_semantics

# Uncomment below line to keep intermediate racket files
keep_temporary_files()

# Parse the dictionay into a list of DSLInstruction types
x86_dsl_list = parse_dict(x86_semantics)
repair_dsl_list = parse_dict(repair_semantics)
halide_dsl_list = parse_dict(halide_semantics)

combined_dsl_list = x86_dsl_list + repair_dsl_list + halide_dsl_list

synth_desc = create_synth_desc("post", True, [], "", "")
sd = StructDef(emit_default = False)



tests = []


# Condition 3
cond_3_name = "typed:vec-add"
cond_3_expr = "(typed:vec-add (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x00 8)) 64 64) (repair-sub_dsl (reg (bv #x01 8)) (reg (bv #x01 8)) 16 64) 16 64)"
cond_3_expected_result = False

tests.append([cond_3_name, cond_3_expr, cond_3_expected_result])





for test in tests:
    inst_name = test[0]
    inst_expr = test[1]
    expected_result = test[2]

    parsed_expression =  read_string_to_dsl(inst_expr, combined_dsl_list)

    relevant_subset_names = []

    # Define visitor function to apply on each Context
    def ctx_visitor_fn(ctx):
        global relevant_subset_names
        relevant_subset_names.append(ctx.dsl_name)
        relevant_subset_names = list(set(relevant_subset_names))
    context_visitor(parsed_expression, ctx_visitor_fn)

    relevant_subset = [dsl_inst for dsl_inst in combined_dsl_list if dsl_inst.name in relevant_subset_names]




    interpreter_framework = synth_desc.emit_interpreter_framework(relevant_subset)

    context_regs = get_unique_context_registers(parsed_expression)

    register_sizes = [reg.size for reg in context_regs]



    repair_util = RepairPostProcessUtils(test_name = inst_name, env_sizes = register_sizes)

    repair_process_name = "repair-post-process"

    statements = []
    statements.append(interpreter_framework)


    statements.append(repair_util.emit_repair_post_process(combined_dsl_list, sd, interpret_name = "", repair_post_process_name = repair_process_name))


    src_expr_name = "src-expr"
    def_src = "(define {} {}\n)".format(src_expr_name, parsed_expression.emit_context_expr_string())

    statements.append(def_src)


    execute_racket_file(statements)






