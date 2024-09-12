import common.Types
import sys
import time
from common.Types import *
from  common.Instructions import Context
from utils.ReadDSL import read_string_to_dsl
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

        self.src_language = src_language
        self.target_language = target_language
        self.bidirectional = bidirectional

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




def parse_pattern_from_string(from_pattern, to_pattern, src_dsl_list, target_dsl_list, bidirectional = True, src_language = None, target_language = None):
    input_expr = read_string_to_dsl(from_pattern, src_dsl_list)
    output_expr = read_string_to_dsl(to_pattern, target_dsl_list)

    return Pattern(input_expr, output_expr, src_dsl_list = src_dsl_list, target_dsl_list = target_dsl_list, bidirectional = bidirectional, src_language = src_language, target_language = target_language)







