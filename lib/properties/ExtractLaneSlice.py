from properties.Property import *
from  utils.DSLInstructionUtils import *
import copy
from  common.Types import *

class ExtractLaneSlice(Property):
    """Check whether the associative property holds on DSL instructions.

    For example, the operations + is associative iff.

    (+ (+ A B) C) == (+ A (+ B C))

    Args:
        Property (class): Base Class for expressng properties
    """



    def __init__(self, dsl_list = [], synth_desc = None):

        super().__init__(name = "ExtractLaneSlice", dsl_list = dsl_list, synth_desc = synth_desc)
        self.context_map = {}
        #self.is_candidate_generator = True





    def get_property_desc(self):
        return "Extract the bitvector expression operating on a lane of a DSLInstruction"

    def generate_candidates(self):
        #expressions = create_exhaustive_expressions_generator(self.dsl_list, 1, use_eq_class = True)
        #return expressions
        return self.dsl_list



    def get_dsl_inst_formal_arg_to_size_map(self,dsl_inst, sample_context):

        func_prototype =  dsl_inst.semantics[0]

        # Operands are ordered in the order they appear in the prototype
        formal_args = func_prototype.strip().split("(")[-1].split(")")[0].strip().split(" ")[1:]
        formal_args = [arg for arg in formal_args if arg != '']



        #print(formal_args)
        arg_to_size_map = {}

        for idx, arg in enumerate(sample_context.context_args):
            if isinstance(arg, BitVector) or isinstance(arg, ConstBitVector):
                arg_to_size_map[formal_args[idx]] = arg.size

        return arg_to_size_map


    def is_store_line(self, line):
        not_include  = ["define", "bvpadhighbits", "for/list", "cond"]
        include  = ["%"]


        not_include_cond = all([word not in line for word in not_include])
        include_cond = all([word in line for word in include])

        return not_include_cond and include_cond


    def is_reducing_op(self, dsl_inst):
        original_sema = dsl_inst.semantics

        for line in original_sema:
            if ".red" in line:
                return True
        return False

    def extract_bitvector_expression(self, dsl_inst):
        bv_expr = []
        original_sema = dsl_inst.semantics

        is_reducing = self.is_reducing_op(dsl_inst)

        arg_map = self.get_dsl_inst_formal_arg_to_size_map(dsl_inst, dsl_inst.contexts[0])
        formal_params = [key for key in arg_map]
        try:
            # Pre-processing
            dsl_inst.semantics = inline_nested_extracts_in_sema(dsl_inst.semantics)
            dsl_inst.semantics = remove_redundant_extracts(dsl_inst.semantics, arg_map)
        except:
            dsl_inst.semantics = original_sema

        apply_cond = False
        for line_idx, line in enumerate(dsl_inst.semantics):
            if "apply" in line:
                next_line = dsl_inst.semantics[line_idx+1]
                if "concat" not in next_line:
                    apply_cond = True

            if "cond" in line:
                apply_cond = True

            if dsl_inst.name in line:
                continue
            elif "extract" in line:
                continue
            elif self.is_store_line(line):
                if apply_cond:
                    apply_cond = False
                continue
            elif "bvpadhighbits" in line:
                continue
            elif "(bv" in line and (apply_cond and is_reducing) :
                bv_expr.append(line)
            elif "(bv" in line and not is_reducing :
                bv_expr.append(line)
            else:
                continue

        return bv_expr


    def property_holds_on_candidate(self, candidate):
        dsl_inst = candidate
        expr = self.extract_bitvector_expression(dsl_inst)
        key = self.serialize_candidate(candidate)
        self.context_map[key] = (candidate, expr)
        return True


    def serialize_candidate(self, candidate):
        return candidate.name

    def get_property_on_candidate(self, candidate):
        key = self.serialize_candidate(candidate)
        input_expression, output_expression = self.context_map[key]
        return {"candidate": candidate.name, "slice_expr" : output_expression }








    def emit_property_to_egg(self, property_map):
        return []








