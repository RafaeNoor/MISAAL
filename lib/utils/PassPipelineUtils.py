from abc import abstractclassmethod, abstractmethod, ABC
import datetime
import traceback
import os
import inspect

class MISAAL_PASS(ABC):

    def __init__(self, pass_name, pass_description, parallelize = True, pool = 4, batch_size = 1024, working_directory = "/tmp/",
                 log_file = "/tmp/log.txt", stop_after_exception = True, src_dsl_list = None, target_dsl_list = None,
                 src_synth_desc = None, target_synth_desc = None):
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
        self.src_synth_desc = src_synth_desc
        self.target_synth_desc = target_synth_desc

        self.passes_results = {}


    def set_dependency_results(self, pass_name, results):
        """
        Set the results of a pass to be used by other passes.
        """
        self.passes_results[pass_name] = results


    @abstractclassmethod
    def get_pass_name(cls):
        return ""

    @abstractclassmethod
    def get_pass_description(cls):
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
        parallel_desc = f"{prefix} Parallelism Enabled:\t{self.parallelize}, POOL:\t{self.pool}, Batch:\t{self.batch_size}"
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


    @classmethod
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
        failed = f"{prefix} Ended with exception, elapsed time:\t {elapsed_time}"
        error_desc = f"{prefix} Exception:\t{exception_}"
        trace_desc = traceback.format_exc()
        self.log(failed)
        self.log(error_desc)
        self.log(trace_desc)


    @abstractmethod
    def execute(self):
        pass

class MISAAL_PASS_PIPELINE:
    def __init__(self, passes, parallelize = True, pool = 4, batch_size = 1024, working_directory = "/tmp/",
                 log_file = "/tmp/log.txt", src_dsl_list = None, target_dsl_list = None, src_synth_desc = None, 
                 target_synth_desc = None, stop_after_exception = True, pass_configs = None):
        self.passes = passes
        self.parallelize = parallelize
        self.stop_after_exception = stop_after_exception
        self.pool = pool
        self.batch_size = batch_size
        self.working_directory = working_directory
        if not os.path.exists(self.working_directory):
            os.makedirs(self.working_directory)
        self.log_file = log_file
        self.src_dsl_list = src_dsl_list
        self.target_dsl_list = target_dsl_list
        self.src_synth_desc = src_synth_desc
        self.target_synth_desc = target_synth_desc
        self.pass_configs = pass_configs or {}

        self.passes_results = {}

        self.check_env()
        self.check_pipeline_valid()
        self.validate_pass_configs()

    def validate_pass_configs(self):
        """
        Validate that the pass configurations are valid:
        1. Check that all pass names in configs exist in the pipeline
        2. Check that all specified parameters exist in the pass classes
        """
        if not self.pass_configs:
            return

        # Get all pass names in the pipeline
        pipeline_pass_names = {
            pass_.get_pass_name() if isinstance(pass_, type) else pass_.get_pass_name()
            for pass_ in self.passes
        }

        for pass_name, configs in self.pass_configs.items():
            # Check if pass exists in pipeline
            if pass_name not in pipeline_pass_names:
                raise ValueError(f"Pass '{pass_name}' specified in pass_configs does not exist in the pipeline")

            # Get the pass class
            pass_class = next(
                p if isinstance(p, type) else p.__class__
                for p in self.passes
                if (p.get_pass_name() if isinstance(p, type) else p.get_pass_name()) == pass_name
            )

            # Get valid parameters for the pass
            valid_params = set(inspect.signature(pass_class.__init__).parameters.keys())

            # Check each parameter
            for param_name, _ in configs:
                if param_name not in valid_params:
                    raise ValueError(
                        f"Parameter '{param_name}' specified for pass '{pass_name}' "
                        f"is not a valid parameter. Valid parameters are: {sorted(valid_params)}"
                    )

    def check_env(self):
        env_variables = ["MISAAL_SRC", "HYDRIDE_ROOT", "PYTHONPATH"]
        for var in env_variables:
            if var not in os.environ:
                raise Exception(f"Environment variable {var} is not set.")

        python_paths = ["code-synthesizer", "codegen-generator"]

        PYTHON_PATH = os.environ["PYTHONPATH"]
        for python_path in python_paths:
            if python_path not in PYTHON_PATH:
                raise Exception(f"Python path {python_path} is not in PYTHONPATH.")


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

    def log(self, *texts):
        concatenated = " ".join([str(t) for t in texts])
        with open(self.log_file, "a+") as LogFile:
            LogFile.write(concatenated + "\n")


    def get_dsl_list_summary(self, dsl_list):
        num_dsl_inst = len(dsl_list)
        num_ctxs = sum([len(dsl_inst.contexts) for dsl_inst in dsl_list])
        return f"Number of DSLInstructions: {num_dsl_inst}, Number of Contexts: {num_ctxs}"

    def execute_pass_pipeline(self):

        # Create the log file
        with open(self.log_file, "w+") as InitLog:
            pass

        self.log("==========================")
        self.log("Executing Pass Pipeline")
        self.log("==========================")
        for idx, pass_ in enumerate(self.passes):
            self.log(f"{idx}. Executing pass: {pass_.get_pass_name()}")
            self.log(f"{idx}. Description: {pass_.get_pass_description()}")
        self.log("==========================")

        if self.src_synth_desc is not None:
            self.log(f"Source Synthesizer Description: {self.src_synth_desc.target_name}")
            src_dsl_list_summary = self.get_dsl_list_summary(self.src_dsl_list)
            self.log(f"Source DSL List: {src_dsl_list_summary}")

        if self.target_synth_desc is not None:  
            self.log(f"Target Synthesizer Description: {self.target_synth_desc.target_name}")
            target_dsl_list_summary = self.get_dsl_list_summary(self.target_dsl_list)
            self.log(f"Target DSL List: {target_dsl_list_summary}")
        self.log("==========================")
        self.log("Executing Passes")
        for pass_ in self.passes:
            # Add pass-specific configurations if they exist
            pass_name = pass_.get_pass_name() if isinstance(pass_, type) else pass_.get_pass_name()
            pass_working_directory = os.path.join(self.working_directory, pass_name)
            if not os.path.exists(pass_working_directory):
                os.makedirs(pass_working_directory)

            # Get base parameters
            pass_params = {
                'parallelize': self.parallelize,
                'pool': self.pool,
                'batch_size': self.batch_size,
                'working_directory': self.working_directory,
                'log_file': os.path.join(self.working_directory, pass_name, "log.txt"),
                'stop_after_exception': self.stop_after_exception,
                'src_dsl_list': self.src_dsl_list,
                'target_dsl_list': self.target_dsl_list,
                'src_synth_desc': self.src_synth_desc,
                'target_synth_desc': self.target_synth_desc
            }


            if pass_name in self.pass_configs:
                for param_name, param_value in self.pass_configs[pass_name]:
                    pass_params[param_name] = param_value

            # Create pass instance with all parameters
            if isinstance(pass_, type):
                pass_instance = pass_(**pass_params)
            else:
                # If it's already an instance, update its attributes
                pass_instance = pass_
                for param_name, param_value in pass_params.items():
                    setattr(pass_instance, param_name, param_value)

            assert pass_instance is not None, f"Pass instance is None for pass {pass_name}"

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
                    return False
            finally:
                pass_instance.log_end()
                self.passes_results[pass_.get_pass_name()] = pass_instance.get_pass_results()

        return True
