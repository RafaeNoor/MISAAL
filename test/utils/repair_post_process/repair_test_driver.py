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

from repair_test_list import tests

# Uncomment below line to keep intermediate racket files
keep_temporary_files()

# Parse the dictionay into a list of DSLInstruction types
x86_dsl_list = parse_dict(x86_semantics)
repair_dsl_list = parse_dict(repair_semantics)
halide_dsl_list = parse_dict(halide_semantics)

combined_dsl_list = x86_dsl_list + repair_dsl_list + halide_dsl_list

synth_desc = create_synth_desc("post", True, [], "", "")
const_fold_name = synth_desc.const_fold_name
sd = StructDef(emit_default = False)


racket_bool_map = {"#f": False , "#t": True}



passed_tests = []
failed_tests = []
error_tests = []




for test in tests:
    inst_name = test.get_name()
    inst_expr = test.get_expr()
    expected_result = test.get_expected_result()
    label = test.get_label()

    parsed_expression =  read_string_to_dsl(inst_expr, combined_dsl_list)

    relevant_subset_names = []

    # Define visitor function to apply on each Context
    def ctx_visitor_fn(ctx):
        global relevant_subset_names
        relevant_subset_names.append(ctx.dsl_name.split("_dsl")[0])
        relevant_subset_names = list(set(relevant_subset_names))
    context_visitor(parsed_expression, ctx_visitor_fn)

    relevant_subset = [dsl_inst for dsl_inst in combined_dsl_list if dsl_inst.name in relevant_subset_names ]

    assert len(relevant_subset_names) == len(relevant_subset)



    interpreter_framework = synth_desc.emit_interpreter_framework(relevant_subset)

    context_regs = get_unique_context_registers(parsed_expression)
    num_regs = context_regs[-1].size + 1

    register_sizes = [8] * num_regs

    for reg in context_regs:
        idx = int(reg.index)
        register_sizes[idx] = reg.size



    repair_util = RepairPostProcessUtils(test_name = inst_name, env_sizes = register_sizes, const_fold_name = const_fold_name)

    repair_process_name = "repair-post-process"

    statements = []
    statements.append(interpreter_framework)


    statements.append(repair_util.emit_repair_post_process(combined_dsl_list, sd, interpret_name = synth_desc.interpreter_name , repair_post_process_name = repair_process_name))


    src_expr_name = "src-expr"
    def_src = "(define {} {}\n)".format(src_expr_name, parsed_expression.emit_context_expr_string())

    statements.append(def_src)

    result_stmt = "(define result {})".format(repair_util.emit_check_property(src_expr_name))
    statements.append(result_stmt)

    rand_prefix = get_random_tempfile_name()

    result_file_name = rand_prefix+".log"

    write_result_to_file = "(write-str-to-file (~v result) \"{}\")".format(result_file_name)

    statements.append(write_result_to_file)


    execute_racket_file(statements)

    if os.path.exists(result_file_name):
        with open(result_file_name, "r") as LogFile:
            contents = LogFile.read().rstrip().lstrip()
            boolean = racket_bool_map[contents]
            if boolean == expected_result:
                print("PASSED")
                passed_tests.append(label)
            else:
                failed_tests.append(label)
        os.remove(result_file_name)


    else:
        error_tests.append(label)






num_passed = len(passed_tests)
num_failed = len(failed_tests)
num_error = len(error_tests)

total_tests = len(tests)

print("=*="*15, "Test Summary","=*="*15)
print("[ PASSED Tests ]:\t {} / {}".format(num_passed, total_tests))
for passed in passed_tests:
    print("–", passed)
print("[ FAILED Tests ]:\t {} / {}".format(num_failed, total_tests))
for failed in failed_tests:
    print("–", failed)
print("[ ERROR Tests ]:\t {} / {}".format(num_error, total_tests))
for errs in error_tests:
    print("–", errs)
