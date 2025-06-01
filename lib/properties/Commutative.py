from properties.Property import *
from  utils.DSLInstructionUtils import *
import copy
from  common.Types import *
import json

class Commutative(Property):
    """Class for inferring the commutative property on DSL Instructions. This property
    returns a list of pair of indices for which symbolic/concrete vector inputs are commutative with respect
    to each other.

    For example:
    (vec-add a b) applies element wise integer addition to input symbolic vectors a and b.

    We know integer addition is commutative hence applies this property would yield the
    property:
    [[0,1]]

    That is, symbolic vectors at index 0 and 1 can commute with each other.

    Note that the indices refers to the an ordered list of symbolic vectors from the total arguments
    to the DSL instruction, not the actual argument index which may contain other parameters.

    Args:
        Property (BaseClass): Inherits from base class Property
    """


    def __init__(self, dsl_list = [], synth_desc = None):

        # Prune masked expression, handle masked property generation seperately

        dsl_list = [dsl_inst for dsl_inst in dsl_list if "mask" not in dsl_inst.name]


        super().__init__(name = "Commutative", dsl_list = dsl_list, synth_desc = synth_desc)

        self.context_map = {}




    def get_property_desc(self):
        return "Check Commutativity for DSLInstructions"

    def generate_candidates(self):
        """Generates a list 2-tupple of candidates of the form:
        (DSLInstruction, [Pair of Indicies]), where the Pair of indices lists
        possible commuting pairs

        Returns:
            [(DSL_Instruction, Pair of Indices)]
        """

        tuples = []

        for dsl_inst in self.dsl_list:
            permutable_args = self.get_permutable_args_candidates_instruction(dsl_inst)
            for pairs in permutable_args:
                tuples.append((dsl_inst, pairs))

        return tuples

    def get_permutable_args_candidates_instruction(self, dsl_inst):
        """Identify the permutable arg candidates which can be applied on the overall equivalence class. We currently
        take the intersection of the possible candidates across contexts.

        Args:
            dsl_inst (DSLInstruction): DSLInstruction type
        """
        context_pairs = [set(self.get_commutable_args_candidates_context(ctx)) for ctx in dsl_inst.contexts]


        intersected_pairs = context_pairs[0]

        for pairs in context_pairs[1:]:
            intersected_pairs = intersected_pairs.intersection(pairs)


        return list(intersected_pairs)






    def get_commutable_args_candidates_context(self, ctx):
        """Returns a list of 2-tupples for arguments for a given context
        which may be commutable. The criterion for this requires that the operands have the
        same bitvector size. We will verify indeed that these operands compute in a subsequent step.

        Args:
            ctx (Context): Specific Context from a DSLInstruction.
        """

        # Map from input size to
        arg_sizes_map = {}
        for idx, arg in enumerate(ctx.context_args):
            if isinstance(arg, ConstBitVector) or isinstance(arg, BitVector):
                size_key = str(arg.size)

                if size_key not in arg_sizes_map:
                    arg_sizes_map[size_key] = []

                arg_sizes_map[size_key].append(idx)


        permutable_args = []

        for size_key in arg_sizes_map:

            arg_indices = arg_sizes_map[size_key]

            for i in range(0, len(arg_indices)):
                for j in range(i+1 , len(arg_indices)):
                    permutable_args.append((arg_indices[i], arg_indices[j]))


        return permutable_args


    def property_holds_on_candidate(self, candidate):

        dsl_inst = candidate[0]
        pair = candidate[1]

        sample_ctx = self.get_sample_context_for_property(dsl_inst)

        print("Checking if commutativity holds for", dsl_inst.name, "on", pair)


        # We know pairs are of the same size so we have to get the bitvector size
        bv_size = sample_ctx.context_args[pair[0]].size

        reg_0 = Reg("0" , 16, bv_size)
        reg_1 = Reg("1" , 16, bv_size)

        vector_args = [bv_size, bv_size]

        # Create an expression with the two operands swapped
        commute_expr_0 = copy.deepcopy(sample_ctx)
        commute_expr_0.context_args[pair[0]] = reg_0
        commute_expr_0.context_args[pair[1]] = reg_1

        commute_expr_1 = copy.deepcopy(sample_ctx)
        commute_expr_1.context_args[pair[1]] = reg_0
        commute_expr_1.context_args[pair[0]] = reg_1

        # For all other operands not being tested, we insert a symbolic value and bind it to the same place
        other_indices = []
        for idx, arg in enumerate(commute_expr_0.context_args):
            if idx == pair[0] or idx == pair[1]:
                continue

            if not isinstance(arg, BitVector):
                continue

            other_indices.append(idx)


        for count, other_index in enumerate(other_indices):
            arg_size = commute_expr_0.context_args[other_index].size

            reg_i = Reg(str(count + 2), 16, arg_size)
            vector_args.append(arg_size)

            commute_expr_0.context_args[other_index] = reg_i
            commute_expr_1.context_args[other_index] = reg_i






        print(commute_expr_0.emit_context_expr_string())





        property_holds = check_if_contexts_equal(commute_expr_0, commute_expr_1, dsl_inst, dsl_inst, vector_args, self.synth_desc, dsl_list = [dsl_inst])


        if property_holds.returncode == 0:
            key = self.serialize_candidate(candidate)
            self.context_map[key] = (commute_expr_0, commute_expr_1)


        return property_holds.returncode == 0


    def serialize_candidate(self, candidate):
        return candidate[0].name +"_"+str(candidate[1])

    def get_property_on_candidate(self, candidate):
        key = self.serialize_candidate(candidate)
        input_expression, output_expression = self.context_map[key]
        return {"candidate": candidate[0].name, "indices": candidate[1],
                "input_expression": input_expression.emit_context_expr_string(),
                "output_expression": output_expression.emit_context_expr_string()
                }


    def emit_property_to_egg(self, property_map):

        egg_rules = []


        for key in property_map:
            for instance in property_map[key]:

                property_object = instance['property']

                input_expression_string = property_object['input_expression']


                output_expression_string = property_object['output_expression']



                input_expression = read_string_to_dsl(input_expression_string, self.dsl_list)



                output_expression = read_string_to_dsl(output_expression_string, self.dsl_list)


                param_map, reverse_map  = generate_parameter_map(input_expression, output_expression)

                rule = emit_rewrite_expr(input_expression, output_expression, bidirectional = True, param_map = param_map)

                egg_rules.append(rule)

        return egg_rules


    def run_on_completion(self, pmap):
        commutative_map = {}
        for key, props in pmap.items():
            prop = props[0]['property']
            candidate = prop['candidate']
            if candidate not in commutative_map:
                commutative_map[candidate] = []
            commutative_map[candidate].append(prop['indices'])

        cmap_path = f"commutative_map_{self.synth_desc.target_name}.json"
        if self.work_dir is not None:
            cmap_path = os.path.join(self.work_dir, cmap_path)

        with open(cmap_path, "w+") as OutFile:
            OutFile.write(json.dumps(commutative_map, indent = 2))

        return commutative_map





















