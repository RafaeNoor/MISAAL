from properties.Property import *
from patterns.PatternUtils import *
from  utils.DSLInstructionUtils import *
from utils.ReadDSL import read_string_to_dsl
import copy
from  common.Types import *
from utils.ConcretizeUtils import get_valid_concretization_generator

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

                src_expr = read_string_to_dsl(src_pattern_str, self.dsl_list)
                dst_expr = read_string_to_dsl(dst_pattern_str, self.dsl_list)


                try:
                    if is_expression_constant(src_expr, self.dsl_list) or is_expression_constant(dst_expr, self.dsl_list):
                        print("Constant expression encountered!")
                        continue
                except:
                    print("Exception when checking constant")
                    continue


                src_eq_class = get_eq_class_for_ctx(src_expr, self.dsl_list)

                if isinstance(dst_expr, Reg):
                    continue

                dst_eq_class = get_eq_class_for_ctx(dst_expr, self.dsl_list)



                for src_ctx in src_eq_class.contexts:
                    size = src_ctx.out_vectsize
                    for dst_ctx in dst_eq_class.contexts:
                        try:
                            if src_ctx.out_vectsize != dst_ctx.out_vectsize:
                                continue

                            if can_pattern_be_abstracted_for_output_size(src_expr, dst_expr, self.dsl_list, size):
                                yield (src_expr, dst_expr, size, src_ctx, dst_ctx)
                        except:
                            print("Encountered exception")
                            continue




    def property_holds_on_candidate(self, candidate):
        key = self.serialize_candidate(candidate)
        src_expr = copy.deepcopy(candidate[0])
        dst_expr = copy.deepcopy(candidate[1])
        output_size = candidate[2]
        src_ctx = copy.deepcopy(candidate[3])
        dst_ctx = copy.deepcopy(candidate[4])

        print("Testing for", src_ctx.name, dst_ctx.name)

        try:


            src_eq_class = get_eq_class_for_ctx(src_expr, self.dsl_list)
            dst_eq_class = get_eq_class_for_ctx(dst_expr, self.dsl_list)

            valid_src_conc_gen = get_valid_concretization_generator(src_expr, output_size, self.dsl_list)

            for valid_src_conc in valid_src_conc_gen:
                if valid_src_conc.name == src_ctx.name:
                    print("Found matching src context!")
                    src_expr = valid_src_conc
                    break

            valid_dst_conc_gen = get_valid_concretization_generator(dst_expr, output_size, self.dsl_list)

            for valid_dst_conc in valid_dst_conc_gen:
                if valid_dst_conc.name == dst_ctx.name:
                    print("Found matching dst context!")
                    dst_expr = valid_dst_conc
                    break


            # Get valid concretization of src expression with required context in root and
            # then create filtered list


            filtered_list = [e for e in self.dsl_list if e.name not in [src_eq_class.name, dst_eq_class.name]]
            src_eq_class_copy = copy.deepcopy(src_eq_class)
            src_eq_class_copy.contexts = [src_ctx]
            filtered_list += [src_eq_class_copy]

            dst_eq_class_copy = copy.deepcopy(dst_eq_class)
            dst_eq_class_copy.contexts = [dst_ctx]
            filtered_list += [dst_eq_class_copy]


            success, src_expr_str, dst_expr_str = translate_pattern_for_output_size(src_expr, dst_expr, filtered_list, output_size, required_src_ctx = src_ctx, required_dst_ctx = dst_ctx)

            if success:
                self.context_map[key] = (src_expr_str, dst_expr_str)


            return success
        except:
            print("Caught exception")
            return False

    def serialize_candidate(self, candidate):
        key = "+".join([candidate[0].emit_context_expr_string(), candidate[1].emit_context_expr_string(), str(candidate[2]), candidate[3].name, candidate[4].name])
        return key

    def get_property_on_candidate(self, candidate):
        key = self.serialize_candidate(candidate)

        src_expr_str, dst_expr_str = self.context_map[key]

        return {'src': src_expr_str, 'dst': dst_expr_str, 'output_size': candidate[2], 'original_src_expr': candidate[0].emit_context_expr_string(), "original_dst_expr": candidate[1].emit_context_expr_string(), "src_ctx": candidate[3].name, "dst_ctx": candidate[4].name}


    def emit_property_to_egg(self, property_map):
        # Does not apply to this property
        return []















