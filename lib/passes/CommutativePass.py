from utils.PassPipelineUtils import MISAAL_PASS
from properties.Commutative import Commutative
import datetime
import json
import os



class CommutativePass(MISAAL_PASS):

    def __init__(self, parallelize: bool = True, pool: int = 4, batch_size: int = 1024, working_directory: str = "/tmp/", log_file: str = "/tmp/log.txt", src_dsl_list: list = None, target_dsl_list: list = None, src_synth_desc: str = None, target_synth_desc: str = None, stop_after_exception = True):
        pass_name = "CommutativePass"
        pass_desc = "This pass is used to check if the given DSLInstructions are commutative and writes the results to file"
        super().__init__(pass_name, pass_desc, parallelize=parallelize, pool=pool, batch_size=batch_size, working_directory=working_directory, log_file=log_file,
                         src_dsl_list=src_dsl_list, target_dsl_list=target_dsl_list, src_synth_desc=src_synth_desc, target_synth_desc=target_synth_desc, stop_after_exception = stop_after_exception)
        self.prop_result = {}
        

    @classmethod
    def get_pass_name(cls):
        return "CommutativePass"

    @classmethod
    def get_pass_description(cls):
        return "This pass is used to check if the given DSLInstructions are commutative and writes the results to file"

    def get_results_summary(self):
        num_inst_commutative = len([k for k in self.prop_result.keys()])
        return f"Number of commutative equivalence classes: {num_inst_commutative}"

    def get_pass_results(self):
        return self.prop_result



    def execute(self):

        if  self.target_synth_desc is None or self.src_synth_desc.target_name == self.target_synth_desc.target_name :
            contexts = [(self.src_dsl_list, self.src_synth_desc)]
        else:
            contexts = [(self.src_dsl_list, self.src_synth_desc), (self.target_dsl_list, self.target_synth_desc)]


        for idx, (dsl_list, synth_desc) in enumerate(contexts):
            CommutativeProp = Commutative(dsl_list=dsl_list, synth_desc= synth_desc)
            CommutativeProp.set_work_dir(self.working_directory)
            CommutativeProp.parallel = self.parallelize
            CommutativeProp.POOL_SIZE = self.pool
            CommutativeProp.BATCH_SIZE = self.batch_size

            prop_map = CommutativeProp.get_property()
            commutative_map = CommutativeProp.run_on_completion(prop_map)

            

            prop_path = os.path.join(self.working_directory, f"CommutativePropResults_{idx}.json")
            cmap_path = os.path.join(self.working_directory, f"commutative_map_{idx}.json")

            with open(prop_path, "w+") as OutFile:
                json.dump(prop_map, OutFile, indent=4)
            now = datetime.datetime.now()
            prefix = f"[ {now}, {self.pass_name} ]"
            self.log(f"{prefix} Wrote property results to {prop_path}")


            with open(cmap_path, "w+") as OutFile:
                json.dump(commutative_map, OutFile, indent=4)
            self.log(f"{prefix} Wrote commutative map to {cmap_path}")

            self.prop_result.update(commutative_map)


