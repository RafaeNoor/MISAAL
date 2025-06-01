from properties.Property import *
import os
import time
import glob
import pickle
from properties.EqClassEqualDepthV4 import EqClassEqualDepthV4
import random
import sys
import json
from  utils.DSLInstructionUtils import *
from utils.GenerateRandomExpr import create_random_expression
from utils.CodeSynthesizerDesc import *
from utils.CanonicalizeExpressions import CanonicalizeExpression
import copy
from  common.Types import *
import itertools
import numpy as np
from grammar_gen.EqClassExpandGenerator import EqClassExpandGenerator
from utils.DoubleGrammarSynthesisUtils import DoubleGrammarSynthesisUtils
from utils.EnumerateUtils import *
from utils.ConcretizeUtils import *
import gc

# Version of EqClassEqualDepthV4 where the repair map is the entire DSL List
class EqClassEqualDepthV4Full(EqClassEqualDepthV4):

    def __init__(self, dsl_list = [], source_synth_desc = None, target_synth_desc = None, target_dsl_list = [], output_depth = 1, forward_map_path = None, swizzle_dsl_list = [], swizzle_map_path = None, commutative_map_path = None, input_depth = 2, depth_range = False, use_canon_map = True, start_input_depth = 1, start_output_depth =1, bidirectional_test = False, filter_list = None):

        with open("empty_file.json", "w+") as EmptyFile:
            EmptyFile.write("{}\n")
        super().__init__(dsl_list = dsl_list,  source_synth_desc = source_synth_desc, target_synth_desc = target_synth_desc, output_depth = output_depth, forward_map_path = "empty_file.json", swizzle_dsl_list = swizzle_dsl_list, swizzle_map_path = "empty_file.json", commutative_map_path = commutative_map_path, input_depth = input_depth, depth_range = depth_range, use_canon_map = use_canon_map, start_input_depth = start_input_depth, start_output_depth =start_output_depth, bidirectional_test = bidirectional_test, filter_list = filter_list, target_dsl_list = target_dsl_list)
        self.name = "EqClassEqualDepthV4Full"


    def get_relavent_swizzle_dsl_subset(self, dsl_inst):
        return []


    def get_relavent_output_dsl_subset(self, dsl_inst):
        return self.output_dsl_list





