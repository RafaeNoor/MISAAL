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

    

    def __init__(self, dsl_list = [], synth_desc = None):
        super().__init__(name = "SwizzleTransfer", dsl_list = dsl_list, synth_desc = synth_desc)





    def get_property_desc(self):
        return "Check SwizzleTransferability for DSLInstructions"

    def generate_candidates(self):
        """Generates candidates to check for associative property. Candidates are
        described using a 2-tuple where the first element is the DSL instruction and
        the second element is the pair of indices to check the associative property over.

        Additional constraints on the pair of indices are that the size of the operands corresponding
        to the indicies be the same as the output type of the instructions to ensure type legalility.

        
        

        Returns:
           (DSLInstruction, Pair of Indicies): _description_
        """


        tuples = []

        for dsl_inst in self.dsl_list:
            transferable_args = self.get_transferable_args_candidates_instruction(dsl_inst)
            for pairs in transferable_args:
                tuples.append((dsl_inst, pairs))

        return tuples

    def get_transferable_args_candidates_instruction(self, dsl_inst):
        """Identify the transferable arg candidates which can be applied on the overall equivalence class. We currently
        take the intersection of the possible candidates across contexts.

        Args:
            dsl_inst (DSLInstruction): DSLInstruction type
        """
        context_pairs = [set(self.get_transferable_args_candidates_context(ctx)) for ctx in dsl_inst.contexts]

        
        intersected_pairs = context_pairs[0]
        
        for pairs in context_pairs[1:]:
            intersected_pairs = intersected_pairs.intersection(pairs)


        return list(intersected_pairs)






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
                transferable_args.append(list(comb))

        return transferable_args


    def property_holds_on_candidate(self, candidate):

        dsl_inst = candidate[0]
        pair = candidate[1]
        
        sample_ctx = dsl_inst.get_sample_context()

        print("Checking if associativity holds for", dsl_inst.name, "on", pair)

  
        # We know pairs are of the same size so we have to get the bitvector size
        bv_size = sample_ctx.context_args[pair[0]].size
            
        reg_0 = Reg("0" , 16, bv_size)
        reg_1 = Reg("1" , 16, bv_size)
        reg_2 = Reg("2" , 16, bv_size)

        vector_args = [bv_size, bv_size, bv_size]
        
        # We create the two expressions after applying associativity and
        # check if they are equal symbolically

        # Form 1: (+ (+ reg_0 reg_1) reg_2)
        form_1_expr = copy.deepcopy(sample_ctx)
        form_1_inner_expr = copy.deepcopy(sample_ctx)

        form_1_expr.context_args[pair[0]] = form_1_inner_expr
        form_1_expr.context_args[pair[1]] = reg_2

        form_1_inner_expr.context_args[pair[0]] = reg_0
        form_1_inner_expr.context_args[pair[1]] = reg_1

        # Form 2: (+ reg_0 (+ reg_1 reg_2))
        form_2_expr = copy.deepcopy(sample_ctx)
        form_2_inner_expr = copy.deepcopy(sample_ctx)

        form_2_expr.context_args[pair[0]] = reg_0
        form_2_expr.context_args[pair[1]] = form_2_inner_expr

        form_2_inner_expr.context_args[pair[0]] = reg_1
        form_2_inner_expr.context_args[pair[1]] = reg_2
        

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
            form_2_expr.context_args[idx] = reg_i
        
        


        inner_other_indices = []
        for idx, arg in enumerate(form_1_inner_expr.context_args):
            if isinstance(arg, BitVector):
                inner_other_indices.append(idx)


        # Replace this index argument in both pairs of expressions with the same symbolic hole:
        for idx in inner_other_indices:
            bv_size = form_1_inner_expr.context_args[idx].size
            reg_i = Reg(str(len(vector_args)), 16, bv_size)
            vector_args.append(bv_size)

            form_1_inner_expr.context_args[idx] = reg_i
            form_2_inner_expr.context_args[idx] = reg_i
 




        

        property_holds = check_if_contexts_equal(form_1_expr, form_2_expr, dsl_inst, dsl_inst, vector_args, self.synth_desc)

        
        return property_holds.returncode == 0


    def serialize_candidate(self, candidate):
        return candidate[0].name

    def get_property_on_candidate(self, candidate):
        return {"candidate": candidate[0].name, "indices": candidate[1]}


            


        







    