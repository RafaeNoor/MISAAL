from compiler.Compiler import *
import egglog


# Compiler using the EggLog DSL for applying rewrites using the python bindings

class EggLogPyCompiler(CompilerBase):

    def __init__(self, patterns, src_dsl_list = [], target_dsl_list = []):
        super().__init__(patterns, src_dsl_list = src_dsl_list, target_dsl_list = target_dsl_list)


