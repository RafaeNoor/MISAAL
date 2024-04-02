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

class EqualOnValuesDepth(EqualOnValues):


    def __init__(self, dsl_list = [], source_synth_desc = None, target_synth_desc = None, target_dsl_list = [], output_depth = 1):

        #target_dsl_list = self.filter_target_dsl_list(target_dsl_list)
        #dsl_list = self.filter_source_dsl_list(dsl_list)

        print("Source DSL List size:", len(dsl_list))
        print("Target DSL List size:", len(target_dsl_list))

        super().__init__(dsl_list = dsl_list, source_synth_desc = source_synth_desc, target_synth_desc = target_synth_desc, target_dsl_list = target_dsl_list)
        self.name = "EqualOnValuesDepth"
        self.output_depth = output_depth



    def prune_uniform_size_expr_depth(self, pickle_files_path):
        pruned_expr_list = []

        for path in pickle_files_path:

            with open(path, "rb") as handle:
                expr = pickle.load(handle)
                expr_sizes = get_expr_intermediate_sizes(expr)

                unique_sizes = list(set(expr_sizes))

                if len(unique_sizes) == 1:
                    # If expression has the same bitvector sizes throughout, let the depth one case handle that.
                    continue

                pruned_expr_list.append(expr)

        print("Original # expressions {}, Pruned # expressions {}".format(len(pickle_files_path), len(pruned_expr_list)))
        with open("temp.log", "w+") as LogFile:
            LogFile.write("Original # expressions {}, Pruned # expressions {}".format(len(pickle_files_path), len(pruned_expr_list)))
        return pruned_expr_list


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
        #self.output_dsl_list = self.filter_target_dsl_list(self.output_dsl_list)
        print("Target DSL")
        print_dsl_list_summary(self.output_dsl_list)

        base_name = "halide_exprs_d{}".format(self.output_depth)
        expr_fname = "halide_exprs_d{}.pickle".format(self.output_depth)
        read_from_file = os.path.exists(base_name)

        expressions = []
        if read_from_file:
            start_time = time.time()
            print("Exhaustive expressions already generated")
            """
            with open(expr_fname, "rb") as handle:
                print("Reading expressions from", expr_fname)
                expressions = pickle.load(handle)

            end_time = time.time()
            elapsed = end_time - start_time
            print("Reading from file took {} seconds".format(elapsed))
            """
        else:
            print("Generating new expressions path")
            expressions = create_exhaustive_expressions(self.output_dsl_list, self.output_depth)
            os.makedirs(base_name)

            for idx, expr in enumerate(expressions):

                expr_fname = "halide_exprs_d{}_e{}.pickle".format(self.output_depth,idx)
                expr_path = os.path.join(base_name, expr_fname)
                with open(expr_path, "wb") as handle:
                    print("Saving expressions to", expr_path)
                    pickle.dump(expr, handle, protocol=pickle.HIGHEST_PROTOCOL)


        pickle_files = glob.glob(base_name+"/"+"*.pickle")
        print("Number of output expressions: ", len(pickle_files))


        expressions = self.prune_uniform_size_expr_depth(pickle_files)



        compatible_out_size_map = {}

        for dsl_inst in self.input_dsl_list:
            for idx, src_ctx in enumerate(dsl_inst.contexts):
                print(src_ctx.name)
                num_src_ctx_args = self.get_context_num_sym_args(src_ctx)
                input_sizes = self.get_context_input_sizes(src_ctx)
                output_size = src_ctx.out_vectsize
                precision = src_ctx.in_precision
                if str(output_size) not in compatible_out_size_map:
                    compatible_out_size_map[str(output_size)] = [exp for exp in expressions if exp.out_vectsize == output_size]

                compatible_contexts = compatible_out_size_map[str(output_size)]
                masks = map(list, itertools.product([1], repeat=num_src_ctx_args))

                for mask in masks:
                    for dst_ctx in compatible_contexts:
                        if not self.has_common_operand_size(src_ctx, dst_ctx):
                            continue
                        candidate = (src_ctx, dst_ctx, mask)
                        candidates.append(candidate)
        return candidates






    def has_common_operand_size(self, src_ctx, dst_ctx):
        dst_regs = self.get_registers(dst_ctx)
        dst_sizes = [reg.size for reg in dst_regs]
        src_sizes = [arg.size for arg in src_ctx.context_args if isinstance(arg, BitVector)]


        for dst_size in dst_sizes:
            if dst_size in src_sizes:
                return True

        return False

    def property_holds_on_candidate(self, candidate):


        src_ctx = copy.deepcopy(candidate[0])
        dst_ctx = copy.deepcopy(candidate[1])

        mask = candidate[2]

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

            arg.index = reg.index
            arg.precision = reg.precision
            arg.size = reg.size
            arg.signed = reg.signed




        language_to_symbol = {"hvx": "'hvx",
                              "x86": "'x86",
                              "halide": "'halide" ,
                              "halide_hvx": "'halide",
                              "halide_x86": "'halide",
                              }

        statements = []

        src_language_desc = self.source_synth_desc
        target_language_desc = self.target_synth_desc

        if src_language_desc.emit_interpreter:
            statements.append(src_language_desc.emit_interpreter_framework(src_language_dsl))


        if target_language_desc.emit_interpreter and src_language_desc.target_name != target_language_desc.target_name:
            statements.append(target_language_desc.emit_interpreter_framework(target_language_dsl))


        # Create arguments for synthesis. If the bit is set then the corresponding
        # argument is kept as a symbolic hole, otherwise it is set to 0.
        env = []
        for idx,bit in enumerate(mask):
            value = None
            if bit == 1:
                value = "(?? (bitvector {}))".format(src_ctx_regs[idx].size)
            else:
                value = "(bv 0 (bitvector {}))".format(src_ctx_regs[idx].size)

            env.append(value)

        # Add Additionally allocated registers
        for idx in range(len(mask), len(src_ctx_regs)):
            value = "(?? (bitvector {}))".format(src_ctx_regs[idx].size)
            env.append(value)

        define_env = "(define env (vector {}))".format(" ".join(env))
        statements.append(define_env)

        # symbolic operands are non-zero
        statements.append("(assert-non-zero-env env)")



        src_expression = "(define src-expr\n {}\n)".format(src_ctx.emit_context_expr_string())
        dst_expression = "(define dst-expr\n {}\n)".format(dst_ctx.emit_context_expr_string())
        statements.append(src_expression)
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
            if "widen-mul" in dst_ctx.name:
                print("\n\n\n\nHERERERERE\n\n\n\n\n")
            key = self.serialize_candidate(candidate)
            pair = (src_ctx, dst_ctx)
            self.simplify_map[key] = pair

        return is_simplified


    def serialize_candidate(self, candidate):
        return candidate[0].name+"_"+candidate[1].emit_context_expr_string()+"_"+str(candidate[2])

    def get_property_on_candidate(self, candidate):


        key = self.serialize_candidate(candidate)
        (src_ctx, dst_ctx) = self.simplify_map[key]

        src_name = src_ctx.name
        dst_names = self.get_nested_contexts_name(dst_ctx)

        if src_name not in self.forward_map:
            self.forward_map[src_name] = []


        for dst_name in dst_names:
            if dst_name not in self.backward_map:
                self.backward_map[dst_name] = []

        for dst_name in dst_names:
            self.forward_map[src_name].append(dst_name)
            self.backward_map[dst_name].append(src_name)



        property_t = {"src": src_ctx.emit_context_expr_string(), "dst": dst_ctx.emit_context_expr_string(), "mask": candidate[2]}
        return property_t












