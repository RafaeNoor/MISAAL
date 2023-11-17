"""
Defines utilities to write DSLInstructions and contexts
to the dictionary format
"""

import copy
import json
from pyparsing import nestedExpr
from  common.Types import *
from  common.Instructions import Context



def convert_context_to_dict(ctx):
    dictionary = copy.deepcopy({})

    dictionary['in_vectsize'] = ctx.in_vectsize
    dictionary['out_vectsize'] = ctx.out_vectsize
    dictionary['lane_size'] = ctx.lane_size
    dictionary['in_precision'] = ctx.in_precision
    dictionary['out_precision'] = ctx.out_precision
    dictionary['in_vectsize_index'] = ctx.in_vectsize_index
    dictionary['out_vectsize_index'] = ctx.out_vectsize_index
    dictionary['lanesize_index'] = ctx.in_lanesize_index
    dictionary['in_precision_index'] = ctx.in_precision_index
    dictionary['out_precision_index'] = ctx.out_precision_index
    dictionary['arg_permute_map'] = []
    dictionary['Signedness'] = ctx.signedness
    dictionary['Cost'] = ctx.cost
    dictionary['SIMD'] = str(ctx.SIMD)
    dictionary['Extensions'] = ctx.extensions
    dictionary['args'] = ctx.unparsed_args


    return dictionary





def convert_dsl_inst_to_dict(dsl_inst):
    sema = {"target_instructions": {}, "semantics": dsl_inst.semantics}

    for context in dsl_inst.contexts:
        sema['target_instructions'][context.name] = convert_context_to_dict(context)

    return sema

def convert_dsl_list_to_dict(dsl_list):

    global_sema = {}

    for dsl_inst in dsl_list:
        global_sema[dsl_inst.name] = convert_dsl_inst_to_dict(dsl_inst)

    return global_sema



def write_dsl_dict_to_file(dsl_dict, fpath, dict_name):
    with open(fpath, "w+") as WriteFile:
        WriteFile.write("{} =".format(dict_name))
        WriteFile.write(json.dumps(dsl_dict, indent = 4))
        WriteFile.write("\n")







