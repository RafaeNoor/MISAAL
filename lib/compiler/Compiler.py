from utils.DSLInstructionUtils import *
from utils.LiteralHole import LiteralHole
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
        self.target_dsl_list = target_dsl_list + [LiteralHole]

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

    def emit_pattern_matching_based_compiler(self, expr, swizzle_cost = 1):
        raise NotImplementedError()

    def convert_reg_to_compiler_datastructure(self, expr_regs):
        raise NotImplementedError()

    def get_unique_registers(self, expr_regs):
        included = []
        pruned_regs = []
        for reg in expr_regs:
            if reg.index in included:
                continue
            pruned_regs.append(reg)
            included.append(reg.index)
        return pruned_regs


    def compile_expr(self, expr):
        self.initialize_class_map()
        self.initialize_lit_class()
        self.initialize_reg_class()

        expr_regs = get_context_registers(expr)
        expr_regs = self.get_unique_registers(expr_regs)




        reg_data_structures = self.convert_reg_to_compiler_datastructure(expr_regs)

        compiler_functionality = self.emit_pattern_matching_based_compiler(expr)

        compiled_expr = self.apply_rewrite(expr, compiler_functionality, reg_data_structures)

        return compiled_expr





    def apply_rewrite(self, expr, compiler_functionality, reg_data_structures):
        raise NotImplementedError()







