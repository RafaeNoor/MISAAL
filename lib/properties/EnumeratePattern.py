from properties.Property import *
from patterns.PatternUtils import *
from  utils.DSLInstructionUtils import *
from utils.ReadDSL import read_string_to_dsl
import copy
from  common.Types import *

class EnumeratePattern(Property):


    def __init__(self, dsl_list = [], synth_desc = None, input_patterns_dict = {}):

        super().__init__(name = "EnumeratePattern" ,dsl_list = dsl_list, synth_desc = synth_desc, is_candidate_generator = True)
        self.input_patterns_dict = input_patterns_dict
        self.context_map = {}




    def get_property_desc(self):
        return "Given a synthesized concrete pattern, generate all possible output patterns which are also valid given the AutoLLVM IR classes they belond to"

    def generate_candidates(self):
        for key in self.input_patterns_dict:
            prop_list = self.input_patterns_dict[key]
            for prop in prop_list:
                src_pattern_str = prop['property']['src']
                dst_pattern_str = prop['property']['dst']

                print(src_pattern_str)
                src_expr = read_string_to_dsl(src_pattern_str, self.dsl_list)
                dst_expr = read_string_to_dsl(dst_pattern_str, self.dsl_list)

                if is_expression_constant(src_expr, self.dsl_list) or is_expression_constant(dst_expr, self.dsl_list):
                    print("Constant expression encountered!")
                    continue

                src_eq_class = get_eq_class_for_ctx(src_expr, self.dsl_list)

                for ctx in src_eq_class.contexts:
                    size = ctx.out_vectsize
                    if can_pattern_be_abstracted_for_output_size(src_expr, dst_expr, self.dsl_list, size):
                        yield (src_expr, dst_expr, size, ctx)




    def property_holds_on_candidate(self, candidate):
        key = self.serialize_candidate(candidate)
        src_expr = copy.deepcopy(candidate[0])
        dst_expr = copy.deepcopy(candidate[1])
        output_size = candidate[2]
        ctx = candidate[3]


        success, src_expr_str, dst_expr_str = translate_pattern_for_output_size(src_expr, dst_expr, self.dsl_list, output_size, required_src_ctx = ctx)

        if success:
            self.context_map[key] = (src_expr_str, dst_expr_str)


        return success

    def serialize_candidate(self, candidate):
        key = "+".join([candidate[0].emit_context_expr_string(), candidate[1].emit_context_expr_string(), str(candidate[2]), candidate[3].name])
        return key

    def get_property_on_candidate(self, candidate):
        key = self.serialize_candidate(candidate)

        src_expr_str, dst_expr_str = self.context_map[key]

        return {'src': src_expr_str, 'dst': dst_expr_str, 'output_size': candidate[2], 'original_src_expr': candidate[0].emit_context_expr_string(), "original_dst_expr": candidate[1].emit_context_expr_string(), "src_ctx": candidate[3].name}


    def emit_property_to_egg(self, property_map):
        # Does not apply to this property
        return []















