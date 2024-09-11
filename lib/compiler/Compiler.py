from utils.DSLInstructionUtils import *
import sys
import time
from common.Types import *
from  common.Instructions import Context
import subprocess
import os
import tempfile
import glob


class CompilerBase:

    def __init__(self, patterns, src_dsl_list = [], target_dsl_list = []):
        self.patterns = patterns
        self.src_dsl_list = src_dsl_list
        self.target_dsl_list = target_dsl_list

        # Each AutoLLVM IR operation will need to be
        # represented using some data structure.
        # class_map represents the data structure for that.
        self.class_map = {}
        self.lit_class = None
        self.reg_class = None

    def initialize_class_map(self):
        raise NotImplementedError()

    def initialize_lit_class(self):
        raise NotImplementedError()

    def initialize_reg_class(self):
        raise NotImplementedError()

    def emit_pattern_matching_based_compiler(self):
        raise NotImplementedError()

    def convert_reg_to_compiler_datastructure(self, expr_regs):
        raise NotImplementedError()

    def compile_expr(self, expr):
        self.initialize_class_map()
        self.initialize_lit_class()
        self.initialize_reg_class()

        expr_regs = get_context_registers(expr)

        reg_data_structures = self.convert_reg_to_compiler_datastructure(expr_regs)

        compiler_functionality = self.emit_pattern_matching_based_compiler()

        compiled_expr = self.apply_rewrite(expr, compiler_functionality, reg_data_structures)

        return compiled_expr





    def apply_rewrite(self, expr, compiler_functionality, reg_data_structures):
        raise NotImplementedError()







