"""
Defines utilities to generate egglog constructs
"""

import copy
from  common.Types import *
from common.Instructions import *
from utils.ExprParamUtils import serialize_operand_for_param_map
from utils.DSLInstructionUtils import get_context_registers

HYDRIDE_EXPR_LABEL = "HydrideExpr"



def emit_egg_decl_bv():
    return "(datatype BV (LIT i64 i64) (SYMBV i64))"

def emit_egg_define_reg(reg):
    reg_name = "reg_{}".format(reg.index)
    return reg_name , "(let {} (SYMBV {}))".format(reg_name, reg.index)


def emit_egg_decl_scalar():
    return "" #"(datatype SCALAR (INT i64))"

def emit_egg_datatypes(dsl_list, cost = 1):

    symbolic_bvs = emit_egg_decl_bv()
    scalars = emit_egg_decl_scalar()

    dsl_decls = [emit_egg_dsl_decl(dsl_inst, cost = cost) for dsl_inst in dsl_list]

    comment = "; Declaring constructs for instructions"

    decl_insts = "(datatype  {} {})".format(HYDRIDE_EXPR_LABEL, "\n".join( dsl_decls))
    return  "\n".join([comment, symbolic_bvs, scalars ,decl_insts])



def emit_egg_datatypes_two_dsl(input_dsl_list, output_dsl_list,  input_cost = 1, output_cost = 1):

    symbolic_bvs = emit_egg_decl_bv()
    scalars = emit_egg_decl_scalar()

    input_dsl_decls = [emit_egg_dsl_decl(dsl_inst, cost = input_cost) for dsl_inst in input_dsl_list]
    output_dsl_decls = [emit_egg_dsl_decl(dsl_inst, cost = output_cost) for dsl_inst in output_dsl_list]

    comment = "; Declaring constructs for instructions"

    decl_insts = "(datatype  {} {})".format(HYDRIDE_EXPR_LABEL, "\n".join( input_dsl_decls + output_dsl_decls))
    return  "\n".join([comment, symbolic_bvs, scalars ,decl_insts])




def emit_egg_dsl_decl(dsl_inst, cost = 1):
    tokens = []

    tokens.append(dsl_inst.name)

    sample_ctx = dsl_inst.get_sample_context()
    for arg in sample_ctx.context_args:
        if isinstance(arg, BitVector):
            tokens.append(HYDRIDE_EXPR_LABEL)
        elif isinstance(arg, ConstBitVector):
            tokens.append(HYDRIDE_EXPR_LABEL)
        elif isinstance(arg, LaneSize):
            tokens.append("i64")
        elif isinstance(arg, Precision):
            tokens.append("i64")
        elif isinstance(arg, Integer):
            tokens.append("i64")
        elif isinstance(arg, Bool):
            # TODO: Do we need different representation
            # for bools?
            tokens.append("i64")
        elif isinstance(arg, BoundedBitVector):
            print("Not supported currently")
            tokens.append(HYDRIDE_EXPR_LABEL)
        else:
            print(dsl_inst.name)
            print(arg)
            assert False, "Unable to emit egg declaration for dsl_inst"


    return "({} :cost {})".format(" ".join(tokens), cost)




# Main method for converting a DSLExpression to
# an egg log expression.
# For re-writes, we want to maintain the same
# variable names in the input expression and
# output expression when necessary, 'param_map'
# enables mapping leaves of the expressions
# (i.e. register operands and/or precision, size literals
# to free_variable_names)
def emit_expr_to_egg(expr, param_map = {}):

    # TODO: Check if this works, as expr
    # is not a string

    if isinstance(expr, Context):
        return emit_ctx_to_egg(expr, param_map = param_map)
    elif isinstance(expr, BitVector):
        return emit_bv_to_egg(expr)
    elif isinstance(expr, ConstBitVector):
        return emit_const_bv_to_egg(expr)
    elif isinstance(expr, LaneSize):
        return emit_lanesize_to_egg(expr)
    elif isinstance(expr, Precision):
        return emit_precision_to_egg(expr)
    elif isinstance(expr, Integer):
        return emit_int_to_egg(expr)
    elif isinstance(expr, Reg):
        return emit_reg_to_egg(expr)
    elif isinstance(expr, Bool):
        return emit_bool_to_egg(expr)
    else:
        print(expr)
        assert False, "Unsupported type to emit to egg"


def emit_ctx_to_egg(expr, param_map = {}):
    tokens = []

    tokens.append(expr.dsl_name)

    for arg in expr.context_args:

        serialized_name = serialize_operand_for_param_map(expr, arg)

        if serialized_name in param_map:
            tokens.append(param_map[serialized_name])
        else:
            tokens.append(emit_expr_to_egg(arg, param_map = param_map))

    return "({}\n)".format("\n".join(tokens))


def emit_bv_to_egg(expr):
    return "(BV {})".format(expr.size)


def emit_const_bv_to_egg(expr):
    if "#x" in expr.value:
        hex_str = "0x"+ expr.value.split("#x")[-1]
        return "(LIT {} {})".format(int(hex_str, 16), expr.size)
    else:
        return "(LIT {} {})".format(expr.value, expr.size)



def emit_lanesize_to_egg(expr):

    return "{}".format(expr.value)
    #return "(INT {})".format(expr.value)

def emit_precision_to_egg(expr):
    return "{}".format(expr.value)
    #return "(INT {})".format(expr.value)


def emit_int_to_egg(expr):
    return "{}".format(expr.value)
    #return "(INT {})".format(expr.value)

def emit_bool_to_egg(expr):
    return "{}".format(int(expr.value == "#t"))
    #return "(INT {})".format(int(expr.value == "#t"))


def emit_reg_to_egg(expr):
    return "reg_{}".format(expr.index)


def emit_rewrite_expr(candidate, simplified, bidirectional = False, param_map = None):

    if param_map is None:
        param_map = copy.deepcopy({})

    candidate_expr = emit_expr_to_egg(candidate, param_map = param_map)
    simplified_expr = emit_expr_to_egg(simplified, param_map = param_map)

    if bidirectional:
        return "(birewrite \n{}\n {}\n)".format(candidate_expr, simplified_expr)
    else:
        return "(rewrite \n{}\n{}\n)".format(candidate_expr, simplified_expr)



# EggLog has constraints on when a bi-rewrite can be applied.
# This method checks if the properties are valid.
def is_birewrite_valid(expr1, expr2):

    if isinstance(expr2, Reg):
        # Currently egg log doesn't
        # allow these simplifications
        return False

    regs_expr1 = get_context_registers(expr1)

    regs_expr2 = get_context_registers(expr2)

    reg_ids_1 = [int(reg.index) for reg in regs_expr1]
    reg_ids_2 = [int(reg.index) for reg in regs_expr2]

    unique_ids_1 = list(set(reg_ids_1))
    unique_ids_2 = list(set(reg_ids_2))

    if len(unique_ids_1) != len(unique_ids_2):
        return False



    return True


