from common.Instructions import *
from utils.DoubleGrammarSynthesisUtils import DoubleGrammarSynthesisUtils


def verify_expression(expr: Context, dsl_inst_list: list):
    assert isinstance(expr, Context) == True
    for dsl_inst in dsl_inst_list:
        assert isinstance(dsl_inst, DSLInstruction) == True
        if expr.name == dsl_inst.name:
            for ctx in dsl_inst.contexts:
                assert isinstance(ctx, Context) == True
                assert len(expr.context_args) == len(ctx.context_args)
                found_match = False
                for lhs_arg, arg in zip(expr.context_args, ctx.context_args):
                    if isinstance(lhs_arg, Context):
                        verify_expression(arg, dsl_inst_list)
                    elif isinstance(lhs_arg, Reg):
                        assert isinstance(lhs_arg, Reg) == True
                    elif found_match == True:
                        if lhs_arg != arg:
                            found_match = False
                    else:
                        if lhs_arg == arg:
                            found_match = True
                assert found_match == True


def get_symbolic_bvs(expr: Context):
    assert isinstance(expr, Context) == True
    symbolic_args = list()
    for arg in expr.context_args:
        if isinstance(arg, Context):
            symbolic_args.extend(get_symbolic_bvs(arg))
        elif isinstance(arg, Reg):
            symbolic_args.append(arg)
    return symbolic_args


def get_barename(name: str):
    if "dsl" in name:
        name = name.split("_dsl")[0]
    if "typed:" in name:
        name = name.split("typed:")[1]
    if "p_" in name[::-1]:
        name_rev = name[::-1].split("p_")[1]
        name = name_rev[::-1]
    return name


def get_output_sizes(expr: Context, dsl_list: list):
    assert isinstance(expr, Context) == True
    output_sizes = set()
    for dsl_inst in dsl_list:
        assert isinstance(dsl_inst, DSLInstruction) == True
        dsl_inst_name = get_barename(dsl_inst.name)
        expr_name = get_barename(expr.name)
        if expr_name == dsl_inst_name:
            for ctx in dsl_inst.contexts:
                output_sizes.add(ctx.out_vectsize)
            break
    return list(output_sizes)


def get_input_sizes(expr: Context, dsl_list: list, input_sizes_dict: dict = dict()):
    assert isinstance(expr, Context) == True
    dict_idx = -1
    if len(input_sizes_dict.keys()) == 0:
        dict_idx = 0
    for dsl_inst in dsl_list:
        assert isinstance(dsl_inst, DSLInstruction) == True
        dsl_inst_name = get_barename(dsl_inst.name)
        expr_name = get_barename(expr.name)
        if expr_name == dsl_inst_name:
            for ctx_idx, ctx in enumerate(dsl_inst.contexts):
                if dict_idx == 0:
                    input_sizes_dict[ctx_idx] = list()
                for arg in expr.context_args:
                    if isinstance(arg, Context):
                        input_sizes_dict = get_input_sizes(
                            arg, dsl_list, input_sizes_dict
                        )
                    elif isinstance(arg, Reg):
                        if dict_idx == 0:
                            input_sizes_dict[ctx_idx].append(ctx.in_vectsize)
                        else:
                            for key in input_sizes_dict.keys():
                                input_sizes_dict[key].append(ctx.in_vectsize)
            break
    # Get rid of duplicate entries
    result = {}
    for key, value in input_sizes_dict.items():
        if value not in result.values():
            result[key] = value
    input_sizes_dict = result
    return input_sizes_dict


def generate_candidates(
    lhs_expr: Context, lhs_dsl_list: list, rhs_expr: Context, rhs_dsl_list: list
):
    # print("\n\nGENERATE CANDIDATES")
    lhs_to_rhs_patterns = dict()
    verify_expression(lhs_expr, lhs_dsl_list)
    output_sizes = get_output_sizes(lhs_expr, lhs_dsl_list)
    # print("output_sizes:")
    # print(output_sizes)
    input_sizes_dict = get_input_sizes(lhs_expr, lhs_dsl_list)
    # print("input_sizes_dict:")
    # print(input_sizes_dict)
    num_lhs_inputs = get_symbolic_bvs(lhs_expr)
    num_rhs_inputs = get_symbolic_bvs(rhs_expr)
    synthesizer = DoubleGrammarSynthesisUtils(lhs_dsl_list, rhs_dsl_list)
    for output_size in output_sizes:
        for _, input_sizes in input_sizes_dict.items():
            # print("===========================")
            # print("output_size:")
            # print(output_size)
            # print("input_sizes:")
            # print(input_sizes)
            success, src_expr_str, dst_expr_str = synthesizer.double_grammar_synthesis(
                lhs_expr,
                rhs_expr,
                custom_src_output_size=output_size,
                custom_dst_output_size=output_size,
                custom_src_input_sizes=input_sizes,
                custom_target_input_sizes=input_sizes,
            )
            if success:
                print("ENUMO_SUCC")
                print("SUCCESS at output size {}!".format(output_size))
                print("Corresponding LHS concretization:")
                print(src_expr_str)
                print("Corresponding RHS concretization:")
                print(dst_expr_str)
            else:
                print("FAILURE!")


def generalize_rules(
    lhs_expr: Context, lhs_dsl_list: list, rhs_expr: Context, rhs_dsl_list: list
):
    assert isinstance(rhs_expr, Context) == True
    assert isinstance(lhs_expr, Context) == True
    print("len(lhs_dsl_list):")
    print(len(lhs_dsl_list))
    print("len(rhs_dsl_list):")
    print(len(rhs_dsl_list))
    generate_candidates(lhs_expr, lhs_dsl_list, rhs_expr, rhs_dsl_list)


# def generalize_pattern(pattern : Pattern):
#  rhs_expr = pattern.src_expr
#  lhs_expr = pattern.target_expr
#  #generalize_rules(lhs_expr, rhs_expr)


from utils.ReadDSL import read_string_to_dsl
from common.DSLParser import parse_dict
from sema.hexsemantics_new import semantics as hvx_semantics
from sema.halide_sema import halide_semantics
from utils.DSLInstructionUtils import *


import os
import json
import sys
from os import listdir
from os.path import isfile, join
from collections import defaultdict


# Uncomment below line to keep intermediate racket files
# keep_temporary_files()

# Parse the dictionay into a list of DSLInstruction types
hvx_dsl_list = parse_dict(hvx_semantics)
halide_dsl_list = parse_dict(halide_semantics)

# file_name = sys.argv[1]
# expr_file = open(file_name)
# content = expr_file.readlines()
# hvx_expr_str = content[1]
# halide_expr_str = content[0]

hvx_expr_str = "(hexagon_V6_vminuh_128B (reg (bv #x00 8)) (hexagon_V6_vminuh_128B (reg (bv #x00 8)) (reg (bv #x01 8)) 1024 1024 0 1024 16 0 0) 1024 1024 0 1024 16 0 0)"
halide_expr_str = "(typed:unsigned-vec-min (reg (bv #x00 8)) (typed:unsigned-vec-min (reg (bv #x00 8)) (reg (bv #x01 8)) 16 1024) 16 1024)"

hvx_expr_ctx = read_string_to_dsl(hvx_expr_str, hvx_dsl_list)
halide_expr_ctx = read_string_to_dsl(halide_expr_str, halide_dsl_list)

print("=" * 5, "Pretty Printing Expressions", "=" * 5)
print(hvx_expr_ctx.emit_context_expr_string())
print(halide_expr_ctx.emit_context_expr_string())


def to_camel_case(snake_str):
    return "".join(x.capitalize() for x in snake_str.lower().split("_"))


def get_all_inst_names(dsl_list):
    ret = []
    print("Printing Inst names")
    for dsl_inst in dsl_list:
        ret.append(dsl_inst.name)
    return ret


def get_num_symbolic_args_from_inst(dsl_inst):
    nums = [get_num_symbolic_args(ctx) for ctx in dsl_inst.contexts]
    names = [ctx.name for ctx in dsl_inst.contexts]
    print(f"Nums for {dsl_inst} : {nums}")
    print(f"Names for {dsl_inst} : {names}")
    assert len(set(nums)) == 1
    return nums[0]


def generate_lang_terms_from_dsl_list(dsl_list):
    ret = []
    for inst in dsl_list:
        curr_num_sym = 0
        for ctx in inst.contexts:
            if curr_num_sym == 0:
                curr_num_sym = get_num_symbolic_args(ctx)
                if curr_num_sym == 1:
                    ret.append(f'"{inst.name}" = {to_camel_case(inst.name)}(Id),')
                else:
                    ret.append(
                        f'"{inst.name}" = {to_camel_case(inst.name)}([Id;({curr_num_sym})]),'
                    )
            elif curr_num_sym != get_num_symbolic_args(ctx):
                if get_num_symbolic_args(ctx) == 1:
                    ret.append(f'"{ctx.name}" = {to_camel_case(ctx.name)}(Id),')
                else:
                    ret.append(
                        f'"{ctx.name}" = {to_camel_case(ctx.name)}([Id;({get_num_symbolic_args(ctx)})]),'
                    )
            else:
                continue
    return ret


def generate_eval_terms_from_dsl_list(dsl_list):
    ret = []
    for inst in dsl_list:
        curr_num_sym = 0
        for ctx in inst.contexts:
            if curr_num_sym == 0:
                curr_num_sym = get_num_symbolic_args(ctx)
                if curr_num_sym == 1:
                    ret.append(f"MISAALLang::{to_camel_case(inst.name)}(a) => vec[]!")
                else:
                    ret.append(
                        f"MISAALLang::{to_camel_case(inst.name)}({[chr(i + 97) for i in range(0, curr_num_sym)]}) => vec[]!".replace(
                            "'", ""
                        )
                    )
            elif curr_num_sym != get_num_symbolic_args(ctx):
                if get_num_symbolic_args(ctx) == 1:
                    ret.append(f"MISAALLang::{to_camel_case(ctx.name)}(a) => vec[]!")
                else:
                    ret.append(
                        f"MISAALLang::{to_camel_case(ctx.name)}({[chr(i + 97) for i in range(0, get_num_symbolic_args(ctx))]}) => vec[]!".replace(
                            "'", ""
                        )
                    )
            else:
                continue
    return ret


# misaal_lang_terms = generate_lang_terms_from_dsl_list(hvx_dsl_list) + generate_lang_terms_from_dsl_list(halide_dsl_list)


def gen_egg_lang(dsl_lists):
    ret_str = "egg::define_language! {\n"
    ret_str += "\tpub enum MISAALLang {\n"
    ret_str += "\t\tLit(Constant),\n"
    for dsl_list in dsl_lists:
        terms = generate_lang_terms_from_dsl_list(dsl_list)
        for term in terms:
            ret_str += f"\t\t{term}\n"
    ret_str += "\t\tVar(Symbol),\n"
    ret_str += "\t}\n"
    ret_str += "}\n"
    return ret_str


def gen_egg_evaluator(dsl_lists):
    ret_str = """fn eval<'a, F>(&'a self, cvec_len: usize, mut get_cvec: F) -> CVec<Self>
    where
        F: FnMut(&'a Id) -> &'a CVec<Self>,
    {
        match self {\n"""
    ret_str += "\t\tMISAALLang::Lit(c) => vec![],\n"
    for dsl_list in dsl_lists:
        terms = generate_eval_terms_from_dsl_list(dsl_list)
        for term in terms:
            ret_str += f"\t\t{term}\n"
    ret_str += " \t\tMISAALLang::Var(_) => vec![],\n"
    ret_str += "\t}\n"
    ret_str += "}\n"
    return ret_str


def generate_enumo_langs(relevance_sets, depth, dsl_lists):
    ret_str = ""
    for i, relevance_set in enumerate(relevance_sets):
        opset = relevance_sets[relevance_set]
        opset.append(relevance_set)
        # print("Opset: ", opset)
        # get num symbolic args from context name
        ret_str += f"let lang_{i} = Lang::new(\n"
        val_list = [
            str(i) for i in range(0, depth * 3)
        ]  # 3 is max num of sym args; parameterize this
        var_list = [
            chr(i + 97) for i in range(0, depth * 3)
        ]  # 3 is max num of sym args; parameterize this
        ret_str += f"\t&{val_list},\n"
        ret_str += f"\t&{var_list},\n"

        op_dict = defaultdict(list)
        for op in opset:
            for dsl_list in dsl_lists:
                for inst in dsl_list:
                    if op == inst.name:
                        # get all contexts with same logic as lang
                        curr_num_sym = 0
                        for ctx in inst.contexts:
                            if curr_num_sym == 0:
                                curr_num_sym = get_num_symbolic_args(ctx)
                                op_dict[str(curr_num_sym)].append(inst.name)
                            elif curr_num_sym != get_num_symbolic_args(ctx):
                                op_dict[str(get_num_symbolic_args(ctx))].append(ctx)
                            else:
                                continue
        for i in op_dict.values():
            ret_str += f"\t&{i},\n"

        ret_str += "\t);\n\n"

        num_sym_args = len(op_dict.keys())

        ret_str += f'let wkld_{i} = iter_metric(base_lang({num_sym_args}), "EXPR", Metric::Depth, {depth})\n'
        ret_str += '\t.plug("VAR", &Workload::new(lang_{i}.vars))\n'
        ret_str += '\t.plug("VAL", &Workload::empty())\n'
        for i in range(0, num_sym_args):
            ret_str += f'\t.plug("OP{i+1}", &Workload::new(lang_{i}.ops[{i}].clone()))\n'
        ret_str += "\t);\n\n"

    return ret_str


f = open("repair_forward_map.json")

relevance_sets = json.load(f)

print(gen_egg_lang([hvx_dsl_list, halide_dsl_list]))
print(gen_egg_evaluator([hvx_dsl_list, halide_dsl_list]))
print(generate_enumo_langs(relevance_sets, 3, [hvx_dsl_list, halide_dsl_list]))

# generate new Lang for each relevance set so that is the onl
