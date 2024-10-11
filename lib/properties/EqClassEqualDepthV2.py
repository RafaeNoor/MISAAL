from properties.Property import *
import os
import time
import glob
import pickle
from properties.EqClassEqualDepth import EqClassEqualDepth
import random
import sys
import json
from  utils.DSLInstructionUtils import *
from utils.GenerateRandomExpr import create_random_expression
from utils.CodeSynthesizerDesc import *
from utils.CanonicalizeExpressions import CanonicalizeExpression
import copy
from  common.Types import *
import itertools
import numpy as np
from grammar_gen.EqClassExpandGenerator import EqClassExpandGenerator
from utils.DoubleGrammarSynthesisUtils import DoubleGrammarSynthesisUtils

class EqClassEqualDepthV2(EqClassEqualDepth):


    def __init__(self, dsl_list = [], source_synth_desc = None, target_synth_desc = None, target_dsl_list = [], output_depth = 1, forward_map_path = None, swizzle_dsl_list = [], swizzle_map_path = None, commutative_map_path = None):



        super().__init__(dsl_list = dsl_list, source_synth_desc = source_synth_desc, target_synth_desc = target_synth_desc, target_dsl_list = target_dsl_list, output_depth = output_depth, forward_map_path = forward_map_path, swizzle_dsl_list = swizzle_dsl_list, swizzle_map_path = swizzle_map_path, commutative_map_path = commutative_map_path)
        self.name = "EqClassEqualDepthV2"
        self.synth_utils = DoubleGrammarSynthesisUtils(input_dsl_list = dsl_list, output_dsl_list = target_dsl_list, swizzle_dsl_list = swizzle_dsl_list, auxilary_dsl_list = [])


    def property_holds_on_candidate(self, candidate):


        src_eq_class = copy.deepcopy(candidate[0])
        arg_max = np.argmin([get_num_symbolic_args(ctx) for ctx in src_eq_class.contexts])
        src_ctx = src_eq_class.contexts[arg_max]
        dst_ctx = copy.deepcopy(candidate[1])
        relavent_output_subset = candidate[2]



        if isinstance(dst_ctx, Reg):
            return False


        dst_eq_class = self.get_eq_class(dst_ctx.dsl_name)

        matching_ctx = False
        for ctx in dst_eq_class.contexts:
            if ctx.out_vectsize == src_ctx.out_vectsize:
                matching_ctx = True

        if not matching_ctx:
            #print(dst_eq_class.name," has no context producing ", src_ctx.out_vectsize)
            return False



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



        success, src_expr_str, dst_expr_str = self.synth_utils.double_grammar_synthesis(src_ctx, dst_ctx)

        if success:
            key = self.serialize_candidate(candidate)
            self.simplify_map[key] = (src_expr_str, dst_expr_str)


        return success


    def serialize_candidate(self, candidate):
        return candidate[0].name+"_"+candidate[1].emit_context_expr_string()

    def get_property_on_candidate(self, candidate):
        key = self.serialize_candidate(candidate)
        (src_ctx_str, dst_ctx_str) = self.simplify_map[key]



        property_t = {"src": src_ctx_str, "dst": dst_ctx_str}
        return property_t





    def run_on_batch_completion(self):
        pass

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
        #self.output_dsl_list = self.filter_target_dsl_list(self.output_dsl_list)
        print("Target DSL")
        print_dsl_list_summary(self.output_dsl_list)


        #self.input_dsl_list = self.filter_source_dsl_list(self.input_dsl_list)


        # Candidate will be defined as:
        # (Equivalence class expression from input DSL, Equivalence class expression from output DSL)

        for dsl_inst in self.input_dsl_list:
            relavent_output_subset = self.get_relavent_output_dsl_subset(dsl_inst)
            print("Relavent set for ",dsl_inst.name)
            for ros in relavent_output_subset:
                print(ros.name)

            src_ctx = self.get_context_with_max_sym_bvs(dsl_inst)
            expressions = create_exhaustive_expressions_generator(relavent_output_subset, self.output_depth, use_eq_class = True, output_size = src_ctx.out_vectsize)
            counter = 0
            for expr in expressions:

                if get_expr_depth(expr) == self.output_depth:
                    canonical_expr = self.canonicalizer.canonicalize(expr)


                    # Hacky way
                    #if canonical_expr.emit_context_expr_string(use_reg_only = True) != expr.emit_context_expr_string(use_reg_only = True):
                    if not self.isCanonical(expr, canonical_expr):
                        continue

                    self.absolute_expr_count += self.get_absolute_count(canonical_expr) * self.get_absolute_count(src_ctx)
                    candidate = (dsl_inst, expr, relavent_output_subset)





                    yield candidate









