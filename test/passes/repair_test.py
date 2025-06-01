import unittest
import logging
from utils.PassPipelineUtils import MISAAL_PASS_PIPELINE
from passes.CommutativePass import CommutativePass
from passes.ComputeOnlyRelevancePass import ComputeOnlyRelevancePass
from common.DSLParser import parse_dict
from utils.CodeSynthesizerDesc import X86_SYNTH_DESC, HALIDE_FOLDED_SYNTH_DESC
from sema.x86SemanticsAllArgs import semantcs as x86_semantics
from sema.halide_folded_full import halide_folded_full as halide_semantics
import os


class TestRepairPass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up logging configuration
        CUR_DIR = os.path.dirname(os.path.abspath(__file__))
        log_file = os.path.join(CUR_DIR, "repair_test.log")
        
        # Configure logging to write to file
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            filename=log_file,
            filemode='w'
        )
        
        # Create a logger for this test
        cls.logger = logging.getLogger('RepairTest')

    def setUp(self):
        self.halide_dsl_list = parse_dict(halide_semantics)
        self.x86_dsl_list = parse_dict(x86_semantics)

        # Get subset of halide and x86 instructions for addition operations
        self.halide_add_insts = [h for h in self.halide_dsl_list if "vec-add" in h.name]
        self.x86_add_insts = [x for x in self.x86_dsl_list if "add_pi8" in x.name]

        # Setup working directory
        CUR_DIR = os.path.dirname(os.path.abspath(__file__))
        self.test_working_dir = os.path.join(CUR_DIR, "work")
        self.logger.info(f"Working directory set to: {self.test_working_dir}")

    def test_repair_pass_execution(self):
        self.logger.info("Starting repair pass execution test")
        
        # Create a pass pipeline with the CommutativePass
        pass_pipeline = MISAAL_PASS_PIPELINE(
            [CommutativePass, ComputeOnlyRelevancePass], 
            working_directory=self.test_working_dir,
            log_file=os.path.join(self.test_working_dir, "pipeline.log"),
            src_dsl_list=self.halide_add_insts,
            src_synth_desc=HALIDE_FOLDED_SYNTH_DESC,
            parallelize=False,
            pool=8,
            batch_size=1024,
            target_dsl_list=self.x86_add_insts,
            target_synth_desc=X86_SYNTH_DESC,
            stop_after_exception=True
        )

        # Run the pass pipeline and check if it succeeds
        result = pass_pipeline.execute_pass_pipeline()
        self.logger.info(f"Pass pipeline execution {'succeeded' if result else 'failed'}")
        self.assertTrue(result, "Pass pipeline execution failed")


if __name__ == "__main__":
    unittest.main()
