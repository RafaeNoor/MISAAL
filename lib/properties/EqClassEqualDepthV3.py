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

        # Variables to maintain current depth for logging purposes
        self.current_input_depth = 0
        self.current_output_depth = 0

        # Sort such that expressions with the least amount of related expressions are enumerated first
        self.sort_input_dsl_list()

    def sort_input_dsl_list(self):

        def num_related_ops(dsl_inst):
            output_set = self.get_relavent_output_dsl_subset(dsl_inst)
            return len(output_set)

        self.input_dsl_list = sorted(self.input_dsl_list, key = num_related_ops)

        for dsl_inst in self.input_dsl_list:
            print(dsl_inst.name)


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


    def run_on_batch_completion(self):
        pass

    def generate_candidates(self):
        """Candidates are randomly generated programs of a specified depth (self.input_depth)

        Returns:
            [DSLExpressions]: _description_
        """


        # Breadth first search
        for input_depth in range(1, self.input_depth+1):
            self.current_input_depth = input_depth
            max_out = min(self.output_depth, input_depth) + 1
            for output_depth in range(1, max_out):
                self.current_output_depth = output_depth
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

                    src_expressions = create_exhaustive_expressions_generator(relavent_swizzle_subset + [dsl_inst], input_depth, use_eq_class = True, output_size = src_ctx.out_vectsize)
                    for src_expr in src_expressions:

                        if isinstance(src_expr, Reg):
                            continue

                        if get_expr_depth(src_expr) != input_depth:
                            continue

                        if not self.expr_contains(src_expr, dsl_inst.name):
                            continue

                        canonical_src_expr = self.canonicalizer.canonicalize(src_expr)

                        if not self.canonicalizer.isCanonical(src_expr, canonical_src_expr):
                            continue

                        target_expressions = create_exhaustive_expressions_generator(relavent_output_subset, output_depth, use_eq_class = True, output_size = src_expr.out_vectsize)
                        for target_expr in target_expressions:


                            if isinstance(target_expr, Reg):
                                continue



                            if get_expr_depth(target_expr) == output_depth:
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

    def get_notify_body(self, count, success_count, start_time):
        parent_body = super().get_notify_body(count, success_count, start_time)
        depth_info = "Current Input Depth = {}, Current Output Depth = {}".format(self.current_input_depth, self.current_output_depth)

        return "\n".join([parent_body, depth_info])

