from common.Instructions import *
from utils.DoubleGrammarSynthesisUtils import DoubleGrammarSynthesisUtils

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

""" print("Context args for HVX expr: ", get_non_symbolic_bvs(hvx_expr_ctx))
for i in get_non_symbolic_bvs(hvx_expr_ctx):
    print(i.value)
 """
print("=" * 5, "Pretty Printing Expressions", "=" * 5)
print(hvx_expr_ctx.emit_context_expr_string())
print(halide_expr_ctx.emit_context_expr_string())


def to_camel_case(snake_str):
    return (
        "".join(x.capitalize() for x in snake_str.lower().split("_"))
        .replace(":", "_")
        .replace("-", "_")
    )


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
    for idx, relevance_set in enumerate(relevance_sets):
        opset = relevance_sets[relevance_set]
        opset.append(relevance_set)
        # print("Opset: ", opset)
        # get num symbolic args from context name
        ret_str += f"let lang_{idx} = Lang::new(\n"
        val_list = [
            str(i) for i in range(0, depth * 3)
        ]  # 3 is max num of sym args; parameterize this
        var_list = [
            chr(i + 97) for i in range(0, depth * 3)
        ]  # 3 is max num of sym args; parameterize this
        ret_str += f"\t&{val_list},\n"
        ret_str += f"\t&{var_list},\n"
        ret_str += "\t&[\n"
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
        max_args = max([int(i) for i in op_dict.keys()])
        for i in range(max_args):
            if op_dict[str(i + 1)] == []:
                ret_str += "\t\t&[],\n"
            else:
                ret_str += f"\t\t&{op_dict[str(i + 1)]},\n"

        ret_str += "\t],\n"
        ret_str += ");\n\n"

        num_sym_args = len(op_dict.keys())

        ret_str += f'let wkld_{idx} = iter_metric(base_lang({num_sym_args}), "EXPR", Metric::Depth, {depth})\n'
        ret_str += f'\t.plug("VAR", &Workload::new(lang_{idx}.vars))\n'
        ret_str += '\t.plug("VAL", &Workload::empty())\n'
        for arg in range(0, num_sym_args):
            ret_str += (
                f'\t.plug("OP{arg+1}", &Workload::new(lang_{idx}.ops[{arg}].clone()))\n'
            )
        ret_str += ";\n\n"

    ret_str = ret_str.replace("'", '"')

    return ret_str


def get_non_symbolic_bvs(expr: Context):
    assert isinstance(expr, Context) == True
    non_symbolic_args = list()
    for arg in expr.context_args:
        # need a way to print BV values
        if isinstance(arg, ConstBitVector):
            non_symbolic_args.append(f"{arg.get_dsl_value()}")
        elif (
            not isinstance(arg, Reg)
            and not isinstance(arg, Context)
            and not isinstance(arg, BitVector)
        ):
            non_symbolic_args.append(arg.value)
    return non_symbolic_args


def generate_validator_from_dsl_list(dsl_list):
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

f = open("repair_forward_map.json")

relevance_sets = json.load(f)

print(
    "non sym args for ctx: ",
    [
        i
        for i in get_non_symbolic_bvs(
            ctx_from_name("hexagon_V6_vrmpybv_128B", hvx_dsl_list)
        )
    ],
)

print(gen_egg_lang([hvx_dsl_list, halide_dsl_list]))
print(gen_egg_evaluator([hvx_dsl_list, halide_dsl_list]))
print(generate_enumo_langs(relevance_sets, 3, [hvx_dsl_list, halide_dsl_list]))

# generate new Lang for each relevance set so that is the onl
