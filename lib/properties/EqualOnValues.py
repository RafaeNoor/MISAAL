from properties.Property import *
import random
import sys
import json
from  utils.DSLInstructionUtils import *
from utils.GenerateRandomExpr import create_random_expression
import copy
from  common.Types import *
import itertools

class EqualOnValues(Property):


    def __init__(self, dsl_list = [], source_synth_desc = None, target_synth_desc = None, target_dsl_list = []):

        # Prune masked expression, handle masked property generation seperately
        dsl_list = [dsl_inst for dsl_inst in dsl_list if "mask" not in dsl_inst.name]
        super().__init__(name = "EqualOnValues", dsl_list = dsl_list, synth_desc = source_synth_desc)
        self.simplify_map = {}
        self.source_synth_desc = source_synth_desc
        self.target_synth_desc = target_synth_desc
        self.input_dsl_list = []

        for dsl_inst in dsl_list:
            if dsl_inst.has_bounded_behavior():
                self.input_dsl_list.append(convert_bounded_dsl_inst_to_multiple_contexts(dsl_inst))
            else:
                self.input_dsl_list.append(dsl_inst)

        self.dsl_list = self.input_dsl_list
        self.output_dsl_list = target_dsl_list

        self.forward_map = {}
        self.backward_map = {}

        # Testing
        #self.input_dsl_list = [d for d in self.input_dsl_list if "vmpy" in d.name]
        #self.output_dsl_list = [d for d in self.output_dsl_list if "widen-mul" in d.name]

        random.shuffle(self.input_dsl_list)



    def get_context_num_sym_args(self, ctx):
        return sum([1 for arg in ctx.context_args if isinstance(arg, BitVector)])

    def get_context_sym_args(self, ctx):
        return ([arg for arg in ctx.context_args if isinstance(arg, BitVector)])


    def get_context_input_sizes(self, ctx):
        return sorted([arg.size for arg in ctx.context_args if isinstance(arg, BitVector)])


    def get_compatible_contexts(self, precision, bitvector_sizes, num_args, output_size, dsl_list):
        # Get those operations with at-least as many symbolic arguments
        # as 'num_args', and supports at least one of the sizes in bitvector_sizes
        compatible = []

        for dsl_inst in dsl_list:
            for context in dsl_inst.contexts:
                supports_input = any([context.supports_input_size(size) for size in bitvector_sizes])
                supports_prec = context.supports_input_precision(precision)
                num_ctx_args = self.get_context_num_sym_args(context)
                if not supports_input:
                    continue

                if context.out_vectsize != output_size:
                    continue
                if not supports_prec:
                    continue

                #if num_ctx_args > num_args:
                #    continue
                compatible.append(context)

        return compatible





    def get_property_desc(self):
        return "Identifies values for which two expressions in different dsls may be equal"

    def generate_candidates(self):
        """Candidates are randomly generated programs of a specified depth (self.input_depth)

        Returns:
            [DSLExpressions]: _description_
        """

        candidates = []

        for dsl_inst in self.input_dsl_list:
            for src_ctx in dsl_inst.contexts:
                num_src_ctx_args = self.get_context_num_sym_args(src_ctx)
                input_sizes = self.get_context_input_sizes(src_ctx)
                output_size = src_ctx.out_vectsize
                precision = src_ctx.in_precision
                compatible_contexts = self.get_compatible_contexts(precision, input_sizes, num_src_ctx_args , output_size, self.output_dsl_list)
                masks = map(list, itertools.product([1], repeat=num_src_ctx_args))

                for mask in masks:
                    for dst_ctx in compatible_contexts:
                        candidate = (src_ctx, dst_ctx, mask)
                        candidates.append(candidate)
        return candidates




    def emit_verify_not_equal(self, left_expr, right_expr):
        return "(verify (assert (not (equal? {} {}))))".format(left_expr, right_expr)



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

        for idx, arg in enumerate(dst_ctx.context_args):
            if not isinstance(arg, BitVector):
                continue

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

            dst_ctx.context_args[idx] = reg



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

        statements.append("(assert (not (equal? src-result (bv 0 (bitvector (bvlength src-result))))))")

        get_cex = "(define cex {})".format(self.emit_verify_not_equal("src-result", "dst-result"))

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
        return candidate[0].name+"_"+candidate[1].name+"_"+str(candidate[2])

    def get_property_on_candidate(self, candidate):


        key = self.serialize_candidate(candidate)
        (src_ctx, dst_ctx) = self.simplify_map[key]

        src_name = src_ctx.name
        dst_name = dst_ctx.name

        if src_name not in self.forward_map:
            self.forward_map[src_name] = []


        if dst_name not in self.backward_map:
            self.backward_map[dst_name] = []

        self.forward_map[src_name].append(dst_name)
        self.backward_map[dst_name].append(src_name)


        property_t = {"src": src_ctx.emit_context_expr_string(), "dst": dst_ctx.emit_context_expr_string(), "mask": candidate[2]}
        return property_t




    def run_on_completion(self):

        for key in self.forward_map:
            self.forward_map[key] = list(set(self.forward_map[key]))

        for key in self.backward_map:
            self.backward_map[key] = list(set(self.backward_map[key]))


        with open("forward_map.json", "w+") as SrcFile:
            SrcFile.write(json.dumps(self.forward_map, indent = 4))

        with open("backward_map.json", "w+") as DstFile:
            DstFile.write(json.dumps(self.backward_map, indent = 4))





    def run_on_batch_completion(self):

        for key in self.forward_map:
            self.forward_map[key] = list(set(self.forward_map[key]))

        for key in self.backward_map:
            self.backward_map[key] = list(set(self.backward_map[key]))


        with open("forward_map_{}_intermediate.json".format(self.name), "w+") as SrcFile:
            SrcFile.write(json.dumps(self.forward_map, indent = 4))

        with open("backward_map_{}_intermediate.json".format(self.name), "w+") as DstFile:
            DstFile.write(json.dumps(self.backward_map, indent = 4))


    def limit_contexts(self, dsl_list, limit):

        for dsl_inst in dsl_list:
            num_ctx = len(dsl_inst.contexts)
            dsl_inst.contexts = dsl_inst.contexts[: min(num_ctx, limit)]
        return dsl_list


    def emit_property_to_egg(self, property_map):

        egg_rules = []


        for key in property_map:
            for instance in property_map[key]:

                property_object = instance['property']

                input_expression_string = property_object['candidate']


                output_expression_string = property_object['simplified']


                input_expression = read_string_to_dsl(input_expression_string, self.input_dsl_list + self.support_dsl)

                print("Read Input successfully!")



                output_expression = read_string_to_dsl(output_expression_string, self.output_dsl_list + self.support_dsl)


                print("Read Output successfully!")

                bidirectional_flag = is_birewrite_valid(input_expression, output_expression)

                #param_map, reverse_map  = generate_parameter_map(input_expression, output_expression)

                rule = emit_rewrite_expr(input_expression, output_expression, bidirectional = bidirectional_flag, param_map = {})

                egg_rules.append(rule)

        return egg_rules


















