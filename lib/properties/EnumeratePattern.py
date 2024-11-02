from properties.Property import *
import gc
from patterns.PatternUtils import *
from  utils.DSLInstructionUtils import *
from utils.ReadDSL import read_string_to_dsl
import copy
from  common.Types import *
from utils.ConcretizeUtils import get_valid_concretization_generator
from common.StructDef import StructDef
from utils.CanonicalizeExpressions import CanonicalizeExpression

class EnumeratePattern(Property):


    def __init__(self, dsl_list = [], synth_desc = None, input_patterns_dict = {}):

        super().__init__(name = "EnumeratePattern" ,dsl_list = dsl_list, synth_desc = synth_desc, is_candidate_generator = True)
        self.input_patterns_dict = input_patterns_dict
        self.context_map = {}
        self.canon_utils = CanonicalizeExpression()




    def get_property_desc(self):
        return "Given a synthesized concrete pattern, generate all possible output patterns which are also valid given the AutoLLVM IR classes they belond to"

    def generate_candidates(self):
        for key in self.input_patterns_dict:
            prop_list = self.input_patterns_dict[key]
            prop_list = prop_list[:1]
            for prop in prop_list:
                src_pattern_str = prop['property']['src']
                dst_pattern_str = prop['property']['dst']

                src_expr = read_string_to_dsl(src_pattern_str, self.dsl_list)
                dst_expr = read_string_to_dsl(dst_pattern_str, self.dsl_list)



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


        try:

            src_expr = candidate[0]
            dst_expr = candidate[1]



            if is_expression_constant(src_expr, self.dsl_list) or is_expression_constant(dst_expr, self.dsl_list):
                print("Constant expression encountered!")
                return False

            output_size = candidate[2]
            src_ctx = candidate[3]
            dst_ctx = candidate[4]

            print("Testing for", src_ctx.name, dst_ctx.name)


            src_eq_class = get_eq_class_for_ctx(src_expr, self.dsl_list)
            dst_eq_class = get_eq_class_for_ctx(dst_expr, self.dsl_list)

            valid_src_conc_gen = get_valid_concretization_generator(src_expr, output_size, self.dsl_list, root_ctx_name = src_ctx.name)


            start_time = time.time()
            for valid_src_conc in valid_src_conc_gen:
                if valid_src_conc.name == src_ctx.name:
                    print("Found matching src context!")
                    src_expr = valid_src_conc
                    break

            end_time = time.time()
            print("Find src expression time Elapsed time", end_time-start_time)
            valid_dst_conc_gen = get_valid_concretization_generator(dst_expr, output_size, self.dsl_list, root_ctx_name = dst_ctx.name)

            start_time = time.time()
            for valid_dst_conc in valid_dst_conc_gen:
                if valid_dst_conc.name == dst_ctx.name:
                    print("Found matching dst context!")
                    dst_expr = valid_dst_conc
                    break

            end_time = time.time()
            print("Find dst expression time Elapsed time", end_time-start_time)


            # Get valid concretization of src expression with required context in root and
            # then create filtered list


            filtered_list = self.dsl_list



            start_time = time.time()
            success, src_expr_str, dst_expr_str = translate_pattern_for_output_size(src_expr, dst_expr, filtered_list, output_size, required_src_ctx = src_ctx, required_dst_ctx = dst_ctx)
            end_time = time.time()
            print("Find conc expression time Elapsed time", end_time-start_time)

            if not success:
                return False

            # Confirm that the parsed expressions match the required structure
            synth_src_expr = read_string_to_dsl(src_expr_str, self.dsl_list)

            # isCanonical matches structure according to DSL list
            if not self.canon_utils.isCanonical(synth_src_expr, src_expr):
                return False

            synth_dst_expr = read_string_to_dsl(dst_expr_str, self.dsl_list)

            # isCanonical matches structure according to DSL list
            if not self.canon_utils.isCanonical(synth_dst_expr, dst_expr):
                return False





            if success:
                self.context_map[key] = (src_expr_str, dst_expr_str)




            return success
        except Exception as e:
            print("Caught exception", e)
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


    def run_on_batch_completion(self):
        gc.collect()















