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


    def __init__(self, dsl_list = [], source_synth_desc = None, target_synth_desc = None, target_dsl_list = [], output_depth = 1, forward_map_path = None, swizzle_dsl_list = [], swizzle_map_path = None, commutative_map_path = None, input_depth = 2, depth_range = False, use_canon_map = True):



        super().__init__(dsl_list = dsl_list, source_synth_desc = source_synth_desc, target_synth_desc = target_synth_desc, target_dsl_list = target_dsl_list, output_depth = output_depth, forward_map_path = forward_map_path, swizzle_dsl_list = swizzle_dsl_list, swizzle_map_path = swizzle_map_path, commutative_map_path = commutative_map_path)
        self.name = "EqClassEqualDepthV3"
        self.synth_utils = DoubleGrammarSynthesisUtils(input_dsl_list = dsl_list, output_dsl_list = target_dsl_list, swizzle_dsl_list = swizzle_dsl_list, auxilary_dsl_list = [], force_contains_all_regs = True)
        self.input_depth = input_depth

        # Variables to maintain current depth for logging purposes
        self.current_input_depth = 0
        self.current_output_depth = 0

        # Sort such that expressions with the least amount of related expressions are enumerated first
        self.sort_input_dsl_list()

        self.depth_range = depth_range


        self.src_canon_map = {}
        self.target_canon_map = {}
        self.use_canon_map = use_canon_map

        self.canon_skipped_src = 0
        self.canon_skipped_dst = 0



    def get_cannon_map_key(self, expr):
        return expr.emit_context_expr_string()

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

    def custom_condition(self, expr):
        if expr.dsl_name.split("_dsl")[0] != 'typed:vec-add':
            return False

        conditions  = [True]
        num_reduce = self.count_contexts(expr ,"reduce") == 1
        num_widen = self.count_contexts(expr ,"widen") == 1
        num_add = self.count_contexts(expr ,"vec-add") == 1
        num_cast = self.count_contexts(expr ,"cast") == 2

        conditions.append(num_reduce)
        conditions.append(num_widen)
        conditions.append(num_add)
        conditions.append(num_cast)


        return all(conditions)

    def custom_expr(self):

        def get_eq_class(name):
            for dsl_inst in self.input_dsl_list + self.output_dsl_list:
                if dsl_inst.name == name:
                    return copy.deepcopy(dsl_inst)

        def get_ctx_with_size(dsl_inst, size):
            for ctx in dsl_inst.contexts:
                if ctx.out_vectsize == size:
                    return ctx

        vec_add = get_eq_class("typed:vec-add")
        widen_mul = get_eq_class("typed:signed-vec-widen-mul")
        reduce_vec = get_eq_class("typed:signed-vector_reduce_add")
        cast_uint = get_eq_class("typed:cast-uint")
        cast_int = get_eq_class("typed:cast-int")

        add_512 = get_ctx_with_size(vec_add, 512)
        reduce_add_512 = get_ctx_with_size(reduce_vec, 512)
        widen_mul_2048 =  get_ctx_with_size(widen_mul, 2048)
        cast_int_1024 = get_ctx_with_size(cast_int, 1024)
        cast_uint_1024 = get_ctx_with_size(cast_uint, 1024)

        ctxs = [add_512, reduce_add_512, widen_mul_2048, cast_int_1024, cast_uint_1024]

        for idx, ctx in enumerate(ctxs):
            assert not ctx is None

        # Start bottom up
        reg0 = Reg("0", 8, 512)
        reg1 = Reg("1", 8, 512)
        reg2 = Reg("2", 32, 512)

        cast_int_1024.context_args[0] = reg0
        cast_uint_1024.context_args[0] = reg1

        widen_mul_2048.context_args[0] = cast_int_1024
        widen_mul_2048.context_args[1] = cast_uint_1024
        reduce_add_512.context_args[1] = widen_mul_2048
        add_512.context_args[0] = reg2
        add_512.context_args[1] = reduce_add_512

        return add_512


    def run_on_batch_completion(self):
        pass

    def generate_candidates(self):
        """Candidates are randomly generated programs of a specified depth (self.input_depth)

        Returns:
            [DSLExpressions]: _description_
        """

        input_start = 1
        output_start = 1

        if not self.depth_range:
            input_start = self.input_depth
            output_start = self.output_depth

        # Breadth first search
        for input_depth in range(input_start, self.input_depth+1):
            self.current_input_depth = input_depth
            #max_out = min(self.output_depth, input_depth) + 1
            max_out = self.output_depth  + 1
            for output_depth in range(output_start, max_out):
                self.current_output_depth = output_depth
                for dsl_inst in self.input_dsl_list:
                    relavent_swizzle_subset = self.get_relavent_swizzle_dsl_subset(dsl_inst)
                    relavent_output_subset = self.get_relavent_output_dsl_subset(dsl_inst)
                    relavent_output_subset.reverse()
                    print("Relavent set for ",dsl_inst.name)
                    for idx, ros in enumerate(relavent_output_subset):
                        print(idx, ".", ros.name)

                    sample_ctx = dsl_inst.get_sample_context()


                    if sample_ctx.out_vectsize == None:
                        continue

                    src_ctx = self.get_context_with_min_sym_bvs(dsl_inst)

                    if src_ctx.out_vectsize == None:
                        continue

                    if len(relavent_output_subset) == 0:
                        continue

                    src_expressions = create_exhaustive_expressions_generator(relavent_swizzle_subset + [dsl_inst], input_depth, use_eq_class = True, output_size = src_ctx.out_vectsize)

                    self.src_canon_map.clear()
                    for src_expr in src_expressions:

                        if isinstance(src_expr, Reg):
                            continue

                        if get_expr_depth(src_expr) != input_depth:
                            continue


                        if not self.expr_contains(src_expr, dsl_inst.name):
                            continue

                        canonical_src_expr = self.canonicalizer.canonicalize(src_expr)

                        if self.use_canon_map:
                            canon_map_key = canonical_src_expr.emit_context_expr_string()
                            if canon_map_key in self.src_canon_map:
                                self.canon_skipped_src += 1
                                continue
                            self.src_canon_map[canon_map_key] = 1
                        else:
                            if not self.canonicalizer.isCanonical(src_expr, canonical_src_expr):
                                self.canon_skipped_src += 1
                                continue

                        target_expressions = create_exhaustive_expressions_generator(relavent_output_subset, output_depth, use_eq_class = True, output_size = src_expr.out_vectsize)
                        self.target_canon_map.clear()
                        for target_count ,target_expr in enumerate(target_expressions):

                            if isinstance(target_expr, Reg):
                                continue


                            if get_expr_depth(target_expr) == output_depth:
                                canonical_target_expr = self.canonicalizer.canonicalize(target_expr)

                                if self.use_canon_map:
                                    canon_map_key = canonical_target_expr.emit_context_expr_string()
                                    if canon_map_key in self.target_canon_map:
                                        self.canon_skipped_dst += 1
                                        continue

                                    self.target_canon_map[canon_map_key] = 1


                                else:
                                    if not self.canonicalizer.isCanonical(target_expr, canonical_target_expr):
                                        self.canon_skipped_dst += 1
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
        skipped_srcs = "Canonicalizer skipped {} Src expressions".format(self.canon_skipped_src)
        skipped_dsts = "Canonicalizer skipped {} Target expressions".format(self.canon_skipped_dst)

        return "\n".join([parent_body, depth_info, skipped_srcs, skipped_dsts])

