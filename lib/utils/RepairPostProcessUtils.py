from common.Instructions import DSLInstruction
from common.Types import *
from common.PredefinedDSL import *


class RepairPostProcessUtils:

    def __init__(self, test_name = "autollvm_ir_class", env_sizes = []):
        self.test_name = test_name
        self.env_sizes = env_sizes
        self.repair_wrapper_name = "repair-wrapper"


    def emit_default_def(self, struct_definer,  repair_post_process_name="hydride:repair-post-process", interpret_name="hydride:interpret"):
        defaults = []

        defaults.append("[(reg id) #f ]")
        defaults.append("[(buffer-index id type size) #f ]")

        defaults.append("[(lit v) #f]")


        for structs in default_structs:
            defaults.append(self.emit_repair_post_process_def(structs, struct_definer,
                            repair_post_process_name=repair_post_process_name, interpret_name=interpret_name)[1:])

        return ["\t{}".format(d) for d in defaults]

    def emit_fallback_def(self):
        return "\t[v (error \"Unrecognized expression\" v)]"

    def emit_is_lit(self, val):
        return "(lit? {})".format(val)

    def emit_repair_expr(self, expr, repair_post_process_name="hydride:repair-post-process"):
        folded_name = expr + "-repaired-post"
        definition = "(define {} ({} {}))".format(
            folded_name, repair_post_process_name, expr)
        return (folded_name, definition)

    def emit_all_lit(self, vals):
        return "(and "+" ".join([self.emit_is_lit(val) for val in vals]) + ")"

    def emit_repair_post_process_def(self, dsl_inst, struct_definer, repair_post_process_name="hydride:repair-post-process", interpret_name="hydride:interpret"):

        self.repair_post_process_name = repair_post_process_name
        interpret = [struct_definer.emit_dsl_struct_use(dsl_inst)]

        fold_subexpr = []
        fold_defs = []

        sample_ctx = dsl_inst.get_sample_context()

        for idx, arg in enumerate(sample_ctx.context_args):

            if isBitVectorType(arg):
                (folded_name, definition) = self.emit_repair_expr(
                    arg.name, repair_post_process_name=repair_post_process_name)

                fold_subexpr.append(folded_name)
                fold_defs.append(definition)


        any_folded_clauses = "[(or {}) #t]".format(" ".join(fold_subexpr))

        other_clauses = []

        else_clause = "[else #f]"

        if dsl_inst.name == self.test_name:
            # Only test conditions for this equivlance class
            else_clause = "[else #t]"
            sym_idxs = self.get_all_possible_symbolic_indices(dsl_inst)

            # Add result of interpreting operands and current expression to definitions outside of cond

            sym_env_name = "sym-env"
            sym_env = "(define {} (vector {}))".format(sym_env_name, " ".join(["(?? (bitvector {}))".format(size) for size in self.env_sizes]))
            fold_defs.append(sym_env)

            interpreted_args = []

            for idx in sym_idxs:
                arg = sample_ctx.context_args[idx]
                exec_arg = "({} {} {})".format(interpret_name, arg.name, sym_env_name)
                exec_arg_name = "{}-interpreted".format(arg.name)
                def_arg = "(define {} {})".format(exec_arg_name, exec_arg)

                fold_defs.append(def_arg)
                interpreted_args.append(exec_arg_name)

            interpret_expr_name = "interpret-prog"
            interpret_expr = "({} {} {})".format(interpret_name, "prog", sym_env_name)
            interpret_expr_def = "(define {} {})".format(interpret_expr_name, interpret_expr)

            fold_defs.append(interpret_expr_def)


            # Condition 1: If the return type of the expression is equivalent to all input operands
            pairs = ["(equal? {} {})".format(interpret_expr_name, interpret_arg) for interpret_arg in interpreted_args]
            all_equal_cond = "[(and {}) #f]".format(" ".join(pairs))
            other_clauses.append(all_equal_cond)

            # Condition 2: Produces a concrete (i.e. constant) value for when interpreted with symbolic inputs
            is_concrete = "[(concrete? {}) #f]".format(interpret_expr_name)
            other_clauses.append(is_concrete)

            # Condition 3: If it is equal to any of the operands always
            for pair in pairs:
                condition = "[{} #f]".format(pair)
                other_clauses.append(condition)





        interpret += fold_defs

        interpret.append("(cond")
        interpret.append(any_folded_clauses)
        interpret += other_clauses
        interpret.append(else_clause)
        interpret.append(")")

        return "\t[ {}\n\t]".format("\n\t\t".join(interpret))

    def get_all_possible_symbolic_indices(self, dsl_inst):
        sample_ctx = dsl_inst.get_sample_context()

        mask = [True] * len(sample_ctx.context_args)

        for ctx in dsl_inst.contexts:
            for idx, arg in enumerate(ctx.context_args):
                if not isinstance(arg, BitVector):
                    mask[idx] = False
        indices = []

        for idx, val in enumerate(mask):
            if val:
                indices.append(idx)

        return indices

    def emit_repair_post_process(self, dsl_inst_ls, struct_definer, repair_post_process_name="hydride:repair-post-process", interpret_name="hydride:interpret"):

        interpret_clauses = self.emit_default_def(
            struct_definer, repair_post_process_name=repair_post_process_name, interpret_name=interpret_name)
        interpret_clauses += [self.emit_repair_post_process_def(
            dsl_inst, struct_definer, repair_post_process_name=repair_post_process_name, interpret_name=interpret_name) for dsl_inst in dsl_inst_ls]
        interpret_clauses.append(self.emit_fallback_def())

        prefix = ";; "+"="*80 + "\n"
        prefix += ";; "+" "*30 + " DSL Repair Post Process Expression"+'\n'
        prefix += ";; "+"="*80 + "\n"

        sufix = "\n;; "+"="*80 + "\n"

        interpreter = "(define ({} prog )\n (destruct prog\n{}\n )\n)".format(
            repair_post_process_name, "\n".join(interpret_clauses))

        main_wrapper = self.emit_main_wrapper(repair_post_process_name)
        return prefix + interpreter + "\n" + main_wrapper + sufix

    def emit_main_wrapper(self, repair_post_process_name = ""):
        return """
        (define ({} expr)
            (define condition ({} src-expr))
            (cond
                [(concrete? condition) condition]
                [else
                    (define cex (verify (assert (not condition))))
                    (sat? cex)
                ]
            )
        )
        """.format(self.repair_wrapper_name, repair_post_process_name)


    def emit_check_property(self, expr_name):
        return "({} {})".format(self.repair_wrapper_name, expr_name)
