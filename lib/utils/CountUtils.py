from common.Types import *
from  common.Instructions import Context
from utils.DSLInstructionUtils import *
import sys
import time
import copy
import sys
import os
import glob


count_memo = {}



def count_num_expressions_helper(ctx_out_map, output_size = None, depth = 1, total_contexts = 0):

    if depth == 0:
        return 1

    if depth == 1 and output_size == None:
        return total_contexts

    key = str(output_size)
    #assert key in ctx_out_map, "Output size {} not in ctx_out_map".format(key)

    if key not in ctx_out_map:
        ctx_out_map[key] = []

    global count_memo
    memo_key = str((output_size, depth))
    if memo_key in count_memo:
        return count_memo[memo_key]

    if depth == 1:
        count_memo[memo_key] = len(ctx_out_map[key])
        return len(ctx_out_map[key])

    total = 0

    for ctx in ctx_out_map[key]:
        ctx_total = 1
        for arg in ctx.context_args:
            if isinstance(arg, BitVector):
                ctx_total *= count_num_expressions_helper(ctx_out_map, output_size = arg.size, depth = depth - 1, total_contexts = total_contexts)
        total += ctx_total


    count_memo[memo_key] = total

    return total











def count_num_expressions(dsl_list, depth):
    global count_memo
    count_memo = {}

    flat_contexts = []

    for dsl_inst in dsl_list:
        for ctx in dsl_inst.contexts:
            flat_contexts.append(ctx)

    total_contexts = len(flat_contexts)
    ctx_out_map = {}

    # Helper to catch all contexts
    ctx_out_map['None'] = []

    for ctx in flat_contexts:

        if ctx.out_vectsize == None:
            #print("Skipping {} as it has no output size".format(ctx.name))
            continue
        key = str(ctx.out_vectsize)

        if key not in ctx_out_map:
            ctx_out_map[key] = []

        ctx_out_map[key].append(ctx)
        ctx_out_map['None'].append(ctx)

    total_count = count_num_expressions_helper(ctx_out_map, output_size = None, depth = depth, total_contexts = total_contexts)

    return total_count














def count_num_expressions_helper_eq_class(dsl_out_map, dsl_list,  output_size = None, depth = 1):
    total_dsl = len(dsl_out_map['None'])

    if depth == 0:
        return 1

    if depth == 1 and output_size == None:
        return total_dsl

    key = str(output_size)
    #assert key in ctx_out_map, "Output size {} not in ctx_out_map".format(key)

    if key not in dsl_out_map:
        dsl_out_map[key] = []

    global count_memo
    memo_key = str((output_size, depth))
    if memo_key in count_memo:
        return count_memo[memo_key]

    if depth == 1:
        count_memo[memo_key] = len(dsl_out_map[key])
        return len(dsl_out_map[key])

    total = 0

    for dsl_inst_name in dsl_out_map[key]:

        dsl_inst = None
        for d in dsl_list:
            if d.name == dsl_inst_name:
                dsl_inst = d
                break

        # For Equivalance class expressions enumeration we explicitly include the minimum
        # number of contexts to capture distinct number of symbolic arguments. In some contexts,
        # bitvector argument may be a constant literal, but in others it could be a symbolic parameter.
        ctx_num_args = []
        ctx_to_enumerate = []

        for ctx in dsl_inst.contexts:
            if ctx.out_vectsize == None:
                continue

            if output_size != None and ctx.out_vectsize != output_size:
                continue


            num_sym = sum([1 for arg in ctx.context_args if isinstance(arg,BitVector)])

            if num_sym in ctx_num_args:
                continue

            ctx_num_args.append(num_sym)
            ctx_to_enumerate.append(ctx)

        dsl_inst_total = 0

        for ctx in ctx_to_enumerate:
            ctx_total = 1

            for arg in ctx.context_args:
                if isinstance(arg, BitVector):
                    ctx_total *= count_num_expressions_helper_eq_class(dsl_out_map, dsl_list,  output_size = arg.size, depth = depth - 1)
            dsl_inst_total += ctx_total

        total +=  dsl_inst_total



    count_memo[memo_key] = total

    return total



def count_num_expressions_eq_class(dsl_list, depth):

    global count_memo
    count_memo = {}


    dsl_out_map = {}

    dsl_out_map['None'] = []

    for dsl_inst in dsl_list:
        for ctx in dsl_inst.contexts:

            if ctx.out_vectsize == None:
                continue

            key = str(ctx.out_vectsize)

            if key not in dsl_out_map:
                 dsl_out_map[key] = []

            if dsl_inst.name not in dsl_out_map[key]:
                dsl_out_map[key].append(dsl_inst.name)

            if dsl_inst.name not in dsl_out_map['None']:
                dsl_out_map['None'].append(dsl_inst.name)





    total_count = count_num_expressions_helper_eq_class(dsl_out_map, dsl_list , output_size = None, depth = depth)

    return total_count
