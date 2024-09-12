from compiler.Compiler import *
from utils.EggLogUtils import *
import subprocess as sb

# Compiler using the EggLog DSL for applying rewrites

class EggLogCompiler(CompilerBase):

    def __init__(self, patterns, src_dsl_list = [], target_dsl_list = [], run_iterations = 10, egg_file_name = None, egg_pkg_path = None):
        super().__init__(patterns, src_dsl_list = src_dsl_list, target_dsl_list = target_dsl_list)
        self.egg_pkg_path = egg_pkg_path
        self.input_cost = 100
        self.output_cost = 1
        self.run_iterations = run_iterations
        if egg_file_name is None:
            egg_file_name = "temp.egg"
        self.egg_file_name = egg_file_name

    def initialize_class_map(self):
        pass

    def initialize_lit_class(self):
        pass

    def initialize_reg_class(self):
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


    def execute_cmd(self, cmd, cur_dir = None):
        if cur_dir is None:
            print("$[ Egg Compiler ]: "," ".join(cmd))
            sb.run(" ".join(cmd), shell = True)
        else:
            print("$[ Egg Compiler: {} ]: ".format(cur_dir)," ".join(cmd))
            sb.run(" ".join(cmd), shell = True, cwd = cur_dir)


    def execute_egglog_file(self, fname):
        # Work around until I figure out how to execute outside of pkg directory
        example_path = os.path.join(self.egg_pkg_path, "example")

        cp_to_example_cmd = ["cp", fname, example_path]
        self.execute_cmd(cp_to_example_cmd)

        target_egg_file = os.path.join(example_path, fname)
        exec_cmd = ["cargo", "run" , target_egg_file]

        self.execute_cmd(exec_cmd, cur_dir = self.egg_pkg_path)



    def apply_rewrite(self, expr, compiler_functionality, reg_data_structures):

        statements = []

        statements.append(compiler_functionality)
        statements += [defn for label, defn in reg_data_structures]


        src_expr_name = "srcexpr"
        src_expr_egg = emit_expr_to_egg(expr)
        define_src_expr = emit_egg_define_var(src_expr_name, src_expr_egg)
        statements.append(define_src_expr)

        statements.append(emit_egg_run_iter(self.run_iterations))

        statements.append(emit_egg_extract_expr(src_expr_name))

        print("Creating egg file:\t", self.egg_file_name)

        with open(self.egg_file_name, "w+") as EggFile:
            EggFile.write("\n".join(statements))

        self.execute_egglog_file(self.egg_file_name)

        return expr




