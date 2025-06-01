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

class EqClassEqualDepthV3Synth(EqClassEqualDepthV3):


    def __init__(self, dsl_list = [], source_synth_desc = None, target_synth_desc = None, target_dsl_list = [], output_depth = 1, forward_map_path = None, swizzle_dsl_list = [], swizzle_map_path = None, commutative_map_path = None, input_depth = 2, depth_range = False, use_canon_map = False, filter_list = None):



        super().__init__(dsl_list = dsl_list, source_synth_desc = source_synth_desc, target_synth_desc = target_synth_desc, target_dsl_list = target_dsl_list, output_depth = output_depth, forward_map_path = forward_map_path, swizzle_dsl_list = swizzle_dsl_list, swizzle_map_path = swizzle_map_path, commutative_map_path = commutative_map_path, input_depth = input_depth, depth_range = depth_range, use_canon_map = use_canon_map)
        self.name = "EqClassEqualDepthV3Synth"
        self.filter_list = filter_list



    def property_holds_on_candidate(self, candidate):
        src_ctx = candidate[0]
        depth = candidate[1]
        subset = copy.deepcopy(candidate[2])

        try:
            success, src_expr_str, dst_expr_str = self.synth_utils.double_grammar_synthesis_hydride(src_ctx, subset, depth = depth)

            if success:
                key = self.serialize_candidate(candidate)
                self.simplify_map[key] = (src_expr_str, dst_expr_str)


            return success
        except KeyboardInterrupt:
            sys.exit(0)
            return False
        except:
            return False


    def serialize_candidate(self, candidate):
        return candidate[0].emit_context_expr_string() + "+D" + str(candidate[1])

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




        for input_depth in range(1,self.input_depth+1):
            self.current_input_depth = input_depth
            for output_depth in range(1, self.output_depth+ 1):
                self.current_output_depth = output_depth
                for input_inst in self.input_dsl_list:

                    if not self.filter_list is None:
                        if input_inst.name not in self.filter_list:
                            continue

                    relavent_swizzle_subset = self.get_relavent_swizzle_dsl_subset(input_inst)
                    relavent_swizzle_subset = deduplicate_dsl_list(relavent_swizzle_subset)
                    relavent_output_subset = self.get_relavent_output_dsl_subset(input_inst)
                    relavent_output_subset = deduplicate_dsl_list(relavent_output_subset)

                    sample_ctx = input_inst.get_sample_context()

                    print("Relavent set for ",input_inst.name)
                    for idx, ros in enumerate(relavent_output_subset):
                        print(idx, ".", ros.name)

                    print("Relavent Swizzles set for ",input_inst.name)
                    for idx, ros in enumerate(relavent_swizzle_subset):
                        print(idx, ".", ros.name)



                    if sample_ctx.out_vectsize == None:
                        continue

                    src_ctx = None


                    src_ctx = self.get_context_with_min_sym_bvs(input_inst)

                    if src_ctx.out_vectsize == None:
                        continue

                    if len(relavent_output_subset) == 0:
                        continue

                    src_expressions = create_exhaustive_expressions_generator(relavent_swizzle_subset + [input_inst], input_depth, use_eq_class = True, output_size = src_ctx.out_vectsize)

                    for src_expr in src_expressions:
                        if isinstance(src_expr, Reg):
                            continue

                        if get_expr_depth(src_expr) != input_depth:
                            continue


                        if not self.expr_contains(src_expr, input_inst.name):
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

                        yield (src_expr, output_depth ,  relavent_output_subset)










