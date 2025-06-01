from utils.PassPipelineUtils import MISAAL_PASS
from passes.CommutativePass import CommutativePass
from properties.RepairRelavanceV4 import RepairRelavanceV4
from properties.RepairRelavanceIntermediates import RepairRelavanceIntermediates
from properties.RepairRelavancePostProcess import RepairRelavancePostProcess
from sema.repairs_sema import repair_semantics
from common.DSLParser import parse_dict

import datetime
import json
import os

class ComputeOnlyRelevancePass(MISAAL_PASS):
    def __init__(self, parallelize: bool = True, pool: int = 4, batch_size: int = 1024, working_directory: str = "/tmp/", log_file: str = "/tmp/log.txt", src_dsl_list: list = None, target_dsl_list: list = None, src_synth_desc: str = None, target_synth_desc: str = None, stop_after_exception = True, post_process = True):
        pass_name = "ComputeOnlyRelevancePass"
        pass_desc = "Check if two DSLInstructions share similar computational semantics independently of data-movements"
        super().__init__(pass_name, pass_desc, parallelize=parallelize, pool=pool, batch_size=batch_size, working_directory=working_directory, log_file=log_file,
                         src_dsl_list=src_dsl_list, target_dsl_list=target_dsl_list, src_synth_desc=src_synth_desc, target_synth_desc=target_synth_desc, stop_after_exception = stop_after_exception)
        self.prop_result = {}
        self.post_process = post_process
        self.repair_dsl_list = parse_dict(repair_semantics)
        self.repair_map = {}
    
    @classmethod
    def get_pass_name(self):
        return "ComputeOnlyRelevancePass"
    @classmethod
    def get_pass_description(self):
        return "Check if two DSLInstructions share similar computational semantics independently of data-movements"
    
    @classmethod
    def pass_depends_on(self):
        """
        Defines the pass dependencies for the current pass so that it can use the results of other passes.
        """
        return [CommutativePass]
    
    def get_pass_results(self):
        return self.repair_map
    
    def get_results_summary(self):
        num_inst_repair = len([k for k in self.repair_map.keys()])
        return f"Number of {self.target_synth_desc.target_name} equivalence classes which have are semantically related to {self.src_synth_desc.target_name}: {num_inst_repair}"
    
    def merge_dict(self, d1, d2):
        merged = {key: list(d1.get(key, []) + d2.get(key, [])) for key in set(d1.keys()) | set(d2.keys())}
        return merged


    def generate_repair_maps(self, *repair_results):
        repair_map = {}

        for repair_result in repair_results:
            result_data = {}
            for key in repair_result:
                tokens = key.split("+")
                src_inst = tokens[0]
                target_inst = tokens[1]
                if not src_inst in result_data:
                    result_data[src_inst] = []
 
                result_data[src_inst].append(target_inst)
            repair_map = self.merge_dict(repair_map, result_data)
        return repair_map

            
    
    def execute(self):

        assert self.src_dsl_list is not None, "Source DSL list is not set"
        assert self.target_dsl_list is not None, "Target DSL list is not set"
        assert self.src_synth_desc is not None, "Source synth description is not set"
        assert self.target_synth_desc is not None, "Target synth description is not set"

        assert "CommutativePass" in self.passes_results, "Expected CommutativePass to be run before ComputeOnlyRelevancePass"
        # Get the commutative map from the CommutativePass results
        cmap = self.passes_results["CommutativePass"]

        # Write cmap to current working directory
        cmap_path = os.path.join(self.working_directory, "cmap.json")
        with open(cmap_path, "w") as f:
            json.dump(cmap, f)

        TARGET_START_DEPTH = 1
        TARGET_DEPTH = 2

        # First we check RepairRelavanceV4
        RepairInstanceV4 = RepairRelavanceV4(dsl_list = self.target_dsl_list, synth_desc = self.target_synth_desc, 
                                           output_dsl_list= self.src_dsl_list, target_synth_desc= self.src_synth_desc, 
                                           commutative_map_path=cmap_path,  target_start_depth = TARGET_START_DEPTH, target_depth = TARGET_DEPTH)
        
        # Then we check RepairRelavanceIntermediates
        RepairInstanceIntermediates = RepairRelavanceIntermediates(dsl_list = self.target_dsl_list, synth_desc = self.target_synth_desc, 
                                           output_dsl_list= self.src_dsl_list, target_synth_desc= self.src_synth_desc, 
                                           commutative_map_path=cmap_path,  target_start_depth = TARGET_START_DEPTH, target_depth = TARGET_DEPTH)
        # Finally we check RepairRelavancePostProcess
        
        RepairInstances = [RepairInstanceV4, RepairInstanceIntermediates]

        for RepairInstance in RepairInstances:
            RepairInstance.set_work_dir(self.working_directory)
            RepairInstance.parallel = self.parallelize
            RepairInstance.POOL_SIZE = self.pool
            RepairInstance.BATCH_SIZE = self.batch_size


            prefix, result = self.invoke_repair_instance(RepairInstance)

        # Now we merge the results from all the repair instances
        repair_prop_results = {}
        for RepairInstance in RepairInstances:
            repair_prop_results = self.merge_dict(repair_prop_results, self.prop_result[RepairInstance.name])
        self.log(f"{prefix} Merged Results Created!")
        results_path = os.path.join(self.working_directory, f"combined_prop_results.json")
        with open(results_path, "w+") as f:
            json.dump(repair_prop_results, f)
        self.log(f"{prefix} Merged Results saved to {results_path}")

        # Now optionally run the post-process to prune out redundant relevances from identities
        if self.post_process:
            RepairInstance = RepairRelavancePostProcess(input_dsl_list = self.target_dsl_list, 
                                           output_dsl_list= self.src_dsl_list, repair_dsl_list=self.repair_dsl_list, target = self.target_synth_desc.target_name, memo_path = results_path)
            RepairInstance.set_work_dir(self.working_directory)
            RepairInstance.parallel = self.parallelize
            RepairInstance.POOL_SIZE = self.pool
            RepairInstance.BATCH_SIZE = self.batch_size
            prefix, repair_prop_results = self.invoke_repair_instance(RepairInstance)



        now = datetime.datetime.now()
        prefix = f"[ {now}, {self.pass_name} ]"
        self.log(f"{prefix} All repairs completed, Generating repair maps")
        repair_map = self.generate_repair_maps(repair_prop_results)
        self.repair_map = repair_map

        repair_map_path = os.path.join(self.working_directory, "repair_map.json")
        with open(repair_map_path, "w") as f:
            json.dump(repair_map, f)
        self.log(f"{prefix} Repair map saved to {repair_map_path}")

        return repair_map

    def invoke_repair_instance(self, RepairInstance):
        start_time = datetime.datetime.now()

        prefix = f"[ {start_time}, {RepairInstance.name} ]"
        self.log(f"{prefix} Start")

        repair_result = RepairInstance.get_property()
        self.prop_result[RepairInstance.name] = repair_result
            
        end_time = datetime.datetime.now()
        prefix = f"[ {end_time}, {RepairInstance.name} ]"
            
        elapsed_time = end_time - start_time
        self.log(f"{prefix} End, Elapsed Time: {elapsed_time}")

        results_path = os.path.join(self.working_directory, f"{RepairInstance.name}_results.json")
        with open(results_path, "w") as f:
            json.dump(repair_result, f)
        self.log(f"{prefix} Results saved to {results_path}")
        return prefix, repair_result
