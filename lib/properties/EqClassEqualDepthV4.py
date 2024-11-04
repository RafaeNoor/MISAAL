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


    def __init__(self, dsl_list = [], source_synth_desc = None, target_synth_desc = None, target_dsl_list = [], output_depth = 1, forward_map_path = None, swizzle_dsl_list = [], swizzle_map_path = None, commutative_map_path = None, input_depth = 2, depth_range = False, use_canon_map = True, start_input_depth = 1, start_output_depth =1, bidirectional_test = False, filter_list = None):




        super().__init__(dsl_list = dsl_list, source_synth_desc = source_synth_desc, target_synth_desc = target_synth_desc, target_dsl_list = target_dsl_list, output_depth = output_depth, forward_map_path = forward_map_path, swizzle_dsl_list = swizzle_dsl_list, swizzle_map_path = swizzle_map_path, commutative_map_path = commutative_map_path, input_depth = input_depth, depth_range = depth_range, use_canon_map = use_canon_map)
        self.name = "EqClassEqualDepthV4"


        self.swizzle_max_num_args = 4
        self.current_gc_iteration = 0
        self.VIRT_MEM_LIMIT_MB =  9216
        self.start_input_depth = start_input_depth
        self.start_output_depth = start_output_depth
        self.gc_log = []
        self.bidirectional_test = bidirectional_test
        self.filter_list = filter_list




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


        test_dsl_list =  self.input_dsl_list + self.swizzle_dsl_list + self.output_dsl_list
        valid_src_conc_gen = get_valid_concretization_generator(src_ctx, output_size, self.input_dsl_list + self.swizzle_dsl_list + self.output_dsl_list)



        valid_dst_conc = get_valid_concretization_generator(dst_ctx, output_size, self.input_dsl_list + self.swizzle_dsl_list + self.output_dsl_list)
        valid_dst_conc = next(valid_dst_conc)

        LIMIT = 1

        count = 0
        input_sizes_visited = []

        contains_swizzle = self.count_contexts(src_ctx, "swizzle") != 0

        for valid_src_conc in valid_src_conc_gen:
            regs = get_unique_context_registers(valid_src_conc)
            reg_sizes = sorted([reg.size for reg in regs])

            if reg_sizes in input_sizes_visited:
                continue

            input_sizes_visited.append(reg_sizes)

            print("Input sizes to test", reg_sizes)

            if valid_src_conc is None or valid_dst_conc is None:
                print("No valid source or dst with output size ", output_size, "for", src_ctx.name, dst_ctx.name)
                continue

            count += 1

            dst_copy = copy.deepcopy(valid_dst_conc)


            success, src_expr_str, dst_expr_str = self.synth_utils.double_grammar_synthesis(valid_src_conc, dst_copy)

            if not success:
                break

            # Confirm that the parsed expressions match the required structure
            synth_src_expr = read_string_to_dsl(src_expr_str, test_dsl_list)

            # isCanonical matches structure according to DSL list
            if not self.canonicalizer.isCanonical(synth_src_expr, valid_src_conc):
                continue

            synth_dst_expr = read_string_to_dsl(dst_expr_str, test_dsl_list)

            # isCanonical matches structure according to DSL list
            if not self.canonicalizer.isCanonical(synth_dst_expr, dst_copy):
                continue


            if success:
                print("SUCCESS!")
                key = self.serialize_candidate(candidate)
                self.simplify_map[key] = (src_expr_str, dst_expr_str)
                return success


            if not contains_swizzle or count >= LIMIT:
                break


        if self.bidirectional_test:
            print("Bidirectional test")

            valid_src_conc_gen = get_valid_concretization_generator(src_ctx, output_size, self.input_dsl_list + self.swizzle_dsl_list + self.output_dsl_list)
            for valid_src_conc in valid_src_conc_gen:
                dst_copy = copy.deepcopy(valid_dst_conc)
                success, dst_expr_str, src_expr_str = self.synth_utils.double_grammar_synthesis(dst_copy, valid_src_conc)

                if success:
                    print("SUCCESS BIDIRECTIONAL!")
                    key = self.serialize_candidate(candidate)
                    self.simplify_map[key] = (src_expr_str, dst_expr_str)
                    return success

                if not contains_swizzle or count >= LIMIT:
                    break




        return False


    def serialize_candidate(self, candidate):
        if isinstance(candidate[1], Reg):
            return candidate[0].emit_context_expr_string()+"_Reg"
        else:
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

                    if not self.filter_list is None:
                        if dsl_inst.name not in self.filter_list:
                            continue


                    relavent_swizzle_subset = self.get_relavent_swizzle_dsl_subset(dsl_inst)
                    relavent_swizzle_subset = deduplicate_dsl_list(relavent_swizzle_subset)
                    relavent_output_subset = self.get_relavent_output_dsl_subset(dsl_inst)
                    relavent_output_subset = deduplicate_dsl_list(relavent_output_subset)

                    relavent_output_subset.reverse()
                    print("Relavent set for ",dsl_inst.name)
                    for idx, ros in enumerate(relavent_output_subset):
                        print(idx, ".", ros.name)

                    print("Relavent Swizzles set for ",dsl_inst.name)
                    for idx, ros in enumerate(relavent_swizzle_subset):
                        print(idx, ".", ros.name)

                    sample_ctx = dsl_inst.get_sample_context()


                    if sample_ctx.out_vectsize == None:
                        print("Skipping as samle context has no outvect size")
                        continue

                    src_ctx = self.get_context_with_min_sym_bvs(dsl_inst)

                    if src_ctx.out_vectsize == None:
                        print("Skipping as src context has no outvect size")
                        continue

                    if len(relavent_output_subset) == 0:
                        print("Output set empty")
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

                        if self.count_contexts(src_expr, dsl_inst.name) != 1:
                            continue








                        if not isinstance(src_expr,Reg) and len(get_unique_context_registers(src_expr)) > 4:
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

                        print(src_expr.emit_context_expr_string())

                        target_expressions = create_exhaustive_expressions_generator_v2(relavent_output_subset, output_depth, output_size = src_ctx.out_vectsize, max_leaves = 5)
                        self.target_canon_map.clear()
                        for target_count ,target_expr in enumerate(target_expressions):

                            if self.should_garbage_collect(target_count):
                                self.collect_garbage()


                            if isinstance(target_expr, Reg) and output_depth != output_start:
                                continue




                            if get_expr_depth(target_expr) == output_depth or isinstance(target_expr, Reg):
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

                                # Equality check
                                if self.canonicalizer.isCanonical(target_expr, src_expr):
                                    continue

                                # TEMP:
                                #if not isinstance(target_expr,Reg) and  not self.expr_contains(target_expr, dsl_inst.name):
                                #    continue
                                if not isinstance(target_expr,Reg) and len(get_unique_context_registers(target_expr)) > 5:
                                    continue

                                self.absolute_expr_count += self.get_absolute_count(canonical_target_expr) * self.get_absolute_count(canonical_src_expr)
                                candidate = (canonical_src_expr, canonical_target_expr, relavent_output_subset, src_ctx.out_vectsize)#src_expr.out_vectsize)


                                yield candidate




    def run_on_batch_completion(self):
        VIRT_MEM = get_process_virtual_memory_megabytes()
        if VIRT_MEM > self.VIRT_MEM_LIMIT_MB:
            self.collect_garbage("BATCH_COMPLETION")

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


