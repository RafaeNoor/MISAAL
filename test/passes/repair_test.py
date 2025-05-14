from utils.PassPipelineUtils import MISAAL_PASS_PIPELINE
from passes.CommutativePass import CommutativePass
from passes.ComputeOnlyRelevancePass import ComputeOnlyRelevancePass
from common.DSLParser import parse_dict
from utils.CodeSynthesizerDesc import X86_SYNTH_DESC, HALIDE_FOLDED_SYNTH_DESC
from sema.x86SemanticsAllArgs import semantcs as x86_semantics
from sema.halide_folded_full import halide_folded_full as halide_semantics
import sys
import os




if __name__ == "__main__":
    halide_dsl_list = parse_dict(halide_semantics)
    x86_dsl_list = parse_dict(x86_semantics)

    # Get subset of halide and x86 instructions for addition operations
    halide_add_insts = [h for h in halide_dsl_list if "vec-add" in h.name]
    x86_add_insts = [x for x in x86_dsl_list if "add_pi8" in x.name]



    # Create a pass pipeline with the CommutativePass
    CUR_DIR = os.path.dirname(os.path.abspath(__file__))
    test_working_dir = os.path.join(CUR_DIR, "work")
    pass_pipeline = MISAAL_PASS_PIPELINE([CommutativePass, ComputeOnlyRelevancePass], working_directory=test_working_dir, 
                                         log_file=os.path.join(test_working_dir, "log.txt"),  
                                         src_dsl_list=halide_add_insts, src_synth_desc=HALIDE_FOLDED_SYNTH_DESC, parallelize = True,
                                         pool=8, batch_size=1024,
                                         target_dsl_list=x86_add_insts, target_synth_desc=X86_SYNTH_DESC, stop_after_exception = True)

    # Run the pass pipeline on the test instruction dictionary
    ok = pass_pipeline.execute_pass_pipeline()

    if ok:
        sys.exit(0)
    else:
        sys.exit(1)
