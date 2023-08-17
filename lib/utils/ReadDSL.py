"""
Define utilities for parsing string form of DSL expression into
python DSLInstruction classes. As specific parameters would be used
we will identify the specific context and bind arguments accordingly.
"""

import copy
from pyparsing import nestedExpr
from  common.Types import *
from  common.Instructions import Context


TEST_STRING = """
(define hydride-expr  (_mm_movm_epi8_dsl ; _mm512_maskz_mov_epi16
	(reg (bv 0 (bitvector 8))) ; < 1 x i32> None
	(lit (bv #b1 (bitvector 1)))
	(lit (bv #x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (bitvector 512)))
	(reg (bv 1 (bitvector 8))) ; < 32 x i16> None
	512
	512
	0
	512
	16
	1
	16
	0
 ))
"""

def get_matching_context(nested_expr, dsl_list):
    dsl_name = nested_expr[0].split("_dsl")[0]

    matching_dsl_inst = None

    for dsl_inst in dsl_list:
        if dsl_inst.name == dsl_name:
            matching_dsl_inst = dsl_inst
            break

    #assert matching_dsl_inst != None, "Unable to find matching context for dsl name:\t"+dsl_name

    # We iterate over the numeric arguments and at each step update matching_context
    # indices until we have a matching context
    matching_context_indices = range(len(matching_dsl_inst.contexts))

    for idx, arg in enumerate(nested_expr[1:]):

        if not isinstance(arg, str):
            continue

        if len(matching_context_indices) == 1:
            break


        assert arg.isnumeric(), "Expected numeric string"


        new_matching_context_indices = []

        parameter_value = int(arg)

        for ci in matching_context_indices:
            ctx = matching_dsl_inst.contexts[ci]
            ctx_arg =  ctx.context_args[idx]


            if isinstance(ctx_arg, LaneSize):
                # value
                if int(ctx_arg.value) == parameter_value:
                    new_matching_context_indices.append(ci)

            elif isinstance(ctx_arg, Precision):
                if int(ctx_arg.value) == parameter_value:
                    new_matching_context_indices.append(ci)
            elif isinstance(ctx_arg, Integer):
                #value
                if int(ctx_arg.value) == parameter_value:
                    new_matching_context_indices.append(ci)
            else:
                assert False, "Corresponding argument in context must be numeric"

        matching_context_indices = new_matching_context_indices

    return copy.deepcopy(matching_dsl_inst.contexts[matching_context_indices[0]])








[['define', 'hydride-expr', ['_mm_movm_epi8_dsl', ['reg', ['bv', '0', ['bitvector', '8']]], ['lit', ['bv', '#b1', ['bitvector', '1']]], ['lit', ['bv', '#x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', ['bitvector', '512']]], ['reg', ['bv', '1', ['bitvector', '8']]], '512', '512', '0', '512', '16', '1', '16', '0']]]
def parse_nested_expr_to_dsl(nested_expr, dsl_list):

    first_term = nested_expr[0]

    # Skip defines if they exist
    if first_term == 'define':
        return parse_nested_expr_to_dsl(nested_expr[2], dsl_list)

    elif first_term == 'reg':
        # Just create a register with arbritary size and precision. Parent of this
        # register will set the registers precision and size
        reg_index_term = nested_expr[1][1]
        reg = Reg(reg_index_term, 8, 8)

        return reg

    elif first_term == 'lit':

        lit_value = nested_expr[1][1]
        lit_size = nested_expr[1][2]

        if isinstance(lit_size, list):
            lit_size = lit_size[1]

        const_bv = ConstBitVector(lit_value, lit_size)

        return const_bv

    elif first_term.endswith("_dsl"):
        # Obtain a copy from the dsl_list whose parameters match then bind symbolic arguments expressions with
        # parsed contexts

        matching_context = get_matching_context(nested_expr, dsl_list)

        for idx, arg in enumerate(matching_context.context_args):
            if isinstance(arg, BitVector):
                matching_context.context_args[idx] = parse_nested_expr_to_dsl(nested_expr[idx + 1], dsl_list) # Offset zero corresponds to the name of the current matching context

        return matching_context


    else:
        assert False, "Unable to parse unrecognized token " + nested_expr







def read_string_to_dsl(input_string, dsl_list):
    lines = input_string.split("\n")

    # remove racket comments
    lines = [line.split(";",1)[0] for line in lines]

    # Join all lines into a single line

    joined_line = " ".join(lines)

    brackets = nestedExpr('(',')').parseString(joined_line).asList()

    return parse_nested_expr_to_dsl(brackets[0], dsl_list)



#read_string_to_dsl(TEST_STRING, [])
