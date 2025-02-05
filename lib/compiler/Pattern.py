import common.Types
import sys
import time
from common.Types import *
from  common.Instructions import Context
from utils.ReadDSL import read_string_to_dsl
from utils.EggLogUtils import is_birewrite_valid
from utils.DSLInstructionUtils import *
from sema.integer_arith_sema import integer_arith_sema_dict
import subprocess
import os
import tempfile
import glob


class Pattern:

    def __init__(self, src_expr, target_expr, src_dsl_list = [] , target_dsl_list = [], name = "pattern", src_language = None, target_language = None, bidirectional = True):
        self.src_expr = src_expr
        self.target_expr = target_expr
        self.src_dsl_list = src_dsl_list
        self.target_dsl_list = target_dsl_list
        self.name = name
        self.integer_arith_sema = parse_dict(integer_arith_sema_dict)

        self.src_language = src_language
        self.target_language = target_language
        self.bidirectional = bidirectional

    def get_pattern_depth(self):
        return max(get_expr_depth(self.src_expr), get_expr_depth(self.target_expr))

    def swap(self):
        src_expr = self.src_expr
        target_expr = self.target_expr
        src_dsl_list = self.src_dsl_list
        target_dsl_list = self.target_dsl_list
        src_language = self.src_language
        target_language = self.target_language

        self.src_expr = target_expr
        self.src_dsl_list = target_dsl_list
        self.src_language = target_language


        self.target_expr = src_expr
        self.target_dsl_list = src_dsl_list
        self.target_language = src_language


    def get_pattern_eq_classes(self):
        self.integer_arith_sema = parse_dict(integer_arith_sema_dict)
        dsl_list = self.src_dsl_list + self.target_dsl_list + self.integer_arith_sema
        expr_names = get_ctx_expr_dsl_names(self.src_expr, dsl_list)
        expr_names += get_ctx_expr_dsl_names(self.target_expr, dsl_list)
        return list(set(expr_names))

    def does_pattern_contain_eq_class(self, dsl_list_names):
        self.integer_arith_sema = parse_dict(integer_arith_sema_dict)
        dsl_list = self.src_dsl_list + self.target_dsl_list + self.integer_arith_sema
        expr_names = get_ctx_expr_dsl_names(self.src_expr, dsl_list)
        expr_names += get_ctx_expr_dsl_names(self.target_expr, dsl_list)
        expr_names =  list(set(expr_names))

        for dsl_list_name in dsl_list_names:
            if dsl_list_name in expr_names:
                return True
        return False



    def set_name(name):
        self.name = name
    def print_pattern(self):
        print("=*="*25)
        print("Name:\t", self.name)
        print("Src Lang:\t", self.src_language)
        print("Target Lang:\t", self.target_language)
        print("Bidirectional:\t", self.bidirectional)

        from_expr_str = self.src_expr.emit_context_expr_string()
        target_expr_str = self.target_expr.emit_context_expr_string()

        print("From Expression:")
        print(from_expr_str)

        print("To Expression:")
        print(target_expr_str)

    def equal_to(self, other_pattern):
        def get_expr_str(expr):
            if isinstance(expr,Context):
                return expr.emit_context_expr_string()
            else:
                return "Reg"

        srq_equal_src = get_expr_str(other_pattern.src_expr) == get_expr_str(self.src_expr)
        dst_equal_dst = get_expr_str(other_pattern.target_expr) == get_expr_str(self.target_expr)

        equal_forward = srq_equal_src and dst_equal_dst

        if equal_forward:
            return True

        src_equal_dst = get_expr_str(other_pattern.src_expr) == get_expr_str(self.target_expr)
        dst_equal_src = get_expr_str(other_pattern.target_expr) == get_expr_str(self.src_expr)


        equal_backward = src_equal_dst and dst_equal_src


        return equal_forward or equal_backward






def parse_pattern_from_string(from_pattern, to_pattern, src_dsl_list, target_dsl_list, bidirectional = True, src_language = None, target_language = None):
    input_expr = read_string_to_dsl(from_pattern, src_dsl_list)
    output_expr = read_string_to_dsl(to_pattern, target_dsl_list)

    bidirectional = bidirectional and is_birewrite_valid(input_expr, output_expr)

    return Pattern(input_expr, output_expr, src_dsl_list = src_dsl_list, target_dsl_list = target_dsl_list, bidirectional = bidirectional, src_language = src_language, target_language = target_language)







