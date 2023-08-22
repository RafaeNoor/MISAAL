from properties.Property import Property
from  utils.DSLInstructionUtils import *
import copy
from  common.Types import *

class Distributive(Property):



    def __init__(self, dsl_list = [], synth_desc = None):
        super().__init__(name = "Distributive", dsl_list = dsl_list, synth_desc = synth_desc)

        # Memo table to avoid recomputing search for expressions producing output of size
        self.size_memo = {}
        self.context_map = {}




    def get_property_desc(self):
        return "Check Distributive for DSLInstructions expression trees of depth 2"

    def get_dsl_insts_with_output_size(self, output_size):
        """Return DSL Instructions which have produce the same output size as specified, and have
        at least two symbolic operands which are of the same size as output_size

        Args:
            output_size (int): _description_

        Returns:
            [DSLInstruction]: _description_
        """

        if str(output_size) in self.size_memo:
            return self.size_memo[str(output_size)]

        matches = []
        for dsl_inst in self.dsl_list:
            sample_ctx = dsl_inst.get_sample_context()

            if sample_ctx.has_output_size() and (sample_ctx.get_output_size() == output_size):
                num_matching_inputs = 0

                # Only check distributivity for type legal programs
                for arg in sample_ctx.context_args:
                    if isinstance(arg, BitVector) and arg.size == output_size:
                        num_matching_inputs += 1

                if num_matching_inputs >= 2:
                    matches.append(dsl_inst)


        self.size_memo[str(output_size)] = matches


        return matches



    def generate_candidates(self):
        """Generate list of 3-tuples where the first element is a DSLInstruction, the second element is also a DSLInstruction,
        and the third element is a pair of indices. The candidate to test is to check if the first DSLInstruciton can be distributed
        across the second DSL Instruction, using the first element indices of the pairs.

        For example: (+ , *, [0,1])
        can be interpreted as checking if:
        A + (C * D) =? (A * C) + (A * D) // Operand at Index 0 is a symbolic hole A and Operand at Index 1 is second DSLInstruction

        By convention we only test the second index to distribute over. Commutativity should be able to capture other cases, but we should
        verify if that is true?

        Returns:
            _type_: _description_
        """

        tuples = []

        for dsl_inst in self.dsl_list:
            distributable_args = self.get_distributable_args_candidates_instruction(dsl_inst)

            outer_context = dsl_inst.get_sample_context()
            for pairs in distributable_args:
                bv_size = outer_context.context_args[pairs[0]].size

                inner_matches = self.get_dsl_insts_with_output_size(bv_size)

                for match in inner_matches:
                    if "mask" in dsl_inst.name or "mask" in match.name:
                        continue
                    tuples.append((dsl_inst, match, pairs))



        return tuples

    def get_distributable_args_candidates_instruction(self, dsl_inst):
        """Identify the distributable arg candidates which can be applied on the overall equivalence class. We currently
        take the intersection of the possible candidates across contexts.

        Args:
            dsl_inst (DSLInstruction): DSLInstruction type
        """
        context_pairs = [set(self.get_distributable_args_candidates_context(ctx)) for ctx in dsl_inst.contexts]


        intersected_pairs = context_pairs[0]

        for pairs in context_pairs[1:]:
            intersected_pairs = intersected_pairs.intersection(pairs)


        return list(intersected_pairs)






    def get_distributable_args_candidates_context(self, ctx):
        """Returns a list of 2-tupples for arguments for a given context
        which may be distributable. The criterion for this requires that the operands have the
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


        distributable_args = []

        for size_key in arg_sizes_map:

            arg_indices = arg_sizes_map[size_key]

            for i in range(0, len(arg_indices)):
                for j in range(i+1 , len(arg_indices)):
                    distributable_args.append((arg_indices[i], arg_indices[j]))


        return distributable_args


    def property_holds_on_candidate(self, candidate):

        outer_dsl_inst = candidate[0]
        inner_dsl_inst = candidate[1]
        pair = candidate[2]

        outer_sample_ctx = outer_dsl_inst.get_sample_context()
        inner_sample_ctx = inner_dsl_inst.get_sample_context()

        print("Checking if Distributivity holds for", outer_dsl_inst.name, "over", inner_dsl_inst.name ,"on", pair)


        # We know pairs are of the same size so we have to get the bitvector size
        bv_size = inner_sample_ctx.context_args[pair[0]].size

        reg_0 = Reg("0" , 16, bv_size)
        reg_1 = Reg("1" , 16, bv_size)
        reg_2 = Reg("2" , 16, bv_size)

        regs = [reg_0, reg_1, reg_2]

        vector_args = [bv_size, bv_size, bv_size]

        # Create expression of the first form. For example: A * (B + C) for (*, +, [0,1])

        # e.g. B + C

        form_1_inner_expression = copy.deepcopy(inner_sample_ctx)

        reg_counter = 1
        for i in range(len(form_1_inner_expression.context_args)):
            arg = form_1_inner_expression.context_args[i]
            if isinstance(arg, BitVector) and arg.size == bv_size:
                form_1_inner_expression.context_args[i] = regs[reg_counter]
                reg_counter += 1

                if reg_counter == len(regs):
                    break

        # e.g. A * (B+C)
        form_1_outer_expression = copy.deepcopy(outer_sample_ctx)

        form_1_outer_expression.context_args[pair[0]] = reg_0
        form_1_outer_expression.context_args[pair[1]] = form_1_inner_expression


        # Create expression of the second form. For example: (A * B) + (A *C) for (*, +, [0,1])

        # Left expression e.g. (A * B)
        form_2_inner_left_expression =  copy.deepcopy(outer_sample_ctx)
        form_2_inner_left_expression.context_args[pair[0]] = reg_0
        form_2_inner_left_expression.context_args[pair[1]] = reg_1

        # Right expression e.g. (A * C)
        form_2_inner_right_expression =  copy.deepcopy(outer_sample_ctx)
        form_2_inner_right_expression.context_args[pair[0]] = reg_0
        form_2_inner_right_expression.context_args[pair[1]] = reg_2


        # (A * B) + (A * C)

        form_2_outer_expression = copy.deepcopy(inner_sample_ctx)
        reg_counter = 0
        regs = [form_2_inner_left_expression, form_2_inner_right_expression]
        for i in range(len(form_2_outer_expression.context_args)):
            arg = form_2_outer_expression.context_args[i]
            if isinstance(arg, BitVector) and arg.size == bv_size:
                form_2_outer_expression.context_args[i] = regs[reg_counter]
                reg_counter += 1

                if reg_counter == 2:
                    break




        # Replace all other operands which are not being processed with symbolic holes of the appropriate size. We have to
        # ensure that such symbolic bitvectors refer to the same operand.

        outer_other_indices = []

        for idx, arg in enumerate(form_1_outer_expression.context_args):
            if isinstance(arg, BitVector) :
                outer_other_indices.append(idx)

        # Replace this index argument in both pairs of expressions with the same symbolic hole:
        for idx in outer_other_indices:
            bv_size = form_1_outer_expression.context_args[idx].size
            reg_i = Reg(str(len(vector_args)), 16, bv_size)
            vector_args.append(bv_size)

            form_1_outer_expression.context_args[idx] = reg_i

            form_2_inner_left_expression.context_args[idx] = reg_i
            form_2_inner_right_expression.context_args[idx] = reg_i



        inner_other_indices = []
        for idx, arg in enumerate(form_1_inner_expression.context_args):
            if isinstance(arg, BitVector):
                inner_other_indices.append(idx)

        for idx in inner_other_indices:
            bv_size = form_1_inner_expression.context_args[idx].size
            reg_i = Reg(str(len(vector_args)), 16, bv_size)
            vector_args.append(bv_size)

            form_1_inner_expression.context_args[idx] = reg_i
            form_2_outer_expression.context_args[idx] = reg_i


    # TODO: Masked operations are distributive only if their mask variables are made the same





        property_holds = check_if_contexts_equal(form_1_outer_expression, form_2_outer_expression, outer_dsl_inst, inner_dsl_inst, vector_args, self.synth_desc)

        if property_holds.returncode == 0:
            self.context_map[self.serialize_candidate(candidate)] = (form_1_outer_expression, form_2_outer_expression)

        print(property_holds.returncode == 0)
        return property_holds.returncode == 0


    def serialize_candidate(self, candidate):
        return (candidate[0].name + "+" + candidate[1].name+"+"+str(candidate[2]))

    def get_property_on_candidate(self, candidate):
        key = self.serialize_candidate(candidate)
        input_expression, output_expression = self.context_map[key]
        return {"candidate": candidate[0].name + candidate[1].name, "indices": candidate[2], "input_expression": input_expression.emit_context_expr_string(),
                "output_expression": output_expression.emit_context_expr_string()}














