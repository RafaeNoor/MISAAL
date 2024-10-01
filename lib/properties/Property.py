from common.Types import *
from datetime import datetime
import time
import psutil
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
from utils.NotificationUtil import send_email

import random

class Property:
    """Abstract class to represent properties for Hydride IR's Equivalence Classes

    """

    def __init__(self, name = "Property", dsl_list = [], synth_desc = None, parallel = True, is_candidate_generator = False, keep_temp_files = False):
        """Class constructor for base class

        Args:
            name (str, optional): _description_. Defaults to "Property".
            dsl_list (list, optional): _description_. Defaults to [].
        """
        self.name = name
        self.dsl_list = dsl_list
        self.synth_desc = synth_desc
        self.parallel = parallel


        self.BATCH_SIZE = 1024
        self.POOL_SIZE = 64

        self.keep_temp_files = keep_temp_files

        self.notify_enabled = True
        self.notify_count = self.BATCH_SIZE
        self.notify_to = 'arnoor2@illinois.edu'
        self.notify_iter = 0



        # Candidates refer to expressions (usually tree's) on which the property will be
        # analyzed.
        self.candidates = []
        self.support_dsl = default_structs
        self.is_candidate_generator = is_candidate_generator

    def set_candidates(self, candidates):
        self.candidates = candidates

        if not self.is_candidate_generator:
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

        if self.is_candidate_generator:
            print("Candidates are generated using generator: indefinite number of candidates")
        else:
            print("Total Number of Candidates: ", len(self.candidates))

        print("BATCH_SIZE:\t{}".format(self.BATCH_SIZE))
        print("POOL_SIZE:\t{}".format(self.POOL_SIZE))
        print("Keep temp files:\t{}".format(self.keep_temp_files))

        if self.keep_temp_files:
            keep_temporary_files()
        else:
            delete_temporary_files()




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


        BATCH_SIZE = self.BATCH_SIZE
        POOL_SIZE = min(self.POOL_SIZE, self.BATCH_SIZE)

        count = 0

        start_time = time.time()

        if self.parallel and not self.is_candidate_generator:
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
                self.run_on_batch_completion()

                with open(self.name+"_"+self.synth_desc.target_name+"_intermediate_results.py", "w+") as WriteFile:
                    WriteFile.write(json.dumps(property_map, indent = 4))

                cleanup_tmp_files()
                self.kill_remaining_child_processes()

        elif not self.is_candidate_generator:
            for i in range(0, len(self.candidates), BATCH_SIZE):
                for j in range(i, min(len(self.candidates), i + BATCH_SIZE)):
                    candidate = self.candidates[j]
                    worker(candidate)

                self.run_on_batch_completion()

                with open(self.name+"_"+self.synth_desc.target_name+"_intermediate_results.py", "w+") as WriteFile:
                    WriteFile.write(json.dumps(property_map, indent = 4))

                cleanup_tmp_files()

        elif self.parallel and self.is_candidate_generator:
            while True:

                if self.should_notify(count):
                    self.notify(count,candidate_count, start_time)

                print("Completed executing {} / {}  jobs   ...".format(count, "INDEFINITE"))
                # create a thread pool with 4 threads
                pool = concurrent.futures.ThreadPoolExecutor(max_workers=POOL_SIZE)
                j = 0

                for candidate in self.candidates:
                    count += 1
                    j+= 1
                    pool.submit(worker, candidate)
                    if j == BATCH_SIZE:
                        break

                if j == 0:
                    # No additional candidate appended, so we have exhausted generator
                    break

                pool.shutdown(wait=True)
                print("Completed compiling pool...")
                self.run_on_batch_completion()

                print("Property", self.name, "holds on", candidate_count,  " candidates ...")


                with open(self.name+"_"+self.synth_desc.target_name+"_intermediate_results.py", "w+") as WriteFile:
                    WriteFile.write(json.dumps(property_map, indent = 4))


                cleanup_tmp_files()
                self.kill_remaining_child_processes()

        elif self.is_candidate_generator:

            num_processed = 0
            while True:

                j = 0
                for candidate in self.candidates:
                    num_processed += 1
                    j+= 1
                    worker(candidate)
                    if j == BATCH_SIZE:
                        break

                if j == 0:
                    break

                self.run_on_batch_completion()

                with open(self.name+"_"+self.synth_desc.target_name+"_intermediate_results.py", "w+") as WriteFile:
                    WriteFile.write(json.dumps(property_map, indent = 4))

                if self.should_notify(num_processed):
                    self.notify(num_processed,candidate_count, start_time)



                cleanup_tmp_files()


        if self.is_candidate_generator:
            print("Property", self.name, "holds on", candidate_count,  " candidates ...")
        else:
            count = len(self.candidates)
            print("Property", self.name, "holds on", candidate_count, "/", len(self.candidates), "candidates ...")

        if self.notify_enabled:
            self.notify(count,candidate_count, start_time)

        print(property_map)
        self.run_on_completion()
        end_time = time.time()
        elapsed_time = end_time - start_time

        with open("property_time_log.txt","a+") as LogFile:
            LogFile.write("{} : {} seconds\n".format(self.name, elapsed_time))


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
            if not os.path.exists('/proc/%d/status' % pid):
                return "-1"
            for ln in open('/proc/%d/status' % pid):
                if ln.startswith('Uid:'):
                    uid = int(ln.split()[UID])
                    return pwd.getpwuid(uid).pw_name

        commands = ["racket", "z3"]

        pid_to_kill = []

        for cmd in commands:
            ids = get_process_id(cmd)

            for _id in ids:
                #if os.path.exists('/proc/%d/status' % _id) and  (owner(_id) == "arnoor2"):
                if  (owner(_id) == "arnoor2"):
                    pid_to_kill.append(_id)

        print("Need to kill {} child processes".format(len(pid_to_kill)))

        for pid in pid_to_kill:
            if psutil.pid_exists(pid):
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


    def get_registers(self, ctx):

        regs = []

        if isinstance(ctx, Context):
            for arg in ctx.context_args:
                regs += self.get_registers(arg)
        elif isinstance(ctx, Reg):
            return [ctx]
        else:
            return []
        # Deduplicate and order according to increasing order

        unique_regs = []

        for reg in regs:
            unique_regs.append(int(reg.index))
        unique_regs = list(set(unique_regs))

        unique_regs.sort()

        # Sort in increasing order
        ordered_regs = ['empty'] * len(unique_regs)

        for reg in regs:
            ordered_regs[unique_regs.index(int(reg.index))] = reg

        return ordered_regs


    def replace_reg_with_expr(self, dsl_expression, input_reg, insert_expr):
        """Given a dsl expression, it traverses the arguments recursively and replaces all
        instances of input reg with insert_expr

        Args:
            dsl_expression (DSLInstruction): _description_
            input_reg (Reg): _description_
            insert_expr (Reg or DSLInstruciton): _description_
        """

        if isinstance(dsl_expression, Context):

            for i in range(len(dsl_expression.context_args)):
                dsl_expression.context_args[i] = self.replace_reg_with_expr(dsl_expression.context_args[i],
                input_reg, insert_expr)
            return dsl_expression
        elif isinstance(dsl_expression, Reg):
            if input_reg.index == dsl_expression.index:
                return insert_expr

        return dsl_expression


    def get_nested_contexts_name(self, ctx):
        if not isinstance(ctx, Context):
            return []

        names = [ctx.name]

        for arg in ctx.context_args:
            names += self.get_nested_contexts_name(arg)
        return list(set(names))

    def run_on_completion(self):
        return


    def run_on_batch_completion(self):
        return

    def should_notify(self, count):
        return self.notify_enabled and (count % self.notify_count == 0)

    def get_notify_subject(self):
        current_date = datetime.today().strftime('%Y-%m-%d')
        self.notify_iter += 1
        return '[MISAAL] {}_{} | {} Iteration {} '.format(self.synth_desc.target_name, self.name, current_date, self.notify_iter)


    def get_notify_body(self, count, success_count, start_time):
        processed_str = "Processed {} candidates , with {} successes".format(count, success_count)


        elapsed_time = time.time() - start_time
        hours = elapsed_time / (60 * 60)

        time_str_sec = "Elapsed time since start: {} seconds".format(elapsed_time)
        time_str_hour = "Elapsed time since start: {} hours".format(hours)

        candidates_per_second = count / elapsed_time

        candidate_rate_str = "Candidate rate: {} candidates per second".format(candidates_per_second)

        BANNER = "======================================="
        HEADER = BANNER + "\n"+ " "*25 + "MISAAL\n" + BANNER

        FOOTER = BANNER

        items = [HEADER, processed_str, time_str_sec, time_str_hour ,candidate_rate_str , FOOTER]

        return "\n".join(items)


    def notify(self, count, success_count ,start_time):
        msg_subject = self.get_notify_subject()
        msg_body = self.get_notify_body(count, success_count,  start_time)
        send_email(self.notify_to, msg_subject, msg_body)





