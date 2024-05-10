from properties.Property import *
from properties.IdentifySwizzles import IdentifySwizzles
from  utils.DSLInstructionUtils import *
import copy
from  common.Types import *
from synthesizer.AllInstructionsSynthesizer import AllInstructionsSynthesizer
from Specification import Specification
from common.StructDef import StructDef
from grammar_generator.TypedSimpleGrammarGenerator import TypedSimpleGrammarGenerator
import sys

class RepairRelavance(IdentifySwizzles):



    def __init__(self, dsl_list = [], synth_desc = None, output_dsl_list = [], repair_dsl_list = [], target_synth_desc = None):

        super().__init__(dsl_list = dsl_list, synth_desc = synth_desc)
        self.name = "RepairRelavance"
        self.is_candidate_generator = True
        self.repair_dsl_list = repair_dsl_list
        self.output_dsl_list = output_dsl_list
        self.input_dsl_list = dsl_list
        self.target_synth_desc = target_synth_desc

        self.output_dsl_list = self.output_dsl_list[:1]

        self.input_dsl_list = [d for d in self.input_dsl_list if d.name == "hexagon_V6_vrmpybv_128B"]




    def get_property_desc(self):
        return "Test if a given output dsl instruction may be used to generate target expression"

    def generate_candidates(self):
        for input_dsl in self.input_dsl_list:
            for output_dsl in self.output_dsl_list:
                yield (input_dsl, output_dsl)
                return
        return



    def get_reducing_factor(self, stream):
        # TODO: implement functionality
        return 4



    def create_prepare_repair_env_func(self, name, slices):
        create_extract = lambda x: "(extract {} {} arg)".format(x[0], x[1])

        concat_expr = "(concat \n{}\n)".format("\n".join([create_extract(s) for s in slices]))

        env_func = "(define ({} arg)\n{}\n)".format(name, concat_expr)

        return env_func




    def create_prepare_repair_env_funcs(self, stream):
        prep_arg_slices = {}

        for line in stream:
            tokens = line.strip().split()
            arg_name = tokens[-1]

            if arg_name not in prep_arg_slices:
                prep_arg_slices[arg_name] = []

            high = tokens[1]
            low = tokens[2]
            prep_arg_slices[arg_name].append((high,low))

        funcs = {}

        for arg in prep_arg_slices:
            funcs[arg] = self.create_prepare_repair_env_func(arg, prep_arg_slices[arg])

        return funcs


    def get_stream_bitvector_sizes(self, stream):
        prep_arg_slices = {}

        for line in stream:
            tokens = line.strip().split()
            arg_name = tokens[-1]

            if arg_name not in prep_arg_slices:
                prep_arg_slices[arg_name] = []

            high = tokens[1]
            low = tokens[2]
            prep_arg_slices[arg_name].append((high,low))

        funcs = {}

        for arg in prep_arg_slices:
            total_sizes = 0
            for (high,low) in prep_arg_slices[arg]:
                total_sizes += int(high) - int(low) + 1
            funcs[arg] = total_sizes


        return funcs

    def create_repair_env_function(self, dsl_inst):
        # Once we've identified the bitslices being extracted in a single iteration we have to create a Rosette function which given the original synthesis env creates the spliced env for the repair

        return False

    def emit_prepare_repair_env(self, slice_stream, modified_sema, input_dsl_inst, ctx):
        funcs = self.create_prepare_repair_env_funcs(slice_stream)

        prototype = modified_sema.split("\n")[0].strip().split("(define")[-1].strip().replace("(","")
        # Skip the name of the context
        prototype = prototype.replace(")","").split()[1:]
        print(prototype)

        sorted_args = []

        for idx, arg in enumerate(prototype):
            if arg in funcs and isinstance(ctx.context_args[idx], BitVector):
                sorted_args.append(arg)


        prepare_clauses = []

        for idx , arg in enumerate(sorted_args):
            clause = "({} (vector-ref env {}))".format(arg, idx)
            prepare_clauses.append(clause)

        env_function_clauses = [defs for arg, defs in funcs.items()]
        env_function_clauses.append("(vector {})".format(" ".join(prepare_clauses)))

        return "(define (prepare-env env)\n{}\n)".format("\n".join(env_function_clauses))



    def get_context_num_sym_args(self, ctx):
        return sum([1 for arg in ctx.context_args if isinstance(arg, BitVector)])

    def get_context_sym_args(self, ctx):
        return ([arg for arg in ctx.context_args if isinstance(arg, BitVector)])


    def get_context_input_sizes(self, ctx):
        return sorted([arg.size for arg in ctx.context_args if isinstance(arg, BitVector)])

    def get_grammar_desc(self,out_precision, reduce_factor, input_sizes, input_precs, input_signedness):
        print("Output precision: ", out_precision)
        print("Input precision: ", input_precs)
        print("Input sizes: ", input_sizes)
        print("Input Signedness: ", input_signedness)
        relavent_dsls = []
        count = 0

        for dsl_inst in self.repair_dsl_list:
            dsl_inst_copy = copy.deepcopy(dsl_inst)
            dsl_inst_copy.contexts = []

            for ctx in dsl_inst.contexts:
                if input_signedness == 1 and ctx.signedness == 0:
                    continue

                if input_signedness == 0 and ctx.signedness == 1:
                    continue
                if all([ctx.in_vectsize < input_size for input_size in input_sizes]) and ctx.in_vectsize < out_precision:
                    continue

                if (ctx.in_precision > out_precision and all([ctx.in_precision > input_prec for input_prec in input_precs])) or (ctx.out_precision > out_precision and all([ctx.out_precision > input_prec for input_prec in input_precs])):
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


        input_shapes = []
        for i in range(len(input_sizes)):
            input_shapes.append([1, input_sizes[i]// input_precs[i]])

        spec = Specification(semantics = [], output_shape = [1, 1], input_shapes = input_shapes, args = ["SYMBOLIC_BV_{}".format(i_size) for i_size in input_sizes], input_precision = input_precs, output_precision = out_precision)
        spec.print_spec()

        gg = TypedSimpleGrammarGenerator()
        sd = StructDef()
        syn = AllInstructionsSynthesizer(spec= spec, dsl_operators = relavent_dsls, grammar_generator = gg, step = 0, scale_factor = 1, target = "repair")

        grammar_name = "test_grammar"
        grammar_def = syn.emit_synthesis_grammar(main_grammar_name = grammar_name)


        return grammar_name, grammar_def

    def property_holds_on_candidate(self, candidate):
        input_dsl_inst = candidate[0]
        modified_sema = self.get_instrumented_semantics(input_dsl_inst)

        statements = []
        statements.append(HYDRIDE_HEADER)

        arg_id = np.argmin([get_num_symbolic_args(ctx) for ctx in input_dsl_inst.contexts])

        src_ctx = input_dsl_inst.contexts[int(arg_id)]
        bv_streams = self.get_bv_streams(input_dsl_inst, modified_sema, 0, src_ctx)
        streams = bv_streams.split("STORE")
        stream_0 = streams[0].strip().split("\n")


        reduce_factor = self.get_reducing_factor(stream_0)

        modified_env_func = self.emit_prepare_repair_env(stream_0, modified_sema, input_dsl_inst, src_ctx)

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

        src_expr = "(define spec-expr {})".format(src_ctx.emit_context_expr_string())
        statements.append(src_expr)


        src_regs_count = len(src_ctx_regs)

        bitwidth_sizes = [str(arg.size) for arg in src_ctx_regs]

        bw_list_def = "(define bitwidth-list (list {}))".format(" ".join(bitwidth_sizes))
        statements.append(bw_list_def)

        stream_bv_sizes = self. get_stream_bitvector_sizes(stream_0)
        synth_input_sizes = [size for arg, size in stream_bv_sizes.items()]
        input_precs = [in_precision] * len(synth_input_sizes)


        input_signedness = src_ctx.signedness
        grammar_name, grammar_def = self.get_grammar_desc(out_precision, reduce_factor, synth_input_sizes, input_precs, input_signedness)


        statements.append(grammar_def)

        prepare_env = "prepare-env"
        target_interpreter_def = self.emit_create_updated_interpreter(prepare_env)

        statements.append(target_interpreter_def)



        invoke_ref_def = self.invoke_ref(out_precision, output_size, invoke_name = "invoke-ref", interpreter_name = "hvx:interpret", index = 0, is_lane_func = False)

        invoke_ref_lane_def = self.invoke_ref(out_precision, output_size, invoke_name = "invoke-ref-lane", interpreter_name = "hvx:interpret", index = 0, is_lane_func = True)

        statements.append(invoke_ref_def)
        statements.append(invoke_ref_lane_def)
        statements.append("(define optimize? #t)")

        synth_query = self.emit_synthesis_query()
        results = "(define-values (sat? mat elapsed) {})".format(synth_query)

        statements.append(results)
        joined_stmt = "\n".join(statements)
        print(joined_stmt)
        with open("repair.test.rkt", "w+") as WriteFile:
            WriteFile.write(joined_stmt)



        key = self.serialize_candidate(candidate)
        return True


    def invoke_ref(self, output_precision, outvect_size, invoke_name = "invoke-ref", interpreter_name= "hvx:interpreter", index = 0, is_lane_func = False):
        full_result = "(define spec-result-full ({} spec-expr env))".format(interpreter_name)
        output_lanes = outvect_size / output_precision

        adjusted_index = int(output_lanes - index - 1)
        low_offset = "(define result.i.low (* {} {}))".format(adjusted_index, output_precision)
        high_offset = "(define result.i.high (+ result.i.low (- {} 1)))".format(output_precision)
        extract_slice = "(extract result.i.high result.i.low spec-result-full)"

        body = [full_result, low_offset, high_offset, extract_slice, "\n"]

        body = "\n".join(body)

        if is_lane_func:
            return "(define ({} lane-idx env)\n{})".format(invoke_name , body)
        else:
            return "(define ({}  env)\n{})".format(invoke_name , body)







    def emit_synthesis_query(self, grammar_name = "grammar", interpreter_name = "rel-rep-interpret", cost_name = "repair:cost"):
        return "(synthesize-sol-iterative invoke-ref invoke-ref-lane {} bitwidth-list optimize? {} {} (list) (list) 25 'z3 (list))".format(grammar_name, interpreter_name, cost_name)

    def emit_create_updated_interpreter(self, prepare_func_name , wrapper_interpreter_name = "rel-rep-interpret", inner_interpreter_name = "repair:interpret"):
        return "(define ({} expr env)\n({} expr ({} env)\n)\n)".format(wrapper_interpreter_name, inner_interpreter_name, prepare_func_name)

    def serialize_candidate(self, candidate):
        return candidate[0].name + candidate[1].name

    def get_property_on_candidate(self, candidate):
        key = self.serialize_candidate(candidate)
        return {"candidate": candidate[0].name, "output_expression" : candidate[1].name }








    def emit_property_to_egg(self, property_map):
        return []








