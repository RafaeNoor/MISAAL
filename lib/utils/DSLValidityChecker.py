from utils.DSLInstructionUtils import *
import copy
import sys
from common.Types import *


def check_validity_context(dsl_inst, context):

    statements = []
    statements.append(dsl_inst.get_semantics())

    args = []
    for ctx_arg in context.context_args:
        if isinstance(ctx_arg, BitVector):
            args.append("(bv 0 (bitvector {}))".format(ctx_arg.size))
        elif isinstance(ctx_arg, ConstBitVector):
            args.append(ctx_arg.get_rkt_value())
        else:
            args.append(ctx_arg.get_rkt_value())


    invoke_context = "({} {})".format(dsl_inst.name, " ".join(args))
    operation_result = "(define result {})".format(invoke_context)
    statements.append(operation_result)

    clauses = ["(equal? (bvlength result) {})".format(context.out_vectsize), "else"]

    cases = ["(exit 0)", "(exit 1)"]

    statements.append(emit_racket_cond(clauses, cases))


    is_valid = execute_racket_file(statements).returncode == 0

    return is_valid



def check_validity_inst(dsl_inst):

    validity =[ check_validity_context(dsl_inst, ctx) for ctx in dsl_inst.contexts]

    return validity





def check_validity(dsl_list):


    statements= []

    contexts = 0
    for dsl_inst in dsl_list:
        contexts += len(dsl_inst.contexts)
    print("{} DSL Instructions with {} contexts ...".format(len(dsl_list), contexts))

    for dsl_inst in dsl_list:
        inst_validity = check_validity_inst(dsl_inst)

        for idx, validity in enumerate(inst_validity):
            statements.append("Validity of {}:\t{}".format(dsl_inst.contexts[idx].name, validity))

    for stmt in statements:
        print(stmt)


