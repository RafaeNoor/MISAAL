import common.Types
import sys
import time
from common.Types import *
from  common.Instructions import Context
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
        self.target_language = src_language
        self.bidirectional = bidirectional

    def set_name(name):
        self.name = name







