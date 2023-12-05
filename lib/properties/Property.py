from common.Types import *
from common.PredefinedDSL import *
import concurrent.futures
from  utils.DSLInstructionUtils import *
from utils.EggLogUtils import *
import json
from utils.ReadDSL import read_string_to_dsl
from utils.ExprParamUtils import generate_parameter_map
import subprocess
import os
from os import kill
from os import getpid
import signal
import pwd
from subprocess import check_output

import random

class Property:
    """Abstract class to represent properties for Hydride IR's Equivalence Classes

    """

    def __init__(self, name = "Property", dsl_list = [], synth_desc = None, parallel = True):
        """Class constructor for base class

        Args:
            name (str, optional): _description_. Defaults to "Property".
            dsl_list (list, optional): _description_. Defaults to [].
        """
        self.name = name
        self.dsl_list = dsl_list
        self.synth_desc = synth_desc
        self.parallel = parallel

        # Candidates refer to expressions (usually tree's) on which the property will be
        # analyzed.
        self.candidates = []
        self.support_dsl = default_structs

    def set_candidates(self, candidates):
        self.candidates = candidates
        random.shuffle(self.candidates)

    def generate_candidates(self):
        raise NotImplementedError()


    def get_property_desc(self):
        """Abstract method for returning string which describes the property

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError()

    def property_holds_on_candidate(self, candidate):
        """Method for checking if property holds on candidate. This may on the returned
        value for the expression, or with respect to the semantics of the instruction.

        Args:
            instruction (DSLInstruction): Instruction (Equivalence class) on which the property is being inferred

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError()

    def get_property_on_candidate(self, candidate):
        """Returns a python object which captures the relationship of the property on the candidate

        Args:
            candidate (DSLInstruction or Anything): Candidates could be single DSL instructions, DSL Expression Trees, or anything really.

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError()


    def serialize_candidate(self, candidate):
        """Serialize the candidate so that it can be used as a key in a python dictionary

        Args:
            candidate (_type_): _description_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError()


    def get_hydride_import_header(self):
        return """
        #lang rosette
        (require rosette/lib/synthax)
        (require rosette/lib/angelic)
        (require racket/pretty)
        (require data/bit-vector)
        (require rosette/lib/destruct)
        (require rosette/solver/smt/boolector)
        (require hydride)

        ;; Uncomment the line below to enable verbose logging
        (enable-debug)
        (custodian-limit-memory (current-custodian) (* 1000 1024 1024))
        """

    def get_property(self):
        """Main driver method for generating information for properties. In general, the flow would
        consist of generating candidates, checking if the property holds for each candidate and appropriately,
        and finally generating a python dictionary which maps candidates to properties
        """
        print(self.get_property_desc())

        self.set_candidates(
            self.generate_candidates()
        )


        #global property_map
        property_map = {}

        print("Total Number of Candidates: ", len(self.candidates))



        global candidate_count
        candidate_count = 0
        def worker(candidate):
            """Parallelizable method on each candidate

            Args:
                candidate (_type_): _description_
            """
            if self.property_holds_on_candidate(candidate):
                key = self.serialize_candidate(candidate)

                global candidate_count

                candidate_count += 1

                if key not in property_map:
                    property_map[key] = []
                property_map[key].append ({
                    "property_name": self.name,
                    "property": self.get_property_on_candidate(candidate)
                })


        BATCH_SIZE = 384
        POOL_SIZE = min(74, BATCH_SIZE)

        if self.parallel:
            print("Running Property Inference in Parallel")

            # Issue candidates in batches so that we can routinely garbage collect
            # and files generated during synthesis:


            for i in range(0, len(self.candidates), BATCH_SIZE):

                print("Completed executing {} / {}  jobs   ...".format(i, len(self.candidates)))
                # create a thread pool with 4 threads
                pool = concurrent.futures.ThreadPoolExecutor(max_workers=POOL_SIZE)
                for j in range(i, min(len(self.candidates), i + BATCH_SIZE)):
                    candidate = self.candidates[j]
                    pool.submit(worker, candidate)


                pool.shutdown(wait=True)
                print("Completed compiling pool...")

                with open(self.name+"_"+self.synth_desc.target_name+"_intermediate_results.py", "w+") as WriteFile:
                    WriteFile.write(json.dumps(property_map, indent = 4))

                cleanup_tmp_files()
                self.kill_remaining_child_processes()

        else:
            for i in range(0, len(self.candidates), BATCH_SIZE):
                for j in range(i, min(len(self.candidates), i + BATCH_SIZE)):
                    candidate = self.candidates[j]
                    worker(candidate)

                with open(self.name+"_"+self.synth_desc.target_name+"_intermediate_results.py", "w+") as WriteFile:
                    WriteFile.write(json.dumps(property_map, indent = 4))

                cleanup_tmp_files()

        print("Property", self.name, "holds on", candidate_count, "/", len(self.candidates), "candidates ...")
        print(property_map)
        return property_map


    def kill_remaining_child_processes(self):
        def get_process_id(name):
            """Return process ids found by (partial) name or regex.
            >>> get_process_id('kthreadd')
            [2]
            >>> get_process_id('watchdog')
            [10, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61]  # ymmv
            >>> get_process_id('non-existent process')
            []
            """
            child = subprocess.Popen(['pgrep', '-f', name], stdout=subprocess.PIPE, shell=False)
            response = child.communicate()[0]
            return [int(pid) for pid in response.split()]

        UID   = 1
        EUID  = 2
        def owner(pid):
            '''Return username of UID of process pid'''
            for ln in open('/proc/%d/status' % pid):
                if ln.startswith('Uid:'):
                    uid = int(ln.split()[UID])
                    return pwd.getpwuid(uid).pw_name

        commands = ["racket", "z3"]

        pid_to_kill = []

        for cmd in commands:
            ids = get_process_id(cmd)

            for _id in ids:
                if (owner(_id) == "arnoor2"):
                    pid_to_kill.append(_id)

        print("Need to kill {} child processes".format(len(pid_to_kill)))

        for pid in pid_to_kill:
            os.kill(pid, signal.SIGKILL)



    def get_sample_context_for_property(self, dsl_inst):
        sample_context = None
        num_symbolic_args = 0

        for ctx in dsl_inst.contexts:

            ctx_sym_args = 0
            for arg in ctx.context_args:
                if isinstance(arg, BitVector):
                    ctx_sym_args += 1
            if ctx_sym_args > num_symbolic_args:
                num_symbolic_args = ctx_sym_args
                sample_context = ctx
        return sample_context



    def emit_property_to_egg(self, property_map):
        raise NotImplementedError()




