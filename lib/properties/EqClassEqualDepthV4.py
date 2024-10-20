from properties.Property import *
import os
import time
import glob
import pickle
from properties.EqClassEqualDepthV3 import EqClassEqualDepthV3
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
from utils.EnumerateUtils import *
from utils.ConcretizeUtils import *
import gc

class EqClassEqualDepthV4(EqClassEqualDepthV3):


    def __init__(self, dsl_list = [], source_synth_desc = None, target_synth_desc = None, target_dsl_list = [], output_depth = 1, forward_map_path = None, swizzle_dsl_list = [], swizzle_map_path = None, commutative_map_path = None, input_depth = 2, depth_range = False, use_canon_map = True):




        super().__init__(dsl_list = dsl_list, source_synth_desc = source_synth_desc, target_synth_desc = target_synth_desc, target_dsl_list = target_dsl_list, output_depth = output_depth, forward_map_path = forward_map_path, swizzle_dsl_list = swizzle_dsl_list, swizzle_map_path = swizzle_map_path, commutative_map_path = commutative_map_path, input_depth = input_depth, depth_range = depth_range, use_canon_map = use_canon_map)
        self.name = "EqClassEqualDepthV4"


        self.swizzle_max_num_args = 4
        self.current_gc_iteration = 0
        self.VIRT_MEM_LIMIT_MB =  9216
        self.gc_log = []




    def should_garbage_collect(self, iteration):

        VIRT_MEM = get_process_virtual_memory_megabytes()
        if VIRT_MEM > self.VIRT_MEM_LIMIT_MB:

            iterations_since_gc = abs(iteration - self.current_gc_iteration)

            # In case garbage collected happened less than 256 iterations ago
            if iterations_since_gc > 256:
                return True


        return False


    def collect_garbage(self, iteration):
        VIRT_MEM = get_process_virtual_memory_megabytes()
        entry = (iteration, VIRT_MEM)
        self.gc_log.append(entry)
        self.current_gc_iteration = iteration
        gc.collect()

    def property_holds_on_candidate(self, candidate):


        src_ctx = candidate[0]
        dst_ctx = candidate[1]
        output_size = candidate[3]

        valid_src_conc = get_valid_concretization(src_ctx, output_size, self.input_dsl_list + self.swizzle_dsl_list + self.output_dsl_list)

        valid_dst_conc = get_valid_concretization(dst_ctx, output_size, self.input_dsl_list + self.swizzle_dsl_list + self.output_dsl_list)

        if valid_src_conc is None or valid_dst_conc is None:
            print("No valid source or dst with output size ", output_size, "for", src_ctx.name, dst_ctx.name)
            return False


        success, src_expr_str, dst_expr_str = self.synth_utils.double_grammar_synthesis(valid_src_conc, valid_dst_conc)

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

                    src_expressions = create_exhaustive_expressions_generator_v2(relavent_swizzle_subset + [dsl_inst], input_depth, output_size = src_ctx.out_vectsize)

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

                        target_expressions = create_exhaustive_expressions_generator_v2(relavent_output_subset, output_depth, output_size = src_expr.out_vectsize)
                        self.target_canon_map.clear()
                        for target_count ,target_expr in enumerate(target_expressions):

                            if self.should_garbage_collect(target_count):
                                self.collect_garbage()


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
                                candidate = (canonical_src_expr, canonical_target_expr, relavent_output_subset, src_expr.out_vectsize)


                                yield candidate




    def run_on_batch_completion(self):
        gc.collect()

    def get_notify_body(self, count, success_count, start_time):
        parent_body = super().get_notify_body(count, success_count, start_time)
        gc_log_str = "\n".join([str(entry) for entry in self.gc_log ])

        gc_desc = "Garbage Collected Log"

        return "\n".join([parent_body, gc_desc, gc_log_str])


    def get_relavent_swizzle_dsl_subset(self, dsl_inst):

        relevent_swizzles_names = []
        relavent_swizzles = []

        for swizzle_ty in self.swizzle_forward_map:
            ctx_in_map = any([ctx.name in self.swizzle_forward_map[swizzle_ty] for ctx in dsl_inst.contexts])
            if ctx_in_map or dsl_inst.name in self.swizzle_forward_map[swizzle_ty]:
                swizzle_inst = self.get_swizzle_by_name(swizzle_ty)

                if swizzle_inst.name in relevent_swizzles_names:
                    continue

                if get_max_symbolic_args(swizzle_inst) >= 4:
                    continue

                relevent_swizzles_names.append(swizzle_inst.name)

                relavent_swizzles.append(swizzle_inst)



        return relavent_swizzles



    def get_relavent_output_dsl_subset(self, dsl_inst):
        if not dsl_inst.name in self.forward_map:
            return []
        relavent_names = self.forward_map[dsl_inst.name]
        relavent_outputs = [d for d in self.output_dsl_list if d.name in relavent_names]

        relevent_swizzles_names = []
        relavent_swizzles = []

        for swizzle_ty in self.swizzle_forward_map:
            ctx_in_map = any([ctx.name in self.swizzle_forward_map[swizzle_ty] for ctx in dsl_inst.contexts])
            if ctx_in_map or dsl_inst.name in self.swizzle_forward_map[swizzle_ty]:
                swizzle_inst = self.get_swizzle_by_name(swizzle_ty)

                if swizzle_inst.name in relevent_swizzles_names:
                    continue

                if get_max_symbolic_args(swizzle_inst) >= 4:
                    continue

                relevent_swizzles_names.append(swizzle_inst.name)

                relavent_swizzles.append(swizzle_inst)



        return relavent_outputs + relavent_swizzles
