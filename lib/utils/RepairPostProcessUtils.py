from common.Instructions import DSLInstruction
from common.Types import *
from common.PredefinedDSL import *


class RepairPostProcessUtils:

    def __init__(self, test_name = "autollvm_ir_class", env_sizes = [], const_fold_name = "post:const-fold", use_prepared_env_name = None, prepare_env_sizes = []):

        self.const_fold = True
        self.test_name = test_name
        self.env_sizes = env_sizes
        self.repair_wrapper_name = "repair-wrapper"
        self.const_fold_name = const_fold_name
        self.use_prepared_env_name = use_prepared_env_name
        self.prepare_env_sizes = prepare_env_sizes


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
            sym_idxs = self.get_all_possible_symbolic_indices(dsl_inst)

            sym_env_names = []



            or_conditions = []
            and_conditions = []
            for counter, idx in enumerate(sym_idxs):
                arg = sample_ctx.context_args[idx]
                sym_env_name = "sym-env-" + arg.name
                if self.use_prepared_env_name is None:
                    sym_env = "(define {} (vector {}))".format(sym_env_name, " ".join(["(?? (bitvector {}))".format(size) for size in self.env_sizes]))
                else:
                    sym_env = "(define {} ({} (vector {})))".format(sym_env_name, self.use_prepared_env_name ," ".join(["(?? (bitvector {}))".format(size) for size in self.prepare_env_sizes]))

                sym_env_names.append(sym_env_names)
                fold_defs.append(sym_env)

                # Interpret the prog and other arguments

                interpret_prog_name = "prog-interpreted-{}".format(arg.name)
                interpret_prog = "(define {} ({} prog {}))".format(interpret_prog_name ,interpret_name, sym_env_name)

                fold_defs.append(interpret_prog)

                all_non_eq_clauses = []
                equal_arg_clauses = []
                for inner_idx in sym_idxs:
                    inner_arg = sample_ctx.context_args[inner_idx]
                    exec_arg = "({} {} {})".format(interpret_name, inner_arg.name, sym_env_name)
                    exec_arg_name = "{}-interpreted-{}".format(inner_arg.name, arg.name)
                    def_arg = "(define {} {})".format(exec_arg_name, exec_arg)

                    fold_defs.append(def_arg)

                    clause = ""
                    if inner_idx == idx:
                        clause = "(equal? {} {})".format(interpret_prog_name, exec_arg_name)
                    else:
                        clause = "(not (equal? {} {}))".format(interpret_prog_name, exec_arg_name)

                    equal_arg_clauses.append(clause)


                    if counter == 0:
                        # Use first iteration to add case where it's not equal to any of the inputs (while not being concrete)
                        all_non_eq_clauses.append("(not (equal? {} {}))".format(interpret_prog_name, exec_arg_name))



                and_conditions.append("(and {})".format(" ".join(equal_arg_clauses)))

                if counter == 0:
                    or_conditions.append("(and (not (concrete? {})) {})".format(interpret_prog_name," ".join(all_non_eq_clauses)))

                    # Add always concrete literal value
                    always_conc_clause = "[(is-always-concrete {}) #f]".format(interpret_prog_name)
                    other_clauses.append(always_conc_clause)



            and_clause = "(and\n {})".format("\n".join(and_conditions))

            or_conditions.append(and_clause)

            passing_clause = "(or \n{})".format("\n".join(or_conditions))

            other_clauses.append("[{} \n #t]".format(passing_clause))





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

        always_conc_def = self.emit_is_concrete_def()
        main_wrapper = self.emit_main_wrapper(repair_post_process_name)
        return prefix + always_conc_def+ "\n" + interpreter + "\n" + main_wrapper + sufix

    def emit_main_wrapper(self, repair_post_process_name = ""):
        return """
        (define ({} expr)
            (define condition ({} src-expr))
            (cond
                [(concrete? condition) condition]
                [else
                      (define sol
                        (synthesize
                          #:forall (list )
                          #:guarantee (assert condition)
                          )

                        )
                      (println sol)
                      (sat? sol)
                ]
            )
        )
        """.format(self.repair_wrapper_name, repair_post_process_name)


    def emit_check_property(self, expr_name):

        expr = expr_name
        if self.const_fold:
            expr = "({} {})".format(self.const_fold_name, expr)

        return "({} {})".format(self.repair_wrapper_name, expr)

    def emit_is_concrete_def(self):
        return """
        (define (is-always-concrete v)
          (cond
            [(concrete? v)
             #t
             ]
            [else

              (define len (bvlength v))
              (define hole (?? (bitvector len)))

              (define eval-condition (equal? v hole))
              (define sol
                (synthesize
                  #:forall (list v)
                  #:guarantee (assert eval-condition)
                  )
                )
              (sat? sol)

              ]

            )
          )
        """



# For frontends such as Halide, we often have to split vectors and concatenate vectors at different stages
# of the expression. To create the identities required to do so, we first create an identity repair map
# with expressions which extract/ concat slices and the operations themselves. This repair map can be used to derive
# such properties
def create_repair_identity_map(dsl_list, include_self = True):
    legal_bv_ops = ["extract", "concat"]
    extract_concat_dsl_list = []

    for dsl_inst in dsl_list:
        dsl_ops = dsl_inst.get_semantics_ops_list()

        valid = True
        for op in dsl_ops:
            if op not in legal_bv_ops:
                valid = False
                break

        if valid:
            extract_concat_dsl_list.append(dsl_inst)

    repair_identity_map = {}

    for dsl_inst in dsl_list:
        repair_identity_map[dsl_inst.name] = []

        repair_identity_map[dsl_inst.name].append(dsl_inst.name)

        for extract_op in extract_concat_dsl_list:
            repair_identity_map[dsl_inst.name].append(extract_op.name)
        repair_identity_map[dsl_inst.name] = list(set(repair_identity_map[dsl_inst.name]))

        if not include_self:
            repair_identity_map[dsl_inst.name] = [x for x in repair_identity_map[dsl_inst.name] if x != dsl_inst.name]


    return repair_identity_map


def create_repair_swizzle_map(dsl_list, swizzle_list):
    legal_bv_ops = ["extract", "concat", "sign-extend", "zero-extend", "bvssat", "bvusat"]
    extract_concat_dsl_list = []

    for dsl_inst in dsl_list:
        dsl_ops = dsl_inst.get_semantics_ops_list()

        valid = True
        for op in dsl_ops:
            if op not in legal_bv_ops:
                valid = False
                break

        sample_ctx = dsl_inst.get_sample_context()

        if sample_ctx.out_vectsize is None:
            valid = False

        if valid:
            extract_concat_dsl_list.append(dsl_inst.name)

    repair_swizzle_map = {}



    for swizzle in swizzle_list:
        repair_swizzle_map[swizzle.name] = extract_concat_dsl_list



    return repair_swizzle_map

