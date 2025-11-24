from PIM_API_UTILS import PimDeviceEnum, PIM_CONFIG, get_device_type_name
from GenPimFusedCost import evaluate_config, get_csv_name
import subprocess as sb

from utils.DSLInstructionUtils import get_random_tempfile_name

import os
import opentuner
from opentuner.search.manipulator import (ConfigurationManipulator,
                                          IntegerParameter,
                                          LogIntegerParameter,
                                          SelectorParameter,
                                          SwitchParameter,
                                          EnumParameter,
                                          PowerOfTwoParameter,
                                          BooleanParameter,
                                          FloatParameter
                                          )
import argparse

from opentuner import ConfigurationManipulator
from opentuner import EnumParameter
from opentuner import IntegerParameter
from opentuner import MeasurementInterface
from opentuner import Result
from opentuner.search.objective import ThresholdAccuracyMinimizeTime, MinimizeTime
from opentuner.measurement.inputmanager import FixedInputManager

def execute_cmd(cmd):
    print(f"$\t{cmd}")
    try:
        sb.call(cmd, shell = True, stdout=sb.DEVNULL, stderr=sb.DEVNULL)
        return True
    except Exception as e:
        print("Command failed :(", cmd, e)
        return False



class TunerGen:
    def __init__(self, work_dir = './tuner_dir'):
        self.work_dir = work_dir
        self.tuning_params = []

        self.concept_names = {
            "rank": "RANK",
            'bpr': "BANKS_PER_RANK",
            'spb': "SUBARRAYS_PER_BANK",
            'num_rows': 'NUM_ROWS',
            'num_cols': 'NUM_COLS',
            'vf': 'VECTORIZATION_FACTOR',
            'device_type': 'DEVICE_TYPE'
        }




        self.inserted = set()


    def get_tuning_parameters(self):
        assert len(self.tuning_params) == len(self.concept_names), "Need to specify complete tuning params"
        return self.tuning_params



    def create_integer_param(self, _min, _max, power_of_two_only = False, key_name = None):
        assert not key_name is None
        assert self.concept_names[key_name] not in self.inserted
        int_param = None
        if power_of_two_only:
            int_param = PowerOfTwoParameter(self.concept_names[key_name], _min, _max)
        else:
            int_param = IntegerParameter(self.concept_names[key_name], _min, _max)
        self.inserted.add(self.concept_names[key_name])
        self.tuning_params.append(int_param)



    def add_num_ranks_tuning(self, _min, _max, power_of_two_only = True):
        self.create_integer_param(_min, _max, power_of_two_only = power_of_two_only, key_name = 'rank')

    def add_num_banks_per_rank_tuning(self, _min, _max, power_of_two_only = True):
        self.create_integer_param(_min, _max, power_of_two_only = power_of_two_only, key_name = 'bpr')

    def add_num_subarrays_per_bank_tuning(self, _min, _max, power_of_two_only = True):
        self.create_integer_param(_min, _max, power_of_two_only = power_of_two_only, key_name = 'spb')

    def add_num_rows_tuning(self, _min, _max, power_of_two_only = True):
        self.create_integer_param(_min, _max, power_of_two_only = power_of_two_only, key_name = 'num_rows')

    def add_num_cols_tuning(self, _min, _max, power_of_two_only = True):
        self.create_integer_param(_min, _max, power_of_two_only = power_of_two_only, key_name = 'num_cols')

    def add_VF_tuning(self, _min, _max, power_of_two_only = True):
        self.create_integer_param(_min, _max, power_of_two_only = power_of_two_only, key_name = 'vf')

    def add_device_type_tuning(self, device_types = []):
        assert len(device_types) > 0
        key_name = 'device_type'
        assert self.concept_names[key_name] not in self.inserted
        param = EnumParameter(self.concept_names[key_name], device_types)
        self.inserted.add(self.concept_names[key_name])
        self.tuning_params.append(param)


class PIMTuner(MeasurementInterface):
    def __init__(self, args):
        self.tuning_params = args.tuning_params
        self.num_knobs = len(args.tuning_params)

        objective = MinimizeTime()
        input_manager = FixedInputManager(size=self.num_knobs)

        super(PIMTuner, self).__init__(args, program_name="pim_tuning", input_manager=input_manager ,objective = objective)
        self.benchmark_name = args.benchmark_name
        self.evaluate_config_fn = args.evaluate_config_fn

    def manipulator(self):
        manipulator = ConfigurationManipulator()

        for param in self.tuning_params:
            manipulator.add_parameter(param)
        return manipulator

    def compile(self, cfg, id):
        try:
            run_result = self.evaluate_config_fn(cfg, self.benchmark_name)
            return Result(time=run_result['time'])
        except Exception as e:
            print("Returning Error", e)
            return Result(state='ERROR', time=float('inf'))



    def run(self, desired_result, input, limit):

        try:
            cfg = desired_result.configuration.data
            run_result = self.evaluate_config_fn(cfg, self.benchmark_name)
            return Result(time=run_result['time'])
        except Exception as e:
            print("Returning Error", e)
            return Result(state='ERROR', time=float('inf'))


    def run_precompiled(self, desired_result, input, limit, compile_result, id):

        try:
            cfg = desired_result.configuration.data
            run_result = self.evaluate_config_fn(cfg, self.benchmark_name)
            return Result(time=run_result['time'])
        except Exception as e:
            print("Returning Error", e)
            return Result(state='ERROR', time=float('inf'))

    def save_final_config(self, configuration):
        self.manipulator().save_to_file(configuration.data, 'opentuner_final_config.json')



def get_result_stats_from_pim_log_file(fname):
    with open(fname, "r") as StatFile:
        lines = StatFile.readlines()

    pim_command_stats = False
    for line in lines:
        if "PIM Command Stats" in line:
            pim_command_stats = True
            continue

        if pim_command_stats and "TOTAL" in line:
            line_split = line.strip().split()

            runtime = line_split[4]
            energy = line_split[5]
            gops_w = line_split[6]
            read_percent = line_split[7]
            write_percent = line_split[8]
            l_percent = line_split[9]
            return float(runtime),float(energy)


    assert False, "Unreachable"



def get_full_pim_result_stats_from_pim_log_files(compute_fname, datamovement_fname):
    with open(compute_fname, "r") as StatFile:
        lines = StatFile.readlines()

    stats = {

    }

    pim_command_stats = False
    for line in lines:
        if "PIM Command Stats" in line:
            pim_command_stats = True
            continue

        if pim_command_stats and "TOTAL" in line:
            line_split = line.strip().split()

            runtime = line_split[4]
            energy = line_split[5]
            gops_w = line_split[6]
            read_percent = line_split[7]
            write_percent = line_split[8]
            l_percent = line_split[9]

            stats['runtime'] = runtime
            stats['energy'] = energy
            stats['gops_w'] = gops_w
            stats['%R'] = read_percent
            stats["%W"] = write_percent
            stats["%L"] = l_percent

    with open(datamovement_fname, "r") as StatFile:
        lines = StatFile.readlines()

    pim_command_stats = False
    for line in lines:
        if "Data Copy Stats" in line:
            pim_command_stats = True
            continue

        if "PIM Command Stats" in line:
            pim_command_stats = False
            continue

        if pim_command_stats and "TOTAL" in line:
            line_split = line.split(":")[-1].strip().split()


            runtime = line_split[2]
            energy = line_split[6]

            stats['data_movement_runtime'] = runtime
            stats['data_movement_energy'] = energy


    return stats


def is_misaal_decl(line):
    tokens = line.split()
    if len(tokens) < 2:
        return False
    return tokens[1].startswith("misaal_node")


def compile_halide_benchmark(benchmark_name, cfg, perf_file_csv):
    tmp_dir = f"work_dir_{get_random_tempfile_name()}"
    os.mkdir(tmp_dir)
    try:
        VF = cfg['VECTORIZATION_FACTOR']
        RANK = cfg['RANK']
        BANKS_PER_RANK = cfg['BANKS_PER_RANK']
        SUBARRAYS_PER_BANK = cfg['SUBARRAYS_PER_BANK']
        NUM_ROWS = cfg['NUM_ROWS']
        NUM_COLS = cfg['NUM_COLS']
        VECTORIZATION_FACTOR = cfg['VECTORIZATION_FACTOR']
        DEVICE_TYPE = cfg['DEVICE_TYPE']

        GENERATOR_FILE_NAME = f"{tmp_dir}/{benchmark_name}_generator"
        RESULT_HEADER_FILE = f"{tmp_dir}/misaal_pim_lib.h"
        make_gen_cmd = f"g++ --std=c++17 -fno-rtti -O3 -DLOG2VLEN=7  -DVF={VF} -I /home/arnoor2/MISAAL/frontends/halide/distrib/include -I /home/arnoor2/MISAAL/frontends/halide/distrib/tools -g {benchmark_name}/src/{benchmark_name}_generator.cpp /home/arnoor2/MISAAL/frontends/halide/distrib/tools/GenGen.cpp hannk/common_halide.cpp -o {GENERATOR_FILE_NAME} -L /home/arnoor2/MISAAL/frontends/halide/distrib/lib -lHalide -lrt -ldl -lm -lz -lxml2"


        eq_sat_file = f"{benchmark_name}_{tmp_dir}_misaal*.py"

        compile_misaal_cmd = f"export LD_LIBRARY_PATH=/home/arnoor2/MISAAL/frontends/halide/distrib//lib;HL_EXPR_DEPTH=2  HYDRIDE_BENCHMARK={benchmark_name}_{tmp_dir}_misaal  PIM_HEADER_FILE={RESULT_HEADER_FILE} HL_ENABLE_MISAAL=1  MISAAL_EQ_SAT_ITERS=5 HL_ENABLE_HYDRIDE=1 HL_SYNTH_BW=16  HYDRIDE_INITIAL_HASH=\"empty_hash\"  MISAAL_DISABLE_FRONTEND_PATTERNS=1 COST_FILE_CSV_NAME={perf_file_csv} VF={VF} {GENERATOR_FILE_NAME} -t 0 -o {tmp_dir} -g {benchmark_name} -e cpp,h,stmt -f {benchmark_name} target=host-x86-64-no_bounds_query-no_asserts"

        compile_halide_runtime_cmd = f"HL_EXPR_DEPTH=2 HL_ENABLE_HYDRIDE=0 HL_DEBUG_CODEGEN=1  HL_SYNTH_BW=16  MISAAL_DISABLE_FRONTEND_PATTERNS=1 {GENERATOR_FILE_NAME} -r halide_runtime_x86 -o {tmp_dir} -e object,c_header target=host-x86-64-no_bounds_query-no_asserts"


        halide_cpp_fname = f"{tmp_dir}/{benchmark_name}.halide_generated.cpp"


        EXECUTABLE_NAME = f"{tmp_dir}/{benchmark_name}_run.out"
        gen_binary = f"g++ -DHALIDE_CPP_ALWAYS_USE_CPP_VECTORS -DFUSED -DVF={VF} -DNUM_RANKS={RANK} -DNUM_BPR={BANKS_PER_RANK} -DNUM_SPB={SUBARRAYS_PER_BANK} -DNUM_ROWS={NUM_ROWS} -DNUM_COLS={NUM_COLS} -Dbenchmark_{benchmark_name} --std=c++17 -O0 -march=native -mavx512vl -mavx512ifma -I /home/arnoor2/MISAAL/frontends/halide/distrib/include -I {tmp_dir} -I ./ -lstdc++ -ldl -pthread test/run.cpp test/stubs.cpp {halide_cpp_fname} -L ./ -lpimeval {tmp_dir}/halide_runtime_x86.o -o {EXECUTABLE_NAME}"


        success = execute_cmd(make_gen_cmd)
        if not success:
            return 100000

        success = execute_cmd(compile_misaal_cmd)
        if not success:
            return 100000
        success = execute_cmd(compile_halide_runtime_cmd)
        if not success:
            return 100000

        with open(RESULT_HEADER_FILE, "r") as KernelFile:
            kernel_lines = KernelFile.readlines()
        with open(halide_cpp_fname, "r") as InputFile:
            input_lines = InputFile.readlines()

        previous_line_misaal_decl = False
        output_lines = []

        for idx, line in enumerate(input_lines):
            if idx == 0:
                output_lines.append(line)
                continue

            if is_misaal_decl(input_lines[idx - 1]) and not is_misaal_decl(input_lines[idx]):
                output_lines += kernel_lines

            output_lines.append(line)
        with open(halide_cpp_fname, "w") as OutputFile:
            OutputFile.write(" ".join(output_lines))

        success =  execute_cmd(gen_binary)
        if not success:
            return 100000


        LOGFileName = f"{tmp_dir}/output_log.txt"
        with open(LOGFileName, "w+") as LogFile:
            print(f"./{EXECUTABLE_NAME}")
            print(f"pipe to {LOGFileName}")
            sb.call(f"./{EXECUTABLE_NAME}", shell = True, stdout = LogFile, stderr = LogFile)


        exec_time, energy = get_result_stats_from_pim_log_file(LOGFileName)
        sb.call(f"rm -rf {tmp_dir}", shell = True)
        sb.call(f"rm -rf {eq_sat_file}", shell = True)
        return exec_time
    except Exception as e:
        print(e)
        #sb.call(f"rm -rf {tmp_dir}", shell = True)
        return 100000

def compile_halide_benchmark_from_cfg_file(benchmark_name, cfg, perf_file_csv, copy_code_path = None):
    tmp_dir = f"work_dir_{get_random_tempfile_name()}"
    os.mkdir(tmp_dir)
    try:
        VF = cfg['VECTORIZATION_FACTOR']
        FILE=cfg['FILE']

        base_name = os.path.basename(FILE)
        cfg_base_name = os.path.splitext(base_name)[0]

        GENERATOR_FILE_NAME = f"{tmp_dir}/{benchmark_name}_generator"
        RESULT_HEADER_FILE = f"{tmp_dir}/misaal_pim_lib.h"
        make_gen_cmd = f"g++ --std=c++17 -fno-rtti -O3 -DLOG2VLEN=7  -DVF={VF} -I /home/arnoor2/MISAAL/frontends/halide/distrib/include -I /home/arnoor2/MISAAL/frontends/halide/distrib/tools -g {benchmark_name}/src/{benchmark_name}_generator.cpp /home/arnoor2/MISAAL/frontends/halide/distrib/tools/GenGen.cpp hannk/common_halide.cpp -o {GENERATOR_FILE_NAME} -L /home/arnoor2/MISAAL/frontends/halide/distrib/lib -lHalide -lrt -ldl -lm -lz -lxml2"


        eq_sat_file = f"{benchmark_name}_{tmp_dir}_misaal*.py"

        compile_misaal_cmd = f"export LD_LIBRARY_PATH=/home/arnoor2/MISAAL/frontends/halide/distrib//lib;HL_EXPR_DEPTH=2  HYDRIDE_BENCHMARK={benchmark_name}_{tmp_dir}_misaal  PIM_HEADER_FILE={RESULT_HEADER_FILE} HL_ENABLE_MISAAL=1  MISAAL_EQ_SAT_ITERS=5 HL_ENABLE_HYDRIDE=1 HL_SYNTH_BW=16  HYDRIDE_INITIAL_HASH=\"empty_hash\"  MISAAL_DISABLE_FRONTEND_PATTERNS=1 COST_FILE_CSV_NAME={perf_file_csv} VF={VF} {GENERATOR_FILE_NAME} -t 0 -o {tmp_dir} -g {benchmark_name} -e cpp,h,stmt -f {benchmark_name} target=host-x86-64-no_bounds_query-no_asserts"

        compile_halide_runtime_cmd = f"HL_EXPR_DEPTH=2 HL_ENABLE_HYDRIDE=0 HL_DEBUG_CODEGEN=1  HL_SYNTH_BW=16  MISAAL_DISABLE_FRONTEND_PATTERNS=1 {GENERATOR_FILE_NAME} -r halide_runtime_x86 -o {tmp_dir} -e object,c_header target=host-x86-64-no_bounds_query-no_asserts"


        halide_cpp_fname = f"{tmp_dir}/{benchmark_name}.halide_generated.cpp"


        EXECUTABLE_COMPUTE_NAME = f"{tmp_dir}/{benchmark_name}_compute_run.out"
        gen_compute_binary = f"g++ -DHALIDE_CPP_ALWAYS_USE_CPP_VECTORS -DPROFILE_COMPUTE=1 -DFUSED -DVF={VF} -DPIM_CFG_FILE={FILE} -Dbenchmark_{benchmark_name} --std=c++17 -O0 -march=native -mavx512vl -mavx512ifma -I /home/arnoor2/MISAAL/frontends/halide/distrib/include -I {tmp_dir} -I ./ -lstdc++ -ldl -pthread test/run.cpp test/stubs.cpp {halide_cpp_fname} -L ./ -lpimeval {tmp_dir}/halide_runtime_x86.o -o {EXECUTABLE_COMPUTE_NAME}"

        EXECUTABLE_DATA_NAME = f"{tmp_dir}/{benchmark_name}_data_run.out"
        gen_data_binary = f"g++ -DHALIDE_CPP_ALWAYS_USE_CPP_VECTORS -DPROFILE_DATA_MOVEMENT=1 -DVF={VF} -DPIM_CFG_FILE={FILE} -Dbenchmark_{benchmark_name} --std=c++17 -O0 -march=native -mavx512vl -mavx512ifma -I /home/arnoor2/MISAAL/frontends/halide/distrib/include -I {tmp_dir} -I ./ -lstdc++ -ldl -pthread test/run.cpp test/stubs.cpp {halide_cpp_fname} -L ./ -lpimeval {tmp_dir}/halide_runtime_x86.o -o {EXECUTABLE_DATA_NAME}"


        success = execute_cmd(make_gen_cmd)
        if not success:
            return 100000

        success = execute_cmd(compile_misaal_cmd)
        if not success:
            return 100000
        print("MISAAL COMPILATION SUCCESSFUL")
        success = execute_cmd(compile_halide_runtime_cmd)
        if not success:
            return 100000
        print("RUNTIME COMPILATION SUCCESSFUL")

        with open(RESULT_HEADER_FILE, "r") as KernelFile:
            kernel_lines = KernelFile.readlines()
        with open(halide_cpp_fname, "r") as InputFile:
            input_lines = InputFile.readlines()

        if copy_code_path is not None:
            # copy generated code for reference
            result_name = f"{copy_code_path}/{cfg_base_name}_{benchmark_name}_{VF}_header.h"
            execute_cmd(f"cp {RESULT_HEADER_FILE} {result_name}")

        previous_line_misaal_decl = False
        output_lines = []

        for idx, line in enumerate(input_lines):
            if idx == 0:
                output_lines.append(line)
                continue

            if is_misaal_decl(input_lines[idx - 1]) and not is_misaal_decl(input_lines[idx]):
                output_lines += kernel_lines

            output_lines.append(line)
        with open(halide_cpp_fname, "w") as OutputFile:
            OutputFile.write(" ".join(output_lines))

        success =  execute_cmd(gen_compute_binary)
        if not success:
            print("Failed to generate compute binary")
            return 100000

        success =  execute_cmd(gen_data_binary)
        if not success:
            print("Failed to generate data binary")
            return 100000





        LOGFileName = f"{copy_code_path}/{cfg_base_name}_{benchmark_name}_{VF}_compute_log"
        with open(LOGFileName, "w+") as LogFile:
            print(f"./{EXECUTABLE_COMPUTE_NAME}")
            print(f"pipe to {LOGFileName}")
            sb.call(f"./{EXECUTABLE_COMPUTE_NAME} {FILE}", shell = True, stdout = LogFile, stderr = LogFile)

        LOGFileName = f"{copy_code_path}/{cfg_base_name}_{benchmark_name}_{VF}_data_log"
        with open(LOGFileName, "w+") as LogFile:
            print(f"./{EXECUTABLE_DATA_NAME}")
            print(f"pipe to {LOGFileName}")
            sb.call(f"./{EXECUTABLE_DATA_NAME} {FILE}", shell = True, stdout = LogFile, stderr = LogFile)


        exec_time, energy = get_result_stats_from_pim_log_file(LOGFileName)
        sb.call(f"rm -rf {tmp_dir}", shell = True)
        sb.call(f"rm -rf {eq_sat_file}", shell = True)
        return exec_time
    except Exception as e:
        print(e)
        sb.call(f"rm -rf {tmp_dir}", shell = True)
        return 100000





def pim_eval_function(cfg, benchmark_name, copy_code_path = None):
    print(cfg)
    #{'RANK': 1, 'BANKS_PER_RANK': 2, 'SUBARRAYS_PER_BANK': 4, 'NUM_ROWS': 1024, 'NUM_COLS': 1024, 'VECTORIZATION_FACTOR': 64, 'DEVICE_TYPE': <PimDeviceEnum.PIM_DEVICE_BANK_LEVEL: 11>}
    RANK = cfg['RANK']
    BANKS_PER_RANK = cfg['BANKS_PER_RANK']
    SUBARRAYS_PER_BANK = cfg['SUBARRAYS_PER_BANK']
    NUM_ROWS = cfg['NUM_ROWS']
    NUM_COLS = cfg['NUM_COLS']
    VECTORIZATION_FACTOR = cfg['VECTORIZATION_FACTOR']
    DEVICE_TYPE = cfg['DEVICE_TYPE']
    FILE_NAME = cfg['FILE']
    csv_name = None
    GET_PERF = True
    if GET_PERF:
        try:
            valid = evaluate_config(device_type = DEVICE_TYPE, ranks = RANK, bpr = BANKS_PER_RANK, spb = SUBARRAYS_PER_BANK, num_rows = NUM_ROWS, num_cols = NUM_COLS, vf = VECTORIZATION_FACTOR, config_file = FILE_NAME)
            print("evaluate config returned", valid)
            if not valid:
                print("Not valid pim config returning early")
                return {'time': 1000000}
            csv_name = get_csv_name(device_type = DEVICE_TYPE, ranks = RANK, bpr = BANKS_PER_RANK, spb = SUBARRAYS_PER_BANK, num_rows = NUM_ROWS, num_cols = NUM_COLS, vf = VECTORIZATION_FACTOR, config_file = FILE_NAME)
            print("CSV Produced for ", csv_name)
        except Exception as e:
            print("Error in get perf", e)
            return {'time': 1000000}

    if FILE_NAME is not None:
        pim_execution_time  = compile_halide_benchmark_from_cfg_file(benchmark_name, cfg, csv_name, copy_code_path = copy_code_path)
    else:
        pim_execution_time = compile_halide_benchmark(benchmark_name, cfg, csv_name)

    if  csv_name is not None and os.path.exists(csv_name):
        os.remove(csv_name)

    print(f"Execution time for {cfg}: {pim_execution_time}")

    return {'time' : pim_execution_time}




if __name__ == "__main__":
    tuner_gen = TunerGen()



    tuner_gen.add_num_ranks_tuning(1, 16)
    tuner_gen.add_num_banks_per_rank_tuning(1, 16)
    tuner_gen.add_num_subarrays_per_bank_tuning(1, 16)
    tuner_gen.add_num_rows_tuning(1024, 4096)
    tuner_gen.add_num_cols_tuning(1024, 4096)
    tuner_gen.add_VF_tuning(256, 4096)
    tuner_gen.add_device_type_tuning(device_types = [PimDeviceEnum.PIM_DEVICE_BANK_LEVEL])



    argparser = opentuner.default_argparser()

    parsed_args = argparser.parse_args()
    parsed_args.tuning_params = tuner_gen.get_tuning_parameters()
    parsed_args.evaluate_config_fn = pim_eval_function
    parsed_args.benchmark_name = "convolution"


    pim_tuner = PIMTuner(parsed_args)
    PIMTuner.main(parsed_args)
