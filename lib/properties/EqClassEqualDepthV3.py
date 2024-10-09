from properties.Property import *
import os
import time
import glob
import pickle
from properties.EqClassEqualDepthV2 import EqClassEqualDepthV2
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

class EqClassEqualDepthV3(EqClassEqualDepthV2):


    def __init__(self, dsl_list = [], source_synth_desc = None, target_synth_desc = None, target_dsl_list = [], output_depth = 1, forward_map_path = None, swizzle_dsl_list = [], swizzle_map_path = None, commutative_map_path = None, input_depth = 2):



        super().__init__(dsl_list = dsl_list, source_synth_desc = source_synth_desc, target_synth_desc = target_synth_desc, target_dsl_list = target_dsl_list, output_depth = output_depth, forward_map_path = forward_map_path, swizzle_dsl_list = swizzle_dsl_list, swizzle_map_path = swizzle_map_path, commutative_map_path = commutative_map_path)
        self.name = "EqClassEqualDepthV3"
        self.synth_utils = DoubleGrammarSynthesisUtils(input_dsl_list = dsl_list, output_dsl_list = target_dsl_list, swizzle_dsl_list = swizzle_dsl_list, auxilary_dsl_list = [], force_contains_all_regs = True)
        self.input_depth = input_depth


    def property_holds_on_candidate(self, candidate):


        src_ctx = candidate[0]
        dst_ctx = candidate[1]

        success, src_expr_str, dst_expr_str = self.synth_utils.double_grammar_synthesis(src_ctx, dst_ctx)

        if success:
            key = self.serialize_candidate(candidate)
            self.simplify_map[key] = (src_expr_str, dst_expr_str)


        return success


    def serialize_candidate(self, candidate):
        return candidate[0].emit_context_expr_string()+"_"+candidate[1].emit_context_expr_string()

    def get_property_on_candidate(self, candidate):
        key = self.serialize_candidate(candidate)
        (src_ctx_str, dst_ctx_str) = self.simplify_map[key]



        property_t = {"src": src_ctx_str, "dst": dst_ctx_str}
        return property_t



    def count_contexts(self, expr, substr = None):
        if isinstance(expr, Context):

            child_results = 0

            for arg in expr.context_args:
                child_results += self.count_contexts(arg, substr = substr)

            if substr is None:
                return 1  + child_results
            else:
                if substr in expr.name:
                    return 1 + child_results
            return child_results
        return 0

    def custom_test(self, expr):
        num_nodes = self.count_contexts(expr)
        num_swizzles = self.count_contexts(expr, substr = "swizzle")


        return (num_nodes == 3) and (num_swizzles == 2) and ("swizzle" not in expr.name)

    def run_on_batch_completion(self):
        pass

    def generate_candidates(self):
        """Candidates are randomly generated programs of a specified depth (self.input_depth)

        Returns:
            [DSLExpressions]: _description_
        """

        candidates = []

        for dsl_inst in self.input_dsl_list:
            relavent_swizzle_subset = self.get_relavent_swizzle_dsl_subset(dsl_inst)
            relavent_output_subset = self.get_relavent_output_dsl_subset(dsl_inst)
            print("Relavent set for ",dsl_inst.name)
            for ros in relavent_output_subset:
                print(ros.name)

            sample_ctx = dsl_inst.get_sample_context()

            if sample_ctx.out_vectsize == None:
                continue

            src_ctx = self.get_context_with_min_sym_bvs(dsl_inst)

            if src_ctx.out_vectsize == None:
                continue

            if len(relavent_output_subset) == 0:
                continue

            src_expressions = create_exhaustive_expressions_generator(relavent_swizzle_subset + [dsl_inst], self.input_depth, use_eq_class = True, output_size = src_ctx.out_vectsize)
            for src_expr in src_expressions:

                if isinstance(src_expr, Reg):
                    continue

                if not self.custom_test(src_expr):
                    continue

                print(src_expr.dsl_name)
                if not self.expr_contains(src_expr, dsl_inst.name):
                    continue

                canonical_src_expr = self.canonicalizer.canonicalize(src_expr)

                if not self.canonicalizer.isCanonical(src_expr, canonical_src_expr):
                    continue

                target_expressions = create_exhaustive_expressions_generator(relavent_output_subset, self.output_depth, use_eq_class = True, output_size = src_expr.out_vectsize)
                for target_expr in target_expressions:


                    if isinstance(target_expr, Reg):
                        continue

                    if "add" not in target_expr.name:
                        continue

                    if self.count_contexts(target_expr, substr = "swizzle") > 0:
                        continue

                    if not self.count_contexts(target_expr, substr = "widen-mul") == 2:
                        continue

                    if get_expr_depth(target_expr) == self.output_depth:
                        canonical_target_expr = self.canonicalizer.canonicalize(target_expr)


                        # Hacky way
                        #if canonical_expr.emit_context_expr_string(use_reg_only = True) != expr.emit_context_expr_string(use_reg_only = True):
                        if not self.canonicalizer.isCanonical(target_expr, canonical_target_expr):
                            continue

                        self.absolute_expr_count += self.get_absolute_count(canonical_target_expr) * self.get_absolute_count(canonical_src_expr)
                        candidate = (canonical_src_expr, canonical_target_expr, relavent_output_subset)


                        yield candidate





    def get_context_with_min_sym_bvs(self, dsl_inst):
        arg_min = np.argmin([get_num_symbolic_args(ctx) for ctx in dsl_inst.contexts])

        min_ctx = dsl_inst.contexts[arg_min]
        valid_contexts = [ctx for ctx in dsl_inst.contexts if get_num_symbolic_args(ctx)  == get_num_symbolic_args(min_ctx)]

        max_out = 0
        max_ctx = None

        for ctx in valid_contexts:
            print(ctx.name)
            if ctx.out_vectsize > max_out:
                max_out = ctx.out_vectsize
                max_ctx = ctx


        assert not max_ctx is None, dsl_inst.name

        return max_ctx


