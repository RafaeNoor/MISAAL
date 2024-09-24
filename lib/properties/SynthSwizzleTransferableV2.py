from properties.EqClassEqualDepth import *
from utils.DSLInstructionUtils import *
import copy
import numpy as np
from properties.Property import *

class SynthSwizzleTransferableV2(EqClassEqualDepth):

    def __init__(self, dsl_list = [],  swizzle_dsl_list = [], input_depth = 1, output_depth = 1, depth_range = True, synth_desc = None, commutative_map_path = None):


        super().__init__(dsl_list = dsl_list, output_depth = output_depth, swizzle_dsl_list = swizzle_dsl_list, source_synth_desc = synth_desc, target_synth_desc = synth_desc, commutative_map_path = commutative_map_path)
        self.input_depth = input_depth
        self.name = "SynthSwizzleTransferableV2"
        self.depth_range = depth_range
        self.useCanon = True



    def get_property_desc(self):
        return "Uses semantics of swizzles to identify swizzle movment patterns which may involve change of swizzles"

    def expr_contains_swizzles(self, expr):

        if isinstance(expr, Context):
            cond = "swizzle" in expr.name

            if cond:
                return True
            return any([self.expr_contains_swizzles(arg) for arg in expr.context_args])

        return False


    def expr_count_swizzles(self, expr):

        count = 0

        if isinstance(expr, Context):
            cond = "swizzle" in expr.name
            if cond:
                count += 1
            count+= sum([self.expr_count_swizzles(arg) for arg in expr.context_args])

        return count

    def generate_candidates(self):
        for dsl_inst in self.input_dsl_list:
            eq_class_copy = copy.deepcopy(dsl_inst)
            arg_max = np.argmax([get_num_symbolic_args(ctx) for ctx in eq_class_copy.contexts])

            enumerate_list = [eq_class_copy] + self.swizzle_dsl_list

            src_expressions = create_exhaustive_expressions_generator(enumerate_list, self.input_depth, use_eq_class = True, output_size = eq_class_copy.contexts[arg_max].out_vectsize)


            for src_expr in src_expressions:
                if not self.depth_range and get_expr_depth(src_expr) != self.input_depth:
                    continue

                canon_src = self.canonicalizer.canonicalize(src_expr)
                if  self.useCanon and not self.isCanonical(src_expr, canon_src):
                    continue

                target_expressions = create_exhaustive_expressions_generator(enumerate_list, self.output_depth, use_eq_class = True, output_size = eq_class_copy.contexts[arg_max].out_vectsize)
                for target_expr in target_expressions:
                    if not self.depth_range and get_expr_depth(target_expr) != self.output_depth:
                        continue

                    canon_target = self.canonicalizer.canonicalize(target_expr)
                    if  self.useCanon and not self.isCanonical(target_expr, canon_target):
                        continue

                    # If neither expressions contain swizzles then do not test
                    if (not self.expr_contains_swizzles(src_expr)) and (not self.expr_contains_swizzles(target_expr)):
                        continue


                    if src_expr.emit_context_expr_string() == target_expr.emit_context_expr_string():
                        continue



                    self.absolute_expr_count += self.get_absolute_count(src_expr) * self.get_absolute_count(target_expr)

                    candidate = (src_expr, target_expr, enumerate_list)
                    yield candidate



    def property_holds_on_candidate(self, candidate):


        src_ctx = copy.deepcopy(candidate[0])
        dst_ctx = copy.deepcopy(candidate[1])
        relavent_output_subset = candidate[2]


        key = self.serialize_candidate(candidate)

        if isinstance(dst_ctx, Reg):
            return False

        print(emit_compact_context_expr_str(src_ctx))
        print(emit_compact_context_expr_str(dst_ctx))


        dst_eq_class = self.get_eq_class(dst_ctx.dsl_name)

        matching_ctx = False
        for ctx in dst_eq_class.contexts:
            if ctx.out_vectsize == src_ctx.out_vectsize:
                matching_ctx = True

        if not matching_ctx:
            #print(dst_eq_class.name," has no context producing ", src_ctx.out_vectsize)
            return False





        input_sizes = self.get_context_input_sizes(src_ctx)
        output_size = src_ctx.out_vectsize
        precision = src_ctx.in_precision

        src_ctx_sym_args = self.get_registers(src_ctx)

        src_ctx_regs = src_ctx_sym_args

        reg_arg_map = {}
        for idx, arg in enumerate(src_ctx_sym_args):
            key = str(arg.size)
            if key not in reg_arg_map:
                reg_arg_map[key] = []
            reg_arg_map[key].append(arg)

        src_regs_count = len(src_ctx_regs)


        # Bind expression to target expression
        reg_arg_idx_map = {}
        for key in reg_arg_map:
            reg_arg_idx_map[key] = 0

        dst_regs = self.get_registers(dst_ctx)


        common_param =  False


        for idx, arg in enumerate(dst_regs):
            reg = None
            key = str(arg.size)
            if key not in reg_arg_idx_map:
                # Create a new register for left over values
                reg = Reg(str(len(src_ctx_regs)), precision, arg.size)
                src_ctx_regs.append(reg)
            else:
                index = reg_arg_idx_map[key]
                reg = reg_arg_map[key][index]
                updated_index = (index + 1) % len(reg_arg_map[key])
                reg_arg_idx_map[key] = updated_index

            if int(reg.index) < src_regs_count:
                common_param = True

            arg.index = reg.index
            arg.precision = reg.precision
            arg.size = reg.size
            arg.signed = reg.signed

        if not common_param:
            return False



        language_to_symbol = {"hvx": "'hvx",
                              "x86": "'x86",
                              "halide": "'halide" ,
                              "halide_hvx": "'halide",
                              "halide_x86": "'halide",
                              }

        statements = []

        src_language_desc = self.source_synth_desc
        # Need to create a new desc for swizzles and target inst comined
        #target_language_desc = self.target_synth_desc
        target_language_desc = create_synth_desc("base_", True, self.target_synth_desc.target_vector_sizes, "", "")
        target_language_desc.emit_sema = False

        target_language_dsl =  relavent_output_subset #self.output_dsl_list + self.swizzle_dsl_list
        src_language_dsl = relavent_output_subset

        if src_language_desc.emit_interpreter:
            statements.append(src_language_desc.emit_interpreter_framework(src_language_dsl))

        #if target_language_desc.emit_interpreter and src_language_desc.target_name != target_language_desc.target_name:
        #    statements.append(target_language_desc.emit_struct_def(self.swizzle_dsl_list))
        #    statements.append(target_language_desc.emit_interpreter_def(target_language_dsl))
        #    statements.append(target_language_desc.emit_cost_def(target_language_dsl))


        env = []
        for idx in range(len(src_ctx_regs)):
            value = "(?? (bitvector {}))".format(src_ctx_regs[idx].size)
            env.append(value)





        # Define dst expression as a grammar of possible
        # concrete Eq class members in the same structure
        input_precs = [arg.precision for arg in src_ctx_regs]

        GrammarGenerator = EqClassExpandGenerator(dsl_list = target_language_dsl  , output_bitwidth = output_size, input_sizes = [arg.size for arg in src_ctx_regs], input_precs = input_precs)
        dst_expression_label ,dst_expression_grammar =  GrammarGenerator.emit_grammar(dst_ctx, prefix = "dst")

        src_expression_label ,src_expression_grammar =  GrammarGenerator.emit_grammar(src_ctx, prefix = "src")
        statements.append(src_expression_grammar)

        #src_expression = "(define src-expr\n {}\n)".format(src_ctx.emit_context_expr_string())

        src_expression = "(define src-expr\n ({})\n)".format(src_expression_label)

        statements.append(src_expression)


        statements.append(dst_expression_grammar)

        grammar_fn = "(define (grammar-fn i) ({}))".format(dst_expression_label)
        statements.append(grammar_fn)

        statements.append(self.get_invoke_spec(spec_name = "src-expr"))

        statements.append(self.get_invoke_spec_lane(spec_name = "src-expr", output_prec = src_ctx.out_precision))

        statements.append("(define optimize? #t)")

        statements.append("(define symbolic? #f)")

        statements.append("(define interpreter {})".format(src_language_desc.interpreter_name))

        statements.append("(define cost-model {})".format(src_language_desc.cost_name))
        leaves_sizes = "(define leaves-sizes (list {}))".format(" ".join([str(arg.size) for arg in src_ctx_regs]))
        statements.append(leaves_sizes)



        execute_synthesis = "(define-values (satisfiable? mat-src mat-dst)  (expanded-grammar-synthesize invoke-spec invoke-spec-lane src-expr ({}) leaves-sizes optimize? interpreter cost-model  symbolic? 30 'z3))".format(dst_expression_label)
        statements.append(execute_synthesis)



        if_sat = "(exit 0)"
        if_unsat = "(exit 1)"

        conditional = "(cond [satisfiable? {}] [else {}])".format(if_sat, if_unsat)
        statements.append(conditional)

        result = execute_racket_file(statements)

        is_simplified = result.returncode == 0


        if is_simplified:
            print("SUCCESS")
            key = self.serialize_candidate(candidate)
            pair = (src_ctx, dst_ctx)
            self.simplify_map[key] = pair

        return is_simplified


    def serialize_candidate(self, candidate):
        return candidate[0].emit_context_expr_string() +"_"+candidate[1].emit_context_expr_string()


    def get_invoke_spec(self, spec_name = "spec-expr", env_name = "env"):
        interpret_name = self.source_synth_desc.interpreter_name
        interpret_stmt =   "({} {} {})".format(interpret_name, spec_name, env_name)
        return "(define (invoke-spec {}  {})\n {})".format(spec_name, env_name, interpret_stmt)


    def get_invoke_spec_lane(self, spec_name = "spec-expr", env_name = "env", output_prec = 8):
        interpret_name = self.source_synth_desc.interpreter_name
        interpret_stmt =   "({} {} {})".format(interpret_name, spec_name, env_name)
        low_offset = "(define low (* {} lane-idx))".format(str(output_prec))
        high_offset = "(define high (+ low (- {} 1)))".format(str(output_prec))
        extract = "(define slice (extract high low {}))".format(interpret_stmt)
        stmts = [low_offset, high_offset, extract, "slice"]
        return "(define (invoke-spec-lane {} lane-idx {})\n {})".format(spec_name, env_name, "\n".join(stmts))


    def get_property_on_candidate(self, candidate):
        key = self.serialize_candidate(candidate)
        (src_ctx, dst_ctx) = self.simplify_map[key]



        property_t = {"src": src_ctx.emit_context_expr_string(), "dst": dst_ctx.emit_context_expr_string(), 'src_compact': emit_compact_context_expr_str(src_ctx), 'dst_compact': emit_compact_context_expr_str(dst_ctx)}
        return property_t


    def run_on_batch_completion(self):
        return

