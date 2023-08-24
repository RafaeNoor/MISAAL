from common.Types import *
from  common.Instructions import Context
import subprocess
import os
import tempfile
import glob
import copy


def class_name(arg):

    if isinstance(arg, ConstBitVector):
        return "const_bv"
    elif isinstance(arg,LaneSize):
        return "lane_size"
    elif isinstance(arg, Precision):
        return "prec"
    elif isinstance(arg, Integer):
        return "int"
    elif isinstance(arg, Bool):
        return "bool"
    elif isinstance(arg, Reg):
        return "reg"+str(arg.index)
    elif isinstance(arg, Context):
        return arg.name
    else:
        print("Unable to identify class name for:\t", arg)
        assert False, "Unsupported class name type"

def serialize_operand_for_param_map(expr, arg):
    for idx, ctx_arg in enumerate(expr.context_args):
        if ctx_arg != arg:
            continue

        if isinstance(arg, Reg):
            return class_name(arg)
        else:
            return expr.name+"_"+class_name(arg)+"_"+str(idx)
    print("\n\n",arg.get_dsl_value(), "\nfor\n", expr.emit_context_expr_string() )
    assert False, "Unreachable"



def find_integer_arg_with_same_value(input_map, reverse_map,  value):
    for key, operand in reverse_map.items():
        if isinstance(operand, Integer):
            if operand.value == value:
                return key
    return None


def find_lane_size_arg_with_same_value(input_map, reverse_map,  value):
    for key, operand in reverse_map.items():
        if isinstance(operand, LaneSize):
            if operand.value == value:
                return key
    return None


def find_precision_arg_with_same_value(input_map, reverse_map,  value):
    for key, operand in reverse_map.items():
        if isinstance(operand, Precision):
            if operand.value == value:
                return key
    return None


def find_arg_with_same_value(input_map, reverse_map, input_arg):

    if isinstance(input_arg, Integer):
        return find_integer_arg_with_same_value(input_map, reverse_map, input_arg.value)
    elif isinstance(input_arg, Precision):
        return find_precision_arg_with_same_value(input_map, reverse_map, input_arg.value)

    elif isinstance(input_arg, LaneSize):
        return find_lane_size_arg_with_same_value(input_map, reverse_map, input_arg.value)
    else:
        print(input_arg)
        assert False, "Unsupported argument type: " + str(input_arg)




# Creates a map from leaf parameters of expressions
# to free variable names.
def generate_parameter_map(expr1, expr2, input_map = None, reverse_map = None):

    if input_map is None:
        input_map = copy.deepcopy({})

    if reverse_map is None:
        reverse_map = copy.deepcopy({})

    current_map = input_map
    current_reverse_map = reverse_map



    for idx, e1 in enumerate(expr1.context_args):

        if isinstance(e1, Context):
            updated_map , updated_reverse_map = generate_parameter_map(e1, expr2, input_map = current_map, reverse_map = current_reverse_map)
            current_map, current_reverse_map  = updated_map, updated_reverse_map
        elif isinstance(e1, Reg) or isinstance(e1, ConstBitVector):
            serialized_name = serialize_operand_for_param_map(expr1, e1)
            current_map[serialized_name] = serialized_name
            current_reverse_map[serialized_name] = e1
        else:
            serialized_name = serialize_operand_for_param_map(expr1, e1)
            matching_arg_name = find_arg_with_same_value(current_map, current_reverse_map, e1)
            if matching_arg_name != None:
                current_map[serialized_name] = current_map[matching_arg_name]
            else:

                current_map[serialized_name] = serialized_name
                current_reverse_map[serialized_name] = e1



    # Repeat for expression expr2. TODO: Refactor into single loop

    for idx, e2 in enumerate(expr2.context_args):

        if isinstance(e2, Context):
            updated_map , updated_reverse_map = generate_parameter_map(expr1, e2, input_map = current_map, reverse_map = current_reverse_map)
            current_map, current_reverse_map  = updated_map, updated_reverse_map
        elif isinstance(e2, Reg) or isinstance(e2, ConstBitVector):
            serialized_name = serialize_operand_for_param_map(expr2, e2)
            current_map[serialized_name] = serialized_name
            current_reverse_map[serialized_name] = e2
        else:


            serialized_name = serialize_operand_for_param_map(expr2, e2)
            matching_arg_name = find_arg_with_same_value(current_map, current_reverse_map, e2)
            if matching_arg_name != None:
                current_map[serialized_name] = current_map[matching_arg_name]
            else:
                current_map[serialized_name] = serialized_name
                current_reverse_map[serialized_name] = e2


    return current_map, current_reverse_map




