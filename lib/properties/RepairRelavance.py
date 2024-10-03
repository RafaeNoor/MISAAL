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
import sys

class RepairRelavance(IdentifySwizzles):



    def __init__(self, dsl_list = [], synth_desc = None, output_dsl_list = [], repair_dsl_list = [], target_synth_desc = None, target_start_depth = None,target_depth = 3, const_fold = False):

        super().__init__(dsl_list = dsl_list, synth_desc = synth_desc)
        self.name = "RepairRelavance"
        self.deduplicate_slices = True
        self.is_candidate_generator = True
        self.repair_dsl_list = repair_dsl_list
        self.output_dsl_list = output_dsl_list
        self.input_dsl_list = dsl_list
        input_test_list = [
            "_mm512_cvtepu8_epi32",
        ]

        #self.input_dsl_list = [d for d in self.input_dsl_list if d.name in input_test_list]

        self.target_synth_desc = target_synth_desc
        self.optimize = True
        self.target_start_depth = target_start_depth
        self.target_depth = target_depth
        self.const_fold = const_fold


        test_list = [
            "typed:cast-int",
        ]
        #self.output_dsl_list = [d for d in self.output_dsl_list if d.name in test_list]

        repair_test_list = [
            "repair-bwnot",
        ]

        #self.repair_dsl_list = [d for d in self.repair_dsl_list if d.name in repair_test_list]

        self.context_map = {}
        self.ctx_slice_sizes_operand_map = {}



    def get_property_desc(self):
        return "Test if a given output dsl instruction may be used to generate target expression"

    def generate_candidates(self):
        start_depth = self.target_depth
        if not self.target_start_depth is None:
            start_depth = self.target_start_depth
        for depth in range(start_depth, self.target_depth + 1):
            for input_dsl in self.input_dsl_list:
                for output_dsl in self.output_dsl_list:
                    visited_bv_ops = []

                    for idx,ctx in enumerate(input_dsl.contexts):
                        ops = get_expr_bv_ops(ctx)

                        if ops in visited_bv_ops:
                            continue

                        visited_bv_ops.append(ops)

                        candidate = (input_dsl, output_dsl, depth, idx)
                        candidate_key = self.serialize_candidate(candidate)
                        # If property already holds on shallower depths then continue
                        if candidate_key in self.context_map:
                            continue


                        yield candidate
        return



    def emit_get_constraints_function(self, target_dsl, constraint_fn_name = "constraint-fn", query_inst_name = ""):

        self.contains_name = "test_:contains"
        contains_name = self.contains_name
        sd = StructDef()

        query_inst_id = -1
        for dsl_inst in target_dsl:
            if dsl_inst.name == query_inst_name:
                query_inst_id = dsl_inst.dsl_id



        contains_query = "({}  expr {} ({} env))".format(contains_name, query_inst_id, "prepare-env")
        if self.const_fold:
            contains_query = "({} (test_:const-fold expr) {} ({} env))".format(contains_name, query_inst_id, "prepare-env")

        func = "(define ({} expr env)\n{}\n)".format(constraint_fn_name , contains_query)

        return func



    def get_reducing_factor(self, stream):
        # TODO: implement functionality
        extract_count = {}

        for extract in stream:
            arg = extract.strip().split(" ")[-1]
            if arg not in extract_count:
                extract_count[arg] = 0
            extract_count[arg] +=1


        return max([c for a,c in extract_count.items()])



    def create_prepare_repair_env_func(self, name, slices):
        create_extract = lambda x: "(extract {} {} arg)".format(x[0], x[1])

        if self.deduplicate_slices:
            unique_slices = list(set(slices))
            unique_slices = sorted(unique_slices, key = lambda x : slices.index(x))
            slices = unique_slices
        concat_expr = "(concat \n{}\n)".format("\n".join([create_extract(s) for s in slices]))

        env_func = "(define ({} arg)\n{}\n)".format(name, concat_expr)

        return env_func


    def get_scaled_context(self, ctx, num_lanes = 1):


        scaled_ctx = copy.deepcopy(ctx)
        current_lanes = ctx.out_vectsize // ctx.out_precision
        scale_factor = current_lanes // num_lanes
        if scale_factor == 1:
            return scaled_ctx
        scaled_ctx.scale_context(scale_factor)
        return scaled_ctx



    def create_prepare_repair_env_funcs(self, stream):
        prep_arg_slices = {}
        slice_sizes = {}



        for line in stream:
            tokens = line.strip().split()
            arg_name = tokens[-1]

            if arg_name not in prep_arg_slices:
                prep_arg_slices[arg_name] = []

            if arg_name not in slice_sizes:
                slice_sizes[arg_name] = []

            high = tokens[1]
            low = tokens[2]
            slice_sizes[arg_name] += [(high, low)]
            prep_arg_slices[arg_name].append((high,low))

        funcs = {}

        for arg in prep_arg_slices:
            funcs[arg] = self.create_prepare_repair_env_func(arg, prep_arg_slices[arg])

        total_slice_map = {}

        for key in prep_arg_slices:
            total_slice_map[key] = 0

            if self.deduplicate_slices:
                prep_arg_slices[key] = list(set(prep_arg_slices[key]))
            for high,low in prep_arg_slices[key]:
                total_slice_map[key] += int(high) - int(low) + 1




        return funcs , total_slice_map


    def get_stream_bitvector_sizes(self, stream, modified_sema, ctx ):

        prototype = modified_sema.split("\n")[0].strip().split("(define")[-1].strip().replace("(","")
        # Skip the name of the context
        prototype = prototype.replace(")","").split()[1:]

        sorted_args = []

        for idx, arg in enumerate(prototype):
            if isinstance(ctx.context_args[idx], BitVector) or isinstance(ctx.context_args[idx], Reg) :
                sorted_args.append(arg)


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
            # If it's a constant value do not include in grammar
            if not arg in sorted_args:
                continue
            total_sizes = 0
            for (high,low) in prep_arg_slices[arg]:
                total_sizes += int(high) - int(low) + 1
            funcs[arg] = total_sizes


        return funcs

    def create_repair_env_function(self, dsl_inst):
        # Once we've identified the bitslices being extracted in a single iteration we have to create a Rosette function which given the original synthesis env creates the spliced env for the repair

        return False

    def emit_prepare_repair_env(self, slice_stream, modified_sema, input_dsl_inst, ctx):
        funcs, slice_sizes  = self.create_prepare_repair_env_funcs(slice_stream)

        prototype = modified_sema.split("\n")[0].strip().split("(define")[-1].strip().replace("(","")
        # Skip the name of the context
        prototype = prototype.replace(")","").split()[1:]

        sorted_args = []

        for idx, arg in enumerate(prototype):
            if arg in funcs and isinstance(ctx.context_args[idx], BitVector):
                sorted_args.append(arg)



        prepare_clauses = []

        if ctx.name not in self.ctx_slice_sizes_operand_map:
            self.ctx_slice_sizes_operand_map[ctx.name] = [0] * len(sorted_args)



        for idx , arg in enumerate(sorted_args):
            clause = "({} (vector-ref env {}))".format(arg, idx)
            prepare_clauses.append(clause)
            self.ctx_slice_sizes_operand_map[ctx.name][idx] = slice_sizes[arg]

        env_function_clauses = [defs for arg, defs in funcs.items()]
        env_function_clauses.append("(vector {})".format(" ".join(prepare_clauses)))

        return "(define (prepare-env env)\n{}\n)".format("\n".join(env_function_clauses))



    def get_context_num_sym_args(self, ctx):
        return sum([1 for arg in ctx.context_args if isinstance(arg, BitVector)])

    def get_context_sym_args(self, ctx):
        return ([arg for arg in ctx.context_args if isinstance(arg, BitVector)])


    def get_context_input_sizes(self, ctx):
        return sorted([arg.size for arg in ctx.context_args if isinstance(arg, BitVector)])

    def get_grammar_desc(self,out_precision, reduce_factor, input_sizes, input_precs, input_signedness, src_ctx, output_dsl_inst):
        print("Output precision: ", out_precision)
        print("Input precision: ", input_precs)
        print("Input sizes: ", input_sizes)
        print("Input Signedness: ", input_signedness)

        relavent_dsls = []
        count = 0

        FAST = True
        src_bv_ops = src_ctx.get_bv_ops()
        #print("SRC BV OPS", src_bv_ops)

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

        print("Including number of contexts:", count)
        input_shapes = []
        for i in range(len(input_sizes)):
            input_shapes.append([1, input_sizes[i]// input_precs[i]])

        spec = Specification(semantics = [], output_shape = [1, 1], input_shapes = input_shapes, args = ["SYMBOLIC_BV_{}".format(i_size) for i_size in input_sizes], input_precision = input_precs, output_precision = out_precision)
        spec.print_spec()

        gg = TypedSimpleGrammarGeneratorV2()
        sd = StructDef()
        syn = AllInstructionsSynthesizer(spec= spec, dsl_operators = relavent_dsls, grammar_generator = gg, step = 0, scale_factor = 1, target = "repair")

        grammar_name = "test_grammar"
        grammar_def = syn.emit_synthesis_grammar(main_grammar_name = grammar_name)


        return grammar_name, grammar_def, relavent_dsls








    def property_holds_on_candidate(self, candidate):
        input_dsl_inst = candidate[0]
        modified_sema = self.get_instrumented_semantics(input_dsl_inst)
        depth = candidate[2]
        arg_id = candidate[3]

        key = self.serialize_candidate(candidate)

        if key in self.context_map:
            return False

        statements = []



        src_ctx = input_dsl_inst.contexts[int(arg_id)]
        print(src_ctx.name)
        if src_ctx.get_bv_ops() == []:
            return False
        #print(src_ctx.get_bv_ops())
        src_ctx = copy.deepcopy(src_ctx)
        bv_streams = self.get_bv_streams(input_dsl_inst, modified_sema, 0, src_ctx)
        streams = bv_streams.split("STORE")
        stream_0 = streams[0].strip().split("\n")
        print(stream_0)


        reduce_factor = self.get_reducing_factor(stream_0)
        print("Reduction factor:", reduce_factor)

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

        stream_bv_sizes = self.get_stream_bitvector_sizes(stream_0, modified_sema, src_ctx )
        synth_input_sizes = [size for arg, size in stream_bv_sizes.items()]
        input_precs = [in_precision] * len(synth_input_sizes)


        input_signedness = src_ctx.signedness
        grammar_name, grammar_def, target_dsl = self.get_grammar_desc(out_precision, reduce_factor, synth_input_sizes, input_precs, input_signedness, src_ctx, output_dsl_inst)


        statements.append(grammar_def)

        prepare_env = "prepare-env"
        target_interpreter_def = self.emit_create_updated_interpreter(prepare_env, target_dsl, query_inst_name = output_dsl_inst.name)

        statements.append(target_interpreter_def)

        constraints = self.emit_get_constraints_function(target_dsl, query_inst_name = output_dsl_inst.name)
        statements.append(constraints)


        interpret_name= self.synth_desc.interpreter_name

        invoke_ref_def = self.invoke_ref(out_precision, output_size, invoke_name = "invoke-ref", interpreter_name = interpret_name, index = 0, is_lane_func = False)

        invoke_ref_lane_def = self.invoke_ref(out_precision, output_size, invoke_name = "invoke-ref-lane", interpreter_name = interpret_name, index = 0, is_lane_func = True)

        statements.append(invoke_ref_def)
        statements.append(invoke_ref_lane_def)

        optimize_flag = ["#f", "#t"][int(self.optimize)]
        statements.append("(define optimize? {})".format(optimize_flag))

        statements.append("(define grammar (test_grammar {}))".format(depth))

        synth_query = self.emit_synthesis_query()
        results = "(define-values (sat? mat elapsed) {})".format(synth_query)

        statements.append(results)

        fname_prefix = get_random_tempfile_name()
        read_from_fname = fname_prefix+".log"+".rkt"

        holes = ["(?? (bitvector {}))".format(size) for size in bitwidth_sizes]
        folded_satisfies = "(constraint-fn (aggressive-test_:const-fold mat) (vector {}))".format(" ".join(holes))

        test = "(cond [\n(and sat? {}) (write-str-to-file (~v mat) \"{}\") (exit 0)]\n [else (exit 1)])".format(folded_satisfies, read_from_fname)
        statements.append(test)


        joined_stmt = "\n".join(statements)


        ret_code = execute_racket_file(statements)

        success = ret_code.returncode == 0


        if success:
            with open(read_from_fname, "r") as ReadFile:
                self.context_map[key] = ReadFile.read()
            os.remove(read_from_fname)



        return success

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







    def emit_synthesis_query(self, grammar_name = "grammar", interpreter_name = "rel-rep-interpret", cost_name = "test_:cost"):
        return "(synthesize-sol-iterative-constraints invoke-ref invoke-ref-lane {} bitwidth-list optimize? {} {} (list) (list) 25 'z3 (list) constraint-fn)".format(grammar_name, interpreter_name, cost_name)

    def emit_create_updated_interpreter(self, prepare_func_name , target_dsl, wrapper_interpreter_name = "rel-rep-interpret", inner_interpreter_name = "repair:interpret", query_inst_name = ""):

        contains_prop = ContainsDef()


        synth_desc = create_synth_desc("test_", True, [], "", "")
        synth_desc.emit_sema = False

        statements = []

        interpreter_fw = synth_desc.emit_interpreter_framework(target_dsl)
        statements.append(interpreter_fw)

        self.contains_name = "test_:contains"
        contains_name = self.contains_name
        sd = StructDef()
        contains_def = contains_prop.emit_contains(target_dsl ,sd,  interpreter_name = synth_desc.interpreter_name, contains_name = contains_name)
        statements.append(contains_def)

        query_inst_id = -1
        for dsl_inst in target_dsl:
            if dsl_inst.name == query_inst_name:
                query_inst_id = dsl_inst.dsl_id

        contains_query = "(assert ({} expr {} ({} env)))".format(contains_name, query_inst_id, prepare_func_name)
        interpret_cmd = "({} expr ({} env)\n)".format(synth_desc.interpreter_name, prepare_func_name)

        #interpreter_body = [contains_query, interpret_cmd]
        # Temporarily seperating out contains query
        interpreter_body = [interpret_cmd]



        outer_interpret = "(define ({} expr env)\n{}\n)".format(wrapper_interpreter_name, "\n".join(interpreter_body))

        statements.append(outer_interpret)

        return "\n".join(statements)

    def emit_create_updated_cost_model(self, target_dsl, cost_name):
        pass

    def serialize_candidate(self, candidate):
        return candidate[0].name + "+" + candidate[1].name #+ "+" + str(candidate[2])

    def get_property_on_candidate(self, candidate):
        key = self.serialize_candidate(candidate)
        synth_expr = self.context_map[key]
        return {"candidate": candidate[0].name, "output_expression" : candidate[1].name, "synth_expression": synth_expr }








    def emit_property_to_egg(self, property_map):
        return []








