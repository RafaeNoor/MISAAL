import common.Types
import itertools
import copy
import sys
from common.Types import *
from  common.Instructions import Context
from utils.DSLInstructionUtils import *
import subprocess
import os
import time




def get_valid_concretization(ref_expr, output_size, dsl_list):



    # Valid expressions is a list of possible concretizations, currently we return the first valid one
    valid_expressions = get_valid_concretization_helper(ref_expr, output_size, dsl_list)




    #assert len(valid_expressions) >= 1, "No valid expression found"
    if len(valid_expressions) >= 1:
        return valid_expressions[0]
    else:
        return None


def get_valid_concretization_helper(ref_expr, output_size, dsl_list):

    if isinstance(ref_expr, Reg):
        return [Reg(ref_expr.index, ref_expr.precision, output_size, signed = ref_expr.signed)]


    assert isinstance(ref_expr, Context)

    dsl_inst = get_dsl_inst_for_ctx(ref_expr, dsl_list)

    num_sym_args = 0
    sym_idxs = []

    def get_ctx_sym_args(ctx):
        return sum([1 for arg in ctx.context_args if isinstance(arg, BitVector)])


    def get_sym_arg_indices(ctx):
        return [idx for idx, arg in enumerate(ctx.context_args) if isinstance(arg, BitVector)]

    def get_subexpr_at_idx(idx):
        return ref_expr.context_args[idx]



    for ctx in dsl_inst.contexts:
        if ctx.name == ref_expr.name:
            num_sym_args = get_ctx_sym_args(ctx)
            sym_idxs = get_sym_arg_indices(ctx)


    # Find possible contexts which have the same number of symbolic args and have an output size equal to what is required

    valid_ctxs = []

    for ctx in dsl_inst.contexts:
        ctx_sym_args = get_ctx_sym_args(ctx)

        if ctx_sym_args  != num_sym_args:
            continue

        if ctx.out_vectsize is None:
            continue

        if ctx.out_vectsize == output_size:
            valid_ctxs.append(copy.deepcopy(ctx))


    expressions = []

    for ctx in valid_ctxs:
        idx_arg_map = {}

        vector_space = []
        valid = True
        for idx in sym_idxs:
            sub_ref_expr = get_subexpr_at_idx(idx)
            required_size = ctx.context_args[idx].size

            valid_sub_exprs = get_valid_concretization_helper(sub_ref_expr, required_size, dsl_list)


            if  len(valid_sub_exprs) == 0:
                valid = False
                break
            idx_arg_map[str(idx)] = valid_sub_exprs
            vector_space.append(range(len(valid_sub_exprs)))


        if not valid:
            continue

        # Once all indices are iterated over and some possible combination exists,
        # we form a cross-product of the index space of all args, and create a
        # copy of the expression according to that product.
        index_combo = itertools.product(*vector_space)


        for index in index_combo:
            ctx_copy =copy.deepcopy(ctx)
            for idx ,vec_idx in enumerate(index):
                sym_idx = sym_idxs[idx]
                key = str(sym_idx)
                valid_sub_exprs = idx_arg_map[key]
                ctx_copy.context_args[sym_idx] =  copy.deepcopy(valid_sub_exprs[vec_idx])
            expressions.append(ctx_copy)


    return expressions






def get_possible_output_sizes_of_eq_class(ctx_, dsl_list):

    if isinstance(ctx_, Reg):
        return set()

    for dsl_inst in dsl_list:
        sizes = []
        ret_size = False
        for ctx in dsl_inst.contexts:
            if ctx.name == ctx_.name:
                ret_size = True

            if ctx.out_vectsize != None:
                continue

            sizes.append(ctx.out_vectsize)

        if ret_size:
            return set(sizes)
    return set()




def get_possible_input_sizes_of_eq_class(ctx_, dsl_list):

    if isinstance(ctx_, Reg):
        return set()

    for dsl_inst in dsl_list:
        sizes = []
        ret_size = False
        for ctx in dsl_inst.contexts:
            if ctx.name == ctx_.name:
                ret_size = True

            for arg in ctx.context_args:
                if isinstance(arg, BitVector):
                    sizes.append(arg.size)

        if ret_size:
            return set(sizes)
    return set()


# Testing if a valid concretization of function exists

def does_valid_concretization_exist(ref_expr, output_size, dsl_list):

    if isinstance(ref_expr, Reg):
        return True


    if isinstance(ref_expr, Context):

        eq_class = None
        for dsl_inst in dsl_list:
            if dsl_inst.name ==  ref_expr.dsl_name.split("_dsl")[0]:
                eq_class = dsl_inst
                break

        valid_contexts = [ctx for ctx in eq_class.contexts if ctx.out_vectsize == output_size]

        if len(valid_contexts) == 0:
            return False

        sym_indices = [idx for idx, arg in enumerate(ref_expr.context_args) if isinstance(arg, BitVector) or isinstance(arg, Reg)]

        for valid_ctx in valid_contexts:
            valid = True
            for  sym_idx in  sym_indices:
                ref_expr_arg = ref_expr.context_args[sym_idx]
                valid_expr_size = valid_ctx.context_args[sym_idx].size
                valid = valid and does_valid_concretization_exist(ref_expr_arg, valid_expr_size, dsl_list)

                if not valid:
                    break

            if valid:
                return True
        return False

    return False
























