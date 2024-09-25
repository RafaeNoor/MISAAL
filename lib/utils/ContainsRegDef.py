from common.Instructions import DSLInstruction
from common.Types import *
from common.PredefinedDSL import default_structs



class ContainsRegDef:

    def __init__(self, contains_index_name = "reg_idx", contains_name = "contains_reg"):
        self.contains_index_name = contains_index_name
        self.contains_name = contains_name
        return

    def emit_reg_condition(self, idx_name = "id"):
        bv_cond = "(equal? (bitvector->natural {})  {})".format(idx_name, self.contains_index_name)
        int_cond = "(equal? {}  {})".format(idx_name, self.contains_index_name)
        condition = "(cond [(bv? {}) {} ] [else {}])".format(idx_name, bv_cond, int_cond)
        return condition

    def emit_default_def(self, struct_definer):

        defaults = []
        defaults.append("[(lit v) #f ]")
        defaults.append("[(reg id) {} ]".format(self.emit_reg_condition(idx_name = "id")))
        defaults.append("[(buffer-index id type size) {} ]".format(self.emit_reg_condition(idx_name = "id")))
        return ["\t{}".format(d) for d in defaults]

    def emit_dsl_contains_def(self, dsl_inst, struct_definer):

        clause = [struct_definer.emit_dsl_struct_use(dsl_inst)]



        sample_ctx = dsl_inst.get_sample_context()

        sub_clause = []
        for idx,arg in enumerate(sample_ctx.context_args):
            if isBitVectorType(arg):
                arg_contains = "({} {} {})".format(self.contains_name, arg.name, self.contains_index_name)
                sub_clause.append(arg_contains)

        condition = "(or {})".format("\n".join(sub_clause))

        clause.append(condition)







        return "\t[ {}\n\t]".format("\n\t\t".join(clause))


    def emit_fallback_def(self):
        return "\t[v  (error \"Unrecognized Term in contain reg\" v)]"

    def emit_contains(self, dsl_list, struct_definer):
        default_contains = self.emit_default_def(
            struct_definer)

        dsl_contains = [self.emit_dsl_contains_def(
            dsl_inst, struct_definer) for dsl_inst in dsl_list]

        contains_clauses = default_contains + dsl_contains + [self.emit_fallback_def()]


        prefix = ";; "+"="*80 + "\n"
        prefix += ";; "+" "*30 + " DSL Contains Reg Def"+'\n'
        prefix += ";; "+"="*80 + "\n"

        sufix = "\n;; "+"="*80 + "\n"

        contains_model = "(define ({} prog {})\n (destruct prog\n{}\n )\n)".format(
            self.contains_name, self.contains_index_name, "\n".join(contains_clauses))
        return prefix + contains_model + sufix
