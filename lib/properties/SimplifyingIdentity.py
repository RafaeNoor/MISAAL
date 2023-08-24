from properties.Property import Property
import json
from  utils.DSLInstructionUtils import *
from utils.GenerateRandomExpr import create_random_expression
import copy
from  common.Types import *

class SimplifyingIdentity(Property):
    """SimplifyingIdentity property refers to those expressions which can be reduced to smaller expressions
    with fewer instructions. For example:
        (+ A (- B A)) can be simplified to A (at least for integers).

        In this case the simplified expression is one of the operands, but it may be another
        smaller expression entirely. We make use of synthesis to find smaller expressions.

    Args:
        Property (_type_): _description_
    """


    def __init__(self, dsl_list = [], synth_desc = None, num_iterations = 1000, input_depth = 2, permute_limit = 5):

        # Prune masked expression, handle masked property generation seperately

        dsl_list = [dsl_inst for dsl_inst in dsl_list if "mask" not in dsl_inst.name]
        super().__init__(name = "SimplifyingIdentity", dsl_list = dsl_list, synth_desc = synth_desc)
        self.num_iterations = num_iterations
        self.input_depth = input_depth
        self.permute_limit = permute_limit
        self.simplify_map = {}






    def get_property_desc(self):
        return "Check Simplifying Instruction properties for DSLInstructions expressions"

    def generate_candidates(self):
        """Candidates are randomly generated programs of a specified depth (self.input_depth)

        Returns:
            [DSLExpressions]: _description_
        """


        expressions = []
        for i in range(self.num_iterations):

            ## Inclusive for loop
            for depth in range(1, self.input_depth + 1):

                try:
                    expr, discard = create_random_expression(self.dsl_list, depth = depth,
                    required_output_precision = None, required_output_size = None)
                    expressions += self.permute_ordering_of_registers(expr, limit = self.permute_limit)
                except:
                    continue

        return expressions


    def get_registers(self, ctx):

        regs = []

        if isinstance(ctx, Context):
            for arg in ctx.context_args:
                regs += self.get_registers(arg)
        elif isinstance(ctx, Reg):
            return [ctx]
        else:
            return []
        # Deduplicate and order according to increasing order

        unique_regs = []

        for reg in regs:
            unique_regs.append(int(reg.index))
        unique_regs = list(set(unique_regs))

        unique_regs.sort()

        # Sort in increasing order
        ordered_regs = ['empty'] * len(unique_regs)

        for reg in regs:
            ordered_regs[unique_regs.index(int(reg.index))] = reg

        return ordered_regs

    def replace_reg_with_expr(self, dsl_expression, input_reg, insert_expr):
        """Given a dsl expression, it traverses the arguments recursively and replaces all
        instances of input reg with insert_expr

        Args:
            dsl_expression (DSLInstruction): _description_
            input_reg (Reg): _description_
            insert_expr (Reg or DSLInstruciton): _description_
        """

        if isinstance(dsl_expression, Context):

            for i in range(len(dsl_expression.context_args)):
                dsl_expression.context_args[i] = self.replace_reg_with_expr(dsl_expression.context_args[i],
                input_reg, insert_expr)
            return dsl_expression
        elif isinstance(dsl_expression, Reg):
            if input_reg.index == dsl_expression.index:
                return insert_expr

        return dsl_expression


    def permute_ordering_of_registers(self, dsl_expression, limit = 5):
        """To get simplfying identity property, we may require that an operand be used
        multiple times :
        e.g. a + a + a = 3 * a

        We first identify all the registers which are of the same bitvector size, and then permute
        them. We also include the degenerate case where all registers are unique.

        Args:
            dsl_expression (_type_): _description_
            limit (int, optional): _description_. Defaults to 5.
        """

        ordered_regs = self.get_registers(dsl_expression)

        # Cluster registers according to their sizes
        size_to_regs_map = {}

        for idx, reg in enumerate(ordered_regs):

            key = str(reg.size)

            if key not in size_to_regs_map:
                size_to_regs_map[key] = []

            size_to_regs_map[key].append(idx)



        combinations = [dsl_expression]

        for key in size_to_regs_map:

            if len(combinations) >= limit:
                break

            if len(size_to_regs_map[key]) == 1:
                continue


            matching_regs = size_to_regs_map[key]

            for i in range(len(matching_regs)):
                for j in range(i+1,len(matching_regs)):

                    if len(combinations) >= limit:
                        return combinations

                    reg_i = ordered_regs[matching_regs[i]]
                    reg_j = ordered_regs[matching_regs[j]]
                    cloned_expression = copy.deepcopy(dsl_expression)

                    cloned_expression = self.replace_reg_with_expr(cloned_expression, reg_i, reg_j)
                    combinations.append(cloned_expression)
        return combinations










    def property_holds_on_candidate(self, candidate):


        dsl_expression = candidate

        #print(candidate.emit_context_expr_string())
        #return False


        regs = self.get_registers(dsl_expression)

        # After permuting the register arguments, some expressions may have some discontinuity in the registers
        # included. For example, consider the expression (min reg_1 reg_1) . It's only using reg_1, so we need to create
        # a dummy register for reg_0

        used_regs = [int(reg.index) for reg in regs]
        max_regs = max(used_regs)

        adjusted_regs = [[]] * (max_regs + 1)

        for i in range(len(adjusted_regs)):

            if i in used_regs:
                # Find corresponding reg type info
                for reg in regs:
                    if int(reg.index) == i:
                        adjusted_regs[i] = reg

            else:
                adjusted_regs[i] = Reg(str(i), 8, 8)



        regs = adjusted_regs

        input_sizes = [str(reg.size) for reg in regs]
        input_precs = [str(reg.precision) for reg in regs]
        (is_simplified, simplified_expr) =  simplify_expression(dsl_expression, self.synth_desc, input_sizes, input_precs)



        if is_simplified:
            self.simplify_map[candidate.emit_context_expr_string()] = simplified_expr



        return is_simplified


    def serialize_candidate(self, candidate):
        return candidate.emit_context_expr_string()

    def get_property_on_candidate(self, candidate):
        property_t = {"candidate": candidate.emit_context_expr_string(), "simplified": self.simplify_map[candidate.emit_context_expr_string()]}

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


                input_expression = read_string_to_dsl(input_expression_string, self.dsl_list)



                output_expression = read_string_to_dsl(output_expression_string, self.dsl_list)


                param_map, reverse_map  = generate_parameter_map(input_expression, output_expression)

                rule = emit_rewrite_expr(input_expression, output_expression, bidirectional = True, param_map = param_map)

                egg_rules.append(rule)

        return egg_rules


















