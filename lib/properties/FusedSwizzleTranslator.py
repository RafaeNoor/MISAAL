from properties.Property import *
from properties.Translator import Translator
import random
import sys
import json
from  utils.DSLInstructionUtils import *
from  utils.CodeSynthesizerDesc import *
from utils.WriteDSL import *
from utils.GenerateRandomExpr import create_random_expression
import copy
import tempfile
from  common.Types import *

class FusedSwizzleTranslator(Translator):


    def __init__(self, dsl_list = [], source_synth_desc = None, target_synth_desc = None, target_dsl_list = [],   num_iterations = 1500, input_depth = 2, permute_limit = 3, exhaustive = False, shuffle_deriviation_map_path = "", swizzles = []):

        # Prune masked expression, handle masked property generation seperately

        dsl_list = [dsl_inst for dsl_inst in dsl_list if "mask" not in dsl_inst.name]

        # Temporary testing
        #dsl_list = [dsl_inst for dsl_inst in dsl_list if "hexagon_V6_vmpybv_128B"  in dsl_inst.name]

        super().__init__(dsl_list = dsl_list, source_synth_desc = source_synth_desc, target_synth_desc = target_synth_desc, target_dsl_list = target_dsl_list ,
                         num_iterations = num_iterations, input_depth = input_depth, permute_limit = permute_limit, exhaustive = exhaustive)
        self.name = "FusedSwizzleTranslator"
        self.swizzles = swizzles

        # Maps names of swizzle contexts to source language contexts
        self.shuffle_deriviation_map = self.merge_derivation_map(json.load(open(shuffle_deriviation_map_path)))




    def merge_derivation_map(self, d_map):

        pairs = []
        # Merge hvx_swizzle_1 and hvx_swizzle_152
        pairs.append(('hvx_swizzle_1', 'hvx_swizzle_152'))

        # Merge hvx_swizzle_44 and hvx_swizzle_0
        pairs.append(('hvx_swizzle_44', 'hvx_swizzle_0'))

        for (sw1, sw2) in pairs:
            combined = d_map[sw1] + d_map[sw2]
            combined = list(set(combined))
            d_map[sw1] = combined
            d_map[sw2] = combined

        return d_map


    def get_property_desc(self):
        return "Translation of expression from a source language with fused swizzles to a target language"

    def get_context_by_name(self, name):
        for dsl_inst in self.dsl_list+self.swizzles:
            for ctx in dsl_inst.contexts:
                if ctx.name == name:
                    return ctx, dsl_inst
        #assert False, "Unable to find ctx by name:" + name
        return None, None



    def generate_candidates(self):
        """Candidates are randomly generated programs of a specified depth (self.input_depth)

        Returns:
            (SwizzleContext ,DSLContext, Bool): Candidate consists of a swizzle context being applied to the target operation it is derived from. Because a swizzle may be applied to both the operands or to the result, we add a boolean flag to specify both cases.
        """

        swizzle_contexts = []
        for sw in self.swizzles:
            swizzle_contexts += sw.contexts


        candidates = []


        for swc in swizzle_contexts:
            relavent_insts_name = self.shuffle_deriviation_map[swc.name]



            for rin in relavent_insts_name:
                ctx, parent_inst = self.get_context_by_name(rin)

                if ctx == None:
                    continue


                expr_input_precision = ctx.in_precision
                swizzle_input_precision = swc.in_precision

                expr_output_size = ctx.out_vectsize
                swizzle_output_size = swc.out_vectsize

                expr_input_size = ctx.in_vectsize
                swizzle_input_size = swc.in_vectsize

                if  swizzle_input_size == expr_output_size:
                    # If we want to swizzle result, then we must check that
                    # the result of the operation has the same type as the input to the swizzle
                    candidates.append((swc, ctx, False))

                if  swizzle_output_size == expr_input_size:
                    candidates.append((swc, ctx, True))




        return candidates



    def get_swizzle_operand_index(self, swizzle_ctx):

        assert isinstance(swizzle_ctx, Context), "Expected Swizzle context!"
        for idx, arg in enumerate(swizzle_ctx.context_args):
            if isinstance(arg, BitVector):
                return idx
        return -1

    def get_swizzle_operand_indicies(self, swizzle_ctx):

        indicies = []
        assert isinstance(swizzle_ctx, Context), "Expected Swizzle context!"
        for idx, arg in enumerate(swizzle_ctx.context_args):
            if isinstance(arg, BitVector):
                indicies.append(idx)
        return indicies




    def property_holds_on_candidate(self, candidate):

        swizzle_ctx = candidate[0]
        dsl_expr = candidate[1]
        swizzle_operand = candidate[2]



        expr_input_precision = dsl_expr.in_precision
        swizzle_input_precision = swizzle_ctx.in_precision

        expr_output_size = dsl_expr.out_vectsize
        swizzle_output_size = swizzle_ctx.out_vectsize

        expr_input_size = dsl_expr.in_vectsize
        swizzle_input_size = swizzle_ctx.in_vectsize

        if not swizzle_operand and swizzle_input_size != expr_output_size:
            # If we want to swizzle result, then we must check that
            # the result of the operation has the same type as the input to the swizzle
            return False

        if swizzle_operand and swizzle_output_size != expr_input_size:
            # Similarly for the other way around
            return False



        # TODO: Create swizzle expression to synthesize

        swizzle_indicies = self.get_swizzle_operand_indicies(swizzle_ctx)
        dsl_expr_sym_indicies = self.get_swizzle_operand_indicies(dsl_expr)

        dsl_expr_sym_indicies = [idx for idx in dsl_expr_sym_indicies if dsl_expr.context_args[idx].size == expr_input_size]



        num_dsl_operands = len(dsl_expr_sym_indicies)
        num_swizzle_operands = len(swizzle_indicies)


        # Form 1: Apply swizzle to expr result

        form_1_regs = [Reg(str(i), expr_input_precision, dsl_expr.context_args[dsl_expr_sym_indicies[i % len(dsl_expr_sym_indicies)]].size) for i in range(len(dsl_expr_sym_indicies) * num_swizzle_operands)]
        form_1_expr = copy.deepcopy(swizzle_ctx)
        inner_expr_copy = copy.deepcopy(dsl_expr)

        # Bind non-relavent symbolic operands with registers
        for idx, arg in enumerate(inner_expr_copy.context_args):
            if isinstance(arg,BitVector) and idx not in dsl_expr_sym_indicies:
                new_reg = Reg(str(len(form_1_regs)), expr_input_precision, arg.size)
                form_1_regs.append(new_reg)
                inner_expr_copy.context_args[idx] = new_reg


        form_1_inner_exprs = [copy.deepcopy(inner_expr_copy) for i in range(num_swizzle_operands)]

        for i in range(num_swizzle_operands):
            start_offset = i * num_dsl_operands
            for j in range(num_dsl_operands):
                form_1_inner_exprs[i].context_args[dsl_expr_sym_indicies[j]] = form_1_regs[start_offset + j]


        # Bind dsl expressions to swizzle context operands
        for idx, swizzle_idx in enumerate(swizzle_indicies):
            form_1_expr.context_args[swizzle_idx] = form_1_inner_exprs[idx]


        # Form 2: Apply swizzle to expr operands

        form_2_regs = [Reg(str(i), swizzle_input_precision, swizzle_ctx.context_args[swizzle_indicies[i % len(swizzle_indicies)]].size) for i in range(len(swizzle_indicies) * num_dsl_operands)]
        form_2_expr = copy.deepcopy(dsl_expr)
        form_2_inner_exprs = [copy.deepcopy(swizzle_ctx) for i in range(num_dsl_operands)]


        # Bind non-relavent symbolic operands with registers
        for idx, arg in enumerate(form_2_expr.context_args):
            if isinstance(arg,BitVector) and idx not in dsl_expr_sym_indicies:
                new_reg = Reg(str(len(form_2_regs)), expr_input_precision, arg.size)
                form_2_regs.append(new_reg)
                form_2_expr.context_args[idx] = new_reg


        # Bind relavent symbolic operands with registers to swizzle contexts
        for i in range(num_dsl_operands):
            start_offset = i * num_swizzle_operands
            for j in range(num_swizzle_operands):
                form_2_inner_exprs[i].context_args[swizzle_indicies[j]] = form_2_regs[start_offset + j]


        # Bind swizzle contexts to dsl expression operands
        for idx, swizzle_idx in enumerate(dsl_expr_sym_indicies):
            form_2_expr.context_args[swizzle_idx] = form_2_inner_exprs[idx]






        regs = []
        spec_expr = None

        if swizzle_operand:
            regs = form_2_regs
            spec_expr = form_2_expr
        else:
            regs = form_1_regs
            spec_expr = form_1_expr




        input_sizes = [str(reg.size) for reg in regs]
        input_precs = [str(reg.precision) for reg in regs]



        ignore ,dsl_inst =  self.get_context_by_name(dsl_expr.name)
        ignore ,swizzle_inst =  self.get_context_by_name(swizzle_ctx.name)

        combined_list = [dsl_inst, swizzle_inst]


        # Create new dictionary for synthesis containing both swizzles and target instructions
        # except the current swizzle being used in spec. This way we can synthesize the change of
        # instructions when swizzle is happening

        base_prefix = "dict_"+ next(tempfile._get_candidate_names())

        dict_name = base_prefix+"_sema"
        sema_path = "/tmp/"+base_prefix+".py"

        converted_dict = convert_dsl_list_to_dict(combined_list)
        write_dsl_dict_to_file(converted_dict, sema_path, dict_name)

        source_code_synth_desc = create_synth_desc("fused", True, self.source_synth_desc.get_target_vector_sizes(), sema_path, dict_name)

        (is_simplified, simplified_expr) =  translate_expression(spec_expr, source_code_synth_desc, self.target_synth_desc,input_sizes, input_precs, src_language_dsl = combined_list, target_language_dsl = self.output_dsl_list)



        if is_simplified:
            self.simplify_map[self.serialize_candidate(candidate)] = (spec_expr, simplified_expr)



        return is_simplified


    def serialize_candidate(self, candidate):
        return candidate[0].name+"+"+candidate[1].name+"+"+str(candidate[2])

    def get_property_on_candidate(self, candidate):
        key = self.serialize_candidate(candidate)
        candidate_expr, simplified_expr = self.simplify_map[key]

        property_t = {"candidate": candidate_expr.emit_context_expr_string(), "simplified": simplified_expr }

        with open("Append_dict.py", "a+") as WriteFile:
            WriteFile.write(json.dumps(property_t, indent = 4))
        return property_t



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


















