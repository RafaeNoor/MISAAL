from compiler.Compiler import *
from utils.EggLogUtils import *
import subprocess as sb

# Compiler using the EggLog DSL for applying rewrites

class EggLogCompiler(CompilerBase):

    def __init__(self, patterns, src_dsl_list = [], target_dsl_list = []):
        super().__init__(patterns, src_dsl_list = src_dsl_list, target_dsl_list = target_dsl_list)
        self.input_cost = 100
        self.output_cost = 1

    def initialize_class_map(self):
        pass

    def initialize_lit_map(self):
        pass

    def initialize_reg_map(self):
        pass


    def emit_pattern_matching_based_compiler(self):
        egglog_decls = emit_egg_datatypes_two_dsl(self.src_dsl_list, self.target_dsl_list, input_cost = self.input_cost, output_cost = self.output_cost)

        egglog_patterns = []
        for pattern in self.patterns:
            rewrite = emit_rewrite_expr(pattern.src_expr, pattern.target_expr, bidirectional = pattern.bidirectional)
            egglog_patterns.append(rewrite)


        egg_log_desc = "\n".join([egglog_decls] + egglog_patterns)
        return egg_log_desc


    def convert_reg_to_compiler_datastructure(self, expr_regs):
        return [emit_egg_define_reg(reg) for reg in expr_regs]


    def apply_rewrite(self, expr, compiler_functionality, reg_data_structures):

