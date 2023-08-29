from properties.Property import Property
from  utils.DSLInstructionUtils import *
import copy
from  common.Types import *


from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) -->  (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(1 ,len(s)+1)))

class SwizzleTransferable(Property):
    """SwizzleTransferable property describes if we can propograte single input - single output swizzles
    on DSL Instructions to it's operands. For instance, in the case of binary operation +, it is swizzle
    transferable iff for given swizzle 'swiz' the following property holds:

    (swiz (+ a b)) == (+ (swiz a) (swiz b))

    Args:
        Property (class): Base Class for expressng properties
    """



    def __init__(self, dsl_list = [], synth_desc = None, swizzles = []):
        super().__init__(name = "SwizzleTransfer", dsl_list = dsl_list, synth_desc = synth_desc)
        self.swizzles = swizzles
        self.context_map = {}



    def get_num_swizzle_inputs(self, swizzle):
        sample_ctx = swizzle.get_sample_context()

        num_bvs = 0
        for arg in sample_ctx.context_args:
            if isinstance(arg, BitVector):
                num_bvs += 1

        return num_bvs



    def get_property_desc(self):
        return "Check SwizzleTransferability for DSLInstructions"

    def generate_candidates(self):
        """Generates candidates to check for swizzle transferable  property. Candidates are
        of the form (DSLInstruction, (Pair of Indices), SwizzleClass )
        """


        tripples = []

        swizzles = [sw for sw in self.swizzles if self.get_num_swizzle_inputs(sw) == 1]
        for dsl_inst in self.dsl_list:
            if "mask" in dsl_inst.name:
                continue
            transferable_args = self.get_transferable_args_candidates_instruction(dsl_inst)
            for swizzle in swizzles:
                for pairs in transferable_args:
                    tripples.append((dsl_inst, pairs, swizzle))

        return tripples

    def get_transferable_args_candidates_instruction(self, dsl_inst):
        """Identify the transferable arg candidates which can be applied on the overall equivalence class. We currently
        take the intersection of the possible candidates across contexts.

        Args:
            dsl_inst (DSLInstruction): DSLInstruction type
        """
        context_pairs = [self.get_transferable_args_candidates_context(ctx) for ctx in dsl_inst.contexts]



        intersected_pairs = context_pairs[0]

        for pairs in context_pairs[1:]:
            intersected_pairs = self.intersect(pairs, intersected_pairs)



        return list(intersected_pairs)



    def intersect(self, pair1, pair2):

        result = []
        for p1 in pair1:
            for p2 in pair2:
                if p1 == p2:
                    result.append(p1)
        return result






    def get_transferable_args_candidates_context(self, ctx):
        """Returns a list of 2-tupples for arguments for a given context
        which may be transferable. The criterion for this requires that the operands have the
        same bitvector size. We will verify indeed that these operands compute in a subsequent step.

        Args:
            ctx (Context): Specific Context from a DSLInstruction.
        """

        # Map from input size to
        arg_sizes_map = {}
        for idx, arg in enumerate(ctx.context_args):
            if not (isinstance(arg, ConstBitVector) or isinstance(arg, BitVector)):
                continue

            if not ctx.has_output_size():
                continue

            # Only include those pairs which
            # have the same size as the output size
            if ctx.get_output_size() != arg.size:
                continue

            size_key = str(arg.size)

            if size_key not in arg_sizes_map:
                arg_sizes_map[size_key] = []

            arg_sizes_map[size_key].append(idx)


        transferable_args = []


        for size_key in arg_sizes_map:

            arg_indices = arg_sizes_map[size_key]

            # Transferability may be across any subset of indices, so we should generate all
            # possible subsets of the arg_indicies and verify on those.
            combinations = powerset(arg_indices)

            for comb in combinations:
                if len(comb) != 2:
                    continue
                transferable_args.append(list(comb))

        return transferable_args


    def get_type_legal_swizzle(self, swizzle_inst, input_size, input_prec):

        for ctx in swizzle_inst.contexts:

            if ctx.in_vectsize == input_size:
                return ctx

        return None

    def get_swizzle_operand_index(self, swizzle_ctx):

        for idx, arg in enumerate(swizzle_ctx.context_args):
            if isinstance(arg, BitVector):
                return idx
        return -1

    def property_holds_on_candidate(self, candidate):

        dsl_inst = candidate[0]
        pair = candidate[1]
        swizzle_inst = candidate[2]

        sample_ctx = dsl_inst.get_sample_context()

        print("Checking if Swizzle Transferability holds for", dsl_inst.name, "on", pair, "with swizzle ", swizzle_inst.name)

        # TODO:  TYPECHECK if swizzle is compatible

        # We know pairs are of the same size so we have to get the bitvector size
        bv_size = sample_ctx.context_args[pair[0]].size

        reg_0 = Reg("0" , 16, bv_size)
        reg_1 = Reg("1" , 16, bv_size)

        vector_args = [bv_size, bv_size, bv_size]

        # We create the two expressions after applying associativity and
        # check if they are equal symbolically


        swizzle = self.get_type_legal_swizzle(swizzle_inst, bv_size, 16)

        # Form 1: (swizzle (+ reg_0 reg_1) )
        form_1_expr = copy.deepcopy(swizzle)
        form_1_inner_expr = copy.deepcopy(sample_ctx)


        swizzle_index = self.get_swizzle_operand_index(swizzle)

        form_1_expr.context_args[swizzle_index] = form_1_inner_expr

        form_1_inner_expr.context_args[pair[0]] = reg_0
        form_1_inner_expr.context_args[pair[1]] = reg_1

        # Form 2: (+ (swizzle reg_0) (swizzle reg_1))
        form_2_expr = copy.deepcopy(sample_ctx)
        form_2_inner_expr_left = copy.deepcopy(swizzle)
        form_2_inner_expr_right = copy.deepcopy(swizzle)

        form_2_expr.context_args[pair[0]] = form_2_inner_expr_left
        form_2_expr.context_args[pair[1]] = form_2_inner_expr_right

        form_2_inner_expr_left.context_args[swizzle_index] = reg_0
        form_2_inner_expr_right.context_args[swizzle_index] = reg_1


        # For all other symbolic operands which are not part of the pair of indices being
        # tested, we created symbolic holes and ensure that they are kept the same in both cases.
        # We handle the outer expression and inner expression cases seperately.
        outer_other_indices = []
        for idx, arg in enumerate(form_1_expr.context_args):
            if isinstance(arg, BitVector):
                outer_other_indices.append(idx)


        # Replace this index argument in both pairs of expressions with the same symbolic hole:
        for idx in outer_other_indices:
            bv_size = form_1_expr.context_args[idx].size
            reg_i = Reg(str(len(vector_args)), 16, bv_size)
            vector_args.append(bv_size)

            form_1_expr.context_args[idx] = reg_i
            form_2_inner_expr_left.context_args[idx] = reg_i
            form_2_inner_expr_right.context_args[idx] = reg_i




        property_holds = check_if_contexts_equal(form_1_expr, form_2_expr, dsl_inst, dsl_inst, vector_args, self.synth_desc)

        if property_holds.returncode == 0:
            key = self.serialize_candidate(candidate)
            self.context_map[key] = (form_1_expr, form_2_expr)





        return property_holds.returncode == 0


    def serialize_candidate(self, candidate):
        return candidate[0].name +"+"+candidate[2].name+"+"+str(candidate[1])

    def get_property_on_candidate(self, candidate):

        key = self.serialize_candidate(candidate)

        (input_expression, output_expression) = self.context_map[key]

        return {"candidate": candidate[0].name, "indices": candidate[1], "input_expression": input_expression, "output_expression": output_expression}














