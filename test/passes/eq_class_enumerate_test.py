import unittest
import logging
from utils.PassPipelineUtils import MISAAL_PASS_PIPELINE
from passes.AutoLLVMEnumerate import AutoLLVMEnumerate
from common.DSLParser import parse_dict
from utils.CodeSynthesizerDesc import X86_SYNTH_DESC, HALIDE_SYNTH_DESC
from sema.halide_folded_full import halide_folded_full as halide_semantics
from sema.x86SemanticsAllArgs import semantcs as x86_semantics
import os
import json


class TestAutoLLVMEnumerate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up logging configuration
        CUR_DIR = os.path.dirname(os.path.abspath(__file__))
        log_file = os.path.join(CUR_DIR, "eq_class_test.log")
        
        # Configure logging to write to file
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            filename=log_file,
            filemode='w'
        )
        
        # Create a logger for this test
        cls.logger = logging.getLogger('AutoLLVMEnumerateTest')

    def setUp(self):
        # Parse DSL lists
        self.halide_dsl_list = parse_dict(halide_semantics)
        self.x86_dsl_list = parse_dict(x86_semantics)

        # Get subset of instructions for testing
        # For Halide, we'll focus on vector operations
        self.halide_test_insts = [h for h in self.halide_dsl_list if "vec-sub" in h.name][:1]
        print(f"Number of Halide test instructions: {len(self.halide_test_insts)}")
        # For x86, we'll focus on vector subtraction instructions
        self.x86_test_insts = [x for x in self.x86_dsl_list if "sub" in x.name and "epi" in x.name][:1]
        print(f"Number of x86 test instructions: {len(self.x86_test_insts)}")

        # Setup working directory
        CUR_DIR = os.path.dirname(os.path.abspath(__file__))
        self.test_working_dir = os.path.join(CUR_DIR, "work")
        if not os.path.exists(self.test_working_dir):
            os.makedirs(self.test_working_dir)
        self.logger.info(f"Working directory set to: {self.test_working_dir}")

        # Create forward map from test instructions
        forward_map = {}
        for halide_inst in self.halide_test_insts:
            forward_map[halide_inst.name] = [x.name for x in self.x86_test_insts]
        
        # Save forward map to a temporary file
        self.forward_map_path = os.path.join(self.test_working_dir, "test_forward_map.json")
        with open(self.forward_map_path, "w+") as f:
            json.dump(forward_map, f, indent=2)

        # Check if file is created and non-empty
        self.assertTrue(os.path.exists(self.forward_map_path), "Forward map file was not created")
        self.assertGreater(os.path.getsize(self.forward_map_path), 0, "Forward map file is empty")

        # Setup pass configurations with only forward_map_path
        self.pass_configs = {
            "AutoLLVMEnumerate": [
                ("forward_map_path", self.forward_map_path)
            ]
        }

    def test_halide_to_x86_execution(self):
        """Test AutoLLVMEnumerate with Halide IR to x86 translation"""
        self.logger.info("Starting Halide to x86 equivalence class test")
        
        # Create a pass pipeline with AutoLLVMEnumerate
        pass_pipeline = MISAAL_PASS_PIPELINE(
            [AutoLLVMEnumerate], 
            working_directory=self.test_working_dir,
            log_file=os.path.join(self.test_working_dir, "pipeline_halide_x86.log"),
            src_dsl_list=self.halide_test_insts,
            src_synth_desc=HALIDE_SYNTH_DESC,
            target_dsl_list=self.x86_test_insts,
            target_synth_desc=X86_SYNTH_DESC,
            parallelize=True,
            pool=6,
            batch_size=1024,
            stop_after_exception=True,
            pass_configs=self.pass_configs
        )

        # Run the pass pipeline and check if it succeeds
        result = pass_pipeline.execute_pass_pipeline()
        print("Pass pipeline result", result)
        self.logger.info(f"Halide to x86 pass pipeline execution {'succeeded' if result else 'failed'}")
        self.assertTrue(result, "Halide to x86 pass pipeline execution failed")

        # Check if results were generated
        results = pass_pipeline.passes_results.get(AutoLLVMEnumerate.get_pass_name(), {})
        self.assertGreater(len(results), 0, "No equivalence classes were found")

    def tearDown(self):
        # Clean up the temporary forward map file
        if os.path.exists(self.forward_map_path):
            os.remove(self.forward_map_path)


if __name__ == "__main__":
    unittest.main() 