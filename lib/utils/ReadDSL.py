"""
Define utilities for parsing string form of DSL expression into
python DSLInstruction classes. As specific parameters would be used
we will identify the specific context and bind arguments accordingly.
"""

import copy
from utils.LiteralHole import LiteralHole, LiteralHoleReg
from pyparsing import nestedExpr
from  common.Types import *
from  common.Instructions import Context


TEST_STRING = """
(hexagon_V6_vabsdiffh_128B_dsl
(reg 0)
(reg 1)  1024  1024  0  1024  16  -1  -1  0  0  );<64 x i16>
"""

def get_matching_context(nested_expr, dsl_list):
    dsl_name = ""

    if "dsl" in nested_expr[0]:
        dsl_name = nested_expr[0].split("_dsl")[0]
    else:
        dsl_name = nested_expr[0]

    # Support replacing typed operations
    dsl_name = dsl_name.replace("typed_", "typed:")
    #print("DSL Name to search:", dsl_name)

    matching_dsl_inst = None

    for dsl_inst in dsl_list:
        if dsl_inst.name == dsl_name:
            matching_dsl_inst = dsl_inst
            break

    #assert matching_dsl_inst != None, "Unable to find matching context for dsl name:\t"+dsl_name

    # We iterate over the numeric arguments and at each step update matching_context
    # indices until we have a matching context

    #print("searching for dsl_name", dsl_name)
    matching_context_indices = range(len(matching_dsl_inst.contexts))

    num_reg_like_arguments = 0
    #print("Checking:", nested_expr[1:])
    for idx, arg in enumerate(nested_expr[1:]):

        new_matching_context_indices = []

        if not isinstance(arg, str):
            # May be parsing halide expresison,  check if this is a buffer index



            if isinstance(arg, list) and arg[0] != 'lit':
                num_reg_like_arguments += 1

            if isinstance(arg, list) and arg[0] == 'buffer-index':

                # Get type matching context
                for ci in matching_context_indices:
                    ctx = matching_dsl_inst.contexts[ci]
                    is_signed = int(not 'u' in arg[2])

                    # TODO: Should this be removed?
                    #if ctx.signedness != None and ctx.signedness != is_signed:
                    #    print("Signedness does not match")
                    #    continue

                    ctx_arg =  ctx.context_args[idx]

                    if ctx_arg.size != int(arg[3]):
                        #print("Size does not match", ctx_arg.size, int(arg[3]))
                        continue

                    #input_prec = int(arg[2].split("int")[-1])
                    #if ctx.in_precision != input_prec:
                    #    print("Precision does not match", ctx.in_precision, input_prec)
                    #    continue

                    new_matching_context_indices.append(ci)
                matching_context_indices = new_matching_context_indices
            continue


        if len(matching_context_indices) == 1:
            break



        assert arg.lstrip("-").isnumeric() or arg in ["#t", "#f"], "Expected numeric string {}".format(arg)



        parameter_value = None

        is_numeric = arg.lstrip("-").isnumeric()


        if is_numeric:
            parameter_value = int(arg)
        else:
            parameter_value = arg

        for ci in matching_context_indices:
            ctx = matching_dsl_inst.contexts[ci]
            ctx_arg =  ctx.context_args[idx]

            if isinstance(ctx_arg, LaneSize) and is_numeric:
                # value
                if int(ctx_arg.value) == parameter_value:
                    new_matching_context_indices.append(ci)

            elif isinstance(ctx_arg, Precision) and is_numeric:
                if int(ctx_arg.value) == parameter_value:
                    new_matching_context_indices.append(ci)
            elif isinstance(ctx_arg, Integer) and is_numeric:
                #value
                if int(ctx_arg.value) == parameter_value:
                    new_matching_context_indices.append(ci)
            elif not is_numeric and isinstance(ctx_arg, Bool):
                if ctx_arg.value == parameter_value:
                    new_matching_context_indices.append(ci)
            elif is_numeric and isinstance(ctx_arg, Bool):
                print(" Bool PARAMETER VALUE, ",parameter_value, " ctx_Arg value", ctx_arg.to_int())
                print(type(parameter_value), type(ctx_arg.to_int()))
                if parameter_value == 1 or parameter_value == 0:
                    if ctx_arg.to_int() == parameter_value:
                        print("Boolean value matches")
                        new_matching_context_indices.append(ci)
                else:
                    print("Parameter value is neither")
            else:
                print(parameter_value)
                print(ctx_arg)
                assert False, "Corresponding argument in context must be numeric or boolean"

        matching_context_indices = new_matching_context_indices

    if len(matching_context_indices) != 1:
        # Split on registers
        print("Num reg like arguments",num_reg_like_arguments)

        for ctx_idx in  matching_context_indices:
            test_ctx = matching_dsl_inst.contexts[ctx_idx]
            num_ctx_args =  sum([1 for arg in test_ctx.context_args if isinstance(arg, BitVector)])


            if num_reg_like_arguments ==  num_ctx_args:
                matching_context_indices = [ctx_idx]
                break

        print("MATCHING INDICES: ", matching_context_indices)
        print("Matching dsl_inst: ",matching_dsl_inst.name)
        matching_context_indices = [matching_context_indices[0]]

    assert len(matching_context_indices) == 1, "Unable to find matching context in DSL Parsing: {}".format(matching_context_indices)
    ctx_copy =  copy.deepcopy(matching_dsl_inst.contexts[matching_context_indices[0]])

    return ctx_copy










[['define', 'hydride-expr', ['_mm_movm_epi8_dsl', ['reg', ['bv', '0', ['bitvector', '8']]], ['lit', ['bv', '#b1', ['bitvector', '1']]], ['lit', ['bv', '#x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', ['bitvector', '512']]], ['reg', ['bv', '1', ['bitvector', '8']]], '512', '512', '0', '512', '16', '1', '16', '0']]]
def parse_nested_expr_to_dsl(nested_expr, dsl_list, expecting_return_size = None):


    first_term = nested_expr[0]

    # Skip defines if they exist
    if first_term == 'define':
        return parse_nested_expr_to_dsl(nested_expr[2], dsl_list, expecting_return_size =  expecting_return_size)

    elif first_term == 'reg':
        # Just create a register with arbritary size and precision. Parent of this
        # register will set the registers precision and size
        reg_index_term  = None

        if isinstance(nested_expr[1], list):
            reg_index_term = nested_expr[1][1]
        else:
            reg_index_term = nested_expr[1]

        if reg_index_term.startswith("#x"):
            reg_index_term = str(int(reg_index_term[2:], 16))

        reg_size = 8
        if not expecting_return_size is None:
            reg_size = expecting_return_size

        reg = Reg(reg_index_term, 8, reg_size)

        return reg


    elif first_term == 'buffer-index':
        #TODO: Need to figure out how to handle buffer index
        #['vec-absd', ['buffer-index', '0', "'uint16 1024)          (buffer-index  1 '", 'uint16', '1024']]
        reg_index_term = nested_expr[1]

        reg_size = 8
        if not expecting_return_size is None:
            reg_size = expecting_return_size

        reg = Reg(reg_index_term, 8, reg_size)
        return reg
    elif first_term == 'lit':

        lit_value = nested_expr[1][1]
        lit_size = nested_expr[1][2]

        if isinstance(lit_size, list):
            lit_size = lit_size[1]

        const_bv = ConstBitVector(lit_value, lit_size)

        return const_bv

    elif first_term == 'LIT':

        lit_value = nested_expr[1]
        lit_value = lit_value.replace("\"","")
        lit_value = hex(int(lit_value))
        if lit_value.startswith("-"):
            lit_value = lit_value[1:]
        lit_value = "#x" + lit_value[2:]
        lit_size = nested_expr[2]

        const_bv = ConstBitVector(lit_value, int(lit_size))

        return const_bv

    elif first_term == 'int-imm':

        lit_value = nested_expr[1][1]
        lit_size = nested_expr[1][2]

        if isinstance(lit_size, list):
            lit_size = lit_size[1]

        const_bv = ConstBitVector(lit_value, lit_size)

        return const_bv

    elif first_term == 'typed:int-imm':

        lit_value = nested_expr[1][1]
        lit_size = nested_expr[1][2]

        if isinstance(lit_size, list):
            lit_size = lit_size[1]

        const_bv = ConstBitVector(lit_value, lit_size)

        return const_bv

    elif first_term == 'SCALAR':
        scalar_value = Integer("scalar",value = nested_expr[1])
        return scalar_value

    elif first_term.endswith("_dsl"):
        # Obtain a copy from the dsl_list whose parameters match then bind symbolic arguments expressions with
        # parsed contexts

        matching_context = get_matching_context(nested_expr, dsl_list)

        for idx, arg in enumerate(matching_context.context_args):
            if isinstance(arg, BitVector) or isinstance(arg, ConstBitVector):
                matching_context.context_args[idx] = parse_nested_expr_to_dsl(nested_expr[idx + 1], dsl_list, expecting_return_size = arg.size) # Offset zero corresponds to the name of the current matching context

        return matching_context


    else:
        #print("Possibly dsl instruction in halide")

        matching_context = get_matching_context(nested_expr, dsl_list)

        for idx, arg in enumerate(matching_context.context_args):
            if isinstance(arg, BitVector) or isinstance(arg, ConstBitVector):
                matching_context.context_args[idx] = parse_nested_expr_to_dsl(nested_expr[idx + 1], dsl_list, expecting_return_size = arg.size) # Offset zero corresponds to the name of the current matching context

        if matching_context != None:
            return matching_context

        print(nested_expr)
        assert False, "Unable to parse unrecognized token " + nested_expr







def read_string_to_dsl(input_string, dsl_list):
    dsl_list = dsl_list + [LiteralHole, LiteralHoleReg]
    lines = input_string.replace("'","").split("\n")

    # remove racket comments
    lines = [line.split(";",1)[0] for line in lines]

    # Join all lines into a single line

    joined_line = " ".join(lines)

    brackets = nestedExpr('(',')').parseString(joined_line).asList()

    return parse_nested_expr_to_dsl(brackets[0], dsl_list)



#read_string_to_dsl(TEST_STRING, [])
