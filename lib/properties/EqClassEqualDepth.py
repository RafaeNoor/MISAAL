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
from utils.CodeSynthesizerDesc import *
from utils.CanonicalizeExpressions import CanonicalizeExpression
import copy
from  common.Types import *
import itertools
import numpy as np
from grammar_gen.EqClassExpandGenerator import EqClassExpandGenerator

class EqClassEqualDepth(EqualOnValues):


    def __init__(self, dsl_list = [], source_synth_desc = None, target_synth_desc = None, target_dsl_list = [], output_depth = 1, forward_map_path = None, swizzle_dsl_list = [], swizzle_map_path = None, commutative_map_path = None):


        print("Source DSL List size:", len(dsl_list))
        print("Target DSL List size:", len(target_dsl_list))

        super().__init__(dsl_list = dsl_list, source_synth_desc = source_synth_desc, target_synth_desc = target_synth_desc, target_dsl_list = target_dsl_list)
        self.name = "EqClassEqualDepth"
        self.swizzle_dsl_list = swizzle_dsl_list
        self.swizzle_forward_map = {}

        self.canonicalizer = CanonicalizeExpression(commutative_map_path = commutative_map_path)

        self.absolute_expr_count = 0

        if not swizzle_map_path is None:
            with open(swizzle_map_path, "r") as JsonFile:
                self.swizzle_forward_map = json.load(JsonFile)




        self.output_depth = output_depth
        self.is_candidate_generator = True

        self.forward_map = {}

        if not forward_map_path is None:
            with open(forward_map_path, "r") as JsonFile:
                self.forward_map = json.load(JsonFile)



    def isCanonical(self, expr, canonical_expr):
        if isinstance(expr, Context) and not isinstance(canonical_expr, Context):
            return False

        if not isinstance(expr, Context) and isinstance(canonical_expr, Context):
            return False

        if isinstance(expr, Reg) and not isinstance(canonical_expr, Reg):
            return False

        if not isinstance(expr, Reg) and isinstance(canonical_expr, Reg):
            return False

        if isinstance(expr, Reg) and  isinstance(canonical_expr, Reg):
            return True


        if isinstance(expr, Context) and isinstance(canonical_expr, Context):
            same_name = expr.dsl_name == canonical_expr.dsl_name

            if not same_name:
                return False

            condition = True

            for idx in range(len(expr.context_args)):
                arg = expr.context_args[idx]
                canon_arg = canonical_expr.context_args[idx]


                if isinstance(arg, Reg):
                    condition = condition and self.isCanonical(arg, canon_arg)

                if isinstance(canon_arg, Reg):
                    condition = condition and self.isCanonical(arg, canon_arg)

                if isinstance(arg, Context):
                    condition = condition and self.isCanonical(arg, canon_arg)

                if isinstance(canon_arg, Context):
                    condition = condition and self.isCanonical(arg, canon_arg)
            return condition

        return True




    def filter_target_dsl_list(self, dsl_list):
        filtered = []

        substrs = ["cast-int", "reduce", ":signed-vec-widen-mul",  "vec-add" ]

        substrs = ['typed:signed-vec-le', 'typed:signed-vec-lt', 'typed:vec-eq', 'typed:signed-vec-widen-mul', 'typed:concat_vectors', 'typed:signed-vector_reduce_add', 'typed:xBroadcast', 'typed:vec-saturate', 'typed:slice_vectors', 'typed:cast-uint', 'typed:cast-int', 'typed:signed-vec-abs', 'typed:vec-bwnot', 'typed:signed-vec-rounding_halving_add', 'typed:signed-vec-sat-sub', 'typed:signed-vec-sat-add', 'typed:vec-add', 'typed:vec-bwand', 'typed:signed-vec-div', 'typed:signed-vec-mul', 'typed:signed-vec-mod', 'typed:vec-shl', 'typed:vec-sub', 'typed:signed-vec-max', 'typed:signed-vec-shr', 'typed:signed-vec-absd', 'typed:signed-vec-min', 'typed:signed-vec-halving_add']
        #substrs = ["typed:vec-bwand"]
        contexts = ["typed:cast-int_0_ip8_is1024_op32_os4096_signed_1","typed:signed_vector_reduce_add_w4_4096_32_4096"]
        #contexts = []
        for dsl_inst in dsl_list:
            include = any([s in dsl_inst.name for s in substrs])
            if not include:
                continue

            dsl_inst_copy = copy.deepcopy(dsl_inst)
            filtered.append(dsl_inst_copy)


        return filtered



    def filter_source_dsl_list(self, dsl_list):
        filtered = []

        ctxs = ["_mm256_maddubs_epi16"]
        substrs = ["_mm256_maddubs_epi16"]

        for dsl_inst in dsl_list:
            insert = any([s in dsl_inst.name for s in substrs])
            if insert:
                dsl_inst.contexts = [c for c in dsl_inst.contexts if c.name in ctxs]
                filtered.append(dsl_inst)

        return filtered


    def get_testing_expression(self):
        vec_add_dsl = self.get_eq_class("typed:vec-add")

        vec_reduce_dsl = self.get_eq_class("typed:signed-vector_reduce_add")

        cast_int_dsl = self.get_eq_class("typed:cast-int")

        vec_widen_mul_dsl = self.get_eq_class("typed:signed-vec-widen-mul")

        vec_add_ctx = [copy.deepcopy(ctx) for ctx in vec_add_dsl.contexts if ctx.name == 'typed:vec-add_p32_s1024_signed_None'][0]

        vec_reduce_ctx = [copy.deepcopy(ctx) for ctx in vec_reduce_dsl.contexts if ctx.name == "typed:signed_vector_reduce_add_w4_4096_32_4096" ][0]

        cast_int_ctx = [copy.deepcopy(ctx) for ctx in cast_int_dsl.contexts if ctx.name == 'typed:cast-int_0_ip16_is2048_op32_os4096_signed_1'][0]

        vec_widen_mul_ctx = [copy.deepcopy(ctx) for ctx in vec_widen_mul_dsl.contexts if ctx.name == 'typed:signed-vec-widen-mul_p8_s1024_signed_1'][0]



        reg_2 = Reg(str(2), 32, 1024)
        reg_0 = Reg(str(0), 8, 1024)
        reg_1 = Reg(str(1), 8, 1024)

        vec_add_ctx.context_args[0] = vec_reduce_ctx
        vec_add_ctx.context_args[1] = reg_2

        vec_reduce_ctx.context_args[1] = cast_int_ctx

        cast_int_ctx.context_args[0] = vec_widen_mul_ctx

        vec_widen_mul_ctx.context_args[0] = reg_0
        vec_widen_mul_ctx.context_args[1] = reg_1

        return vec_add_ctx




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
        #self.output_dsl_list = self.filter_target_dsl_list(self.output_dsl_list)
        print("Target DSL")
        print_dsl_list_summary(self.output_dsl_list)


        self.input_dsl_list = self.filter_source_dsl_list(self.input_dsl_list)


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

                    self.absolute_expr_count += self.get_absolute_count(canonical_expr)
                    candidate = (dsl_inst, expr, relavent_output_subset)





                    yield candidate


    def get_absolute_count(self, expr):
        if isinstance(expr, Context):

            current_dsl = None
            """
            if 'swizzle' in expr.name:
                swizzle_name = self.get_swizzle_by_name(expr.dsl_name).split("_dsl")[0]

                current_dsl = self.get_swizzle_by_name(swizzle_name)
            else:
                for dsl_inst in self.output_dsl_list:
                    if dsl_inst.name == expr.dsl_name:
                        current_dsl = dsl_inst
                        break
            """
            current_dsl = self.get_eq_class(expr.dsl_name)

            count = len([ctx for ctx in current_dsl.contexts if ctx.out_vectsize == expr.out_vectsize])


            for arg in expr.context_args:
                count = count * self.get_absolute_count(arg)
            return count




        return 1

    def get_swizzle_by_name(self, name):
        for dsl_inst in self.swizzle_dsl_list:
            if dsl_inst.name == name:
                return dsl_inst
            for ctx in dsl_inst.contexts:
                if ctx.name == name:
                    return dsl_inst
        assert False, "Could not find {}".format(name)


    def get_relavent_output_dsl_subset(self, dsl_inst):
        if not dsl_inst.name in self.forward_map:
            return []
        relavent_names = self.forward_map[dsl_inst.name]
        relavent_outputs = [d for d in self.output_dsl_list if d.name in relavent_names]

        relevent_swizzles_names = []
        relavent_swizzles = []

        for swizzle_ty in self.swizzle_forward_map:
            if dsl_inst.name in self.swizzle_forward_map[swizzle_ty]:
                swizzle_inst = self.get_swizzle_by_name(swizzle_ty)

                if swizzle_inst.name in relevent_swizzles_names:
                    continue

                relevent_swizzles_names.append(swizzle_inst.name)

                relavent_swizzles.append(swizzle_inst)



        return relavent_outputs + relavent_swizzles


    def get_eq_class(self, eq_class_name):
        eq_class_name = eq_class_name.split("_dsl")[0]
        for dsl_inst in self.input_dsl_list+self.output_dsl_list+self.swizzle_dsl_list:
            if dsl_inst.name == eq_class_name:
                return dsl_inst
        print("Unable to find", eq_class_name)
        assert False,"Unreachable"

    def get_context_with_max_sym_bvs(self, dsl_inst):
        arg_max = np.argmax([get_num_symbolic_args(ctx) for ctx in dsl_inst.contexts])
        src_ctx = dsl_inst.contexts[arg_max]
        return src_ctx


    def property_holds_on_candidate(self, candidate):


        src_eq_class = copy.deepcopy(candidate[0])

        arg_max = np.argmax([get_num_symbolic_args(ctx) for ctx in src_eq_class.contexts])
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



        language_to_symbol = {"hvx": "'hvx",
                              "x86": "'x86",
                              "halide": "'halide" ,
                              "halide_hvx": "'halide",
                              "halide_x86": "'halide",
                              }

        statements = []

        src_language_desc = self.source_synth_desc
        # Need to create a new desc for swizzles and target inst comined
        #target_language_desc = self.target_synth_desc
        target_language_desc = create_synth_desc("base_", True, self.target_synth_desc.target_vector_sizes, "", "")
        target_language_desc.emit_sema = False

        target_language_dsl =  relavent_output_subset #self.output_dsl_list + self.swizzle_dsl_list
        src_language_dsl = self.input_dsl_list

        if src_language_desc.emit_interpreter:
            statements.append(src_language_desc.emit_interpreter_framework(src_language_dsl))

        for swizzle in self.swizzle_dsl_list:
            statements.append(swizzle.get_semantics())


        if target_language_desc.emit_interpreter and src_language_desc.target_name != target_language_desc.target_name:
            statements.append(target_language_desc.emit_struct_def(self.swizzle_dsl_list))
            statements.append(target_language_desc.emit_interpreter_def(target_language_dsl))
            statements.append(target_language_desc.emit_cost_def(target_language_dsl))


        env = []
        for idx in range(len(src_ctx_regs)):
            value = "(?? (bitvector {}))".format(src_ctx_regs[idx].size)
            env.append(value)




        src_expression = "(define src-expr\n {}\n)".format(src_ctx.emit_context_expr_string())

        statements.append(src_expression)

        # Define dst expression as a grammar of possible
        # concrete Eq class members in the same structure
        input_precs = [arg.precision for arg in src_ctx_regs]

        GrammarGenerator = EqClassExpandGenerator(dsl_list = target_language_dsl  , output_bitwidth = output_size, input_sizes = [arg.size for arg in src_ctx_regs], input_precs = input_precs)
        dst_expression_label ,dst_expression_grammar =  GrammarGenerator.emit_grammar(dst_ctx)




        statements.append(dst_expression_grammar)

        grammar_fn = "(define (grammar-fn i) ({}))".format(dst_expression_label)
        statements.append(grammar_fn)

        statements.append(self.get_invoke_spec(spec_name = "src-expr"))

        statements.append(self.get_invoke_spec_lane(spec_name = "src-expr", output_prec = src_ctx.out_precision))

        statements.append("(define optimize? #t)")

        statements.append("(define symbolic? #f)")

        statements.append("(define interpreter {})".format(target_language_desc.interpreter_name))

        statements.append("(define cost-model {})".format(target_language_desc.cost_name))
        leaves_sizes = "(define leaves-sizes (list {}))".format(" ".join([str(arg.size) for arg in src_ctx_regs]))
        statements.append(leaves_sizes)



        execute_synthesis = "(define-values (satisfiable? mat el)  (synthesize-sol-with-depth {} {} invoke-spec invoke-spec-lane grammar-fn leaves-sizes optimize? interpreter cost-model  symbolic? 30 'z3))".format(self.output_depth, self.output_depth)
        statements.append(execute_synthesis)



        if_sat = "(exit 0)"
        if_unsat = "(exit 1)"

        conditional = "(cond [satisfiable? {}] [else {}])".format(if_sat, if_unsat)
        statements.append(conditional)

        result = execute_racket_file(statements)

        is_simplified = result.returncode == 0


        if is_simplified:
            key = self.serialize_candidate(candidate)
            pair = (src_ctx, dst_ctx)
            self.simplify_map[key] = pair

        return is_simplified


    def get_invoke_spec(self, spec_name = "spec-expr", env_name = "env"):
        interpret_name = self.source_synth_desc.interpreter_name
        interpret_stmt =   "({} {} {})".format(interpret_name, spec_name, env_name)
        return "(define (invoke-spec  {})\n {})".format(env_name, interpret_stmt)


    def get_invoke_spec_lane(self, spec_name = "spec-expr", env_name = "env", output_prec = 8):
        interpret_name = self.source_synth_desc.interpreter_name
        interpret_stmt =   "({} {} {})".format(interpret_name, spec_name, env_name)
        low_offset = "(define low (* {} lane-idx))".format(str(output_prec))
        high_offset = "(define high (+ low (- {} 1)))".format(str(output_prec))
        extract = "(define slice (extract high low {}))".format(interpret_stmt)
        stmts = [low_offset, high_offset, extract, "slice"]
        return "(define (invoke-spec-lane lane-idx {})\n {})".format(env_name, "\n".join(stmts))

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



        property_t = {"src": src_ctx.emit_context_expr_string(), "dst": dst_ctx.emit_context_expr_string()}
        return property_t

    def get_notify_body(self, count, success_count, start_time):
        processed_str = "Processed {} candidates , with {} successes".format(count, success_count)


        elapsed_time = time.time() - start_time
        hours = elapsed_time / (60 * 60)

        time_str_sec = "Elapsed time since start: {} seconds".format(elapsed_time)
        time_str_hour = "Elapsed time since start: {} hours".format(hours)

        candidates_per_second = count / elapsed_time


        candidate_rate_str = "Candidate rate: {} candidates per second".format(candidates_per_second)


        processed_abs_str = "Processed {} absolute candidates ".format(self.absolute_expr_count)

        abs_candidates_per_second = self.absolute_expr_count / elapsed_time

        abs_candidates_rate = "Absolute Candidate rate: {} candidates per second".format(abs_candidates_per_second)

        average_exprs_per_candidate = 0

        if count != 0:
            average_exprs_per_candidate = self.absolute_expr_count / count

        avg_candidates_rate = "Average # Expression rate: {} expressions per candidate".format(average_exprs_per_candidate)



        BANNER = "======================================="
        HEADER = BANNER + "\n"+ " "*25 + "MISAAL\n" + BANNER

        FOOTER = BANNER

        items = [HEADER, processed_str, time_str_sec, time_str_hour ,candidate_rate_str ,processed_abs_str , abs_candidates_rate, avg_candidates_rate , FOOTER]

        return "\n".join(items)




    def run_on_batch_completion(self):

        for key in self.forward_map:
            self.forward_map[key] = list(set(self.forward_map[key]))

        for key in self.backward_map:
            self.backward_map[key] = list(set(self.backward_map[key]))


        with open("forward_map_{}_intermediate.json".format(self.name), "w+") as SrcFile:
            SrcFile.write(json.dumps(self.forward_map, indent = 4))

        with open("backward_map_{}_intermediate.json".format(self.name), "w+") as DstFile:
            DstFile.write(json.dumps(self.backward_map, indent = 4))
    def emit_property_to_egg(self, property_map):
        return []







