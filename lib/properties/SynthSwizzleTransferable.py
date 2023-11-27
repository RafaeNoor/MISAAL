from properties.Property import *
from properties.SwizzleTransferable import SwizzleTransferable
from utils.CodeSynthesizerDesc import create_synth_desc
from  utils.DSLInstructionUtils import *
from utils.WriteDSL import *
import copy
from  common.Types import *
import tempfile


class SynthSwizzleTransferable(SwizzleTransferable):



    def __init__(self, dsl_list = [], synth_desc = None, swizzles = []):
        super().__init__( dsl_list = dsl_list, synth_desc = synth_desc, swizzles = swizzles)
        self.name = "SynthSwizzleTransfer"


    def generate_candidates(self):
        """Generates candidates to check for swizzle transferable  property. Candidates are
        of the form (DSLInstruction, (Pair of Indices), SwizzleClass , Bool)

        The Bool variable refers to whether to apply the swizzle to the result or the operands
        """


        quads = []

        swizzles = [sw for sw in self.swizzles if self.get_num_swizzle_inputs(sw) <= 2]
        for dsl_inst in self.dsl_list:
            if "mask" in dsl_inst.name:
                continue
            transferable_args = self.get_transferable_args_candidates_instruction(dsl_inst)
            for swizzle in swizzles:
                for pairs in transferable_args:
                    quads.append((dsl_inst, pairs, swizzle, True))
                    quads.append((dsl_inst, pairs, swizzle, False))

        return quads



    def get_property_desc(self):
        return "Check SynthSwizzleTransferability for DSLInstructions"


    def property_holds_on_candidate(self, candidate):

        dsl_inst = candidate[0]
        pair = candidate[1]
        swizzle_inst = candidate[2]

        num_swizzle_operands = self.get_num_swizzle_inputs(swizzle_inst)

        apply_on_result = candidate[3]

        sample_ctx = dsl_inst.get_sample_context()

        input_precision = sample_ctx.in_precision

        print("Checking if Swizzle Transferability holds for", dsl_inst.name, "on", pair, "with swizzle ", swizzle_inst.name, "which takes ", num_swizzle_operands, "operands")

        # TODO:  TYPECHECK if swizzle is compatible

        # We know pairs are of the same size so we have to get the bitvector size
        bv_size = sample_ctx.context_args[pair[0]].size

        num_regs = num_swizzle_operands * 2
        regs = [Reg(str(i), input_precision, bv_size) for i in range(num_regs)]

        reg_0 = Reg("0" , 16, bv_size)
        reg_1 = Reg("1" , 16, bv_size)

        #vector_args = [bv_size, bv_size, bv_size]

        vector_args = [bv_size] * num_regs

        # We create the two expressions after applying associativity and
        # check if they are equal symbolically


        swizzle = self.get_type_legal_swizzle(swizzle_inst, bv_size, input_precision)
        if swizzle is None:
            return False

        # Form 1: (swizzle (+ reg_0 reg_1) )
        # Form 1: (swizzle (+ reg_0 reg_1) (+ reg_2 reg_3))
        # Form 1: Swizzle on result of operations


        form_1_expr = copy.deepcopy(swizzle)
        form_1_inner_exprs = [copy.deepcopy(sample_ctx) for i in range(num_swizzle_operands)]


        swizzle_indices = self.get_swizzle_operand_indicies(swizzle)

        for idx, swizzle_index in enumerate(swizzle_indices):
            form_1_expr.context_args[swizzle_index] = form_1_inner_exprs[idx]
            form_1_inner_exprs[idx].context_args[pair[0]] = regs[(idx*2)]
            form_1_inner_exprs[idx].context_args[pair[1]] = regs[(idx*2)+1]




        # Form 2: (+ (swizzle reg_0) (swizzle reg_1))
        # Form 2: (+ (swizzle reg_0 reg_1) (swizzle reg_2 reg_3))
        # Form 2: Swizzle on operands

        form_2_expr = copy.deepcopy(sample_ctx)
        form_2_inner_expr_left = copy.deepcopy(swizzle)
        form_2_inner_expr_right = copy.deepcopy(swizzle)

        form_2_expr.context_args[pair[0]] = form_2_inner_expr_left
        form_2_expr.context_args[pair[1]] = form_2_inner_expr_right

        left_start_offset = 0
        right_start_offset = len(regs) // 2

        for idx, swizzle_index in enumerate(swizzle_indices):
            form_2_inner_expr_left.context_args[swizzle_index] = regs[left_start_offset + idx]
            form_2_inner_expr_right.context_args[swizzle_index] = regs[right_start_offset + idx]





        # For all other symbolic operands which are not part of the pair of indices being
        # tested, we created symbolic holes and ensure that they are kept the same in both cases.
        # We handle the outer expression and inner expression cases seperately.
        outer_other_indices = []
        for idx, arg in enumerate(form_1_inner_exprs[0].context_args):
            if isinstance(arg, BitVector):
                outer_other_indices.append(idx)


        # Replace this index argument in both pairs of expressions with the same symbolic hole:
        for idx in outer_other_indices:
            bv_size = form_1_inner_exprs[0].context_args[idx].size
            reg_i = Reg(str(len(vector_args)), input_precision, bv_size)
            vector_args.append(bv_size)

            for j in range(len(form_1_inner_exprs)):
                form_1_inner_exprs[j].context_args[idx] = reg_i
            form_2_expr.context_args[idx] = reg_i


        synth_spec = None

        if apply_on_result:
            synth_spec = form_1_expr
        else:
            synth_spec = form_2_expr


        # Create new dictionary for synthesis containing both swizzles and target instructions
        # except the current swizzle being used in spec. This way we can synthesize the change of
        # instructions when swizzle is happening
        combined_list = self.dsl_list + [sw for sw in self.swizzles if sw.name != swizzle_inst.name]

        base_prefix = "dict_"+ next(tempfile._get_candidate_names())

        dict_name = base_prefix+"_sema"
        sema_path = "/tmp/"+base_prefix+".py"

        converted_dict = convert_dsl_list_to_dict(combined_list)
        write_dsl_dict_to_file(converted_dict, sema_path, dict_name)


        combined_synth_desc = create_synth_desc("swizzle_ctx",True, self.synth_desc.get_target_vector_sizes(), sema_path ,dict_name)
        combined_synth_desc.emit_sema = False


        input_sizes = [str(i) for i in vector_args]
        input_precs = [str(input_precision)] * len(vector_args)

        (is_simplified, simplified_expr) =  translate_expression(synth_spec, self.synth_desc, combined_synth_desc, input_sizes, input_precs, src_language_dsl = [dsl_inst, swizzle_inst], target_language_dsl = [dsl_inst, swizzle_inst])



        if is_simplified:
            key = self.serialize_candidate(candidate)
            self.context_map[key] = (synth_spec, simplified_expr)



        return is_simplified


    def serialize_candidate(self, candidate):
        return candidate[0].name +"+"+candidate[2].name+"+"+str(candidate[1])+"+"+str(candidate[3])

    def get_property_on_candidate(self, candidate):

        key = self.serialize_candidate(candidate)

        (input_expression, output_expression) = self.context_map[key]

        return {"candidate": candidate[0].name, "indices": candidate[1], "input_expression": input_expression.emit_context_expr_string(), "output_expression": output_expression}














