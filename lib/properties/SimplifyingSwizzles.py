from properties.Property import *
import json
from  utils.DSLInstructionUtils import *
from utils.GenerateRandomExpr import create_random_expression
import copy
from  common.Types import *
from properties.SimplifyingIdentity import SimplifyingIdentity
from properties.Translator import Translator

class SimplifyingSwizzles(Translator):


    def __init__(self, dsl_list = [], synth_desc = None, num_iterations = 1000, input_depth = 2, permute_limit = 1):

        # Prune masked expression, handle masked property generation seperately

        dsl_list = [dsl_inst for dsl_inst in dsl_list if "mask" not in dsl_inst.name]
        #dsl_list = [dsl_inst for dsl_inst in dsl_list if get_max_symbolic_args(dsl_inst) <= 2]

        print("DSL Inst: ", len(dsl_list))



        super().__init__(dsl_list = dsl_list, source_synth_desc = synth_desc , target_synth_desc = synth_desc, num_iterations = num_iterations, target_dsl_list = dsl_list, input_depth = input_depth,
                         permute_limit = permute_limit)
        self.name = "SimplifyingSwizzles"

        self.dsl_list = dsl_list






    def get_property_desc(self):
        return "Check Simplifying Instruction properties for Swizzle expressions"

    def generate_candidates(self):
        """Candidates are randomly generated programs of a specified depth (self.input_depth)

        Returns:
            [DSLExpressions]: _description_
        """


        contexts = 0
        insts = len(self.dsl_list)

        for d in self.dsl_list:
            contexts+= len(d.contexts)

        print("{} equivalence classes with total {} contexts".format(insts,contexts))


        expressions = []

        for d in range(1, self.input_depth + 1 ):
            expressions_d = create_exhaustive_expressions(self.dsl_list, d)

            print("Number of candidates generated at depth {} is {}...".format(d, len(expressions_d)))
            expressions += expressions_d




        return expressions




















