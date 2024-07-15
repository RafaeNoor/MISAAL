import pprint
import copy
import json
import sys

# Generate python semantics dictionary for MLIR arith and vector dialects

pp = pprint.PrettyPrinter(indent=1)


# Inclusive
SIZE_EXPONENT_2 = 12 + 1
PREC_EXPONENT_2 = 6 + 1

simd_sizes = [pow(2, i) for i in range(3, SIZE_EXPONENT_2)]
simd_precs = [pow(2, i) for i in range(3, PREC_EXPONENT_2)]




# Signedness one applies to both
mlir_binary_simd_ops_contexts = [
    {"name": "add", "bvops": ["bvadd", "extract"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": None},
    {"name": "sub", "bvops": ["bvsub", "extract"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": None},
    {"name": "andi", "bvops": ["bvand", "extract"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": None},

    {"name": "ori", "bvops": ["bvor", "extract"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": None},

    {"name": "xori", "bvops": ["bvxor", "extract"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": None},

    # Left shift is sign-agnostic
    {"name": "shli", "bvops": ["extract", "bvshl"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": None},

    # Signed Operations
    {"name": "mul", "bvops": ["bvmul", "extract", "sign-extend"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": 1},
    {"name": "divsi", "bvops": ["bvsdiv", "extract", "sign-extend"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": 1},
    {"name": "sat-add", "bvops": ["bvaddnsw", "extract", "sign-extend"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": 1},
    {"name": "sat-sub", "bvops": ["bvsubnsw", "extract", "sign-extend"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": 1},
    {"name": "modsi", "bvops": ["bvsrem", "extract"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": 1},
    {"name": "maxsi", "bvops": ["bvsmax", "bvsgt", "extract"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": 1},
    {"name": "minsi", "bvops": ["bvsmin", "bvslt", "extract"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": 1},
    {"name": "vec-shrsi", "bvops": ["extract", "bvashr"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": 1},


    # UnSigned Operations
    {"name": "mul", "bvops": ["bvmul", "extract", "zero-extend"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": 0},
    {"name": "divui", "bvops": ["bvudiv", "extract", "zero-extend"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": 0},
    {"name": "sat-add", "bvops": ["bvaddnuw", "extract", "zero-extend"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": 0},
    {"name": "sat-sub", "bvops": ["bvsubnuw", "extract", "zero-extend"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": 0},
    {"name": "modui", "bvops": ["bvurem", "extract"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": 0},
    {"name": "maxui", "bvops": ["bvumax", "bvugt", "extract"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": 0},
    {"name": "minui", "bvops": ["bvumin", "bvult", "extract"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": 0},
    {"name": "vec-shrui", "bvops": ["extract", "bvlshr"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": 0},

]


mlir_unary_ops_contexts = [

]


mlir_ternary_ops_contexts = [
    {"name": "select", "bvops": ["if", "bveq", "extract", "concat"], "sizes": simd_sizes, "precs": simd_precs, "signedness": 1},
]

mlir_widening_ops_contexts = [

    # Signed

    {"name": "mulsi_extended", "bvops": ["bvmul", "extract", "sign-extend"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": 1},


    # Unsigned

    {"name": "mului_extended", "bvops": ["bvmul", "extract", "zero-extend"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": 0},


]


mlir_cast_ops_contexts = [

    # Down-casting ops

    {"name": "trunci", "bvops": ["extract", "concat"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": None},


    # up-casting ops

    {"name": "extsi", "bvops": ["extract", "concat", "sign-extend"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": 1},

    {"name": "extui", "bvops": ["extract", "concat", "zero-extend"],
        "sizes": simd_sizes, "precs": simd_precs, "signedness": 0},

]

"""


mlir_slice_vector_contexts = [
    {"name": "slice_vectors", "bvops": ["extract",  "concat"], "from_sizes": slice_from_sizes,
        "from_precs": slice_from_precs,  "to_sizes": slice_to_sizes, "signedness": 1},

]


mlir_concat_vector_contexts = [
    {"name": "concat_vectors", "bvops": ["extract",  "concat"], "from_sizes": concat_from_sizes,
        "from_precs": concat_from_precs,  "to_sizes": concat_to_sizes, "signedness": 1},

]








mlir_broadcast_contexts = [
    {"name": "xBroadcast", "bvops": ["extract", "concat"], "input_sizes": input_broadcast_sizes,
        "output_sizes": output_broadcast_sizes, "signedness": None},
]

"""

def create_broadcast_mlir_dict_entry(classes):

    semantics_dict = {}

    for desc in classes:

        target_desc = {"target_instructions": {}, "semantics": desc["bvops"]}
        for is_idx in range(len(desc['input_sizes'])):
            for os_idx in range(len(desc['output_sizes'])):
                input_size = desc['input_sizes'][is_idx]
                output_size = desc['output_sizes'][os_idx]

                args = ["SYMBOLIC_BV_{}".format(
                    input_size), str(output_size // input_size)]

                entry = copy.deepcopy({
                    "args": args,
                    "in_vectsize": input_size,
                    "out_vectsize": output_size,
                    "lanesize": input_size,
                    "in_precision": input_size,
                    "out_precision": input_size,
                    "in_vectsize_index": None,
                    "out_vectsize_index": None,
                    "in_lanesize_index": None,
                    "out_lanesize_index": None,
                    "in_precision_index": None,
                    "out_precision_index": None,
                    "arg_permute_map": [],
                    "Signedness": desc['signedness'],
                    "Cost": "None",
                    "SIMD": "False",
                    "Extensions": ['mlir'],
                    "ctx_sema": desc["bvops"],
                })
                target_desc['target_instructions'][desc['name']+"_is"+str(
                    input_size)+"_os"+str(output_size)+"_signed_"+str(desc['signedness'])] = entry

        if desc['name'] in semantics_dict:
            semantics_dict[desc['name']]['semantics'] += desc['bvops']
            for key in target_desc['target_instructions']:
                semantics_dict[desc['name']
                               ]['target_instructions'][key] = target_desc['target_instructions'][key]
        else:
            semantics_dict[desc['name']] = target_desc

    return semantics_dict


def create_cast_mlir_dict_entry_past(classes):

    semantics_dict = {}

    for desc in classes:

        target_desc = {"target_instructions": {}, "semantics": desc["bvops"]}
        for is_idx in range(len(desc['from_sizes'])):
            for ip_idx in range(len(desc['from_precs'])):
                input_size = desc['from_sizes'][is_idx]
                output_size = desc['to_sizes'][is_idx]
                input_prec = desc['from_precs'][ip_idx]
                output_prec = desc['to_precs'][ip_idx]

                args = []

                if desc['name'] == "vec-saturate":
                    signed_arg = ["#f", "#t"][int(desc['signedness'] == 1)]
                    args = ["SYMBOLIC_BV_{}".format(input_size), str(
                        output_size // output_prec), str(output_prec), signed_arg]
                else:
                    args = ["SYMBOLIC_BV_{}".format(input_size), str(
                        output_size // output_prec), str(output_prec)]

                entry = copy.deepcopy({
                    "args": args,
                    "in_vectsize": input_size,
                    "out_vectsize": output_size,
                    "lanesize": input_prec,
                    "in_precision": input_prec,
                    "out_precision": output_prec,
                    "in_vectsize_index": None,
                    "out_vectsize_index": None,
                    "in_lanesize_index": None,
                    "out_lanesize_index": 2,
                    "in_precision_index": None,
                    "out_precision_index": 2,
                    "arg_permute_map": [],
                    "Signedness": desc['signedness'],
                    "Cost": "None",
                    "SIMD": "False",
                    "Extensions": ['mlir'],
                    "ctx_sema": desc["bvops"],
                })
                target_desc['target_instructions'][desc['name']+"_ip"+str(input_prec)+"_is"+str(input_size) + "_op"+str(
                    output_prec)+"_os"+str(output_size) + "_signed_"+str(desc['signedness'])] = entry

        if desc['name'] in semantics_dict:
            semantics_dict[desc['name']]['semantics'] += desc['bvops']
            for key in target_desc['target_instructions']:
                semantics_dict[desc['name']
                               ]['target_instructions'][key] = target_desc['target_instructions'][key]
        else:
            semantics_dict[desc['name']] = target_desc

    return semantics_dict


def create_cast_mlir_dict_entry(classes):

    semantics_dict = {}

    for desc in classes:

        target_desc = {"target_instructions": {}, "semantics": desc["bvops"]}
        for input_size in desc['sizes']:
            for output_size in desc['sizes']:
                for input_prec in desc['precs']:
                    for output_prec in desc['precs']:

                        if input_size == output_size:
                            continue

                        if input_size < output_size and 'trunc' in desc['name']:
                            continue

                        if input_size > output_size and 'ext' in desc['name']:
                            continue

                        if input_size % input_prec != 0:
                            continue

                        input_lanes = input_size / input_prec

                        if input_lanes != (output_size / output_prec):
                            continue


                        args = ["SYMBOLIC_BV_{}".format(input_size), str(input_prec), str(input_size), str(output_prec), str(output_size)]


                        entry = copy.deepcopy({
                            "args": args,
                            "in_vectsize": input_size,
                            "out_vectsize": output_size,
                            "lanesize": input_prec,
                            "in_precision": input_prec,
                            "out_precision": output_prec,
                            "in_vectsize_index": 2,
                            "out_vectsize_index": 4,
                            "in_lanesize_index": 1,
                            "out_lanesize_index": 3,
                            "in_precision_index": 1,
                            "out_precision_index": 3,
                            "arg_permute_map": [],
                            "Signedness": desc['signedness'],
                            "Cost": "None",
                            "SIMD": "False",
                            "Extensions": ['mlir'],
                            "ctx_sema": desc["bvops"],
                        })
                        target_desc['target_instructions'][desc['name']+"_ip"+str(input_prec)+"_is"+str(input_size) + "_op"+str(
                            output_prec)+"_os"+str(output_size) + "_signed_"+str(desc['signedness'])] = entry

        if desc['name'] in semantics_dict:
            semantics_dict[desc['name']]['semantics'] += desc['bvops']
            for key in target_desc['target_instructions']:
                semantics_dict[desc['name']
                               ]['target_instructions'][key] = target_desc['target_instructions'][key]
        else:
            semantics_dict[desc['name']] = target_desc

    return semantics_dict

def create_concat_mlir_dict_entry(classes):

    semantics_dict = {}

    for desc in classes:

        target_desc = {"target_instructions": {}, "semantics": desc["bvops"]}
        for is_idx in range(len(desc['from_sizes'])):
            for ip_idx in range(len(desc['from_precs'])):
                input_size = desc['from_sizes'][is_idx]
                output_size = desc['to_sizes'][is_idx]
                input_prec = desc['from_precs'][ip_idx]
                output_prec = desc['from_precs'][ip_idx]

                args = ["SYMBOLIC_BV_{}".format(
                    input_size)] * (output_size // input_size)
                entry = copy.deepcopy({
                    "args": args,
                    "in_vectsize": input_size,
                    "out_vectsize": output_size,
                    "lanesize": input_prec,
                    "in_precision": input_prec,
                    "out_precision": output_prec,
                    "in_vectsize_index": None,
                    "out_vectsize_index": None,
                    "in_lanesize_index": None,
                    "out_lanesize_index": None,
                    "in_precision_index": None,
                    "out_precision_index": None,
                    "arg_permute_map": [],
                    "Signedness": desc['signedness'],
                    "Cost": "None",
                    "SIMD": "False",
                    "Extensions": ['mlir'],
                    "ctx_sema": desc["bvops"],
                })
                target_desc['target_instructions'][desc['name']+"_ip"+str(input_prec)+"_is"+str(input_size) + "_op"+str(
                    output_prec)+"_os"+str(output_size) + "_signed_"+str(desc['signedness'])] = entry

        if desc['name'] in semantics_dict:
            semantics_dict[desc['name']]['semantics'] += desc['bvops']
            for key in target_desc['target_instructions']:
                semantics_dict[desc['name']
                               ]['target_instructions'][key] = target_desc['target_instructions'][key]
        else:
            semantics_dict[desc['name']] = target_desc

    return semantics_dict


def create_slice_mlir_dict_entry(classes):

    semantics_dict = {}

    for desc in classes:

        target_desc = {"target_instructions": {}, "semantics": desc["bvops"]}
        for is_idx in range(len(desc['from_sizes'])):
            for ip_idx in range(len(desc['from_precs'])):
                input_size = desc['from_sizes'][is_idx]
                output_size = desc['to_sizes'][is_idx]
                input_prec = desc['from_precs'][ip_idx]
                output_prec = desc['from_precs'][ip_idx]

                # slice vector base stride num elements

                # Assuming stride of one for slicing
                # Choosing different offsets

                for offset in range(0, input_size // output_size):

                    slice_offset = str((offset * output_size) // input_prec)
                    slice_stride = str(1)
                    slice_elems = str(output_size // input_prec)
                    args = ["SYMBOLIC_BV_{}".format(
                        input_size), slice_offset, slice_stride, slice_elems]
                    entry = copy.deepcopy({
                        "args": args,
                        "in_vectsize": input_size,
                        "out_vectsize": output_size,
                        "lanesize": input_prec,
                        "in_precision": input_prec,
                        "out_precision": output_prec,
                        "in_vectsize_index": None,
                        "out_vectsize_index": None,
                        "in_lanesize_index": None,
                        "out_lanesize_index": None,
                        "in_precision_index": None,
                        "out_precision_index": None,
                        "arg_permute_map": [],
                        "Signedness": desc['signedness'],
                        "Cost": "None",
                        "SIMD": "False",
                        "Extensions": ['mlir'],
                        "ctx_sema": desc["bvops"],
                    })
                    target_desc['target_instructions'][desc['name']+"_ip"+str(input_prec)+"_is"+str(input_size) + "_op"+str(output_prec)+"_os"+str(
                        output_size) + "_signed_"+str(desc['signedness']) + "_{}_{}_{}".format(slice_offset, slice_stride, slice_elems)] = entry

        if desc['name'] in semantics_dict:
            semantics_dict[desc['name']]['semantics'] += desc['bvops']
            for key in target_desc['target_instructions']:
                semantics_dict[desc['name']
                               ]['target_instructions'][key] = target_desc['target_instructions'][key]
        else:
            semantics_dict[desc['name']] = target_desc

    return semantics_dict


def create_nary_mlir_dict_entry(classes, n=1):

    semantics_dict = {}

    for desc in classes:
        target_desc = {"target_instructions": {},
                       "semantics": desc["bvops"]}.copy()
        for size in desc['sizes']:
            for prec in desc['precs']:

                if prec > size:
                    continue

                entry = copy.deepcopy({
                    "args": ["SYMBOLIC_BV_{}".format(size)] * n + [str(prec), str(size)],
                    "in_vectsize": size,
                    "out_vectsize": size,
                    "lanesize": prec,
                    "in_precision": prec,
                    "out_precision": prec,
                    "in_vectsize_index": n + 1,
                    "out_vectsize_index": n + 1,
                    "in_lanesize_index": n,
                    "out_lanesize_index": n,
                    "in_precision_index": n,
                    "out_precision_index": n,
                    "arg_permute_map": [],
                    "Signedness": desc['signedness'],
                    "Cost": "None",
                    "SIMD": "True",
                    "Extensions": ['mlir'],
                    "ctx_sema": desc["bvops"],
                })

                target_desc['target_instructions'][desc['name']+"_p" +
                                                   str(prec)+"_s"+str(size)+"_signed_"+str(desc['signedness'])] = entry

        if desc['name'] in semantics_dict:
            semantics_dict[desc['name']]['semantics'] += desc['bvops']
            semantics_dict[desc['name']]['semantics'] = list(
                set(semantics_dict[desc['name']]['semantics']))

            for key in target_desc['target_instructions']:
                assert key not in semantics_dict[desc['name']
                                                 ]['target_instructions'], "Key should not be present in dict"
                semantics_dict[desc['name']
                               ]['target_instructions'][key] = target_desc['target_instructions'][key]
        else:
            semantics_dict[desc['name']] = target_desc.copy()

    return semantics_dict

def create_select_mlir_dict_entry(classes):


    semantics_dict = {}

    for desc in classes:
        target_desc = {"target_instructions": {},
                       "semantics": desc["bvops"]}.copy()
        for size in desc['sizes']:
            for prec in desc['precs']:

                if prec > size:
                    continue

                if size % prec != 0:
                    continue

                mask_size = size // prec



                entry = copy.deepcopy({
                    "args": ["SYMBOLIC_BV_{}".format(mask_size), "SYMBOLIC_BV_{}".format(size) , "SYMBOLIC_BV_{}".format(size)] +  [str(prec), str(size)],
                    "in_vectsize": size,
                    "out_vectsize": size,
                    "lanesize": prec,
                    "in_precision": prec,
                    "out_precision": prec,
                    "in_vectsize_index": 4,
                    "out_vectsize_index": 4,
                    "in_lanesize_index": 3,
                    "out_lanesize_index": 3,
                    "in_precision_index": 3,
                    "out_precision_index": 3,
                    "arg_permute_map": [],
                    "Signedness": desc['signedness'],
                    "Cost": "None",
                    "SIMD": "True",
                    "Extensions": ['mlir'],
                    "ctx_sema": desc["bvops"],
                })

                target_desc['target_instructions'][desc['name']+"_p" +
                                                   str(prec)+"_s"+str(size)+"_signed_"+str(desc['signedness'])] = entry

        if desc['name'] in semantics_dict:
            semantics_dict[desc['name']]['semantics'] += desc['bvops']
            semantics_dict[desc['name']]['semantics'] = list(
                set(semantics_dict[desc['name']]['semantics']))

            for key in target_desc['target_instructions']:
                assert key not in semantics_dict[desc['name']
                                                 ]['target_instructions'], "Key should not be present in dict"
                semantics_dict[desc['name']
                               ]['target_instructions'][key] = target_desc['target_instructions'][key]
        else:
            semantics_dict[desc['name']] = target_desc.copy()

    return semantics_dict


def create_widening_mlir_dict_entry(classes):

    semantics_dict = {}

    for desc in classes:

        target_desc = {"target_instructions": {}, "semantics": desc["bvops"]}
        for input_size in desc['sizes']:
            for prec in desc['precs']:

                if prec > input_size:
                    continue

                output_size = input_size * 2
                output_prec = prec * 2

                entry = copy.deepcopy({
                    "args": ["SYMBOLIC_BV_{}".format(input_size)] * 2 + [str(prec), str(input_size)],
                    "in_vectsize": input_size,
                    "out_vectsize": output_size,
                    "lanesize": prec,
                    "in_precision": prec,
                    "out_precision": output_prec,
                    "in_vectsize_index": 3,
                    "out_vectsize_index": 3,
                    "in_lanesize_index": 2,
                    "out_lanesize_index": None,
                    "in_precision_index": 2,
                    "out_precision_index": None,
                    "arg_permute_map": [],
                    "Signedness": desc['signedness'],
                    "Cost": "None",
                    "SIMD": "True",
                    "Extensions": ['mlir'],
                    "ctx_sema": desc["bvops"],
                })
                target_desc['target_instructions'][desc['name']+"_p" +
                                                   str(prec)+"_s"+str(input_size)+"_signed_"+str(desc['signedness'])] = entry

        if desc['name'] in semantics_dict:
            semantics_dict[desc['name']]['semantics'] += desc['bvops']
            for key in target_desc['target_instructions']:
                semantics_dict[desc['name']
                               ]['target_instructions'][key] = target_desc['target_instructions'][key]
        else:
            semantics_dict[desc['name']] = target_desc

    return semantics_dict


unary_dict = create_nary_mlir_dict_entry(mlir_unary_ops_contexts, n=1)
simd_dict = create_nary_mlir_dict_entry(mlir_binary_simd_ops_contexts, n=2)
ternary_dict = create_select_mlir_dict_entry(mlir_ternary_ops_contexts)
widen_dict = create_widening_mlir_dict_entry(mlir_widening_ops_contexts)
cast_dict = create_cast_mlir_dict_entry(mlir_cast_ops_contexts)
"""
broadcast_dict = create_broadcast_mlir_dict_entry(mlir_broadcast_contexts)
slice_dict = create_slice_mlir_dict_entry(mlir_slice_vector_contexts)
concat_dict = create_concat_mlir_dict_entry(mlir_concat_vector_contexts)

mlir_dicts = [concat_dict, slice_dict, broadcast_dict,
                unary_dict, simd_dict, cast_dict, ternary_dict, widen_dict]

"""

mlir_dicts = [simd_dict, unary_dict, ternary_dict, widen_dict, cast_dict]

combined_dict = {}


for dict in mlir_dicts:
    for key in dict:
        combined_dict[key] = dict[key]


print("mlir_semantics = ", end=" ")
pp.pprint(combined_dict)
