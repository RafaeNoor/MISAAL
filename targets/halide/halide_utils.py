import pprint
import copy
import json
import sys
from folded_ops_sema_desc import *

pp = pprint.PrettyPrinter(indent=1)


reduce_factors = [2,3,4]

simd_sizes = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
simd_precs = [8, 16, 32, 64]

cast_from_sizes = [4096, 2048, 1024, 512, 256, 128, 64, 32, 16]
cast_to_sizes = [2048,1024, 512, 256, 128, 64, 32, 16, 8]
cast_from_precs = [64, 32, 16]
cast_to_precs = [32,16, 8]


slice_from_sizes = [4096, 2048, 1024, 512, 256, 128, 64, 32, 16]
slice_to_sizes = [2048, 1024, 512, 256, 128, 64, 32, 16, 8]
slice_from_precs = [8]


concat_from_sizes =[2048, 1024, 512, 256, 128, 64, 32, 16, 8]
concat_to_sizes = [4096,2048, 1024, 512, 256, 128, 64, 32, 16]
concat_from_precs = [8]


widening_input_sizes = [8, 16, 32, 64, 128, 256, 512,1024, 2048]
widening_input_precs = [8, 16, 32]

input_broadcast_sizes = [8,16,32]
output_broadcast_sizes = [16,32,64,128, 256, 512,1024, 2048, 4096]

halide_binary_simd_ops_contexts = [
    {"name": "vec-add", "bvops": ["bvadd", "extract"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": [0,1,-1], 'sema': vec_add_sema},

    {"name": "vec-sub", "bvops": ["bvsub", "extract"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": [0,1,-1], 'sema': vec_sub_sema},

    {"name": "vec-bwand", "bvops": ["bvand", "extract"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": [-1], 'sema': vec_and_sema},

    {"name": "vec-bwor", "bvops": ["bvor", "extract"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": [-1], 'sema': vec_bwor_sema},

    {"name": "vec-bwxor", "bvops": ["bvxor", "extract"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": [-1], 'sema': vec_bwxor_sema},

    {"name": "vec-div", "bvops": ["bvsdiv", "extract", "sign-extend"] , "sizes": simd_sizes, "precs": simd_precs , "signedness": [0,1], 'sema': vec_div_sema },

    {"name": "vec-mod", "bvops": ["bvsrem", "extract"] , "sizes": simd_sizes, "precs": simd_precs , "signedness": [0,1], 'sema': vec_mod_sema },

    {"name": "vec-max", "bvops": ["bvsmax", "bvsgt" , "extract"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": [0,1], 'sema': vec_max_sema},
    {"name": "vec-min", "bvops": ["bvsmin", "bvslt" , "extract"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": [0,1], 'sema': vec_min_sema},

    {"name": "vec-absd", "bvops": ["extract", "bvsub", "bvsmax", "bvsmin"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness":[0,1], 'sema': vec_absd_sema  },

    {"name": "vec-shr", "bvops": ["extract", "bvashr"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": [0,1], 'sema':vec_shr_sema},

    # Left shift is sign-agnostic
    {"name": "vec-shl", "bvops": ["extract", "bvshl"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": [-1], 'sema': vec_shl_sema},


]


# Those operations which internally require widening
halide_binary_widen_prec_simd_ops_contexts = [

    {"name": "vec-mul", "bvops": ["bvmul", "extract", "sign-extend"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": [0,1], 'sema': vec_mul_sema, "keep_widen": False},

    {"name": "vec-widen-mul", "bvops": ["bvmul", "extract", "sign-extend"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": [0,1], 'sema': vec_widen_mul_sema, "keep_widen": True},

    {"name": "vec-rounding_shift_right", "bvops": ["bvshl", "bvashr", "bvssat", "bvsdiv", "sign-extend"] , "sizes": simd_sizes, "precs": simd_precs , "signedness": [0,1], 'sema': vec_rnd_shift_right_sema , "keep_widen": False},

    {"name": "vec-rounding_halving_add", "bvops": ["extract", "bvadd", "sign-extend", "bvsdiv"] , "sizes": simd_sizes, "precs": simd_precs , "signedness": [0,1] , "keep_widen": False, 'sema': vec_rnd_hlv_add_sema},

    {"name": "vec-halving_add", "bvops": ["extract", "bvadd", "sign-extend", "bvsdiv"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": [0,1], "keep_widen": False, 'sema': vec_hlv_add_sema},

]



halide_binary_comparison_ops_contexts = [
    {"name": "vec-eq", "bvops": ["if", "extract", "bveq", "eq"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": [-1], 'sema': vec_eq_sema},

    {"name": "vec-lt", "bvops": ["bvult", "extract"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": [0,1], 'sema':vec_lt_sema},
    {"name": "vec-le", "bvops": ["bvult","bvule", "bveq", "extract"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": [0,1], 'sema': vec_le_sema},

    {"name": "vec-gt", "bvops": ["bvult", "extract"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": [0,1], 'sema':vec_gt_sema},
    {"name": "vec-ge", "bvops": ["bvult","bvule", "bveq", "extract"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": [0,1], 'sema': vec_ge_sema},


]




# Those operations which internally require widening
halide_ternary_widen_prec_simd_ops_contexts = [

    {"name": "vec-rounding_mul_shift_right", "bvops": ["bvmul", "extract", "sign-extend"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": [0,1], 'sema': vec_rnd_mul_shift_right_sema, "keep_widen": False},

]


halide_cast_extend_ops_contexts = [


    # up-casting ops
    {"name": "cast-extend", "bvops": ["extract", "sign-extend", "concat" , "zero-extend" ] , "from_sizes": cast_to_sizes, "from_precs": cast_to_precs ,  "to_sizes": cast_from_sizes, "to_precs": cast_from_precs ,"signedness": [0,1], 'sema': cast_extend_sema },


]

halide_cast_truncate_ops_contexts = [


    # down-casting ops
    {"name": "cast-truncate", "bvops": ["extract", "concat"] , "from_sizes": cast_from_sizes, "from_precs": cast_from_precs ,  "to_sizes": cast_to_sizes, "to_precs": cast_to_precs ,"signedness": [0], 'sema': cast_truncate_sema },


]

halide_cast_saturate_ops_contexts = [


    # down-casting ops
    {"name": "vec-saturate", "bvops": ["extract", "concat", "bvsaturate", "bvssat", "bvusat"] , "from_sizes": cast_from_sizes, "from_precs": cast_from_precs ,  "to_sizes": cast_to_sizes, "to_precs": cast_to_precs ,"signedness": [0,1], 'sema': cast_saturate_sema },


]

halide_cast_ops_contexts = [

    # Down-casting ops
    {"name": "cast-int", "bvops": ["extract", "sign-extend", "concat" ] , "from_sizes": cast_from_sizes, "from_precs": cast_from_precs ,  "to_sizes": cast_to_sizes, "to_precs": cast_to_precs ,"signedness": 1 , "input_signed": 1},
    #{"name": "cast-int", "bvops": ["extract", "sign-extend", "concat" ] , "from_sizes": cast_from_sizes, "from_precs": cast_from_precs ,  "to_sizes": cast_to_sizes, "to_precs": cast_to_precs ,"signedness": 1 , "input_signed": 0},

    {"name": "cast-uint", "bvops": ["extract", "zero-extend", "concat" ] , "from_sizes": cast_from_sizes, "from_precs": cast_from_precs ,  "to_sizes": cast_to_sizes, "to_precs": cast_to_precs ,"signedness": 0,  "input_signed": 1 },
    #{"name": "cast-uint", "bvops": ["extract", "zero-extend", "concat" ] , "from_sizes": cast_from_sizes, "from_precs": cast_from_precs ,  "to_sizes": cast_to_sizes, "to_precs": cast_to_precs ,"signedness": 0 , "input_signed": 0},

    {"name": "vec-saturate", "bvops": ["extract", "bvssat", "concat" ] , "from_sizes": cast_from_sizes, "from_precs": cast_from_precs ,  "to_sizes": cast_to_sizes, "to_precs": cast_to_precs ,"signedness": 1 , "input_signed": 1},
    #{"name": "vec-saturate", "bvops": ["extract", "bvssat", "concat" ] , "from_sizes": cast_from_sizes, "from_precs": cast_from_precs ,  "to_sizes": cast_to_sizes, "to_precs": cast_to_precs ,"signedness": 1 , "input_signed": 0},

    {"name": "vec-saturate", "bvops": ["extract", "bvusat", "concat" ] , "from_sizes": cast_from_sizes, "from_precs": cast_from_precs ,  "to_sizes": cast_to_sizes, "to_precs": cast_to_precs ,"signedness": 0 , "input_signed": 1},
    #{"name": "vec-saturate", "bvops": ["extract", "bvusat", "concat" ] , "from_sizes": cast_from_sizes, "from_precs": cast_from_precs ,  "to_sizes": cast_to_sizes, "to_precs": cast_to_precs ,"signedness": 0 , "input_signed": 0},


    # up-casting ops
    {"name": "cast-int", "bvops": ["extract", "sign-extend", "concat" ] , "from_sizes": cast_to_sizes, "from_precs": cast_to_precs ,  "to_sizes": cast_from_sizes, "to_precs": cast_from_precs ,"signedness": 1 , "input_signed": 1},
    #{"name": "cast-int", "bvops": ["extract", "sign-extend", "concat" ] , "from_sizes": cast_to_sizes, "from_precs": cast_to_precs ,  "to_sizes": cast_from_sizes, "to_precs": cast_from_precs ,"signedness": 1 , "input_signed": 0},

    {"name": "cast-uint", "bvops": ["extract", "zero-extend", "concat" ] , "from_sizes": cast_to_sizes, "from_precs": cast_to_precs ,  "to_sizes": cast_from_sizes, "to_precs": cast_from_precs ,"signedness": 0 , "input_signed": 1},
    #{"name": "cast-uint", "bvops": ["extract", "zero-extend", "concat" ] , "from_sizes": cast_to_sizes, "from_precs": cast_to_precs ,  "to_sizes": cast_from_sizes, "to_precs": cast_from_precs ,"signedness": 0 , "input_signed": 0},

]


halide_slice_vector_contexts = [
    {"name": "slice_vectors", "bvops": ["extract",  "concat" ] , "from_sizes": slice_from_sizes, "from_precs": slice_from_precs ,  "to_sizes": slice_to_sizes, "signedness": [-1], 'sema': vec_slice_sema },

]


halide_concat_vector_contexts = [
    {"name": "concat_vectors", "bvops": ["extract",  "concat" ] , "from_sizes": concat_from_sizes, "from_precs": concat_from_precs ,  "to_sizes": concat_to_sizes, "signedness": [-1], 'sema': vec_concat_sema },

]



halide_unary_ops_contexts = [

    #{"name": "vec-abs", "bvops": ["abs", "extract", "sign-extend", "bitvector->integer"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": 1},
    {"name": "vec-bwnot", "bvops": ["bvnot", "extract"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": [-1], 'sema':vec_bw_not_sema},

]


halide_ternary_ops_contexts = [

    # Signed

    {"name": "vec-rounding_mul_shift_right", "bvops": ["bvshl", "bvashr", "bvssat", "bvsdiv", "sign-extend"] , "sizes": simd_sizes, "precs": simd_precs , "signedness": 1 },


    # Unsigned
    {"name": "vec-rounding_mul_shift_right", "bvops": ["bvmul","bvshl", "bvlshr", "bvusat", "bvudiv", "zero-extend"] , "sizes": simd_sizes, "precs": simd_precs  , "signedness": 0},

]


halide_widening_ops_contexts = [

    # Signed

    {"name": "vec-widen-mul", "bvops": ["bvmul", "extract", "sign-extend"] , "sizes": widening_input_sizes, "precs": widening_input_precs  , "signedness": 1},


    # Unsigned

    {"name": "vec-widen-mul", "bvops": ["bvmul", "extract", "zero-extend"] , "sizes": widening_input_sizes, "precs": widening_input_precs  , "signedness": 0},


]



halide_broadcast_contexts = [
    {"name": "xBroadcast", "bvops": ["extract", "concat"] , "input_sizes": input_broadcast_sizes, "output_sizes": output_broadcast_sizes , "signedness": [-1] , 'sema': vec_broadcast_sema},
]



def create_broadcast_halide_dict_entry(classes):

    semantics_dict = {}

    typed_name = "typed-folded:"+"xBroadcast"
    for desc in classes:

        target_desc = {"target_instructions": {}, "semantics": desc["sema"]}
        for is_idx in range(len(desc['input_sizes'])):
            for os_idx in range(len(desc['output_sizes'])):
                input_size = desc['input_sizes'][is_idx]
                output_size = desc['output_sizes'][os_idx]

                if output_size <= input_size:
                    continue

                if output_size % input_size != 0:
                    continue


                args = ["SYMBOLIC_BV_{}".format(input_size), str(input_size),  str(output_size // input_size)]



                entry = copy.deepcopy({
                    "args": args,
                    "in_vectsize": input_size,
                    "out_vectsize": output_size,
                    "lanesize": input_size,
                    "in_precision" : input_size,
                    "out_precision": input_size,
                    "in_vectsize_index": 1,
                    "out_vectsize_index": None,
                    "in_lanesize_index": 1,
                    "out_lanesize_index": 1,
                    "in_precision_index": 1,
                    "out_precision_index": 1,
                    "arg_permute_map": [],
                    "Signedness": -1,
                    "Cost": "None",
                    "SIMD": "False",
                    "Extensions" : ['halide'],
                    "ctx_sema": desc["bvops"],
                })

                target_desc['target_instructions'][typed_name+"_is"+str(input_size)+"_os"+str(output_size)+"_signed_"+str(-1)] = entry

        if typed_name in semantics_dict:
            #semantics_dict[typed_name]['semantics'] += desc['bvops']
            #for key in target_desc['target_instructions']:
            #    semantics_dict[typed_name]['target_instructions'][key] = target_desc['target_instructions'][key]
            pass
        else:
            semantics_dict[typed_name] = target_desc


    return semantics_dict

def create_cast_truncate_halide_dict_entry(classes):

    semantics_dict = {}

    for desc in classes:

        target_desc = {"target_instructions": {}, "semantics": desc["sema"]}
        for is_idx in range(len(desc['from_sizes'])):
            for ip_idx in range(len(desc['from_precs'])):
                for sign in desc['signedness']:
                    input_size = desc['from_sizes'][is_idx]
                    output_size = desc['to_sizes'][is_idx]
                    input_prec = desc['from_precs'][ip_idx]
                    output_prec = desc['to_precs'][ip_idx]

                    sign_val = None
                    if sign == 1:
                        sign_val = 1
                    elif sign == 0:
                        sign_val = 0

                    if input_size == output_size:
                        continue

                    if input_prec > input_size:
                        continue

                    if output_prec > output_size:
                        continue

                    input_lanes = input_size // input_prec
                    output_lanes = output_size // output_prec

                    if input_lanes != output_lanes:
                        continue

                    typed_name = "typed-folded:"+desc['name']


                    args = ["SYMBOLIC_BV_{}".format(input_size), str(input_prec), str(input_size), str(output_prec)]



                    entry = copy.deepcopy({
                        "args": args,
                        "in_vectsize": input_size,
                        "out_vectsize": output_size,
                        "lanesize": input_prec,
                        "in_precision" : input_prec,
                        "out_precision": output_prec,
                        "in_vectsize_index": 2,
                        "out_vectsize_index": None,
                        "in_lanesize_index": 1,
                        "out_lanesize_index": 3,
                        "in_precision_index": 1,
                        "out_precision_index": 3,
                        "arg_permute_map": [],
                        "Signedness": sign,
                        "Cost": "None",
                        "SIMD": "False",
                        "Extensions" : ['halide'],
                        "ctx_sema": desc["bvops"],
                    })
                    target_desc['target_instructions'][typed_name+"_ip"+str(input_prec)+"_is"+str(input_size)+ "_op"+str(output_prec)+"_os"+str(output_size)  +"_signed_"+str(sign)] = entry

        if typed_name in semantics_dict:
            #semantics_dict[typed_name]['semantics'] += desc['bvops']
            #for key in target_desc['target_instructions']:
            #    semantics_dict[typed_name]['target_instructions'][key] = target_desc['target_instructions'][key]
            pass
        else:
            semantics_dict[typed_name] = target_desc


    return semantics_dict



def create_cast_saturate_halide_dict_entry(classes):

    semantics_dict = {}

    for desc in classes:

        target_desc = {"target_instructions": {}, "semantics": desc["sema"]}
        for is_idx in range(len(desc['from_sizes'])):
            for ip_idx in range(len(desc['from_precs'])):
                for sign in desc['signedness']:
                    input_size = desc['from_sizes'][is_idx]
                    output_size = desc['to_sizes'][is_idx]
                    input_prec = desc['from_precs'][ip_idx]
                    output_prec = desc['to_precs'][ip_idx]

                    sign_val = None
                    if sign == 1:
                        sign_val = 1
                    elif sign == 0:
                        sign_val = 0

                    if input_size == output_size:
                        continue

                    if input_prec > input_size:
                        continue

                    if output_prec > output_size:
                        continue

                    input_lanes = input_size // input_prec
                    output_lanes = output_size // output_prec

                    if input_lanes != output_lanes:
                        continue

                    typed_name = "typed-folded:"+desc['name']


                    args = ["SYMBOLIC_BV_{}".format(input_size), str(input_prec), str(input_size), str(output_prec), str(sign_val)]



                    entry = copy.deepcopy({
                        "args": args,
                        "in_vectsize": input_size,
                        "out_vectsize": output_size,
                        "lanesize": input_prec,
                        "in_precision" : input_prec,
                        "out_precision": output_prec,
                        "in_vectsize_index": 2,
                        "out_vectsize_index": None,
                        "in_lanesize_index": 1,
                        "out_lanesize_index": 3,
                        "in_precision_index": 1,
                        "out_precision_index": 3,
                        "arg_permute_map": [],
                        "Signedness": sign,
                        "Cost": "None",
                        "SIMD": "False",
                        "Extensions" : ['halide'],
                        "ctx_sema": desc["bvops"],
                    })
                    target_desc['target_instructions'][typed_name+"_ip"+str(input_prec)+"_is"+str(input_size)+ "_op"+str(output_prec)+"_os"+str(output_size)  +"_signed_"+str(sign)] = entry

        if typed_name in semantics_dict:
            #semantics_dict[typed_name]['semantics'] += desc['bvops']
            #for key in target_desc['target_instructions']:
            #    semantics_dict[typed_name]['target_instructions'][key] = target_desc['target_instructions'][key]
            pass
        else:
            semantics_dict[typed_name] = target_desc


    return semantics_dict


def create_cast_extend_halide_dict_entry(classes):

    semantics_dict = {}

    for desc in classes:

        target_desc = {"target_instructions": {}, "semantics": desc["sema"]}
        for is_idx in range(len(desc['from_sizes'])):
            for ip_idx in range(len(desc['from_precs'])):
                for sign in desc['signedness']:
                    input_size = desc['from_sizes'][is_idx]
                    output_size = desc['to_sizes'][is_idx]
                    input_prec = desc['from_precs'][ip_idx]
                    output_prec = desc['to_precs'][ip_idx]

                    sign_val = None
                    if sign == 1:
                        sign_val = 1
                    elif sign == 0:
                        sign_val = 0

                    if input_size == output_size:
                        continue

                    if input_prec > input_size:
                        continue

                    if output_prec > output_size:
                        continue

                    input_lanes = input_size // input_prec
                    output_lanes = output_size // output_prec

                    if input_lanes != output_lanes:
                        continue

                    typed_name = "typed-folded:"+desc['name']


                    args = ["SYMBOLIC_BV_{}".format(input_size), str(input_prec), str(input_size), str(output_prec), str(sign_val)]



                    entry = copy.deepcopy({
                        "args": args,
                        "in_vectsize": input_size,
                        "out_vectsize": output_size,
                        "lanesize": input_prec,
                        "in_precision" : input_prec,
                        "out_precision": output_prec,
                        "in_vectsize_index": 2,
                        "out_vectsize_index": None,
                        "in_lanesize_index": 1,
                        "out_lanesize_index": 3,
                        "in_precision_index": 1,
                        "out_precision_index": 3,
                        "arg_permute_map": [],
                        "Signedness": sign,
                        "Cost": "None",
                        "SIMD": "False",
                        "Extensions" : ['halide'],
                        "ctx_sema": desc["bvops"],
                    })
                    target_desc['target_instructions'][typed_name+"_ip"+str(input_prec)+"_is"+str(input_size)+ "_op"+str(output_prec)+"_os"+str(output_size)  +"_signed_"+str(sign)] = entry

        if typed_name in semantics_dict:
            #semantics_dict[typed_name]['semantics'] += desc['bvops']
            #for key in target_desc['target_instructions']:
            #    semantics_dict[typed_name]['target_instructions'][key] = target_desc['target_instructions'][key]
            pass
        else:
            semantics_dict[typed_name] = target_desc


    return semantics_dict


def create_concat_halide_dict_entry(classes):

    semantics_dict = {}

    for desc in classes:
        typed_name = "typed-folded:"+desc['name']

        target_desc = {"target_instructions": {}, "semantics": desc["sema"]}
        for is_idx in range(len(desc['from_sizes'])):
            for ip_idx in range(len(desc['from_precs'])):
                input_size = desc['from_sizes'][is_idx]
                output_size = desc['to_sizes'][is_idx]
                input_prec = desc['from_precs'][ip_idx]
                output_prec = desc['from_precs'][ip_idx]


                if input_prec > input_size:
                    continue

                if output_prec > output_size:
                    continue




                args = (["SYMBOLIC_BV_{}".format(input_size)] * (output_size // input_size)) + [str(input_prec), str(input_size)]
                entry = copy.deepcopy({
                    "args": args,
                    "in_vectsize": input_size,
                    "out_vectsize": output_size,
                    "lanesize": input_prec,
                    "in_precision" : input_prec,
                    "out_precision": output_prec,
                    "in_vectsize_index": len(args)-1,
                    "out_vectsize_index": None,
                    "in_lanesize_index": len(args)-2,
                    "out_lanesize_index": len(args)-2,
                    "in_precision_index": len(args)-2,
                    "out_precision_index": len(args)-2,
                    "arg_permute_map": [],
                    "Signedness": -1,
                    "Cost": "None",
                    "SIMD": "False",
                    "Extensions" : ['halide'],
                    "ctx_sema": desc["bvops"],
                })
                target_desc['target_instructions'][typed_name+"_ip"+str(input_prec)+"_is"+str(input_size)+ "_op"+str(output_prec)+"_os"+str(output_size)  +"_signed_"+str(-1) ] = entry

        if typed_name in semantics_dict:
            #semantics_dict[typed_name]['semantics'] += desc['bvops']
            #for key in target_desc['target_instructions']:
            #    semantics_dict[typed_name]['target_instructions'][key] = target_desc['target_instructions'][key]
            pass
        else:
            semantics_dict[typed_name] = target_desc


    return semantics_dict

def create_slice_halide_dict_entry(classes):

    semantics_dict = {}

    for desc in classes:

        typed_name = "typed-folded:"+desc['name']
        target_desc = {"target_instructions": {}, "semantics": desc["sema"]}
        for is_idx in range(len(desc['from_sizes'])):
            for ip_idx in range(len(desc['from_precs'])):
                input_size = desc['from_sizes'][is_idx]
                output_size = desc['to_sizes'][is_idx]
                input_prec = desc['from_precs'][ip_idx]
                output_prec = desc['from_precs'][ip_idx]



                if input_prec > input_size:
                    continue

                if output_prec > output_size:
                    continue



                # slice vector base stride num elements

                # Assuming stride of one for slicing
                # Choosing different offsets

                for offset in range(0, input_size // output_size):

                    slice_offset = str((offset * output_size) // input_prec)
                    slice_stride = str(1)
                    slice_elems = str(output_size // input_prec)
                    args = ["SYMBOLIC_BV_{}".format(input_size), str(input_prec), str(input_size), slice_offset, slice_stride, slice_elems]
                    entry = copy.deepcopy({
                        "args": args,
                        "in_vectsize": input_size,
                        "out_vectsize": output_size,
                        "lanesize": input_prec,
                        "in_precision" : input_prec,
                        "out_precision": output_prec,
                        "in_vectsize_index": 2,
                        "out_vectsize_index": None,
                        "in_lanesize_index": 1,
                        "out_lanesize_index": 1,
                        "in_precision_index": 1,
                        "out_precision_index": 1,
                        "arg_permute_map": [],
                        "Signedness": -1,
                        "Cost": "None",
                        "SIMD": "False",
                        "Extensions" : ['halide'],
                        "ctx_sema": desc["bvops"],
                    })
                    target_desc['target_instructions'][typed_name+"_ip"+str(input_prec)+"_is"+str(input_size)+ "_op"+str(output_prec)+"_os"+str(output_size)  +"_signed_"+str(-1) + "_{}_{}_{}".format(slice_offset, slice_stride, slice_elems)] = entry

        if typed_name in semantics_dict:
            #semantics_dict['semantics'] += desc['bvops']
            #for key in target_desc['target_instructions']:
            #    semantics_dict[typed_name]['target_instructions'][key] = target_desc['target_instructions'][key]
            pass
        else:
            semantics_dict[typed_name] = target_desc


    return semantics_dict

def create_nary_halide_dict_entry(classes,n = 1):

    semantics_dict = {}

    for desc in classes:
        typed_name = "typed-folded:"+desc['name']


        target_desc = {"target_instructions": {}, "semantics": desc["sema"]}.copy()
        for size in desc['sizes']:
            for prec in desc['precs']:
                for sign in desc['signedness']:

                    sign_val = None


                    if sign == 1:
                        sign_val = 1
                    elif sign == 0:
                        sign_val = 0
                    elif sign is None or sign == -1:
                        sign_val = -1

                    if prec > size:
                        continue
                    entry = copy.deepcopy({
                        "args": (["SYMBOLIC_BV_{}".format(size)] * n) + [str(prec), str(size), str(sign_val)],
                        "in_vectsize": size,
                        "out_vectsize": size,
                        "lanesize": prec,
                        "in_precision" : prec,
                        "out_precision": prec,
                        "in_vectsize_index": n + 1,
                        "out_vectsize_index": n + 1,
                        "in_lanesize_index": n,
                        "out_lanesize_index": n,
                        "in_precision_index": n,
                        "out_precision_index": n,
                        "arg_permute_map": [],
                        "Signedness": sign,
                        "Cost": "None",
                        "SIMD": "True",
                        "Extensions" : ['halide'],
                        "ctx_sema": desc["bvops"],
                    })


                    target_desc['target_instructions'][typed_name+"_p"+str(prec)+"_s"+str(size)+"_signed_"+str(sign)] = entry




        if typed_name in semantics_dict:
        #    semantics_dict[typed_name]['semantics'] += desc['bvops']
        #    semantics_dict[typed_name]['semantics'] = list(set(semantics_dict[typed_name]['semantics']))



            for key in target_desc['target_instructions']:
                assert key not in semantics_dict[typed_name]['target_instructions'], "Key should not be present in dict"
                semantics_dict[typed_name]['target_instructions'][key] = target_desc['target_instructions'][key]
        else:
            semantics_dict[typed_name] = target_desc.copy()



    return semantics_dict


def create_nary_widen_halide_dict_entry(classes,n = 1):

    semantics_dict = {}

    for desc in classes:
        typed_name = "typed-folded:"+desc['name']
        keep_widen = desc['keep_widen']


        target_desc = {"target_instructions": {}, "semantics": desc["sema"]}.copy()
        for size in desc['sizes']:
            for prec in desc['precs']:
                for sign in desc['signedness']:

                    sign_val = None

                    widen_prec = prec * 2

                    if sign == 1:
                        sign_val = 1
                    elif sign == 0:
                        sign_val = 0
                    elif sign is None or sign == -1:
                        sign_val = -1

                    output_size = size
                    output_prec = prec
                    if keep_widen:
                        output_size = size * 2
                        output_prec = prec * 2


                    if prec > size:
                        continue
                    entry = copy.deepcopy({
                        "args": (["SYMBOLIC_BV_{}".format(size)] * n) + [str(prec), str(widen_prec), str(size), str(sign_val)],
                        "in_vectsize": size,
                        "out_vectsize": output_size,
                        "lanesize": prec,
                        "in_precision" : prec,
                        "out_precision": output_prec,
                        "in_vectsize_index": n + 2,
                        "out_vectsize_index": None if keep_widen else n+2 ,
                        "in_lanesize_index": n,
                        "out_lanesize_index": n+1 if keep_widen else n,
                        "in_precision_index": n,
                        "out_precision_index": n+1 if keep_widen else n,
                        "arg_permute_map": [],
                        "Signedness": sign,
                        "Cost": "None",
                        "SIMD": "True",
                        "Extensions" : ['halide'],
                        "ctx_sema": desc["bvops"],
                    })


                    target_desc['target_instructions'][typed_name+"_p"+str(prec)+"_s"+str(size)+"_signed_"+str(sign)] = entry




        if typed_name in semantics_dict:
        #    semantics_dict[typed_name]['semantics'] += desc['bvops']
        #    semantics_dict[typed_name]['semantics'] = list(set(semantics_dict[typed_name]['semantics']))



            for key in target_desc['target_instructions']:
                assert key not in semantics_dict[typed_name]['target_instructions'], "Key should not be present in dict"
                semantics_dict[typed_name]['target_instructions'][key] = target_desc['target_instructions'][key]
        else:
            semantics_dict[typed_name] = target_desc.copy()



    return semantics_dict

def create_nary_comparison_halide_dict_entry(classes,n = 1):

    semantics_dict = {}

    for desc in classes:
        typed_name = "typed-folded:"+desc['name']


        target_desc = {"target_instructions": {}, "semantics": desc["sema"]}.copy()
        for size in desc['sizes']:
            for prec in desc['precs']:
                for sign in desc['signedness']:

                    if prec > size:
                        continue
                    entry = copy.deepcopy({
                        "args": (["SYMBOLIC_BV_{}".format(size)] * n) + [str(prec), str(size), str(sign)],
                        "in_vectsize": size,
                        "out_vectsize": size // prec,
                        "lanesize": prec,
                        "in_precision" : prec,
                        "out_precision": 1,
                        "in_vectsize_index": n + 1,
                        "out_vectsize_index": None,
                        "in_lanesize_index": n,
                        "out_lanesize_index": None,
                        "in_precision_index": n,
                        "out_precision_index": None,
                        "arg_permute_map": [],
                        "Signedness": sign,
                        "Cost": "None",
                        "SIMD": "True",
                        "Extensions" : ['halide'],
                        "ctx_sema": desc["bvops"],
                    })


                    target_desc['target_instructions'][typed_name+"_p"+str(prec)+"_s"+str(size)+"_signed_"+str(sign)] = entry




        if typed_name in semantics_dict:



            for key in target_desc['target_instructions']:
                assert key not in semantics_dict[typed_name]['target_instructions'], "Key should not be present in dict"
                semantics_dict[typed_name]['target_instructions'][key] = target_desc['target_instructions'][key]
        else:
            semantics_dict[typed_name] = target_desc.copy()



    return semantics_dict


def create_widening_halide_dict_entry(classes):

    semantics_dict = {}

    for desc in classes:

        typed_name = desc['name']

        if desc['signedness'] == 1:
            typed_name = "typed-folded:signed-"+desc['name']
        elif desc['signedness'] == 0:
            typed_name = "typed-folded:unsigned-"+desc['name']

        target_desc = {"target_instructions": {}, "semantics": desc["bvops"]}
        for size in desc['sizes']:
            for prec in desc['precs']:
                if prec > size:
                    continue
                entry = copy.deepcopy({
                    "args": (["SYMBOLIC_BV_{}".format(size)] * 2) + [str(prec), str(size)],
                    "in_vectsize": size,
                    "out_vectsize": size * 2,
                    "lanesize": prec,
                    "in_precision" : prec,
                    "out_precision": prec * 2,
                    "in_vectsize_index": 3,
                    "out_vectsize_index": None,
                    "in_lanesize_index": 2,
                    "out_lanesize_index": 2,
                    "in_precision_index": 2,
                    "out_precision_index": 2,
                    "arg_permute_map": [],
                    "Signedness": desc['signedness'],
                    "Cost": "None",
                    "SIMD": "True",
                    "Extensions" : ['halide'],
                    "ctx_sema": desc["bvops"],
                })
                target_desc['target_instructions'][typed_name+"_p"+str(prec)+"_s"+str(size)+"_signed_"+str(desc['signedness'])] = entry

        if typed_name in semantics_dict:
            semantics_dict[typed_name]['semantics'] += desc['bvops']
            for key in target_desc['target_instructions']:
                semantics_dict[typed_name]['target_instructions'][key] = target_desc['target_instructions'][key]
        else:
            semantics_dict[typed_name] = target_desc


    return semantics_dict


reduce_contexts = [

    {"name": "vec-reduce-add", "bvops": ["bvadd", "extract"], "sizes": simd_sizes, "precs": simd_precs, "signedness": [-1], "reduce_factors": reduce_factors, 'sema': vec_reduce_sema} ,

]



def create_reduce_dict_entry(classes):

    semantics_dict = {}

    for desc in classes:
        target_desc = {"target_instructions": {},
                       "semantics": desc["sema"]}.copy()

        typed_name = "typed-folded:"+desc['name']
        for size in desc['sizes']:
            for prec in desc['precs']:
                for reduce_factor in desc['reduce_factors']:
                    for sign in desc['signedness']:

                        if prec > size:
                            continue


                        if size % reduce_factor != 0:
                            continue

                        if size // reduce_factor < prec:
                            continue


                        entry = copy.deepcopy({
                            "args": [str(reduce_factor), "SYMBOLIC_BV_{}".format(size), str(prec), str(size), str(sign)] ,
                            "in_vectsize": size,
                            "out_vectsize": size // reduce_factor,
                            "lanesize": prec,
                            "in_precision": prec,
                            "out_precision": prec,
                            "in_vectsize_index": 3,
                            "out_vectsize_index": None,
                            "in_lanesize_index": 2,
                            "out_lanesize_index": 2,
                            "in_precision_index": 2,
                            "out_precision_index": 2,
                            "arg_permute_map": [],
                            "Signedness": sign,
                            "Cost": "None",
                            "SIMD": "True",
                            "Extensions": ['halide'],
                            "ctx_sema": desc["bvops"],
                        })

                        target_desc['target_instructions'][typed_name+"_p" + str(prec)+"_s"+str(size)+"_signed_"+str(sign) + "_reduce_"+str(reduce_factor)] = entry

        if typed_name in semantics_dict:
            pass

        else:
            semantics_dict[typed_name] = target_desc.copy()

    return semantics_dict




unary_dict = create_nary_halide_dict_entry(halide_unary_ops_contexts, n = 1)
simd_dict = create_nary_halide_dict_entry(halide_binary_simd_ops_contexts, n = 2)
comparison_ops =  create_nary_comparison_halide_dict_entry(halide_binary_comparison_ops_contexts, n = 2)
broadcast_dict =  create_broadcast_halide_dict_entry(halide_broadcast_contexts)
reduce_dicts = create_reduce_dict_entry(reduce_contexts)
slice_dict = create_slice_halide_dict_entry(halide_slice_vector_contexts)
concat_dict = create_concat_halide_dict_entry(halide_concat_vector_contexts)
cast_extend_dict = create_cast_extend_halide_dict_entry(halide_cast_extend_ops_contexts)
cast_truncate_dict = create_cast_truncate_halide_dict_entry(halide_cast_truncate_ops_contexts)
cast_saturate_dict = create_cast_saturate_halide_dict_entry(halide_cast_saturate_ops_contexts)
binary_widen_ops_dict = create_nary_widen_halide_dict_entry(halide_binary_widen_prec_simd_ops_contexts, n = 2)


ternary_widen_ops_dict = create_nary_widen_halide_dict_entry(halide_ternary_widen_prec_simd_ops_contexts, n = 3)
"""
ternary_dict = create_nary_halide_dict_entry(halide_ternary_ops_contexts, n = 3)
widen_dict = create_widening_halide_dict_entry(halide_widening_ops_contexts)
"""


#halide_dicts = [concat_dict ,slice_dict, broadcast_dict, unary_dict ,simd_dict, cast_dict, ternary_dict, widen_dict, comparison_ops, reduce_dicts]
halide_dicts = [broadcast_dict,unary_dict, simd_dict, comparison_ops, reduce_dicts, slice_dict, concat_dict, cast_extend_dict, cast_truncate_dict , cast_saturate_dict, binary_widen_ops_dict, ternary_widen_ops_dict]




combined_dict = {}


for dict in halide_dicts:
    for key in dict:
        combined_dict[key] = dict[key]



print("halide_semantics = ", end = " ")
pp.pprint(combined_dict)
#print(json.dumps(combined_dict, indent = 4))





