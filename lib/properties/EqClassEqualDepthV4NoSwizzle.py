from properties.Property import *
import os
import time
import glob
import pickle
from properties.EqClassEqualDepthV4 import EqClassEqualDepthV4
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

class EqClassEqualDepthV4NoSwizzle(EqClassEqualDepthV4):


    def __init__(self, dsl_list = [], source_synth_desc = None, target_synth_desc = None, target_dsl_list = [], output_depth = 1, forward_map_path = None, swizzle_dsl_list = [], swizzle_map_path = None, commutative_map_path = None, input_depth = 2, depth_range = False, use_canon_map = True, start_input_depth = 1, start_output_depth =1, bidirectional_test = False, filter_list = None):




        with open("empty_file.json", "w+") as EmptyFile:
            EmptyFile.write("{}\n")
        super().__init__(dsl_list = dsl_list,  source_synth_desc = source_synth_desc, target_synth_desc = target_synth_desc, output_depth = output_depth, forward_map_path = forward_map_path, swizzle_dsl_list = swizzle_dsl_list, swizzle_map_path = "empty_file.json", commutative_map_path = commutative_map_path, input_depth = input_depth, depth_range = depth_range, use_canon_map = use_canon_map, start_input_depth = start_input_depth, start_output_depth =start_output_depth, bidirectional_test =
                         bidirectional_test, filter_list = filter_list, target_dsl_list = target_dsl_list)
        self.name = "EqClassEqualDepthV4NoSwizzle"


    def get_relavent_swizzle_dsl_subset(self, dsl_inst):
        return self.get_relavent_output_dsl_subset(dsl_inst)





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
                    src_ctx = self.get_context_with_max_sym_bvs(dsl_inst)
                    print(src_ctx.name)

                    if src_ctx.out_vectsize == None:
                        print("Skipping as src context has no outvect size")
                        continue

                    if len(relavent_output_subset) == 0:
                        print("Output set empty")
                        continue

                    src_expressions = create_exhaustive_expressions_generator_v2(relavent_swizzle_subset + [dsl_inst], input_depth, output_size = src_ctx.out_vectsize, max_leaves = 3)

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






                        if not isinstance(src_expr,Reg) and len(get_unique_context_registers(src_expr)) > 3:
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



                        target_expressions = create_exhaustive_expressions_generator_v2(relavent_output_subset, output_depth, output_size = src_ctx.out_vectsize, max_leaves = 4)
                        self.target_canon_map.clear()
                        for target_count ,target_expr in enumerate(target_expressions):


                            if self.should_garbage_collect(target_count):
                                self.collect_garbage()


                            if isinstance(target_expr, Reg) and output_depth != output_start:
                                continue

                            if not isinstance(target_expr,Reg) and len(get_unique_context_registers(target_expr)) > 3:
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



                                self.absolute_expr_count += self.get_absolute_count(canonical_target_expr) * self.get_absolute_count(canonical_src_expr)
                                candidate = (canonical_src_expr, canonical_target_expr, relavent_output_subset, src_ctx.out_vectsize)
                                yield candidate
