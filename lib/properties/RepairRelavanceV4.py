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
from properties.RepairRelavanceV3 import RepairRelavanceV3
import sys
from utils.DoubleGrammarSynthesisUtils import DoubleGrammarSynthesisUtils
from pyparsing import nestedExpr
from utils.CanonicalizeExpressions import CanonicalizeExpression
from utils.ContainsRegDef import ContainsRegDef
from common.StructDef import StructDef

class RepairRelavanceV4(RepairRelavanceV3):



    def __init__(self, dsl_list = [], synth_desc = None, output_dsl_list = [], repair_dsl_list = [], target_synth_desc = None, target_start_depth = None,target_depth = 3, const_fold = False, commutative_map_path = None, force_contains_all_regs = True, memo_path = None):


        # Sort dsl list so that we can inspect dot-product related relevance earlier
        dsl_list = sort_dsl_list(dsl_list, ["bvmul", "sign-extend", "bvadd", "zero-extend"])


        input_test_list = [
            #"_mm256_maddubs_epi16",
            #"_mm256_dpbusd_epi32",
        ]

        #dsl_list = [d for d in dsl_list if d.name in input_test_list]


        print(dsl_list)

        output_test_list = [
            #"typed:signed-vec-widen-mul",
            #"typed:vec-add",
            "typed:signed-vector_reduce_add",
        ]

        #output_dsl_list = [d for d in output_dsl_list if d.name in output_test_list]

        print(output_dsl_list)


        repair_test_list = [
            #"repair-vector-reduce-add",
            "repair-add",
        ]

        #repair_dsl_list = [d for d in repair_dsl_list if d.name in repair_test_list]


        super().__init__(dsl_list = dsl_list, synth_desc = synth_desc, output_dsl_list = output_dsl_list, repair_dsl_list = repair_dsl_list, target_synth_desc = target_synth_desc, target_start_depth = target_start_depth, target_depth = target_depth, const_fold = const_fold, commutative_map_path = commutative_map_path, force_contains_all_regs = force_contains_all_regs, memo_path = memo_path)
        self.name = "RepairRelavanceV4"
        self.ctx_formal_param_names = {}
        self.current_depth = 0
        self.skip_exception = True


    def get_property_desc(self):
        return "Test if a given output dsl instruction may be used to generate target expression (Version 4)"

    def generate_candidates(self):
        start_depth = self.target_depth
        if not self.target_start_depth is None:
            start_depth = self.target_start_depth
        for depth in range(start_depth, self.target_depth + 1):
            self.current_depth = depth
            for input_dsl in self.input_dsl_list:
                for output_dsl in self.output_dsl_list:
                    candidate_prep = (input_dsl, output_dsl, depth)
                    skip = False
                    if self.skip_exception:
                        try:
                            candidate_generator = self.prepare_candidate_generator(candidate_prep, use_max_args = False)

                            # Generator internally will query state to know
                            # if the repair property is already valid hence we will exit early
                            for candidate in candidate_generator:
                                key = self.serialize_candidate(candidate)
                                if key in self.context_map:
                                    skip = True
                                    break
                                yield candidate
                            if skip:
                                continue

                            if not self.has_differing_number_of_symbolic_args(input_dsl):
                                continue

                            candidate_generator = self.prepare_candidate_generator(candidate_prep, use_max_args = True)

                            # Generator internally will query state to know
                            # if the repair property is already valid hence we will exit early
                            for candidate in candidate_generator:
                                key = self.serialize_candidate(candidate)
                                if key in self.context_map:
                                    skip = True
                                    break
                                yield candidate
                        except KeyboardInterrupt:
                            print("Keybord interrupt")
                            sys.exit()
                        except:
                            continue
                    else:
                        candidate_generator = self.prepare_candidate_generator(candidate_prep, use_max_args = False)
                        print(candidate_generator)

                        # Generator internally will query state to know
                        # if the repair property is already valid hence we will exit early
                        for candidate in candidate_generator:
                            key = self.serialize_candidate(candidate)
                            if key in self.context_map:
                                skip = True
                                break
                            yield candidate

                        if not self.has_differing_number_of_symbolic_args(input_dsl):
                            continue

                        if skip:
                            continue

                        candidate_generator = self.prepare_candidate_generator(candidate_prep, use_max_args = True)

                        # Generator internally will query state to know
                        # if the repair property is already valid hence we will exit early
                        for candidate in candidate_generator:
                            key = self.serialize_candidate(candidate)
                            if key in self.context_map:
                                skip = True
                                break
                            yield candidate




        return

    def has_differing_number_of_symbolic_args(self,input_dsl):
        num_sym_args = []

        for ctx in input_dsl.contexts:
            num_args = sum([1 for arg in ctx.context_args if isinstance(arg, BitVector)])
            num_sym_args.append(num_args)

        num_sym_args = list(set(num_sym_args))

        return len(num_sym_args) > 1

    def get_bv_streams_key(self, src_ctx):
        return src_ctx.name

    def get_repair_context_index(self, dsl_expr, use_max_args = False):
        max_args = 0

        if use_max_args:
            max_args = max([self.get_context_num_sym_args(ctx) for ctx in dsl_expr.contexts])
        else:
            max_args = min([self.get_context_num_sym_args(ctx) for ctx in dsl_expr.contexts])

        relavent_indices = [i for i in range(len(dsl_expr.contexts))  if self.get_context_num_sym_args(dsl_expr.contexts[i]) == max_args]


        return_idx = relavent_indices[0]
        if dsl_expr.contexts[return_idx].in_precision is None:
            return return_idx

        max_prec = dsl_expr.contexts[return_idx].in_precision
        for idx in relavent_indices:
            cur_prec = dsl_expr.contexts[idx].in_precision

            if cur_prec is None:
                continue

            if max_prec is None:
                max_prec = cur_prec

            if cur_prec > max_prec:
                max_prec = cur_prec
                return_idx = idx

        return return_idx

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
            self.bv_streams_map[stream_map_key] = stream_0

        print(input_dsl_inst.name)
        print(stream_0)

        if stream_0 == ['']:
            return


        reduce_factor = self.get_reducing_factor(stream_0)
        print("Reduction factor:", reduce_factor)

        repair_env_obj = self.emit_prepare_repair_env(stream_0, modified_sema, input_dsl_inst, src_ctx)
        modified_env_func = repair_env_obj['env_fn']
        env_sizes = repair_env_obj['ordered_sizes']

        print(modified_env_func)

        sliced_sizes = env_sizes
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
        #stream_bv_sizes = self.get_stream_bitvector_sizes(stream_0, modified_sema, src_ctx )
        synth_input_sizes = sliced_sizes #[size for arg, size in stream_bv_sizes.items()]
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
            candidate['prepare-env-function'] = modified_env_func

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
        return {"candidate": candidate['src_dsl'].name, "output_expression" : dst_expr_str, "synth_expression": src_expr_str, 'env-func': candidate['prepare-env-function'], 'target_input_sizes': candidate['custom_target_input_sizes']}


    def split_define_line(self, line):
        assert "(define" in line, "Assertion broken!"
        line = line.replace("\"","").strip()
        print(line)
        brackets = nestedExpr('(',')').parseString(line).asList()
        print(brackets)
        assert len(brackets) == 1
        [defn_key_word, label, expr] = brackets[0]

        # Only valid for bitvector ops
        if expr[0] not in BV_OPS:
            return "", "", False

        return label, expr, True


    def is_valid_define_line(self, line):
        line = line.replace("\"","").strip()
        if "(define" not in line:
            return False
        if ")" not in line:
            return False

        return True



    def handle_profile_bv_expr(self, label, expr, extract_labels, is_extract = False):
        stmt = ""
        if is_extract:
            brackets = nestedExpr('(',')').parseString(expr).asList()[0]
            print(brackets)
            hi =  brackets[1]
            lo =  brackets[2]
            arg =  brackets[3]
            if isinstance(arg, list) and arg[0] == 'bv':
                arg = "({})".format(" ".join(arg))
            stmt = "(printf \"(define reg_{} (extract ~a ~a ~a))\\n\"  {} {} \"{}\")".format(extract_labels.index(label), hi, lo, arg)
        else:
            stmt = "(printf \"(define ({}) {} )\\n\")".format(label, expr)
            pass
        return stmt

    def init_expr_map(self, dsl_inst, ctx):
        func_prototype =  dsl_inst.semantics[0]
        # Operands are ordered in the order they appear in the prototype
        formal_args = func_prototype.strip().split("(")[-1].split(")")[0].strip().split(" ")[1:]

        formal_args = [arg for arg in formal_args if arg != '']

        if ctx.name not in self.ctx_formal_param_names:
            self.ctx_formal_param_names[ctx.name] = formal_args



        expr_map = {}

        for idx, arg in enumerate(ctx.context_args):
            if isinstance(arg, BitVector):
                continue
            elif isinstance(arg, ConstBitVector):
                lit_racket_value =  "(bv {} {})".format(arg.value, arg.size)
                expr_map[formal_args[idx]] = lit_racket_value
            else:
                expr_map[formal_args[idx]] = str(arg.value)

        return expr_map


    # Updated instrumentation which print's out expression for intermediate values
    def get_instrumented_semantics(self, dsl_inst, ctx_index):
        print("Obtaining instrumented semantics")
        new_sema = []


        original_sema = dsl_inst.semantics

        arg_map = self.get_dsl_inst_formal_arg_to_size_map(dsl_inst, dsl_inst.contexts[ctx_index])
        formal_params = [key for key in arg_map]
        try:
            # Pre-processing
            dsl_inst.semantics = inline_nested_extracts_in_sema(dsl_inst.semantics)
            dsl_inst.semantics = remove_redundant_extracts(dsl_inst.semantics, arg_map)
        except:
            print("Exception encountered in profiling semantics")
            dsl_inst.semantics = original_sema


        # Maps Rosette Value name to fully inlined expression derivation
        # Intialize expression map according to formal param context specific values
        expr_map = self.init_expr_map(dsl_inst, dsl_inst.contexts[ctx_index])
        print("Initial expr map", expr_map)

        extract_labels = []

        apply_cond = False
        for line_idx, line in enumerate(dsl_inst.semantics):
            if "apply" in line:
                next_line = dsl_inst.semantics[line_idx+1]
                if "concat" not in next_line:
                    apply_cond = True

            if "cond" in line:
                apply_cond = True

            if dsl_inst.name in line:
                new_sema.append(line.replace(dsl_inst.name, self.get_profiling_name(dsl_inst)).replace("\"", ""))
            elif self.is_valid_define_line(line) :
                label, expr, isBVOp = self.split_define_line(line)

                if isBVOp:
                    is_extract = "(extract" in line

                    if is_extract and label not in extract_labels:
                        extract_labels.append(label)
                    inlined_terms = []

                    for term in expr:
                        if term in expr_map:
                            inlined_terms.append(expr_map[term])
                        else:
                            inlined_terms.append(term)
                    expr_to_rosette = "({})".format(" ".join(inlined_terms))
                    print(expr_to_rosette)
                    updated_stmt = self.handle_profile_bv_expr(label, expr_to_rosette, extract_labels , is_extract = is_extract)
                    if is_extract:
                        expr_to_rosette = "reg_{}".format(extract_labels.index(label))
                        pass

                    expr_map[label] = expr_to_rosette
                    new_sema.append(updated_stmt)

                new_sema.append(line.replace("\"", ""))
                if isBVOp:
                    # Obtain bitvector sizes dynamically to avoid complex analysis
                    stmt = "(printf \"(SIZE {} ~a)\\n\" (bvlength {}))".format(label, label)
                    if is_extract:
                        stmt = "(printf \"(SIZE {} ~a)\\n\" (bvlength {}))".format( "reg_{}".format(extract_labels.index(label)), label)
                    new_sema.append(stmt)




            elif self.is_store_line(line):
                if apply_cond:
                    new_sema.append('(printf \"LANE\\n\")')
                    new_sema.append(line.replace("\"", ""))
                    apply_cond = False
                else:
                    new_sema.append('(printf \"STORE\\n\")')
                    new_sema.append(line.replace("\"", ""))
            else:
                new_sema.append(line.replace("\"", ""))

        return "\n".join(new_sema)







    def get_reducing_factor(self, stream):
        # Count number of lane seperating calls per output lane
        return sum([1 for c in stream if c == 'LANE'])


    def bind_slice_regs(self, expr, reg_map, lane_idx):
        if isinstance(expr, list):
            for idx, term in enumerate(expr):
                if isinstance(term, str) and term in reg_map:
                    if lane_idx < len(reg_map[term]):
                        expr[idx] = reg_map[term][lane_idx]
                    else:
                        expr[idx] = reg_map[term][0]
                else:
                    expr[idx] = self.bind_slice_regs(term, reg_map, lane_idx)
            return expr
        else:
            return expr


    def get_size_map(self, stmts):
        size_map = {}
        for stmt in stmts:
            brackets = nestedExpr('(',')').parseString(stmt).asList()[0]
            label = brackets[1]
            size = brackets[2]
            size_map[label] = size

        return size_map

    def emit_prepare_repair_env(self, slice_stream, modified_sema, input_dsl_inst, ctx):

        size_defn = [line for line in slice_stream if "SIZE" in line]
        print(size_defn)

        size_map = self.get_size_map(size_defn)


        slice_stream = [line for line in slice_stream if not "SIZE" in line]

        # First create functions for variables and function per lane
        lane_idx = 0

        var_label_map = {}


        # We don't want to include the final intermediate value as part of
        # the possible symbolic values since that would be a degenerate case
        slice_stream = slice_stream[:-1]
        for line in slice_stream:

            if line == 'LANE':
                lane_idx += 1
                continue
            brackets = nestedExpr('(',')').parseString(line).asList()[0]
            print(brackets)
            label = brackets[1]

            if isinstance(label, list):
                label = label[0]

            if label not in var_label_map:
                var_label_map[label] = []

            var_label_map[label].append(brackets[2])

        # Replace all instances of reg in the expression labels with the corresponding indices

        regs = [key for key in var_label_map if key.startswith("reg")]

        reg_map = {}
        for reg in regs:
            reg_map[reg] = var_label_map[reg]

        non_regs = [key for key in var_label_map if not key.startswith("reg")]

        # Place registers first and then non-reg
        non_regs = regs + non_regs


        for label in non_regs:
            for lane_idx, lane_context in enumerate(var_label_map[label]):
                previous_expr = var_label_map[label][lane_idx]
                var_label_map[label][lane_idx] = self.bind_slice_regs(previous_expr, reg_map, lane_idx)

        print(json.dumps(var_label_map, indent = 4))


        # Create Rosette functions to create slices and concat for non-regs

        non_reg_fn_defn = {}
        for label in non_regs:
            to_concat = ["\n"]
            for term in var_label_map[label]:
                flattened_term = self.convert_nested_list_to_rosette(term)
                to_concat.append(flattened_term)

            defn = "(define {} (concat {}))".format(label, "\n".join(to_concat))
            non_reg_fn_defn[label] = defn




        non_reg_size_map = {}

        for label in non_regs:
            non_reg_size_map[label] = len(var_label_map[label]) * int(size_map[label])

        ordered_keys = [label for label in non_regs]
        ordered_defns = [non_reg_fn_defn[label] for label in ordered_keys]
        ordered_sizes = [non_reg_size_map[label] for label in ordered_keys]

        print(json.dumps(non_reg_fn_defn, indent = 4))
        print(non_reg_size_map)

        # Create prepare env function

        formal_param_defs = ["\n"]

        sym_args_counter = 0
        for idx, arg in enumerate(ctx.context_args):
            formal_name = self.ctx_formal_param_names[ctx.name][idx]
            if isinstance(arg, BitVector):
                defn = "(define {} (vector-ref env {}))".format(formal_name, sym_args_counter)
                sym_args_counter += 1

                formal_param_defs.append(defn)


        formal_param_defs = "\n".join(formal_param_defs)

        prepare_env_fn = "(define (prepare-env env) {} \n {} \n (vector {})\n)".format(formal_param_defs, "\n".join(ordered_defns), " ".join(ordered_keys))

        result_obj = {'env_fn':  prepare_env_fn, 'ordered_keys': ordered_keys, 'ordered_defns': ordered_defns, 'ordered_sizes': ordered_sizes, 'formal_param_defs': formal_param_defs}
        return result_obj






    def  convert_nested_list_to_rosette(self, expr):
        flat = []
        if isinstance(expr, list):
            for item in expr:
                flat_term = self.convert_nested_list_to_rosette(item)
                flat.append(flat_term)
        else:
            return expr

        return "({})".format(" ".join(flat))


    def get_stream_bitvector_sizes(self, stream, modified_sema, ctx ):

        prototype = modified_sema.split("\n")[0].strip().split("(define")[-1].strip().replace("(","")
        # Skip the name of the context
        prototype = prototype.replace(")","").split()[1:]

        sorted_args = []

        for idx, arg in enumerate(prototype):
            if isinstance(ctx.context_args[idx], BitVector) or isinstance(ctx.context_args[idx], Reg) :
                sorted_args.append(arg)


        prep_arg_slices = {}




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

    def get_notify_body(self, count, success_count, start_time):
        orig_body = super().get_notify_body(count, success_count, start_time)
        current_depth_str  = "Current Depth:\t{}".format(str(self.current_depth))
        return "\n".join([orig_body, current_depth_str])

