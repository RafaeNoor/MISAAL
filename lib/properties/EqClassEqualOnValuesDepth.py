from properties.Property import *
import os
import time
import glob
import pickle
from properties.EqualOnValues import EqualOnValues
import random
import sys
import json
from  utils.DSLInstructionUtils import *
from utils.GenerateRandomExpr import create_random_expression
import copy
from  common.Types import *
import itertools
import numpy as np
from grammar_gen.EqClassExpandGenerator import EqClassExpandGenerator

class EqClassEqualOnValuesDepth(EqualOnValues):


    def __init__(self, dsl_list = [], source_synth_desc = None, target_synth_desc = None, target_dsl_list = [], output_depth = 1):


        print("Source DSL List size:", len(dsl_list))
        print("Target DSL List size:", len(target_dsl_list))

        super().__init__(dsl_list = dsl_list, source_synth_desc = source_synth_desc, target_synth_desc = target_synth_desc, target_dsl_list = target_dsl_list)
        self.name = "EqClassEqualOnValuesDepth"
        self.output_depth = output_depth
        self.is_candidate_generator = True



    def filter_target_dsl_list(self, dsl_list):
        filtered = []

        substrs = ["cast-int", "reduce"]#, "widen-mul"]
        #substrs = ["typed:vec-bwand"]
        contexts = ["typed:cast-int_0_ip8_is1024_op32_os4096_signed_1","typed:signed_vector_reduce_add_w4_4096_32_4096"]
        #contexts = []
        for dsl_inst in dsl_list:
            include = any([s in dsl_inst.name for s in substrs])
            if not include:
                continue

            dsl_inst_copy = copy.deepcopy(dsl_inst)

            if False:
                dsl_inst_copy.contexts = []
                for ctx in dsl_inst.contexts:
                    if ctx.name not in contexts:
                        continue

                    if "hvx" in self.source_synth_desc.target_name:
                        if ctx.out_vectsize not in [1024, 2048, 4096]:
                            continue

                        dsl_inst_copy.contexts.append(ctx)



            filtered.append(dsl_inst_copy)


        return filtered



    def filter_source_dsl_list(self, dsl_list):
        filtered = []

        ctxs = ["hexagon_V6_vrmpybv_acc_128B"]
        substrs = ["hexagon_V6_vrmpybv_128B"]
        for dsl_inst in dsl_list:
            insert = any([s in dsl_inst.name for s in substrs])

            if insert:
                dsl_inst.contexts = [c for c in dsl_inst.contexts if c.name in ctxs]
                filtered.append(dsl_inst)

        return filtered



    def get_property_desc(self):
        return "Identifies values for which two expressions in different dsls may be equal"

    def generate_candidates(self):
        """Candidates are randomly generated programs of a specified depth (self.input_depth)

        Returns:
            [DSLExpressions]: _description_
        """

        candidates = []

        print("Source DSL")
        print_dsl_list_summary(self.input_dsl_list)

        print("Target DSL [Pre Filter]")
        print_dsl_list_summary(self.output_dsl_list)
        # self.output_dsl_list = self.filter_target_dsl_list(self.output_dsl_list)
        print("Target DSL")
        print_dsl_list_summary(self.output_dsl_list)


        self.input_dsl_list = self.filter_source_dsl_list(self.input_dsl_list)


        # Candidate will be defined as:
        # (Equivalence class expression from input DSL, Equivalence class expression from output DSL)

        for dsl_inst in self.input_dsl_list:
            expressions = create_exhaustive_expressions_generator(self.output_dsl_list, self.output_depth, use_eq_class = True)
            for expr in expressions:
                candidate = (dsl_inst, expr)
                yield candidate





    def property_holds_on_candidate(self, candidate):


        src_eq_class = copy.deepcopy(candidate[0])

        arg_max = np.argmax([get_num_symbolic_args(ctx) for ctx in src_eq_class.contexts])
        src_ctx = src_eq_class.contexts[arg_max]
        dst_ctx = copy.deepcopy(candidate[1])



        num_src_ctx_args = self.get_context_num_sym_args(src_ctx)
        input_sizes = self.get_context_input_sizes(src_ctx)
        output_size = src_ctx.out_vectsize
        precision = src_ctx.in_precision

        src_ctx_sym_args = self.get_context_sym_args(src_ctx)

        src_ctx_regs = []

        reg_arg_map = {}
        for idx, arg in enumerate(src_ctx_sym_args):
            reg = Reg(str(idx),precision, arg.size)
            src_ctx_regs.append(reg)

            key = str(arg.size)
            if key not in reg_arg_map:
                reg_arg_map[key] = []
            reg_arg_map[key].append(reg)



        src_regs_count = len(src_ctx_regs)

        # Bind arguments to the source context

        count = 0
        for idx, arg in enumerate(src_ctx.context_args):
            if not isinstance(arg, BitVector):
                continue
            src_ctx.context_args[idx] = src_ctx_regs[count]
            count += 1


        # Bind expression to target expression
        reg_arg_idx_map = {}
        for key in reg_arg_map:
            reg_arg_idx_map[key] = 0

        dst_regs = self.get_registers(dst_ctx)


        common_param =  False

        for idx, arg in enumerate(dst_regs):
            reg = None
            key = str(arg.size)
            if key not in reg_arg_idx_map:
                # Create a new register for left over values
                reg = Reg(str(len(src_ctx_regs)), precision, arg.size)
                src_ctx_regs.append(reg)
            else:
                index = reg_arg_idx_map[key]
                reg = reg_arg_map[key][index]
                updated_index = (index + 1) % len(reg_arg_map[key])
                reg_arg_idx_map[key] = updated_index

            if int(reg.index) < src_regs_count:
                common_param = True

            arg.index = reg.index
            arg.precision = reg.precision
            arg.size = reg.size
            arg.signed = reg.signed

        if not common_param:
            return False


        #print(src_ctx.emit_context_expr_string())
        #print(dst_ctx.emit_context_expr_string())

        language_to_symbol = {"hvx": "'hvx",
                              "x86": "'x86",
                              "halide": "'halide" ,
                              "halide_hvx": "'halide",
                              "halide_x86": "'halide",
                              }

        statements = []

        src_language_desc = self.source_synth_desc
        target_language_desc = self.target_synth_desc

        target_language_dsl = self.output_dsl_list
        src_language_dsl = self.input_dsl_list

        if src_language_desc.emit_interpreter:
            statements.append(src_language_desc.emit_interpreter_framework(src_language_dsl))


        if target_language_desc.emit_interpreter and src_language_desc.target_name != target_language_desc.target_name:
            statements.append(target_language_desc.emit_interpreter_framework(target_language_dsl))


        env = []
        for idx in range(len(src_ctx_regs)):
            value = "(?? (bitvector {}))".format(src_ctx_regs[idx].size)
            env.append(value)


        define_env = "(define env (vector {}))".format(" ".join(env))
        statements.append(define_env)

        # symbolic operands are non-zero
        statements.append("(assert-non-zero-env env)")



        src_expression = "(define src-expr\n {}\n)".format(src_ctx.emit_context_expr_string())

        statements.append(src_expression)

        # Define dst expression as a grammar of possible
        # concrete Eq class members in the same structure

        GrammarGenerator = EqClassExpandGenerator(dsl_list = target_language_dsl, output_bitwidth = output_size, input_sizes = [arg.size for arg in src_ctx_regs])
        dst_expression_label ,dst_expression_grammar =  GrammarGenerator.emit_grammar(dst_ctx)

        statements.append(dst_expression_grammar)
        dst_expression = "(define dst-expr\n ({})\n)".format(dst_expression_label)
        statements.append(dst_expression)

        src_result = "(define src-result {})".format(src_language_desc.interpret_expr("src-expr", "env"))

        dst_result = "(define dst-result {})".format(target_language_desc.interpret_expr("dst-expr", "env"))
        statements.append(src_result)
        statements.append(dst_result)

        slice_size = min(64, src_ctx.out_vectsize)

        src_slice = "(define src-slice (extract {} 0 src-result))".format(slice_size - 1)

        dst_slice = "(define dst-slice (extract {} 0 dst-result))".format(slice_size - 1)

        statements.append(src_slice)
        statements.append(dst_slice)


        statements.append("(assert (not (equal? src-slice (bv 0 (bitvector {})))))".format(slice_size))

        # Assert result is not equal to any input operand (when types match)
        statements.append("(assert-value-not-in-env src-result env)")



        get_cex = "(define cex {})".format(self.emit_verify_not_equal("src-slice", "dst-slice"))

        statements.append(get_cex)


        if_sat = "(exit 0)"
        if_unsat = "(exit 1)"

        conditional = "(cond [(sat? cex) {}] [else {}])".format(if_sat, if_unsat)
        statements.append(conditional)

        result = execute_racket_file(statements)

        is_simplified = result.returncode == 0


        if is_simplified:
            key = self.serialize_candidate(candidate)
            pair = (src_ctx, dst_ctx)
            self.simplify_map[key] = pair

        return is_simplified

    def get_ctx_expr_eq_class_names(self, expr):

        if isinstance(expr, Context):
            names = [expr.dsl_name.split("_dsl")[0]]
            for arg in expr.context_args:
                names += self.get_ctx_expr_eq_class_names(arg)
            return list(set(names))
        else:
            return []


    def serialize_candidate(self, candidate):
        return candidate[0].name+"_"+candidate[1].emit_context_expr_string()

    def get_property_on_candidate(self, candidate):
        key = self.serialize_candidate(candidate)
        (src_ctx, dst_ctx) = self.simplify_map[key]

        src_names = self.get_ctx_expr_eq_class_names(src_ctx)
        dst_names = self.get_ctx_expr_eq_class_names(dst_ctx)

        src_name = src_names[0]

        if src_name not in self.forward_map:
            self.forward_map[src_name] = []


        for dst_name in dst_names:
            if dst_name not in self.backward_map:
                self.backward_map[dst_name] = []

        for dst_name in dst_names:
            self.forward_map[src_name].append(dst_name)
            self.backward_map[dst_name].append(src_name)



        property_t = {"src": src_ctx.emit_context_expr_string(), "dst": dst_ctx.emit_context_expr_string()}
        return property_t





    def emit_property_to_egg(self, property_map):
        return []







