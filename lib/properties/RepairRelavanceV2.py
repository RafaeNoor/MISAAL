from properties.Property import *
from utils.ContainsDef import ContainsDef
from properties.IdentifySwizzles import IdentifySwizzles
from  utils.DSLInstructionUtils import *
import copy
from  common.Types import *
from synthesizer.AllInstructionsSynthesizer import AllInstructionsSynthesizer
from Specification import Specification
from common.StructDef import StructDef
from grammar_gen.TypedSimpleGrammarGeneratorV2 import TypedSimpleGrammarGeneratorV2
from utils.CodeSynthesizerDesc import create_synth_desc
from properties.RepairRelavance import RepairRelavance
import sys
from utils.DoubleGrammarSynthesisUtils import DoubleGrammarSynthesisUtils

from utils.CanonicalizeExpressions import CanonicalizeExpression
from utils.ContainsRegDef import ContainsRegDef
from common.StructDef import StructDef

class RepairRelavanceV2(RepairRelavance):



    def __init__(self, dsl_list = [], synth_desc = None, output_dsl_list = [], repair_dsl_list = [], target_synth_desc = None, target_start_depth = None,target_depth = 3, const_fold = False, commutative_map_path = None, force_contains_all_regs = True, memo_path = None):



        super().__init__(dsl_list = dsl_list, synth_desc = synth_desc, output_dsl_list = output_dsl_list, repair_dsl_list = repair_dsl_list, target_depth = target_depth, target_start_depth = target_start_depth)
        self.name = "RepairRelavanceV2"
        self.memo_path = memo_path
        self.synth_utils = DoubleGrammarSynthesisUtils(input_dsl_list = dsl_list, output_dsl_list = output_dsl_list, swizzle_dsl_list = [], auxilary_dsl_list = repair_dsl_list)

        self.canonicalizer = CanonicalizeExpression(commutative_map_path = commutative_map_path)
        self.useCanon = True

        #self.POOL_SIZE = 16
        #self.BATCH_SIZE = 1024
        self.contains_reg_def = ContainsRegDef()
        self.struct_def = StructDef()
        self.force_contains_all_regs = force_contains_all_regs




    def get_property_desc(self):
        return "Test if a given output dsl instruction may be used to generate target expression"

    def generate_candidates(self):
        start_depth = self.target_depth
        if not self.target_start_depth is None:
            start_depth = self.target_start_depth
        for depth in range(start_depth, self.target_depth + 1):
            for input_dsl in self.input_dsl_list:
                for output_dsl in self.output_dsl_list:
                    candidate = (input_dsl, output_dsl, depth)
                    candidate_key = self.serialize_candidate(candidate)
                    # If property already holds on shallower depths then continue
                    if candidate_key in self.context_map:
                        continue

                    yield candidate


        return




    def get_grammar_relevant_dsl(self,out_precision, reduce_factor, input_sizes, input_precs, input_signedness, src_ctx, output_dsl_inst):

        #print("Output precision: ", out_precision)
        #print("Input precision: ", input_precs)
        #print("Input sizes: ", input_sizes)
        #print("Input Signedness: ", input_signedness)

        relavent_dsls = []
        count = 0

        FAST = True
        src_bv_ops = src_ctx.get_bv_ops()

        for dsl_inst in self.repair_dsl_list:
            dsl_inst_copy = copy.deepcopy(dsl_inst)
            dsl_inst_copy.contexts = []

            for ctx in dsl_inst.contexts:
                if "div" in ctx.name:
                    continue
                ctx_lanes = ctx.in_vectsize // ctx.in_precision

                if ctx_lanes != 1 and ctx_lanes != reduce_factor:
                    continue


                if FAST:
                    ctx_bv_ops = ctx.get_bv_ops()
                    def intersection(lst1, lst2):
                        return list(set(lst1) & set(lst2))

                    #print("CTX BV OP",ctx_bv_ops)
                    common = intersection(ctx_bv_ops, src_bv_ops)
                    #print(common)
                    if len(common) == 0:
                        continue
                    else:
                        #print("Common!")
                        pass


                if input_signedness == 1 and ctx.signedness == 0:
                    continue

                if input_signedness == 0 and ctx.signedness == 1:
                    continue

                if all([ctx.in_vectsize < input_size for input_size in input_sizes]) and ctx.in_vectsize < out_precision:
                    continue

                if (ctx.in_precision > out_precision and all([ctx.in_precision > input_prec for input_prec in input_precs])) or (ctx.out_precision > out_precision and all([ctx.out_precision > input_prec for input_prec in input_precs])):
                    continue

                # Skip no-op operations
                if "cast" in ctx.name and ctx.in_precision == ctx.out_precision:
                    continue

                if "saturate" in ctx.name and ctx.in_precision == ctx.out_precision:
                    continue



                # If operating on scalars with required scalar sizes
                if ctx.in_precision in input_precs and ctx.in_vectsize == ctx.in_precision:
                    dsl_inst_copy.contexts.append(ctx)
                    continue

                # If operating on scalars with required scalar sizes
                if ctx.out_precision == out_precision and ctx.out_vectsize == ctx.out_precision:
                    dsl_inst_copy.contexts.append(ctx)
                    continue

                # If operating on vectors with reduce_factor lanes
                if ctx.in_vectsize // ctx.in_precision == reduce_factor:
                    dsl_inst_copy.contexts.append(ctx)
                    continue

                # If operating on vectors with reduce_factor lanes
                if ctx.out_vectsize // ctx.out_precision == reduce_factor:
                    dsl_inst_copy.contexts.append(ctx)
                    continue


            relavent_dsls.append(dsl_inst_copy)
            count += len(dsl_inst_copy.contexts)


        # Including contexts from must include equivlance class
        output_eq_class = copy.deepcopy(output_dsl_inst)
        output_eq_class.contexts = []
        for ctx in output_dsl_inst.contexts:
            current_lanes = ctx.out_vectsize // ctx.out_precision
            if current_lanes == 1 or current_lanes == reduce_factor:
                output_eq_class.contexts.append(ctx)
            elif ctx.can_scale_context() and not (ctx.extensions is None) and 'halide' not in ctx.extensions:
                # Scale down the instruction to required size
                scalar_case = self.get_scaled_context(ctx, num_lanes = 1)

                output_eq_class.contexts.append(scalar_case)

                if reduce_factor != 1:
                    reduce_factor_case = self.get_scaled_context(ctx, num_lanes = reduce_factor)
                    output_eq_class.contexts.append(reduce_factor_case)

        relavent_dsls.append(output_eq_class)
        count += len(output_eq_class.contexts)



        relavent_dsls = [d for d in relavent_dsls if len(d.contexts) != 0]


        return relavent_dsls






    def get_repair_context_index(self, dsl_expr):
        max_args = max([self.get_context_num_sym_args(ctx) for ctx in dsl_expr.contexts])

        relavent_indices = [i for i in range(len(dsl_expr.contexts))  if self.get_context_num_sym_args(dsl_expr.contexts[i]) == max_args]


        return_idx = relavent_indices[0]
        if False:
            min_prec = dsl_expr.contexts[return_idx].in_precision
            for idx in relavent_indices:
                cur_prec = dsl_expr.contexts[idx].in_precision
                if cur_prec < min_prec:
                    min_prec = cur_prec
                    return_idx = idx
        else:
            max_prec = dsl_expr.contexts[return_idx].in_precision
            for idx in relavent_indices:
                cur_prec = dsl_expr.contexts[idx].in_precision
                if cur_prec > max_prec:
                    max_prec = cur_prec
                    return_idx = idx

        return return_idx


    def property_holds_on_candidate(self, candidate):
        input_dsl_inst = candidate[0]
        modified_sema = self.get_instrumented_semantics(input_dsl_inst)
        depth = candidate[2]
        arg_id = self.get_repair_context_index(input_dsl_inst)

        key = self.serialize_candidate(candidate)

        if key in self.context_map:
            return False




        src_ctx = input_dsl_inst.contexts[int(arg_id)]
        print(src_ctx.name)
        if src_ctx.get_bv_ops() == []:
            return False
        src_ctx = copy.deepcopy(src_ctx)
        bv_streams = self.get_bv_streams(input_dsl_inst, modified_sema, 0, src_ctx)
        streams = bv_streams.split("STORE")
        stream_0 = streams[0].strip().split("\n")
        print(stream_0)


        reduce_factor = self.get_reducing_factor(stream_0)
        print("Reduction factor:", reduce_factor)

        modified_env_func = self.emit_prepare_repair_env(stream_0, modified_sema, input_dsl_inst, src_ctx)
        sliced_sizes = self.ctx_slice_sizes_operand_map[src_ctx.name]
        print("Sliced sizes:\t",sliced_sizes)

        statements = []
        statements.append(modified_env_func)


        output_dsl_inst = candidate[1]


        num_src_ctx_args = self.get_context_num_sym_args(src_ctx)
        input_sizes = self.get_context_input_sizes(src_ctx)
        output_size = src_ctx.out_vectsize
        in_precision = src_ctx.in_precision
        out_precision = src_ctx.out_precision

        src_ctx_sym_args = self.get_context_sym_args(src_ctx)

        src_ctx_regs = []

        reg_arg_map = {}
        for idx, arg in enumerate(src_ctx_sym_args):
            reg = Reg(str(idx),in_precision, arg.size)
            src_ctx_regs.append(reg)

            key = str(arg.size)
            if key not in reg_arg_map:
                reg_arg_map[key] = []
            reg_arg_map[key].append(reg)

        src_reg_counter = 0
        for idx, arg in enumerate(src_ctx.context_args):
            if isinstance(arg, BitVector):
                src_ctx.context_args[idx] = src_ctx_regs[src_reg_counter]
                src_reg_counter+=1



        src_regs_count = len(src_ctx_regs)

        bitwidth_sizes = [str(arg.size) for arg in src_ctx_regs]


        stream_bv_sizes = self.get_stream_bitvector_sizes(stream_0, modified_sema, src_ctx )
        synth_input_sizes = [size for arg, size in stream_bv_sizes.items()]
        input_precs = [in_precision] * len(synth_input_sizes)


        input_signedness = src_ctx.signedness
        target_dsl = self.get_grammar_relevant_dsl(out_precision, reduce_factor, synth_input_sizes, input_precs, input_signedness, src_ctx, output_dsl_inst)


        statements.append(self.contains_reg_def.emit_contains([input_dsl_inst] ,self.struct_def))

        # Output size must be the output precision since we're testing on one lane
        enumerate_target_program = create_exhaustive_expressions_generator(target_dsl, depth, use_eq_class = True, output_size = out_precision)

        def invoke_ref_custom(interpreter_name, invoke_ref_name = "invoke-spec"):
            invoke_ref_def = self.invoke_ref(out_precision, output_size, invoke_name = invoke_ref_name, interpreter_name = interpreter_name, index = 0, is_lane_func = False, num_regs = src_regs_count)
            return invoke_ref_name, invoke_ref_def

        def invoke_ref_lane_custom(interpreter_name, invoke_ref_name = "invoke-spec-lane"):
            invoke_ref_lane_def = self.invoke_ref(out_precision, output_size, invoke_name = invoke_ref_name, interpreter_name = interpreter_name, index = 0, is_lane_func = True, num_regs = src_regs_count)
            return invoke_ref_name, invoke_ref_lane_def

        def invoke_target_custom(interpreter_name):
            invoke_target_name = "invoke-target-repair"
            invoke_target_def = "(define ({} expr env) ({} expr (prepare-env env)))".format(invoke_target_name, interpreter_name)
            return invoke_target_name, invoke_target_def

        target_input_sizes =  sliced_sizes  #src_regs_count * [src_ctx.in_precision * reduce_factor]

        for expr in enumerate_target_program:
            if get_expr_depth(expr) != depth:
                continue

            if not self.expr_contains(expr, output_dsl_inst.name):
                continue

            canon_target = self.canonicalizer.canonicalize(expr)
            if self.useCanon and  not self.canonicalizer.isCanonical(expr, canon_target):
                continue



            success, src_expr_str, dst_expr_str = self.synth_utils.double_grammar_synthesis(src_ctx, expr, invoke_ref_custom = invoke_ref_custom, invoke_ref_lane_custom = invoke_ref_lane_custom ,invoke_target_custom= invoke_target_custom, additional_statements = statements, custom_src_output_size = src_ctx.out_vectsize, custom_dst_output_size = src_ctx.out_precision , custom_target_input_sizes = target_input_sizes)

            if success:
                key = self.serialize_candidate(candidate)
                self.context_map[key] = (src_expr_str, dst_expr_str)
                return True




        return False


    def emit_contains_assertion(self, expr_name = "spec-expr", num_regs = 1):
        if self.force_contains_all_regs:
            is_symbolic = "(not (concrete? {}))".format(expr_name)
            contains_regs = ["({} {} {})".format(self.contains_reg_def.contains_name, expr_name, idx) for idx in range(0, num_regs)]
            contains_all = "(assert (and {}))".format(" ".join(contains_regs))

            condition = "(cond [{} {}])".format(is_symbolic, contains_all)
            return condition

        else:
            return ""

    def invoke_ref(self, output_precision, outvect_size, invoke_name = "invoke-ref", interpreter_name= "hvx:interpreter", index = 0, is_lane_func = False, num_regs = 1):

        constraint = self.emit_contains_assertion(expr_name = "spec-expr", num_regs = num_regs)

        full_result = "(define spec-result-full ({} spec-expr env))".format(interpreter_name)
        output_lanes = outvect_size / output_precision




        adjusted_index = int(output_lanes - index - 1)
        low_offset = "(define result.i.low (* {} {}))".format(adjusted_index, output_precision)
        high_offset = "(define result.i.high (+ result.i.low (- {} 1)))".format(output_precision)
        extract_slice = "(extract result.i.high result.i.low spec-result-full)"

        body = [constraint,full_result, low_offset, high_offset, extract_slice, "\n"]

        body = "\n".join(body)

        if is_lane_func:
            return "(define ({} spec-expr lane-idx env)\n{})".format(invoke_name , body)
        else:
            return "(define ({} spec-expr env)\n{})".format(invoke_name , body)



    def expr_contains(self, expr, name):
        if isinstance(expr, Context):
            if name == expr.dsl_name:
                return True
            conds = []
            for arg in expr.context_args:
                conds.append(self.expr_contains(arg, name))
            return any(conds)
        return False

    def serialize_candidate(self, candidate):
        return candidate[0].name + "+" + candidate[1].name

    def get_property_on_candidate(self, candidate):
        key = self.serialize_candidate(candidate)
        src_expr_str, dst_expr_str = self.context_map[key]
        return {"candidate": candidate[0].name, "output_expression" : dst_expr_str, "synth_expression": src_expr_str}








    def emit_property_to_egg(self, property_map):
        return []








