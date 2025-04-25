from properties.Property import *
from utils.ContainsDef import ContainsDef
from properties.IdentifySwizzles import IdentifySwizzles
from  utils.DSLInstructionUtils import *
import copy
import json
from  common.Types import *
from synthesizer.AllInstructionsSynthesizer import AllInstructionsSynthesizer
from Specification import Specification
from common.StructDef import StructDef
from grammar_gen.TypedSimpleGrammarGeneratorV2 import TypedSimpleGrammarGeneratorV2
from utils.CodeSynthesizerDesc import create_synth_desc
from properties.RepairRelavanceV4 import RepairRelavanceV4
import sys
from utils.DoubleGrammarSynthesisUtils import DoubleGrammarSynthesisUtils
from pyparsing import nestedExpr
from utils.CanonicalizeExpressions import CanonicalizeExpression
from utils.ContainsRegDef import ContainsRegDef
from common.StructDef import StructDef
import time


# Version of repair relevance to work on synthesizing any intermediate value in the src language. More formally, inst_A is relevant to inst_B if there exists some
# repaired program containing inst_A which produces symbolically equivalent results to any intermediate value of inst_B at a given lane.
class RepairRelavanceIntermediates(RepairRelavanceV4):



    def __init__(self, dsl_list = [], synth_desc = None, output_dsl_list = [], repair_dsl_list = [], target_synth_desc = None, target_start_depth = None,target_depth = 3, const_fold = False, commutative_map_path = None, force_contains_all_regs = True, memo_path = None):

        force_contains_all_regs = False

        input_test_list = [
            #"_mm512_sllv_epi16",
            # "_mm256_dpbusd_epi32",
            "_mm_add_si64"
        ]

        # dsl_list = [d for d in dsl_list if d.name in input_test_list]

        output_test_list = [
            #"typed:signed-vec-mul",
            #"typed:cast-uint",
            "typed:vec-shl",
        ]

        #output_dsl_list = [d for d in output_dsl_list if d.name in output_test_list]

        repair_test_list = [
            "repair-add",
        ]

        #repair_dsl_list = [d for d in repair_dsl_list if d.name in repair_test_list]

        super().__init__(dsl_list = dsl_list, synth_desc = synth_desc, output_dsl_list = output_dsl_list, repair_dsl_list = repair_dsl_list, target_synth_desc = target_synth_desc, target_start_depth = target_start_depth, target_depth = target_depth, const_fold = const_fold, commutative_map_path = commutative_map_path, force_contains_all_regs = force_contains_all_regs, memo_path = memo_path)

        self.name = "RepairRelavanceIntermediates"
        self.skip_exception = True
    def get_property_desc(self):
        return "Test if a given output dsl instruction may be used to generate target expression (Version Intermediates)"



    def prepare_candidate_generator(self, candidate_prep, use_max_args = True):
        input_dsl_inst = candidate_prep[0]
        arg_id = self.get_repair_context_index(input_dsl_inst, use_max_args = use_max_args)
        modified_sema = self.get_instrumented_semantics(input_dsl_inst, arg_id)
        print(modified_sema)
        depth = candidate_prep[2]


        src_ctx = input_dsl_inst.contexts[int(arg_id)]
        if src_ctx.get_bv_ops() == []:
            return

        stream_map_key = self.get_bv_streams_key(src_ctx)
        stream_0 = None

        src_ctx = copy.deepcopy(src_ctx)
        if stream_map_key in self.bv_streams_map:
            stream_0 = self.bv_streams_map[stream_map_key]
        else:
            bv_streams = self.get_bv_streams(input_dsl_inst, modified_sema, 0, src_ctx)
            streams = bv_streams.split("STORE")
            stream_0 = streams[0].strip().split("\n")
            reduce_factor = self.get_reducing_factor(stream_0)
            if reduce_factor == 1:
                # Discard all lane calls
                stream_0 = [line for line in stream_0 if "LANE" not in line]

            self.bv_streams_map[stream_map_key] = stream_0

        print(input_dsl_inst.name)
        print(stream_0)

        if stream_0 == ['']:
            print("EMPTY STREAM RETURNING")
            return


        reduce_factor = self.get_reducing_factor(stream_0)
        print("Reduction factor:", reduce_factor)

        repair_env_obj = self.emit_prepare_repair_env(stream_0, modified_sema, input_dsl_inst, src_ctx)
        modified_env_func = repair_env_obj['env_fn']
        env_sizes = repair_env_obj['ordered_sizes']
        ordered_keys = repair_env_obj['ordered_keys']
        ordered_defns = repair_env_obj['ordered_defns']
        formal_param_defs = repair_env_obj['formal_param_defs']


        sliced_sizes = env_sizes
        print("Sliced sizes:\t",sliced_sizes)






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



        synth_input_sizes = sliced_sizes #[size for arg, size in stream_bv_sizes.items()]
        input_precs = [in_precision] * len(synth_input_sizes)




        output_dsl_inst = candidate_prep[1]
        input_signedness = src_ctx.signedness
        target_dsl = self.get_grammar_relevant_dsl(out_precision, reduce_factor, synth_input_sizes, input_precs, input_signedness, src_ctx, output_dsl_inst)

        print("Target DSL Size: ", len(target_dsl))



        for idx, intermediate_val_name in enumerate(ordered_keys):
            if intermediate_val_name.startswith("reg"):
                continue

            if idx+1 == len(ordered_keys):
                continue

            forward_keys = ordered_keys[idx:]
            forward_defns = ordered_defns[idx:]
            forward_sizes = env_sizes[idx:]

            assert len(forward_keys) == len(forward_defns)
            assert len(forward_keys) == len(forward_sizes)


            for forward_idx, forward_val_name in enumerate(forward_keys):
                backward_keys = ordered_keys[:idx+forward_idx]
                backward_defns = ordered_defns[:idx+forward_idx]
                backward_sizes = env_sizes[:idx+forward_idx]

                #backward_keys = ordered_keys
                #backward_defns = ordered_defns
                #backward_sizes = env_sizes


                forward_val_defn = forward_defns[forward_idx]
                forward_val_size = forward_sizes[forward_idx]

                print("FORWARD VAL DEFN", forward_val_defn)
                print("idx", idx)
                print("forward_idx", forward_idx)
                print("forward_sizes", forward_sizes)
                print("forward_defns", forward_defns)

                custom_env_func = self.create_prepare_env_fn(formal_param_defs, backward_defns, backward_keys)



                # Output size must be the output precision since we're testing on one lane
                enumerate_target_program = create_exhaustive_expressions_generator(target_dsl, depth, use_eq_class = True, output_size = forward_val_size)


                print("Required output size: ", forward_val_size)
                for expr in enumerate_target_program:

                    statements = []
                    statements.append(custom_env_func)


                    target_input_sizes =  backward_sizes
                    if get_expr_depth(expr) != depth:
                        continue

                    if not self.expr_contains(expr, output_dsl_inst.name):
                        continue


                    canon_target = self.canonicalizer.canonicalize(expr)
                    if self.useCanon and  not self.canonicalizer.isCanonical(expr, canon_target):
                        continue



                    candidate = copy.deepcopy({})
                    candidate['src_dsl'] = input_dsl_inst
                    candidate['target_dsl'] = output_dsl_inst
                    candidate['src_expr'] = src_ctx
                    candidate['target_expr'] = expr
                    candidate['additional_statements'] = statements
                    candidate['custom_target_input_sizes'] = target_input_sizes
                    candidate['prepare-env-function'] = custom_env_func
                    candidate['target_output_size'] = forward_val_size
                    candidate['formal_param_defs'] = formal_param_defs
                    candidate['forward_val_defn'] = forward_val_defn
                    candidate['forward_val_name'] = forward_val_name





                    src_expr_regs = get_unique_context_registers(src_ctx)
                    bitwidth_sizes = [arg.size for arg in src_expr_regs]
                    candidate['src_env_sizes'] = bitwidth_sizes




                    key = self.serialize_candidate(candidate)

                    if key in self.context_map:
                        # Exit early from generator
                        return



                    yield candidate


        return



    def property_holds_on_candidate(self, candidate):
        src_ctx = (candidate['src_expr'])
        target_expr = (candidate['target_expr'])
        statements = candidate['additional_statements']
        custom_target_input_sizes = candidate['custom_target_input_sizes']
        target_output_size = candidate['target_output_size']
        formal_param_defs = candidate['formal_param_defs']
        forward_val_defn = candidate['forward_val_defn']
        forward_val_name = candidate['forward_val_name']

        def invoke_ref_custom(interpreter_name, invoke_ref_name = "invoke-spec"):
            invoke_stmts = []
            invoke_stmts = [formal_param_defs]
            invoke_stmts += [forward_val_defn]
            invoke_stmts += [forward_val_name]

            invoke_ref_def = "(define ({} spec-expr env)\n{})".format(invoke_ref_name, "\n".join(invoke_stmts))

            return invoke_ref_name, invoke_ref_def

        def invoke_ref_lane_custom(interpreter_name, invoke_ref_name = "invoke-spec-lane"):

            invoke_stmts = []
            invoke_stmts = [formal_param_defs]
            invoke_stmts += [forward_val_defn]
            invoke_stmts += [forward_val_name]

            invoke_ref_lane_def = "(define ({} spec-expr lane-idx env)\n{})".format(invoke_ref_name, "\n".join(invoke_stmts))
            return invoke_ref_name, invoke_ref_lane_def

        def invoke_target_custom(interpreter_name):
            invoke_target_name = "invoke-target-repair"
            invoke_target_def = "(define ({} expr env) ({} expr (prepare-env env)))".format(invoke_target_name, interpreter_name)
            return invoke_target_name, invoke_target_def

        key = self.serialize_candidate(candidate)

        #if key in self.context_map:
        #    return False



        synth_utils = DoubleGrammarSynthesisUtils(input_dsl_list = self.input_dsl_list, output_dsl_list = self.output_dsl_list, swizzle_dsl_list = [], auxilary_dsl_list = self.repair_dsl_list)
        success, src_expr_str, dst_expr_str = synth_utils.double_grammar_synthesis(src_ctx, target_expr, invoke_ref_custom = invoke_ref_custom, invoke_ref_lane_custom = invoke_ref_lane_custom ,invoke_target_custom= invoke_target_custom, additional_statements = statements, custom_src_output_size = src_ctx.out_vectsize, custom_dst_output_size = target_output_size, custom_target_input_sizes = custom_target_input_sizes, is_src_grammar = False)

        print("RESULT OF CONTEXT:", success)

        if success:
            print("SUCCESS!")
            self.context_map[key] = (src_expr_str, dst_expr_str)
            return True




        return False


    def get_property_on_candidate(self, candidate):
        key = self.serialize_candidate(candidate)
        src_expr_str, dst_expr_str = self.context_map[key]
        return {"candidate": candidate['src_dsl'].name, "output_expression" : dst_expr_str, "synth_expression": src_expr_str, 'env-func': candidate['prepare-env-function'], 'target_input_sizes': candidate['custom_target_input_sizes'], 'src_env_sizes': candidate['src_env_sizes'] }




    def create_prepare_env_fn(self, formal_param_defs, ordered_defns, ordered_keys):

        prepare_env_fn = "(define (prepare-env env) {} \n {} \n (vector {})\n)".format(formal_param_defs, "\n".join(ordered_defns), " ".join(ordered_keys))

        return prepare_env_fn

