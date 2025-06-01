from utils.PassPipelineUtils import MISAAL_PASS
from properties.EqClassEqualDepthV4 import EqClassEqualDepthV4
import datetime
import json
import os

class EqClassEqualDepthV4Pass(MISAAL_PASS):

    def __init__(self, parallelize: bool = True, pool: int = 4, batch_size: int = 1024, 
                 working_directory: str = "/tmp/", log_file: str = "/tmp/log.txt", 
                 src_dsl_list: list = None, target_dsl_list: list = None, 
                 src_synth_desc: str = None, target_synth_desc: str = None,
                 stop_after_exception = True, output_depth: int = 1, input_depth: int = 1,
                 depth_range: bool = True, use_canon_map: bool = False,
                 start_input_depth: int = 1, start_output_depth: int = 1,
                 bidirectional_test: bool = False, filter_list: list = None,
                 ensure_structure: bool = True, forward_map_path: str = None,
                 swizzle_map_path: str = None, commutative_map_path: str = None):
        pass_name = "EqClassEqualDepthV4Pass"
        pass_desc = "This pass identifies equivalent expressions up to a specified depth using EqClassEqualDepthV4"
        super().__init__(pass_name, pass_desc, parallelize=parallelize, pool=pool, 
                        batch_size=batch_size, working_directory=working_directory, 
                        log_file=log_file, src_dsl_list=src_dsl_list, 
                        target_dsl_list=target_dsl_list, src_synth_desc=src_synth_desc, 
                        target_synth_desc=target_synth_desc, 
                        stop_after_exception=stop_after_exception)
        
        self.output_depth = output_depth
        self.input_depth = input_depth
        self.depth_range = depth_range
        self.use_canon_map = use_canon_map
        self.start_input_depth = start_input_depth
        self.start_output_depth = start_output_depth
        self.bidirectional_test = bidirectional_test
        self.filter_list = filter_list
        self.ensure_structure = ensure_structure
        self.forward_map_path = forward_map_path
        self.swizzle_map_path = swizzle_map_path
        self.commutative_map_path = commutative_map_path
        self.prop_result = {}

    @classmethod
    def get_pass_name(cls):
        return "EqClassEqualDepthV4Pass"

    @classmethod
    def get_pass_description(cls):
        return "This pass identifies equivalent expressions up to a specified depth using EqClassEqualDepthV4"

    def get_results_summary(self):
        num_eq_classes = len(self.prop_result)
        return f"Number of equivalence classes found: {num_eq_classes}"

    def get_pass_results(self):
        return self.prop_result

    def execute(self):

        contexts = [(self.src_dsl_list, self.src_synth_desc)]
        print("Contexts", contexts)

        self.log(f"Forward map path: {self.forward_map_path}")
        self.log(f"Swizzle map path: {self.swizzle_map_path}")
        self.log(f"Commutative map path: {self.commutative_map_path}")
        self.log(f"Working directory: {self.working_directory}")
        self.log(f"Output depth: {self.output_depth}")
        self.log(f"Input depth: {self.input_depth}")
        self.log(f"Depth range: {self.depth_range}")
        self.log(f"Use canon map: {self.use_canon_map}")
        self.log(f"Start input depth: {self.start_input_depth}")
        self.log(f"Start output depth: {self.start_output_depth}")
        self.log(f"Bidirectional test: {self.bidirectional_test}")

        for idx, (dsl_list, synth_desc) in enumerate(contexts):
            prop = EqClassEqualDepthV4(
                dsl_list=dsl_list,
                source_synth_desc=synth_desc,
                target_synth_desc=self.target_synth_desc,
                target_dsl_list=self.target_dsl_list,
                output_depth=self.output_depth,
                input_depth=self.input_depth,
                depth_range=self.depth_range,
                use_canon_map=self.use_canon_map,
                start_input_depth=self.start_input_depth,
                start_output_depth=self.start_output_depth,
                bidirectional_test=self.bidirectional_test,
                filter_list=self.filter_list,
                ensure_structure=self.ensure_structure,
                forward_map_path=self.forward_map_path,
                swizzle_map_path=self.swizzle_map_path,
                commutative_map_path=self.commutative_map_path
            )

            prop.set_work_dir(self.working_directory)
            prop.parallel = self.parallelize
            prop.POOL_SIZE = self.pool
            prop.BATCH_SIZE = self.batch_size

            # Get and run the property
            prop_map = prop.get_property()
            print("Prop map", prop_map)
            eq_class_map = prop.run_on_completion(prop_map)
            print(f"EqClassEqualDepthV4Pass: {eq_class_map}")
            assert eq_class_map is not None, "EqClassEqualDepthV4Pass: eq_class_map is None"

            # Save property results
            prop_path = os.path.join(self.working_directory, f"EqClassEqualDepthV4PropResults_{idx}.json")
            eq_class_path = os.path.join(self.working_directory, f"eq_class_map_{idx}.json")

            with open(prop_path, "w+") as OutFile:
                json.dump(prop_map, OutFile, indent=4)
            now = datetime.datetime.now()
            prefix = f"[ {now}, {self.pass_name} ]"
            self.log(f"{prefix} Wrote property results to {prop_path}")

            with open(eq_class_path, "w+") as OutFile:
                json.dump(eq_class_map, OutFile, indent=4)
            self.log(f"{prefix} Wrote equivalence class map to {eq_class_path}")

            self.prop_result.update(eq_class_map) 