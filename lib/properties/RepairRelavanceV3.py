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
from properties.RepairRelavanceV2 import RepairRelavanceV2
import sys
from utils.DoubleGrammarSynthesisUtils import DoubleGrammarSynthesisUtils

from utils.CanonicalizeExpressions import CanonicalizeExpression
from utils.ContainsRegDef import ContainsRegDef
from common.StructDef import StructDef

class RepairRelavanceV3(RepairRelavanceV2):



    def __init__(self, dsl_list = [], synth_desc = None, output_dsl_list = [], repair_dsl_list = [], target_synth_desc = None, target_start_depth = None,target_depth = 3, const_fold = False, commutative_map_path = None, force_contains_all_regs = True, memo_path = None):


        super().__init__(dsl_list = dsl_list, synth_desc = synth_desc, output_dsl_list = output_dsl_list, repair_dsl_list = repair_dsl_list, target_synth_desc = target_synth_desc, target_start_depth = target_start_depth, target_depth = target_depth, const_fold = const_fold, commutative_map_path = commutative_map_path, force_contains_all_regs = force_contains_all_regs, memo_path = memo_path)
        self.name = "RepairRelavanceV3"
        self.bv_streams_map = {}




    def get_property_desc(self):
        return "Test if a given output dsl instruction may be used to generate target expression (Version 3)"

    def generate_candidates(self):
        start_depth = self.target_depth
        if not self.target_start_depth is None:
            start_depth = self.target_start_depth
        for depth in range(start_depth, self.target_depth + 1):
            for input_dsl in self.input_dsl_list:
                for output_dsl in self.output_dsl_list:
                    candidate_prep = (input_dsl, output_dsl, depth)
                    try:
                        candidate_generator = self.prepare_candidate_generator(candidate_prep)

                        # Generator internally will query state to know
                        # if the repair property is already valid hence we will exit early
                        for candidate in candidate_generator:
                            yield candidate
                    except:
                        with open("ErrorLog_{}.err".format(self.name),"a+") as ErrFile:
                            error_line = "+".join([input_dsl.name, output_dsl.name])
                            ErrFile.write(error_line+"\n")
                            continue



        return

    def get_bv_streams_key(self, src_ctx):
        return src_ctx.name

    def prepare_candidate_generator(self, candidate_prep):
        input_dsl_inst = candidate_prep[0]
        modified_sema = self.get_instrumented_semantics(input_dsl_inst)
        depth = candidate_prep[2]
        arg_id = self.get_repair_context_index(input_dsl_inst)


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
            self.bv_streams_map[stream_map_key] = stream_0

        print(input_dsl_inst.name)
        print(stream_0)

        if stream_0 == ['']:
            return


        reduce_factor = self.get_reducing_factor(stream_0)
        print("Reduction factor:", reduce_factor)

        modified_env_func = self.emit_prepare_repair_env(stream_0, modified_sema, input_dsl_inst, src_ctx)
        sliced_sizes = self.ctx_slice_sizes_operand_map[src_ctx.name]
        print("Sliced sizes:\t",sliced_sizes)

        statements = []
        statements.append(modified_env_func)




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


        output_dsl_inst = candidate_prep[1]
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

        target_input_sizes =  sliced_sizes

        for expr in enumerate_target_program:



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
            candidate['invoke_ref_custom'] = invoke_ref_custom
            candidate['invoke_ref_lane_custom'] = invoke_ref_lane_custom
            candidate['invoke_target_custom'] = invoke_target_custom
            candidate['additional_statements'] = statements
            candidate['custom_target_input_sizes'] = target_input_sizes

            key = self.serialize_candidate(candidate)

            if key in self.context_map:
                # Exit early from generator
                return


            yield candidate





        return





    def property_holds_on_candidate(self, candidate):
        src_ctx = candidate['src_expr']
        target_expr = candidate['target_expr']
        invoke_ref_custom = candidate['invoke_ref_custom']
        invoke_ref_lane_custom = candidate['invoke_ref_lane_custom']
        invoke_target_custom = candidate['invoke_target_custom']
        statements = candidate['additional_statements']
        custom_target_input_sizes = candidate['custom_target_input_sizes']


        success, src_expr_str, dst_expr_str = self.synth_utils.double_grammar_synthesis(src_ctx, target_expr, invoke_ref_custom = invoke_ref_custom, invoke_ref_lane_custom = invoke_ref_lane_custom ,invoke_target_custom= invoke_target_custom, additional_statements = statements, custom_src_output_size = src_ctx.out_vectsize, custom_dst_output_size = src_ctx.out_precision , custom_target_input_sizes = custom_target_input_sizes)

        if success:
            key = self.serialize_candidate(candidate)
            self.context_map[key] = (src_expr_str, dst_expr_str)
            return True




        return False



    def serialize_candidate(self, candidate):
        return candidate['src_dsl'].name + "+" + candidate['target_dsl'].name

    def get_property_on_candidate(self, candidate):
        key = self.serialize_candidate(candidate)
        src_expr_str, dst_expr_str = self.context_map[key]
        return {"candidate": candidate['src_dsl'].name, "output_expression" : dst_expr_str, "synth_expression": src_expr_str}





    def load_previous_property_map(self, memo_path):
        if not os.path.exists(memo_path):
            return

        memo_dict = {}
        with open(memo_path, "r") as MemoFile:
            memo_dict = json.load(MemoFile)



        property_map = {}

        # Update property map
        for key, prop in memo_dict.items():

            entry = prop[0]['property']
            candidate = entry['candidate']
            src_expr_str = entry['synth_expression']
            dst_expr_str = entry['output_expression']

            if key not in property_map:
                property_map[key] = []

            prop_dict = copy.deepcopy({'property_name': self.name, 'property': {'candidate': candidate, 'output_expression': dst_expr_str, 'synth_expression': src_expr_str}})

            property_map[key].append(prop_dict)

        print('Read in {} entries into property_map'.format(len([k for k in memo_dict])))

        return property_map



    def load_previous_context_map(self, memo_path):
        if not os.path.exists(memo_path):
            return

        self.load_previous_property_map(memo_path)

        memo_dict = {}
        with open(memo_path, "r") as MemoFile:
            memo_dict = json.load(MemoFile)


        # Update context map
        for key, prop in memo_dict.items():

            entry = prop[0]['property']
            candidate = entry['candidate']

            src_expr_str = entry['synth_expression']
            dst_expr_str = entry['output_expression']

            self.context_map[key] = src_expr_str , dst_expr_str

        print('Read in {} entries into context_map'.format(len([k for k in memo_dict])))




