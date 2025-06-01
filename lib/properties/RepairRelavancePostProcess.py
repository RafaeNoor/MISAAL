from properties.Property import *
from utils.ReadDSL import read_string_to_dsl
from utils.DSLInstructionUtils import *
from utils.RepairPostProcessUtils import RepairPostProcessUtils
from utils.CodeSynthesizerDesc import create_synth_desc
from common.StructDef import StructDef
from  common.Types import *
import json
import copy
import sys

class RepairRelavancePostProcess(Property):

    def __init__(self, input_dsl_list = [], output_dsl_list = [], repair_dsl_list = [], memo_path = None, target = "x86", base_name = ""):

        super().__init__(name = "RepairRelavancePostProcess"
,dsl_list = input_dsl_list, is_candidate_generator = True)
        self.target = target
        self.input_dsl_list = input_dsl_list
        self.repair_dsl_list = repair_dsl_list
        self.output_dsl_list = output_dsl_list
        self.base_name = base_name

        self.combined_dsl_list = self.input_dsl_list + self.output_dsl_list + self.repair_dsl_list
        self.output_language = self.output_dsl_list + self.repair_dsl_list

        self.repair_results_dict = {}

        if memo_path is None or not os.path.exists(memo_path):
            print(memo_path)
            assert False, "Repair Post process input dictionary does not exist or in-correct path"

        with open(memo_path, "r") as ReadFile:
            self.repair_results_dict = json.load(ReadFile)


        print("#Keys:" , len([key for key in self.repair_results_dict]))

        self.passing_results = {}
        self.failing_results = {}
        self.error_results = {}

        self.synth_desc = create_synth_desc("post-"+self.target, True, [], "", "")
        self.sd = StructDef(emit_default = False)
        self.racket_bool_map = {"#f": False , "#t": True}




    def get_property_desc(self):
        return "Post process results of RepairRelevance to prune non-meaningful expressions"

    def generate_candidates(self):

        try:
            for key in self.repair_results_dict:
                yield key

        except KeyboardInterrupt:
            print("Keyboard exception, exiting ....")

        return





    def property_holds_on_candidate(self, candidate):

        expressions_desc = self.repair_results_dict[candidate]
        test_name = candidate.split("+")[-1]

        failed = True
        error = False

        for expr_desc in expressions_desc:
            test_expr = expr_desc['property']['output_expression']

            parsed_expr = read_string_to_dsl(test_expr, self.combined_dsl_list)
            relevant_subset_names = self.get_nested_contexts_dsl_name(parsed_expr)
            relevant_subset = [dsl_inst for dsl_inst in self.combined_dsl_list if dsl_inst.name in relevant_subset_names ]

            assert len(relevant_subset_names) == len(relevant_subset)

            interpreter_framework = self.synth_desc.emit_interpreter_framework(relevant_subset)

            context_regs = get_unique_context_registers(parsed_expr)
            num_regs = int(context_regs[-1].index) + 1

            register_sizes = [8] * num_regs

            for reg in context_regs:
                idx = int(reg.index)
                register_sizes[idx] = reg.size

            src_env_sizes  =  expr_desc['property']['src_env_sizes']
            repair_util = RepairPostProcessUtils(test_name = test_name, env_sizes = register_sizes, const_fold_name = self.synth_desc.const_fold_name, use_prepared_env_name = "prepare-env", prepare_env_sizes = src_env_sizes)

            repair_process_name = "repair-post-process"

            statements = []
            statements.append(interpreter_framework)


            statements.append(repair_util.emit_repair_post_process(self.output_language, self.sd, interpret_name = self.synth_desc.interpreter_name , repair_post_process_name = repair_process_name))


            src_expr_name = "src-expr"
            def_src = "(define {} {}\n)".format(src_expr_name, parsed_expr.emit_context_expr_string())

            statements.append(def_src)

            statements.append(self.emit_define_reg_replace())

            env_function = expr_desc['property']['env-func']

            statements.append(env_function)


            # Created folded env and inline into src expression
            inline_env = "(define inline-env (create-bind-reg prepare-env (list {})))".format(" ".join([str(size) for size in src_env_sizes]))
            statements.append(inline_env)

            inline_expr_name = "inline-src-expr"
            def_inline = "(define {} ({} {} inline-env))".format(inline_expr_name,  self.synth_desc.bind_name,  src_expr_name)
            statements.append(def_inline)

            for solvers in ["z3", "boolector"]:
                statement_copy = copy.deepcopy(statements)

                set_solver_stmt = "(current-solver ({}))".format(solvers)
                statement_copy.append(set_solver_stmt)

                result_stmt = "(define result {})".format(repair_util.emit_check_property(inline_expr_name))
                statement_copy.append(result_stmt)

                rand_prefix = get_random_tempfile_name()

                result_file_name = rand_prefix+".log"

                write_result_to_file = "(write-str-to-file (~v result) \"{}\")".format(result_file_name)

                statement_copy.append(write_result_to_file)

                expr_desc['solver'] = solvers

                desc_copy = copy.deepcopy(expr_desc)

                execute_racket_file(statement_copy)

                if os.path.exists(result_file_name):
                    with open(result_file_name, "r") as LogFile:
                        contents = LogFile.read().rstrip().lstrip()
                        boolean = self.racket_bool_map[contents]
                        if boolean:
                            print("SUCCESS!")
                            print(parsed_expr.emit_context_expr_string())

                            self.passing_results[candidate] = [desc_copy]
                            self.failing_results.pop(candidate, None)
                            self.error_results.pop(candidate, None)
                            return True
                        else:
                            print("FAILURE")
                            if candidate not in self.failing_results:
                                self.failing_results[candidate] = []
                            self.failing_results[candidate].append(desc_copy) #= self.repair_results_dict[candidate]
                    os.remove(result_file_name)


                else:
                    if candidate not in self.error_results:
                        self.error_results[candidate] = []
                    # Either timeout or failing
                    self.error_results[candidate].append(desc_copy) #= self.repair_results_dict[candidate]
        return False





    def serialize_candidate(self, candidate):
        return candidate

    def get_property_on_candidate(self, candidate):
        key = self.serialize_candidate(candidate)
        return self.passing_results[key][0]

    def emit_property_to_egg(self, property_map):
        return []

    def dump_evaluated_tests(self):
        pass_name = "_".join([self.name,"PASS", self.target, self.base_name]) + ".json"
        fail_name = "_".join([self.name,"FAIL", self.target, self.base_name]) + ".json"
        error_name = "_".join([self.name,"ERROR", self.target, self.base_name]) + ".json"

        with open(pass_name, "w+") as WriteFile:
            WriteFile.write(json.dumps(self.passing_results, indent = 4))

        with open(fail_name, "w+") as WriteFile:
            WriteFile.write(json.dumps(self.failing_results, indent = 4))

        with open(error_name, "w+") as WriteFile:
            WriteFile.write(json.dumps(self.error_results, indent = 4))

    def print_stats(self):
        total_tests = len([key for key in self.repair_results_dict])
        passing_tests = len([key for key in self.passing_results])
        failing_tests = len([key for key in self.failing_results])
        error_tests = len([key for key in self.error_results])

        total_eval_tests = passing_tests + failing_tests + error_tests

        remaining_tests = total_tests - total_eval_tests

        print("=*"*15, "Repair Post Process Summary", "=*"*15)
        print("[ PASSED ]:\t\t", passing_tests , "/", total_tests)
        print("[ FAILED ]:\t\t", failing_tests , "/", total_tests)
        print("[ ERROR ]:\t\t", error_tests , "/", total_tests)




    def run_on_batch_completion(self):
        self.print_stats()
        self.dump_evaluated_tests()

    def run_on_completion(self, pmap):
        self.print_stats()
        self.dump_evaluated_tests()


    def emit_define_reg_replace(self):
        return """(define (create-bind-reg prep-env-fn env-sizes)
              (define (create-sym-test-env i)
                (define size-i (list-ref env-sizes i))
                (define-symbolic* value (bitvector size-i))
                value
                )
              (define sym-input-env (build-vector (length env-sizes) create-sym-test-env ))

              (define test-prepare-env (prep-env-fn sym-input-env))

              (define (reg-replace i)
                (define value (vector-ref test-prepare-env i))
                (cond
                  [(concrete? value) (lit value)]
                  [else (reg (bv i (bitvector 8)))]
                  )
                )

              (build-vector (vector-length test-prepare-env) reg-replace )
              )
              """
