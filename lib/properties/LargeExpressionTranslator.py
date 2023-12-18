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

class LargeExpressionTranslator(Translator):


    def __init__(self, dsl_list = [], source_synth_desc = None, target_synth_desc = None, target_dsl_list = [],   num_iterations = 1500, input_depth = 2, permute_limit = 3, exhaustive = False, shuffle_deriviation_map_path = "", context_deriviation_map_path = "" ,swizzles = []):

        # Prune masked expression, handle masked property generation seperately

        dsl_list = [dsl_inst for dsl_inst in dsl_list if "mask" not in dsl_inst.name]


        super().__init__(dsl_list = dsl_list, source_synth_desc = source_synth_desc, target_synth_desc = target_synth_desc, target_dsl_list = target_dsl_list ,
                         num_iterations = num_iterations, input_depth = input_depth, permute_limit = permute_limit, exhaustive = exhaustive)
        self.name = "LargeExpressionTranslator"
        self.swizzles = swizzles


        # Maps names of swizzle contexts to source language contexts
        self.shuffle_deriviation_map = self.merge_derivation_map(json.load(open(shuffle_deriviation_map_path)))
        self.context_deriviation_map = json.load(open(context_deriviation_map_path))





    def merge_derivation_map(self, d_map):


        # If a swizzle S is derived from a context C, belonging to equivlance class E
        # merge add all other contexts of in E for C.

        for idx,swc in enumerate(d_map):
            orig_contexts = copy.deepcopy(d_map[swc])
            contexts = d_map[swc]



            for c in orig_contexts:
                ctx, dsl_inst = self.get_context_by_name(c)
                if dsl_inst is None:
                    continue
                e_class_members = [dsl_ctx.name for dsl_ctx in dsl_inst.contexts]
                contexts += e_class_members

            contexts = list(set(contexts))

            d_map[swc] = contexts



        pairs = []


        name = lambda x : "hvx_swizzle_{}".format(x)

        def add_pair(lhs, rhs):
            pairs.append((name(lhs), name(rhs)))

        hi_lo = [41, 0, 2, 29, 43]
        even_odd = [1,3,16,18,122,124]

        def gen_pairs(ls):
            for i in range(len(ls)):
                for j in range(i+1, len(ls)):
                    add_pair(ls[i], ls[j])


        gen_pairs(hi_lo)
        gen_pairs(even_odd)


        keys = []
        for (sw1, sw2) in pairs:
            keys += [sw1, sw2]
            combined = d_map[sw1] + d_map[sw2]
            combined = list(set(combined))
            d_map[sw1] = combined
            d_map[sw2] = combined

        return d_map

    def get_property_desc(self):
        return "Translation of expression from a source language with fused swizzles to a target language"

    def get_context_by_name(self, name):
        for dsl_inst in self.dsl_list+self.swizzles+self.output_dsl_list:
            for ctx in dsl_inst.contexts:
                if ctx.name == name:
                    return ctx, dsl_inst
        print("Unable to find context for: ",name)
        return None, None


    def get_nested_contexts_name(self, ctx):
        if not isinstance(ctx, Context):
            return []

        names = [ctx.name]

        for arg in ctx.context_args:
            names += self.get_nested_contexts_name(arg)
        return list(set(names))


    def property_holds_on_candidate(self, candidate):

        src_expr = candidate
        expr_names = self.get_nested_contexts_name(src_expr)


        regs = self.get_registers(src_expr)




        target_context_names = []

        for name in expr_names:
            if name not in self.context_deriviation_map:
                continue
            assert name in self.context_deriviation_map, "{} not in context_deriviation_map".format(name)

            target_context_names += self.context_deriviation_map[name]

        target_context_names = list(set(target_context_names))

        swizzle_names = []
        for name in target_context_names:
            for swc in self.shuffle_deriviation_map:
                if name in self.shuffle_deriviation_map[swc]:
                    swizzle_names.append(swc)
        swizzle_names = list(set(swizzle_names))

        new_dicts = {}

        for name in swizzle_names + target_context_names:
            ctx, dsl_inst = self.get_context_by_name(name)

            if dsl_inst.name not in new_dicts:
                new_dicts[dsl_inst.name] = copy.deepcopy(dsl_inst)
                new_dicts[dsl_inst.name].contexts = []

            new_dicts[dsl_inst.name].contexts.append(ctx)

        combined_list = [new_dicts[key] for key in new_dicts]

        base_prefix = "dict_"+ next(tempfile._get_candidate_names())

        dict_name = base_prefix+"_sema"
        sema_path = "/tmp/"+base_prefix+".py"

        print(combined_list)
        converted_dict = convert_dsl_list_to_dict(combined_list)
        write_dsl_dict_to_file(converted_dict, sema_path, dict_name)


        combined_synth_desc = create_synth_desc("swizzle_ctx",True, self.synth_desc.get_target_vector_sizes(), sema_path ,dict_name)
        combined_synth_desc.emit_sema = True

        input_sizes = [str(reg.size) for reg in  regs]
        input_precs = [str(reg.precision) for reg in  regs]

        (is_simplified, simplified_expr) =  translate_expression(src_expr, self.synth_desc, combined_synth_desc, input_sizes, input_precs, src_language_dsl = self.dsl_list, target_language_dsl = combined_list)



        if is_simplified:
            key = self.serialize_candidate(candidate)
            self.context_map[key] = (src_expr, simplified_expr)



        return is_simplified


    def serialize_candidate(self, candidate):
        return candidate.emit_context_expr_string()

    def get_property_on_candidate(self, candidate):
        key = self.serialize_candidate(candidate)
        candidate_expr, simplified_expr = self.simplify_map[key]

        property_t = {"candidate": candidate_expr.emit_context_expr_string(), "simplified": simplified_expr }

        return property_t





