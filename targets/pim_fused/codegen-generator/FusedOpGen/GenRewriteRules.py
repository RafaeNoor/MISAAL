# Generates the rewrite rules template for the fused operations by construction
import os
from common.Types import *
from  common.Instructions import Context
from pyparsing import nestedExpr
import copy
from sema.bitserial_fused_sema_v2 import bitserial_fused_sema_v2 as bitserial_fused_sema
from common.DSLParser import parse_dict
import json


class GenRewriteRules:
    def __init__(self, rewrite_rules_file, output_file_name, pim_dsl_list):
        self.rewrite_rules_file = rewrite_rules_file
        self.output_file_name = output_file_name
        self.pim_dsl_list = pim_dsl_list
        self.rewrite_rules = []
        self.visited_dsl_exprs = set()
        self.visited_counter = 0
        self.filter_condition = None
        assert os.path.exists(self.rewrite_rules_file), f"Rewrite rules file {self.rewrite_rules_file} does not exist"

    def get_ctx_by_name(self, ctx_name):
        for dsl_inst in self.pim_dsl_list:
            for ctx in dsl_inst.contexts:
                if ctx.name == ctx_name:
                    return ctx
        raise ValueError(f"Context {ctx_name} not found in PIM DSL list")

    def read_expression(self, expr, expected_bitwidth = None, expected_size = None):
        if isinstance(expr, list):
            print(f"Expression list: {expr}")
            assert len(expr) >= 2, f"Expression list: {expr} should have at least 2 elements"
            ctx_name = expr[0]
            ctx = self.get_ctx_by_name(ctx_name)

            expected_sizes = []
            expected_bitwidths = []
            arg_indicies = []
            for idx,arg in enumerate(ctx.context_args):
                if isinstance(arg, BitVector):
                    expected_bitwidths.append(min(ctx.in_precision, arg.size))
                    expected_sizes.append(arg.size)
                    arg_indicies.append(idx)
            assert len(expected_bitwidths) == len(expr) - 1, f"Expected bitwidths and sizes should have the same length"
            sub_exprs = []
            for i in range(1, len(expr)):
                sub_exprs.append(self.read_expression(expr[i], expected_bitwidths[i-1], expected_sizes[i-1]))
            ctx_copy = copy.deepcopy(ctx)
            perm = [v for v in ctx_copy.permutation]
            print(f"Permutation: {perm}")
            print(f"Indices: {arg_indicies}")
            # Permutation: [3, 2, 0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            # Indices: [0, 1, 3]


            sub_exprs_sorted = []

            for perm_idx in perm:
                if perm_idx in arg_indicies:
                    position = arg_indicies.index(perm_idx)
                    sub_exprs_sorted.append(sub_exprs[position])
            print(f"Sub exprs sorted: {sub_exprs_sorted}")







            for idx, sym_idx in enumerate(arg_indicies):
                assert isinstance(ctx_copy.context_args[sym_idx], BitVector), f"Context argument {sym_idx} is not a BitVector"
                ctx_copy.context_args[sym_idx] = sub_exprs_sorted[idx]
            print(f"Context: {ctx_copy.emit_context_expr_string()}")
            return ctx_copy
        elif isinstance(expr, str):
            assert expr.startswith("reg_"), f"Expression string: {expr} does not start with reg_"
            assert expected_bitwidth is not None, f"Expected bitwidth is not provided for expression: {expr}"
            assert expected_size is not None, f"Expected size is not provided for expression: {expr}"
            index = int(expr.split("_")[-1])
            return Reg(index, expected_bitwidth, expected_size)
        else:
            raise ValueError(f"Invalid expression type: {type(expr)}")

    def process_rewrite_rules(self):
        with open(self.rewrite_rules_file, "r") as f:
            lines = f.readlines()
            for idx, line in enumerate(lines):
                print(f"Processing line {idx}: {line}")
                line = line.strip()
                if "SRC EXPR" in line:
                    src_expr_str = lines[idx+1].strip()
                    assert "DST EXPR" in lines[idx+2], f"DST EXPR not found in line {idx+2}"
                    dst_expr_str = lines[idx+3].strip()
                    if self.filter_condition is not None and self.filter_condition(src_expr_str, dst_expr_str):
                        self.process_rewrite_rule(src_expr_str, dst_expr_str)
                    elif self.filter_condition is  None:
                        self.process_rewrite_rule(src_expr_str, dst_expr_str)

        self.get_rewrite_rules_description()

    def get_rewrite_rules_description(self):
        rewrite_rules_description = {}
        for src_expr, dst_expr in self.rewrite_rules:
            key = f"{src_expr.emit_context_expr_string()}_{dst_expr.emit_context_expr_string()}"
            prop = {}
            prop['property_name'] = "GenRewriteRule"
            prop["property"] = {
                "src": src_expr.emit_context_expr_string(),
                "dst": dst_expr.emit_context_expr_string(),
            }

            rewrite_rules_description[key] = [prop]

        with open(self.output_file_name, "w+") as f:
            json.dump(rewrite_rules_description, f, indent=4)


    def get_expr_as_dsl_str(self, expr_list):

        if isinstance(expr_list, list):
            assert len(expr_list) >= 2, f"Expression list: {expr_list} should have at least 2 elements"
            ctx_name = expr_list[0]
            ctx = self.get_ctx_by_name(ctx_name)
            dsl_name = ctx.dsl_name.split("_dsl")[0]

            return_expr = []
            return_expr.append(dsl_name)

            for expr in expr_list[1:]:
                return_expr.append(self.get_expr_as_dsl_str(expr))

            return_expr_str = "(" + " ".join(return_expr) + ")"
            return return_expr_str

        elif isinstance(expr_list, str):
            return expr_list
        else:
            assert False, f"Invalid expression type: {type(expr_list)}"








    def process_rewrite_rule(self, src_expr_str, dst_expr_str):
        src_brackets  = nestedExpr('(',')').parseString(src_expr_str).asList()
        dst_brackets  = nestedExpr('(',')').parseString(dst_expr_str).asList()
        print(src_brackets)
        print(dst_brackets)
        assert len(src_brackets) == 1, f"Expected 1 source expression, got {len(src_brackets)}"
        assert len(dst_brackets) == 1, f"Expected 1 destination expression, got {len(dst_brackets)}"

        src_expr_dsl_str = self.get_expr_as_dsl_str(src_brackets[0])

        if src_expr_dsl_str in self.visited_dsl_exprs:
            print("Already visited", src_expr_dsl_str )
            self.visited_counter += 1
            return
        else:
            self.visited_dsl_exprs.add(src_expr_dsl_str)

        src_expr = self.read_expression(src_brackets[0])


        dst_expr = self.read_expression(dst_brackets[0])


        print(src_expr.emit_context_expr_string())
        print(dst_expr.emit_context_expr_string())
        self.rewrite_rules.append((src_expr, dst_expr))




def custom_filter(src_str, dst_str):
    if "manual" in src_str or "manual" in dst_str:
        return True

    if "scaled" in src_str or "scaled" in dst_str:
        return True

    return False

if __name__ == "__main__":
    rewrite_rules_file = "rewrite_rules.txt"
    output_file_name = "pim_construction_rewrite_rules_templates.py"
    pim_dsl_list = parse_dict(bitserial_fused_sema, keep_duplicate = True)
    gen_rewrite_rules = GenRewriteRules(rewrite_rules_file, output_file_name, pim_dsl_list)

    #gen_rewrite_rules.filter_condition = custom_filter
    gen_rewrite_rules.process_rewrite_rules()
    print(f"Total rewrite rules: {len(gen_rewrite_rules.rewrite_rules)}")
    print(f"Visited repeated {gen_rewrite_rules.visited_counter} expressions")



