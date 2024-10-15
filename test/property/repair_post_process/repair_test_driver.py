import json
from common.DSLParser import parse_dict
from common.StructDef import StructDef
from utils.ReadDSL import read_string_to_dsl
from utils.DSLInstructionUtils import *
from properties.RepairRelavancePostProcess import RepairRelavancePostProcess
from utils.RepairPostProcessUtils import  RepairPostProcessUtils
from utils.CodeSynthesizerDesc import create_synth_desc
import os
import sys

# Python dictionaries for semantics
from sema.x86SemanticsAllArgs import semantcs as x86_semantics
from sema.repairs_sema import repair_semantics
from sema.halide_sema import halide_semantics


# Uncomment below line to keep intermediate racket files
# keep_temporary_files()

# Parse the dictionay into a list of DSLInstruction types
x86_dsl_list = parse_dict(x86_semantics)
repair_dsl_list = parse_dict(repair_semantics)
halide_dsl_list = parse_dict(halide_semantics)

combined_dsl_list = x86_dsl_list + repair_dsl_list + halide_dsl_list

synth_desc = create_synth_desc("post", True, [], "", "")
const_fold_name = synth_desc.const_fold_name
sd = StructDef(emit_default = False)


racket_bool_map = {"#f": False , "#t": True}





version = "test"
repair_memo_name = "test_x86.json"

if not os.path.exists(repair_memo_name):
    repair_memo_name = None
    assert False

PropertyInstance = RepairRelavancePostProcess(input_dsl_list = x86_dsl_list ,output_dsl_list = halide_dsl_list, repair_dsl_list = repair_dsl_list, memo_path = repair_memo_name , target = "x86", base_name = "VERSION_{}".format(version))

property_map = PropertyInstance.get_property()

print(json.dumps(property_map, indent = 4))
