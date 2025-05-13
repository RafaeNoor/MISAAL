from abc import abstractclassmethod, abstractmethod, ABC
import datetime
import os

class MISAAL_PASS(ABC):
    
    def __init__(self, pass_name, pass_description, parallelize = True, pool = 4, batch_size = 1024, working_directory = "/tmp/", log_file = "/tmp/log.txt", stop_after_exception = True, src_dsl_list = None, target_dsl_list = None):
        super().__init__()
        self.pass_name = pass_name
        self.pass_description = pass_description
        self.parallelize = parallelize
        self.pool = pool
        self.batch_size = batch_size
        self.working_directory_base = working_directory
        self.working_directory = os.path.join(self.working_directory_base, self.pass_name)
        if not os.path.exists(self.working_directory):
            os.makedirs(self.working_directory)
        self.log_file = log_file
        self.stop_after_exception = stop_after_exception
        self.src_dsl_list = src_dsl_list
        self.target_dsl_list = target_dsl_list  
        
        self.passes_results = {}


    def set_dependency_results(self, pass_name, results):
        """
        Set the results of a pass to be used by other passes.
        """
        self.passes_results[pass_name] = results


    @abstractclassmethod
    def get_pass_name(cls):
        return ""

    def log(self, *texts):
        concatenated = " ".join([str(t) for t in texts])
        with open(self.log_file, "a+") as LogFile:
            LogFile.write(concatenated + "\n")
            

    def log_init(self):
        now = datetime.datetime.now()
        self.start_time = now

        prefix = f"[ {now}, {self.pass_name} ]"
        header = f"{prefix} Begin"
        parallel_desc = f"{prefix} Parallelism Enabled:\t{self.parallelize}, POOL:\t{self.pool},Batch:\t{self.batch_size}"
        working_directory = f"{prefix} Working Directory: {self.working_directory}"

        self.log(header)
        self.log(parallel_desc)
        self.log(working_directory)
    
    @abstractmethod
    def get_results_summary(self):
        return ""

    @abstractmethod
    def get_pass_results(self):
        return None
    

    def pass_depends_on(self):
        """
        Defines the pass dependencies for the current pass so that it can use the results of other passes.
        """
        return []

    def log_end(self):
        now = datetime.datetime.now()
        self.end_time = now
        prefix = f"[ {now}, {self.pass_name} ]"
        elapsed_time = self.end_time - self.start_time
        completed = f"{prefix} End, elapsed time:\t {elapsed_time}"
        summary = self.get_results_summary()
        summary_desc = f"{prefix} {summary}"

        self.log(completed)
        self.log(summary_desc)

    def log_exception(self, exception_):
        now = datetime.datetime.now()
        self.end_time = now
        prefix = f"[ {now}, {self.pass_name} ]"
        elapsed_time = self.end_time - self.start_time
        failed = f"{prefix} Ended with excpetion, elapsed time:\t {elapsed_time}"
        error_desc = f"{prefix} Exception:\t{exception_}"
        self.log(failed)
        self.log(error_desc)
    

    @abstractmethod
    def execute(self):
        pass

class MISAAL_PASS_PIPELINE:
    def __init__(self, passes: list[MISAAL_PASS], parallelize = True, pool = 4, batch_size = 1024, working_directory = "/tmp/", log_file = "/tmp/log.txt", src_dsl_list = None, target_dsl_list = None):
        self.passes = passes
        self.parallelize = parallelize
        self.pool = pool
        self.batch_size = batch_size
        self.working_directory = working_directory
        self.log_file = log_file
        self.src_dsl_list = src_dsl_list
        self.target_dsl_list = target_dsl_list

        self.passes_results = {}


        self.check_pipeline_valid()

    def check_pipeline_valid(self):
        """
        Check if the pipeline is valid by checking if the passes are in the correct order and if the dependencies are met.
        """
        pass_names = [pass_.get_pass_name() for pass_ in self.passes]
        for i, pass_ in enumerate(self.passes):
            dependencies = pass_.pass_depends_on()
            for dep in dependencies:
                if dep.get_pass_name() not in pass_names[:i]:
                    raise Exception(f"Pass {pass_.get_pass_name()} depends on {dep.get_pass_name()} but it is not in the pipeline.")
        return True 
    
    def execute_pass_pipeline(self):
        for pass_ in self.passes:
            pass_instance = pass_(parallelize=self.parallelize, pool=self.pool, batch_size=self.batch_size, working_directory=self.working_directory, log_file=self.log_file, stop_after_exception=pass_.stop_after_exception, src_dsl_list=self.src_dsl_list, target_dsl_list=self.target_dsl_list)
            
            # Set the results of the dependencies for the current pass
            for dep in pass_.pass_depends_on():
                dep_results = self.passes_results[dep.get_pass_name()]
                pass_instance.set_dependency_results(dep.get_pass_name(), dep_results)
            
            pass_instance.log_init()
            try:
                pass_instance.execute()
            except Exception as e:
                pass_instance.log_exception(e)
                if pass_instance.stop_after_exception:
                    break
            finally:
                pass_instance.log_end()
                self.passes_results[pass_.get_pass_name()] = pass_instance.get_pass_results()


