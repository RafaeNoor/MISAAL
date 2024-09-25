from utils.DSLInstructionUtils import *
from utils.CodeSynthesizerDesc import *
from common.Types import *
from  common.Instructions import Context
import copy
from grammar_gen.EqClassExpandGenerator import EqClassExpandGenerator
import sys

class DoubleGrammarSynthesisUtils:

    def __init__(self, input_dsl_list = [], output_dsl_list = [], swizzle_dsl_list = [], auxilary_dsl_list = []):
        self.input_dsl_list = input_dsl_list
        self.output_dsl_list = output_dsl_list
        self.swizzle_dsl_list = swizzle_dsl_list
        self.auxilary_dsl_list = auxilary_dsl_list


    def get_registers(self, ctx):
        regs = []
        if isinstance(ctx, Context):
            for arg in ctx.context_args:
                regs += self.get_registers(arg)
        elif isinstance(ctx, Reg):
            return [ctx]
        else:
            return []
        # Deduplicate and order according to increasing order

        unique_regs = []

        for reg in regs:
            unique_regs.append(int(reg.index))
        unique_regs = list(set(unique_regs))

        unique_regs.sort()

        # Sort in increasing order
        ordered_regs = ['empty'] * len(unique_regs)

        for reg in regs:
            ordered_regs[unique_regs.index(int(reg.index))] = reg

        return ordered_regs

    def get_relevant_dsl_list(self, exprs):
        dsl_names = []
        for expr in exprs:
            dsl_names += self.get_relevant_dsl_list_names(expr)
        dsl_names = list(set(dsl_names))
        return [self.get_eq_class(name) for name in dsl_names]


    def get_relevant_dsl_list_names(self, expr):
        names = []
        if isinstance(expr, Context):
            names.append(expr.dsl_name)

            for arg in expr.context_args:
                names += self.get_relevant_dsl_list_names(arg)

        return list(set(names))




    def double_grammar_synthesis(self, src_expr, target_expr, invoke_ref_custom = None, invoke_ref_lane_custom = None, invoke_target_custom = None, additional_statements = [], custom_src_output_size = None, custom_dst_output_size = None, custom_src_input_sizes = None, custom_target_input_sizes = None):
        src_ctx = copy.deepcopy(src_expr)
        dst_ctx = copy.deepcopy(target_expr)

        relavent_output_subset = self.get_relevant_dsl_list([dst_ctx])
        print(relavent_output_subset)

        assert len(relavent_output_subset) != 0, "Atleast one AutoLLVM IR class expected for target language"
        relavent_input_subset = self.get_relevant_dsl_list([src_ctx])
        print(relavent_input_subset)
        assert len(relavent_input_subset) != 0, "Atleast one AutoLLVM IR class expected for src language"
        relavent_dsl_subset = self.get_relevant_dsl_list([src_ctx, dst_ctx])
        print(relavent_dsl_subset)

        print("relavent_output_subset", len(relavent_output_subset), len(relavent_output_subset[0].contexts))
        print("relavent_input_subset", len(relavent_input_subset),  len(relavent_input_subset[0].contexts))
        print("relavent_combined_subset", len(relavent_dsl_subset))




        if isinstance(dst_ctx, Reg):
            print("Early return: Dst expression is a context")
            return False, "", ""

        print(emit_compact_context_expr_str(src_ctx))
        print(emit_compact_context_expr_str(dst_ctx))


        dst_eq_class = self.get_eq_class(dst_ctx.dsl_name)

        matching_ctx = False
        for ctx in dst_eq_class.contexts:
            if ctx.out_vectsize == src_ctx.out_vectsize:
                matching_ctx = True

        if not matching_ctx:
            print("Early return: No matching context")
            return False, "", ""



        src_output_size = src_ctx.out_vectsize
        if not custom_src_output_size is None:
            src_output_size = custom_src_output_size

        dst_output_size = src_ctx.out_vectsize
        if not custom_dst_output_size is None:
            dst_output_size = custom_dst_output_size

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
        print(reg_arg_map)

        dst_regs = self.get_registers(dst_ctx)

        """
        common_param =  False


        for idx, arg in enumerate(dst_regs):
            reg = None
            key = str(arg.size)
            if key not in reg_arg_idx_map:
                # Create a new register for every left over values
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
            print("Early return: No common param")
            return False, "" , ""
        """




        statements = additional_statements

        # Need to create a new desc for swizzles and target inst comined
        double_grammar_desc = create_synth_desc("double_target_", True, [], "", "")
        double_grammar_desc.emit_sema = True
        double_grammar_desc.emit_interpreter = True

        target_language_dsl =  relavent_output_subset
        src_language_dsl = relavent_input_subset

        if double_grammar_desc.emit_interpreter:
            statements.append(double_grammar_desc.emit_interpreter_framework(relavent_dsl_subset))

        env = []
        for idx in range(len(src_ctx_regs)):
            value = "(?? (bitvector {}))".format(src_ctx_regs[idx].size)
            env.append(value)



        # Define dst expression as a grammar of possible
        # concrete Eq class members in the same structure
        input_precs = [arg.precision for arg in src_ctx_regs]


        src_input_sizes = [arg.size for arg in src_ctx_regs]
        dst_input_sizes = [arg.size for arg in src_ctx_regs]


        if not custom_src_input_sizes is None:
            src_input_sizes = custom_src_input_sizes
        if not custom_target_input_sizes is None:
            dst_input_sizes = custom_target_input_sizes

        GrammarGeneratorDst = EqClassExpandGenerator(dsl_list = relavent_dsl_subset  , output_bitwidth = dst_output_size , input_sizes = dst_input_sizes, input_precs = input_precs)
        dst_expression_label ,dst_expression_grammar =  GrammarGeneratorDst.emit_grammar(dst_ctx, prefix = "dst")

        GrammarGeneratorSrc = EqClassExpandGenerator(dsl_list = relavent_dsl_subset  , output_bitwidth = src_output_size, input_sizes = src_input_sizes, input_precs = input_precs)

        src_expression_label ,src_expression_grammar =  GrammarGeneratorSrc.emit_grammar(src_ctx, prefix = "src")
        statements.append(src_expression_grammar)

        src_expression = "(define src-expr\n ({})\n)".format(src_expression_label)

        statements.append(src_expression)


        statements.append(dst_expression_grammar)


        if not invoke_ref_custom is None:
            decl , defn = invoke_ref_custom(double_grammar_desc.interpreter_name)
            statements.append(defn)
        else:
            statements.append(self.get_invoke_spec(spec_name = "src-expr", interpret_name = double_grammar_desc.interpreter_name))

        if not invoke_ref_lane_custom is None:
            decl , defn = invoke_ref_lane_custom(double_grammar_desc.interpreter_name)
            statements.append(defn)
        else:
            statements.append(self.get_invoke_spec_lane(spec_name = "src-expr", output_prec = src_ctx.out_precision, interpret_name = double_grammar_desc.interpreter_name))

        statements.append("(define optimize? #t)")

        statements.append("(define symbolic? #f)")

        if not invoke_target_custom  is None:
            interpret_def_name, interpret_def = invoke_target_custom(double_grammar_desc.interpreter_name)
            statements.append(interpret_def)
            statements.append("(define interpreter {})".format(interpret_def_name))
        else:
            statements.append("(define interpreter {})".format(double_grammar_desc.interpreter_name))

        statements.append("(define cost-model {})".format(double_grammar_desc.cost_name))
        leaves_sizes = "(define leaves-sizes (list {}))".format(" ".join([str(arg.size) for arg in src_ctx_regs]))
        statements.append(leaves_sizes)



        execute_synthesis = "(define-values (satisfiable? mat-src mat-dst)  (expanded-grammar-synthesize invoke-spec invoke-spec-lane src-expr ({}) leaves-sizes optimize? interpreter cost-model  symbolic? 30 'z3))".format(dst_expression_label)
        statements.append(execute_synthesis)


        fname_prefix = get_random_tempfile_name()
        read_from_fname_src = fname_prefix+".src.log"+".rkt"
        read_from_fname_dst = fname_prefix+".dst.log"+".rkt"
        write_src_to_file ="(write-str-to-file (~v mat-src) \"{}\")".format(read_from_fname_src)

        write_dst_to_file ="(write-str-to-file (~v mat-dst) \"{}\")".format(read_from_fname_dst)


        if_sat = "\n".join([write_src_to_file ,write_dst_to_file,"(exit 0)"])
        if_unsat = "(exit 1)"

        conditional = "(cond [satisfiable? {}] [else {}])".format(if_sat, if_unsat)
        statements.append(conditional)

        result = execute_racket_file(statements)

        is_simplified = result.returncode == 0

        synth_src_str = ""
        synth_dst_str = ""
        if is_simplified:
            with open(read_from_fname_src, "r") as ReadFile:
                synth_src_str = ReadFile.read()
            os.remove(read_from_fname_src)

            with open(read_from_fname_dst, "r") as ReadFile:
                synth_dst_str = ReadFile.read()
            os.remove(read_from_fname_dst)


        return is_simplified, synth_src_str, synth_dst_str

    def get_context_input_sizes(self, ctx):
        return sorted([arg.size for arg in ctx.context_args if isinstance(arg, BitVector)])

    def get_context_num_sym_args(self, ctx):
        return sum([1 for arg in ctx.context_args if isinstance(arg, BitVector)])

    def get_context_sym_args(self, ctx):
        return ([arg for arg in ctx.context_args if isinstance(arg, BitVector)])

    def get_eq_class(self, eq_class_name):
        eq_class_name = eq_class_name.split("_dsl")[0]
        for dsl_inst in self.input_dsl_list+self.output_dsl_list+self.swizzle_dsl_list + self.auxilary_dsl_list:
            if dsl_inst.name == eq_class_name:
                return dsl_inst
        print("Unable to find", eq_class_name)
        assert False,"Unreachable"

    def get_invoke_spec(self, spec_name = "spec-expr", env_name = "env", interpret_name = "interpret", invoke_spec_name = "invoke-spec"):
        interpret_stmt =   "({} {} {})".format(interpret_name, spec_name, env_name)
        return "(define ({} {}  {})\n {})".format(invoke_spec_name ,spec_name, env_name, interpret_stmt)


    def get_invoke_spec_lane(self, spec_name = "spec-expr", env_name = "env", output_prec = 8, interpret_name = "interpret", invoke_spec_name = "invoke-spec-lane"):
        interpret_stmt =   "({} {} {})".format(interpret_name, spec_name, env_name)
        low_offset = "(define low (* {} lane-idx))".format(str(output_prec))
        high_offset = "(define high (+ low (- {} 1)))".format(str(output_prec))
        extract = "(define slice (extract high low {}))".format(interpret_stmt)
        stmts = [low_offset, high_offset, extract, "slice"]
        return "(define ({} {} lane-idx {})\n {})".format(invoke_spec_name ,spec_name, env_name, "\n".join(stmts))
