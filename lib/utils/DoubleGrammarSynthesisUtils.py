from utils.DSLInstructionUtils import *
from utils.CodeSynthesizerDesc import *
from utils.CanonicalizeExpressions import CanonicalizeExpression
from utils.ReadDSL import read_string_to_dsl
from common.Types import *
from common.StructDef import StructDef
from  common.Instructions import Context
import copy
from grammar_gen.EqClassExpandGenerator import EqClassExpandGenerator
from synthesizer.StepWiseSynthesizer import StepWiseSynthesizer
from synthesizer.AllInstructionsSynthesizer import AllInstructionsSynthesizer
from grammar_generator.TypedSimpleGrammarGenerator import TypedSimpleGrammarGenerator
from utils.ContainsRegDef import ContainsRegDef
import sys

class DoubleGrammarSynthesisUtils:

    def __init__(self, input_dsl_list = [], output_dsl_list = [], swizzle_dsl_list = [], auxilary_dsl_list = [], force_contains_all_regs = True, use_any_reg = True, required_src_name = None, required_dst_name = None, ensure_structure = False):
        self.input_dsl_list = input_dsl_list
        self.output_dsl_list = output_dsl_list
        self.swizzle_dsl_list = swizzle_dsl_list
        self.auxilary_dsl_list = auxilary_dsl_list
        self.struct_def = StructDef()
        self.force_contains_all_regs = force_contains_all_regs
        self.contains_reg_def = ContainsRegDef()
        self.use_any_reg = use_any_reg
        self.required_src_name = required_src_name
        self.required_dst_name = required_dst_name
        self.ensure_structure = ensure_structure



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




    def double_grammar_synthesis(self, src_expr, target_expr, invoke_ref_custom = None, invoke_ref_lane_custom = None, invoke_target_custom = None, additional_statements = [], custom_src_output_size = None, custom_dst_output_size = None, custom_src_input_sizes = None, custom_target_input_sizes = None, is_src_grammar = True):
        src_ctx = copy.deepcopy(src_expr)
        dst_ctx = copy.deepcopy(target_expr)

        print(emit_compact_context_expr_str(src_ctx))
        print(emit_compact_context_expr_str(dst_ctx))

        relavent_output_subset = self.get_relevant_dsl_list([dst_ctx])
        print(relavent_output_subset)

        assert len(relavent_output_subset) != 0 or isinstance(target_expr, Reg), "Atleast one AutoLLVM IR class expected for target language"
        relavent_input_subset = self.get_relevant_dsl_list([src_ctx])
        print(relavent_input_subset)
        assert len(relavent_input_subset) != 0, "Atleast one AutoLLVM IR class expected for src language"
        relavent_dsl_subset = self.get_relevant_dsl_list([src_ctx, dst_ctx])
        print(relavent_dsl_subset)

        #print("relavent_output_subset", len(relavent_output_subset), len(relavent_output_subset[0].contexts))
        #print("relavent_input_subset", len(relavent_input_subset),  len(relavent_input_subset[0].contexts))
        #print("relavent_combined_subset", len(relavent_dsl_subset))




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



        statements = []


        statements += additional_statements

        # Need to create a new desc for swizzles and target inst comined
        double_grammar_desc = create_synth_desc("double_target_", True, [], "", "")
        double_grammar_desc.emit_sema = True
        double_grammar_desc.emit_interpreter = True

        target_language_dsl =  relavent_output_subset
        src_language_dsl = relavent_input_subset

        if double_grammar_desc.emit_interpreter:
            statements.append(double_grammar_desc.emit_interpreter_framework(relavent_dsl_subset))

        if self.force_contains_all_regs:
            statements.append(self.contains_reg_def.emit_contains(relavent_dsl_subset ,self.struct_def))

        num_src_regs = len(src_ctx_regs)

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


        for idx, prec in enumerate(input_precs):
            min_prec = min(prec, dst_input_sizes[idx])
            input_precs[idx] = min_prec

        print("Dst Output Size:", dst_output_size)
        print("Dst Input Sizes:", dst_input_sizes)
        print("Dst Input Precs:", input_precs)


        if len(dst_input_sizes) == 0:
            return False , "", ""


        GrammarGeneratorSrc = EqClassExpandGenerator(dsl_list = relavent_dsl_subset  , output_bitwidth = src_output_size, input_sizes = src_input_sizes, input_precs = input_precs, use_any_reg = self.use_any_reg)

        src_expression_label ,src_expression_grammar =  GrammarGeneratorSrc.emit_grammar(src_ctx, prefix = "src", required_root_name = self.required_src_name)


        if is_src_grammar:
            statements.append(src_expression_grammar)
            src_expression = "(define src-expr\n ({})\n)".format(src_expression_label)
            statements.append(src_expression)
        else:
            src_expression = "(define src-expr\n'()\n)"
            statements.append(src_expression)

        dst_expression_label = None

        GrammarGeneratorDst = EqClassExpandGenerator(dsl_list = relavent_dsl_subset  , output_bitwidth = dst_output_size , input_sizes = dst_input_sizes, input_precs = input_precs, use_any_reg = self.use_any_reg)
        dst_expression_label ,dst_expression_grammar =  GrammarGeneratorDst.emit_grammar(dst_ctx, prefix = "dst", required_root_name = self.required_dst_name)

        statements.append(dst_expression_grammar)


        if not invoke_ref_custom is None:
            decl , defn = invoke_ref_custom(double_grammar_desc.interpreter_name)
            statements.append(defn)
        else:
            statements.append(self.get_invoke_spec(spec_name = "src-expr", interpret_name = double_grammar_desc.interpreter_name, num_regs = num_src_regs))

        if not invoke_ref_lane_custom is None:
            decl , defn = invoke_ref_lane_custom(double_grammar_desc.interpreter_name)
            statements.append(defn)
        else:
            statements.append(self.get_invoke_spec_lane(spec_name = "src-expr", output_prec = src_ctx.out_precision, interpret_name = double_grammar_desc.interpreter_name, num_regs = num_src_regs))

        statements.append("(define optimize? #t)")

        statements.append("(define symbolic? #f)")

        if not invoke_target_custom  is None:
            interpret_def_name, interpret_def = invoke_target_custom(double_grammar_desc.interpreter_name)
            statements.append(interpret_def)
            statements.append("(define interpreter {})".format(interpret_def_name))
        else:
            statements.append("(define interpreter {})".format(double_grammar_desc.interpreter_name))

        statements.append("(define cost-model {})".format(double_grammar_desc.cost_name))
        leaves_sizes_vals = [str(arg.size) for arg in src_ctx_regs]
        if not custom_src_input_sizes is None:
            leaves_sizes_vals = [str(size) for size in custom_src_input_sizes]
        leaves_sizes = "(define leaves-sizes (list {}))".format(" ".join(leaves_sizes_vals))
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

        #print("\n".join(statements))
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

        if self.ensure_structure and is_simplified:
            src_expr = self.read_str_to_expr(synth_src_str)
            dst_expr = self.read_str_to_expr(synth_dst_str)

            if self.structure_matches(src_expr, src_ctx) and self.structure_matches(dst_expr, dst_ctx):
                return is_simplified, synth_src_str, synth_dst_str
            else:
                return False , "", ""


        else:
            return is_simplified, synth_src_str, synth_dst_str


    def read_str_to_expr(self, expr_str):
        combined_list = self.input_dsl_list + self.output_dsl_list + self.swizzle_dsl_list + self.auxilary_dsl_list

        return read_string_to_dsl(expr_str, combined_list)

    def structure_matches(self, expr, ref_expr):
        canon_utils = CanonicalizeExpression()
        return canon_utils.isCanonical(expr, ref_expr)


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

    def get_invoke_spec(self, spec_name = "spec-expr", env_name = "env", interpret_name = "interpret", invoke_spec_name = "invoke-spec", num_regs = 1):

        constraint = self.emit_contains_assertion(expr_name = spec_name, num_regs = num_regs)

        interpret_stmt =   "\n".join([constraint, "({} {} {})".format(interpret_name, spec_name, env_name)])
        return "(define ({} {}  {})\n {})".format(invoke_spec_name ,spec_name, env_name, interpret_stmt)


    def get_invoke_spec_lane(self, spec_name = "spec-expr", env_name = "env", output_prec = 8, interpret_name = "interpret", invoke_spec_name = "invoke-spec-lane", num_regs = 1):

        constraint = self.emit_contains_assertion(expr_name = spec_name, num_regs = num_regs)
        interpret_stmt =   "\n".join(["({} {} {})".format(interpret_name, spec_name, env_name)])
        low_offset = "(define low (* {} lane-idx))".format(str(output_prec))
        high_offset = "(define high (+ low (- {} 1)))".format(str(output_prec))
        extract = "(define slice (extract high low {}))".format(interpret_stmt)
        stmts = [constraint,low_offset, high_offset, extract, "slice"]
        return "(define ({} {} lane-idx {})\n {})".format(invoke_spec_name ,spec_name, env_name, "\n".join(stmts))

    def emit_contains_assertion(self, expr_name = "spec-expr", num_regs = 1):
        if self.force_contains_all_regs:
            is_symbolic = "(not (concrete? {}))".format(expr_name)
            contains_regs = ["({} {} {})".format(self.contains_reg_def.contains_name, expr_name, idx) for idx in range(0, num_regs)]
            contains_all = "(assert (and {}))".format(" ".join(contains_regs))
            condition = "(cond [{} {}])".format(is_symbolic, contains_all)
            return condition
        else:
            return ""



    def double_grammar_synthesis_hydride(self, src_expr, target_list, invoke_ref_custom = None, invoke_ref_lane_custom = None, invoke_target_custom = None, additional_statements = [], custom_src_output_size = None, custom_dst_output_size = None, custom_src_input_sizes = None, custom_target_input_sizes = None, is_src_grammar = True, depth = 2, target = "x86"):
        src_ctx = copy.deepcopy(src_expr)

        print(emit_compact_context_expr_str(src_ctx))

        relavent_output_subset = target_list
        print(relavent_output_subset)

        relavent_input_subset = self.get_relevant_dsl_list([src_ctx])
        input_subset_names = [i.name for i in relavent_input_subset]
        assert len(relavent_input_subset) != 0, "Atleast one AutoLLVM IR class expected for src language"
        relavent_dsl_subset = relavent_input_subset + [t for t in target_list if t.name not in input_subset_names]
        print(relavent_dsl_subset)


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

        statements = []


        statements += additional_statements

        # Need to create a new desc for swizzles and target inst comined
        double_grammar_desc = create_synth_desc("double_target_", True, [], "", "")
        double_grammar_desc.emit_sema = True
        double_grammar_desc.emit_interpreter = True

        target_language_dsl =  relavent_output_subset
        src_language_dsl = relavent_input_subset

        if double_grammar_desc.emit_interpreter:
            statements.append(double_grammar_desc.emit_interpreter_framework(relavent_dsl_subset))

        if self.force_contains_all_regs:
            statements.append(self.contains_reg_def.emit_contains(relavent_dsl_subset ,self.struct_def))

        num_src_regs = len(src_ctx_regs)

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


        for idx, prec in enumerate(input_precs):
            min_prec = min(prec, dst_input_sizes[idx])
            input_precs[idx] = min_prec

        print("Dst Output Size:", dst_output_size)
        print("Dst Input Sizes:", dst_input_sizes)
        print("Dst Input Precs:", input_precs)


        if len(dst_input_sizes) == 0:
            return False , "", ""


        GrammarGeneratorSrc = EqClassExpandGenerator(dsl_list = relavent_dsl_subset  , output_bitwidth = src_output_size, input_sizes = src_input_sizes, input_precs = input_precs, use_any_reg = self.use_any_reg)

        src_expression_label ,src_expression_grammar =  GrammarGeneratorSrc.emit_grammar(src_ctx, prefix = "src")

        if is_src_grammar:
            statements.append(src_expression_grammar)
            src_expression = "(define src-expr\n ({})\n)".format(src_expression_label)
            statements.append(src_expression)
        else:
            src_expression = "(define src-expr\n'()\n)"
            statements.append(src_expression)

        dst_expression_label = None

        TARGET = target
        spec = get_hydride_spec_from_ctx(src_ctx)
        spec.set_target(TARGET)
        spec.input_precision = [16,16]
        spec.input_shapes = [[1,16], [1,16]]
        # Use Hydride heurstic based synthesis for Destination but
        # expanded grammar for Src expression

        #GrammarGeneratorDst = StepWiseSynthesizer(spec = spec, dsl_operators =target_language_dsl , grammar_generator = TypedSimpleGrammarGenerator(), contexts_per_dsl_inst = 2, depth = depth, target = TARGET, step = 0, scale_factor =1)

        print(target_language_dsl)
        GrammarGeneratorDst = AllInstructionsSynthesizer(spec = spec, dsl_operators =target_language_dsl , grammar_generator = TypedSimpleGrammarGenerator(), contexts_per_dsl_inst = 20, depth = depth, target = TARGET, step = 0, scale_factor =1)
        dst_expression_grammar_tree = GrammarGeneratorDst.emit_synthesis_grammar(main_grammar_name = "dst-grammar-wrapper")
        statements.append(dst_expression_grammar_tree)

        dst_expression_label = "dst-grammar-depth-{}".format(depth)

        dst_grammar_def = "(define ({}) (dst-grammar-wrapper {}))".format(dst_expression_label, depth)
        statements.append(dst_grammar_def)







        if not invoke_ref_custom is None:
            decl , defn = invoke_ref_custom(double_grammar_desc.interpreter_name)
            statements.append(defn)
        else:
            statements.append(self.get_invoke_spec(spec_name = "src-expr", interpret_name = double_grammar_desc.interpreter_name, num_regs = num_src_regs))

        if not invoke_ref_lane_custom is None:
            decl , defn = invoke_ref_lane_custom(double_grammar_desc.interpreter_name)
            statements.append(defn)
        else:
            statements.append(self.get_invoke_spec_lane(spec_name = "src-expr", output_prec = src_ctx.out_precision, interpret_name = double_grammar_desc.interpreter_name, num_regs = num_src_regs))

        statements.append("(define optimize? #t)")

        statements.append("(define symbolic? #f)")

        if not invoke_target_custom  is None:
            interpret_def_name, interpret_def = invoke_target_custom(double_grammar_desc.interpreter_name)
            statements.append(interpret_def)
            statements.append("(define interpreter {})".format(interpret_def_name))
        else:
            statements.append("(define interpreter {})".format(double_grammar_desc.interpreter_name))

        statements.append("(define cost-model {})".format(double_grammar_desc.cost_name))
        leaves_sizes_vals = [str(arg.size) for arg in src_ctx_regs]
        if not custom_src_input_sizes is None:
            leaves_sizes_vals = [str(size) for size in custom_src_input_sizes]
        leaves_sizes = "(define leaves-sizes (list {}))".format(" ".join(leaves_sizes_vals))
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

        #print("\n".join(statements))
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
