import common.Types
import json
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
                break

        if ret_size:
            for ctx in dsl_inst.contexts:
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

        ref_expr_ctx = None

        for ctx in eq_class.contexts:
            if ctx.name == ref_expr.name:
                ref_expr_ctx = ctx
                break

        if len(valid_contexts) == 0:
            return False

        sym_indices = [idx for idx, arg in enumerate(ref_expr_ctx.context_args) if isinstance(arg, BitVector) or isinstance(arg, Reg)]

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




def is_expression_template_valid(template):

    if not isinstance(template, list) and not isinstance(template, tuple):
        return False

    if len(template) != 2:
        return False

    if isinstance(template[0], Reg):
        return True

    if isinstance(template[0], ConstBitVector):
        return True


    for sub_temp in template[1]:
        if not is_expression_template_valid(sub_temp[0]):
            return False
    return True


def materialize_expression_template(valid_template):

    assert isinstance(valid_template, list)
    assert len(valid_template) == 2

    expr = valid_template[0]

    if isinstance(expr, Reg):
        #print("Materialize reg size:", expr.size, expr.precision)
        return expr

    if isinstance(expr, ConstBitVector):
        #print("Materialize reg size:", expr.size, expr.precision)
        return expr


    # Else context

    context_copy = copy.deepcopy(expr)

    argument_settings = valid_template[1]

    for arg_ctx in argument_settings:
        expr_ctx, idx = arg_ctx
        materialize_arg = materialize_expression_template(expr_ctx)

        context_copy.context_args[idx] = materialize_arg

    return context_copy







def get_valid_concretization_generator(ref_expr, output_size, dsl_list, root_ctx_name = None):
    valid_expression_templates = get_valid_concretization_generator_helper(ref_expr, output_size, dsl_list, root_ctx_name = root_ctx_name)

    valid = False

    for valid_template in valid_expression_templates:

        if not is_expression_template_valid(valid_template):
            continue
        valid = True
        materialize_context = materialize_expression_template(valid_template)
        yield materialize_context

    if valid:
        return

    print(ref_expr.emit_context_expr_string())
    print(output_size)
    assert False, "Unreachable"
    return None




def get_valid_concretization_generator_helper(ref_expr, output_size, dsl_list, root_ctx_name = None):

    if isinstance(ref_expr, Reg):
        #print("Creating reg of required size: ", output_size)
        yield [Reg(ref_expr.index, ref_expr.precision, output_size, signed = ref_expr.signed), None]
        return []

    if isinstance(ref_expr, ConstBitVector):
        yield [ConstBitVector(ref_expr.value, output_size, name = ref_expr.name), None]
        return []


    assert isinstance(ref_expr, Context)

    def get_ctx_sym_args(ctx):
        return sum([1 for arg in ctx.context_args if isinstance(arg, BitVector)])


    def get_sym_arg_indices(ctx):
        return [idx for idx, arg in enumerate(ctx.context_args) if isinstance(arg, BitVector)]

    def get_subexpr_at_idx(idx):
        return ref_expr.context_args[idx]

    dsl_inst = get_dsl_inst_for_ctx(ref_expr, dsl_list)

    num_sym_args = 0
    sym_idxs = []

    for ctx in dsl_inst.contexts:
        if ctx.name == ref_expr.name:
            num_sym_args = get_ctx_sym_args(ctx)
            sym_idxs = get_sym_arg_indices(ctx)



    valid_ctxs = []

    for ctx in dsl_inst.contexts:


        ctx_sym_args = get_ctx_sym_args(ctx)

        #if ctx_sym_args  != num_sym_args:
        #    continue

        if not root_ctx_name is None and ctx.name != root_ctx_name:
            continue

        if ctx.out_vectsize is None:
            continue



        if ctx.out_vectsize == output_size:
            valid_ctxs.append(ctx)

    for valid_ctx in valid_ctxs:
        ctx = valid_ctx
        if num_sym_args == 4:

            sym_idx_0 = sym_idxs[0]
            sub_ref_expr_0 = get_subexpr_at_idx(sym_idx_0)
            required_size_0 = ctx.context_args[sym_idx_0].size
            generator_0 =  get_valid_concretization_generator_helper(sub_ref_expr_0, required_size_0, dsl_list)
            for config_0 in generator_0:

                if len(config_0) != 2:
                    continue

                sym_idx_1 = sym_idxs[1]
                sub_ref_expr_1 = get_subexpr_at_idx(sym_idx_1)
                required_size_1 = ctx.context_args[sym_idx_1].size
                generator_1 =  get_valid_concretization_generator_helper(sub_ref_expr_1, required_size_1, dsl_list)
                for config_1 in generator_1:
                    if len(config_1) != 2:
                        continue

                    sym_idx_2 = sym_idxs[2]
                    sub_ref_expr_2 = get_subexpr_at_idx(sym_idx_2)
                    required_size_2 = ctx.context_args[sym_idx_2].size
                    generator_2 =  get_valid_concretization_generator_helper(sub_ref_expr_2, required_size_2, dsl_list)
                    for config_2 in generator_2:
                        if len(config_2) != 2:
                            continue

                        sym_idx_3 = sym_idxs[3]
                        sub_ref_expr_3 = get_subexpr_at_idx(sym_idx_3)
                        required_size_3 = ctx.context_args[sym_idx_3].size
                        generator_3 =  get_valid_concretization_generator_helper(sub_ref_expr_3, required_size_3, dsl_list)

                        for config_3 in generator_3:
                            if len(config_3) != 2:
                                continue
                            yield [valid_ctx, [(config_0, sym_idx_0), (config_1, sym_idx_1), (config_2, sym_idx_2), (config_3, sym_idx_3)]]
        elif num_sym_args == 3:

            sym_idx_0 = sym_idxs[0]
            sub_ref_expr_0 = get_subexpr_at_idx(sym_idx_0)
            required_size_0 = ctx.context_args[sym_idx_0].size
            generator_0 =  get_valid_concretization_generator_helper(sub_ref_expr_0, required_size_0, dsl_list)
            for config_0 in generator_0:

                if len(config_0) != 2:
                    continue

                sym_idx_1 = sym_idxs[1]
                sub_ref_expr_1 = get_subexpr_at_idx(sym_idx_1)
                required_size_1 = ctx.context_args[sym_idx_1].size
                generator_1 =  get_valid_concretization_generator_helper(sub_ref_expr_1, required_size_1, dsl_list)
                for config_1 in generator_1:
                    if len(config_1) != 2:
                        continue

                    sym_idx_2 = sym_idxs[2]
                    sub_ref_expr_2 = get_subexpr_at_idx(sym_idx_2)
                    required_size_2 = ctx.context_args[sym_idx_2].size
                    generator_2 =  get_valid_concretization_generator_helper(sub_ref_expr_2, required_size_2, dsl_list)
                    for config_2 in generator_2:
                        if len(config_2) != 2:
                            continue

                        yield [valid_ctx, [(config_0, sym_idx_0), (config_1, sym_idx_1), (config_2, sym_idx_2)]]


        elif num_sym_args == 2:

            sym_idx_0 = sym_idxs[0]
            sub_ref_expr_0 = get_subexpr_at_idx(sym_idx_0)
            required_size_0 = ctx.context_args[sym_idx_0].size
            generator_0 =  get_valid_concretization_generator_helper(sub_ref_expr_0, required_size_0, dsl_list)
            for config_0 in generator_0:

                if len(config_0) != 2:
                    continue

                sym_idx_1 = sym_idxs[1]
                sub_ref_expr_1 = get_subexpr_at_idx(sym_idx_1)
                required_size_1 = ctx.context_args[sym_idx_1].size
                generator_1 =  get_valid_concretization_generator_helper(sub_ref_expr_1, required_size_1, dsl_list)
                for config_1 in generator_1:
                    if len(config_1) != 2:
                        continue
                    yield [valid_ctx, [(config_0, sym_idx_0), (config_1, sym_idx_1)]]


        elif num_sym_args == 1:
            sym_idx = sym_idxs[0]
            sub_ref_expr = get_subexpr_at_idx(sym_idx)
            required_size = ctx.context_args[sym_idx].size
            generator_0 =  get_valid_concretization_generator_helper(sub_ref_expr, required_size, dsl_list)
            for config_0 in generator_0:
                if len(config_0) != 2:
                    continue
                yield [valid_ctx, [(config_0, sym_idx)]]
        else:
            print(ref_expr.emit_context_expr_string())
            assert False, "Unreachable number of sym args {}".format(num_sym_args)


    yield []
    return

