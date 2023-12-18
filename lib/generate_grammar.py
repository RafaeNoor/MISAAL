import sys
import time
import json
import subprocess as sb
from common.DSLParser import parse_dict
#from LatestSemantics import semantcs
from  x86SemanticsAllArgs import semantcs

from common.PredefinedDSL import *
from common.StructDef import StructDef
from interpreter.InterpreterDef import InterpreterDef
from utils.CostDef import CostDef
from utils.GetLengthDef import GetLengthDef
from legal_insts import legal_map
from Specification import Specification, parse_spec
import argparse
import pathlib
from dynamic_imp import dynamic_imp, Dimport


from hexsemantics_new import semantics as hvx_semantics
from ARMSemantics import semantcs as arm_semantics


from grammar_generator.TypedSimpleGrammarGenerator import TypedSimpleGrammarGenerator

from synthesizer.Synthesizer import Synthesizer
from synthesizer.StepWiseSynthesizer import StepWiseSynthesizer
from synthesizer.AllInstructionsSynthesizer import AllInstructionsSynthesizer




parser = argparse.ArgumentParser(description='Generate grammar for synthesis')
parser.add_argument('--spec_name', type=pathlib.Path)
parser.add_argument('--output_path', type=pathlib.Path)
parser.add_argument('--VF', type=int)
parser.add_argument('--is_shuffle', type=int)
parser.add_argument('--scale_factor', type=int)
parser.add_argument('--step', type=int, default = 0)
parser.add_argument('--depth', type=int, default = 3)
parser.add_argument('--target_dict', type=pathlib.Path)
parser.add_argument('--dict_name', type=str)

# FIXME: Don't hardcore target settings
TARGET= "hvx"


args = parser.parse_args()


# Driver Code
print("Target dict path: ", str(args.target_dict))
module_path = str(args.target_dict)#.replace(".py", "").replace("/",".")


print("Module path: ", module_path)
target_sema = Dimport(module_path, args.dict_name)
dsl_list = parse_dict(target_sema.imported)




INPUT_SPEC_NAME = args.spec_name
OUTPUT_GRAMMAR_FILE = args.output_path
VF = args.VF
IS_SHUFFLE = (args.is_shuffle == 1)
SCALE_FACTOR = args.scale_factor

STEP= args.step
DEPTH=args.depth


sd = StructDef()
idd = InterpreterDef()
cd = CostDef()
gg = TypedSimpleGrammarGenerator()
gl = GetLengthDef(get_len_name = "get-length")



hydride_header = """;#============================== Hydride File =================================
;#
;# Part of the Hydride Compiler Infrastructure.
;# <Placeholder for license information>
;#
;#=============================================================================
;#
;# Do NOT modify this file. It is automatically generated.
;#
;#=============================================================================
"""

rosette_imports = """
#lang rosette
(require rosette/lib/synthax)
(require rosette/lib/angelic)
(require racket/pretty)
(require data/bit-vector)
(require rosette/lib/destruct)
(require rosette/solver/smt/boolector)
(require hydride)
(require misaal)


;(provide {}_grammar_operations)

(provide (all-defined-out))

"""

spec = {}

with open(INPUT_SPEC_NAME, "r") as InputFile:
    spec = json.load(InputFile)

with open(OUTPUT_GRAMMAR_FILE, "w+") as OutputFile:
    def write_to_file(line):
        OutputFile.write(line + "\n")

    sp = parse_spec(spec)

    sp.set_target(TARGET)


    write_to_file(rosette_imports.format(spec['name']))
    write_to_file(hydride_header)




    for dsl_inst in dsl_list:
        write_to_file(dsl_inst.get_semantics())


    write_to_file(sd.emit_struct_defs(dsl_list))



    syn_class =  [StepWiseSynthesizer, AllInstructionsSynthesizer][1]

    syn = syn_class(spec = sp, dsl_operators = dsl_list,
                  struct_definer = sd, grammar_generator = gg,
                  contexts_per_dsl_inst = 2,
                  vectorization_factor = VF,
                  depth = DEPTH,
                  is_shuffle = IS_SHUFFLE,
                  legal_map = legal_map,
                  target = TARGET,
                  step = STEP,
                  scale_factor = SCALE_FACTOR
                  )


    grammar_name = spec['name']

    write_to_file(syn.emit_synthesis_grammar(main_grammar_name = grammar_name, include_manual_swizzles = False))

    dsl_subset = syn.dsl_subset


    subset_interpreter = idd.emit_interpreter(dsl_subset, sd, add_assertions = False, interpret_name = grammar_name+":interpret")
    subset_cost_model = cd.emit_cost_model(dsl_subset, sd, cost_name = grammar_name+":cost", use_label = False)
    write_to_file(subset_interpreter)
    write_to_file(subset_cost_model)



