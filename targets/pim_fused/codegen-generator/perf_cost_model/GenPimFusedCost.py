from PIM_API_UTILS import PimDeviceEnum, PIM_CONFIG, get_device_type_name
import itertools
import os
import subprocess as sb
import time
from utils.DSLInstructionUtils import get_random_tempfile_name
import concurrent.futures
import argparse
import glob


def get_template(ranks = 1, bpr = 1, spb = 1, rows = 1, cols = 1, device_type_str="None", config_file = None):
    if config_file is not None:
        return f"""
#include "libpimeval.h"
#include "get_perf_stats.h"

    int main(){{
        pimCreateDeviceFromConfig(PIM_FUNCTIONAL, \"{config_file}\");
        get_perf();
        return 0;
    }}
    """

    return f"""
#include "libpimeval.h"
#include "get_perf_stats.h"

int main(){{
    unsigned numRanks = {ranks};
    unsigned numBankPerRank = {bpr};
    unsigned numSubarrayPerBank = {spb};
    unsigned numRows = {rows};
    unsigned numCols = {cols};
    PimStatus status = pimCreateDevice({device_type_str}, numRanks, numBankPerRank, numSubarrayPerBank, numRows, numCols);
    get_perf();
    return 0;
}}
"""


def get_validity_template(ranks = 1, bpr = 1, spb = 1, rows = 1, cols = 1, device_type_str="None", config_file = None):
    if config_file is not None:
        return f"""
#include "libpimeval.h"
#include <stdio.h>

int main(){{
    pimCreateDeviceFromConfig(PIM_FUNCTIONAL, \"{config_file}\");
    if (status != PIM_OK)  return -1;
    return 0;
}}
    """
    return f"""
#include "libpimeval.h"
#include <stdio.h>

int main(){{
    unsigned numRanks = {ranks};
    unsigned numBankPerRank = {bpr};
    unsigned numSubarrayPerBank = {spb};
    unsigned numRows = {rows};
    unsigned numCols = {cols};
    PimStatus status = pimCreateDevice({device_type_str}, numRanks, numBankPerRank, numSubarrayPerBank, numRows, numCols);
    if (status != PIM_OK)  return -1;
    return 0;
}}
    """

def is_valid_pim_config(device_type = PimDeviceEnum.PIM_DEVICE_BANK_LEVEL, ranks = 1, bpr = 1, spb = 1, num_rows = 1, num_cols = 1, config_file = None):
    cpp_eval_template = get_validity_template(ranks = ranks, bpr = bpr, spb = spb, rows = num_rows, cols = num_cols, device_type_str = get_device_type_name(device_type), config_file = config_file)
    PREFIX = get_random_tempfile_name()

    CPP_FILE_NAME = f"{PREFIX}_valid.cpp"
    with open(CPP_FILE_NAME, "w+") as CppFile:
        CppFile.write(cpp_eval_template)
    BINARY_NAME = f"{PREFIX}.out"
    COMPILE_CMD = f"g++ {CPP_FILE_NAME} -DUNFUSED=1 -L./ -lpimeval -o {BINARY_NAME}"

    LOG_NAME = f"{PREFIX}.log"
    with open(LOG_NAME, "w+") as LogFile:
        return_code = sb.call(COMPILE_CMD, shell = True)
        EXEC_CMD = f"./{BINARY_NAME}"
        return_code = sb.call(EXEC_CMD, shell = True, stdout=LogFile, stderr=LogFile)




    with open(LOG_NAME, "r") as LogFile:
        content = LogFile.read()


    CLEAN_UP_FILES = [CPP_FILE_NAME, BINARY_NAME, LOG_NAME]
    for fname in CLEAN_UP_FILES:
        rm_cmd = f"rm -rf {fname}"
        #print(rm_cmd)
        sb.call(rm_cmd, shell = True)


    return "Error" not in content






def gen_cost_csv():
    DEVICE_TYPES = [PimDeviceEnum.PIM_DEVICE_BANK_LEVEL,PimDeviceEnum.PIM_DEVICE_BITSIMD_V_AP]
    RANKS = [1,2,4,8,16]
    BANKS_PER_RANKS = [2 ** i for i in range(6)]
    SUBARRAYS_PER_BANK = [2 ** i for i in range(6)]
    NUM_ROWS = [2 ** i for i in range(11) if (2 ** i) % 2 == 0]
    NUM_COLS = [2 ** i for i in range(15) if (2 ** i) % 2 == 0]
    VF = [2 ** i for i in range(1,15) if  (2**i) < 1024]

    SINGLE_TEST=True
    if SINGLE_TEST:
        DEVICE_TYPES = [PimDeviceEnum.PIM_DEVICE_BANK_LEVEL]
        RANKS = [4]
        BANKS_PER_RANKS = [128]
        SUBARRAYS_PER_BANK = [32]
        NUM_ROWS = [1024]
        NUM_COLS = [8192]
        VF = [1024]

    EXIST_TEST=False

    COUNT_COMBINATIONS = False
    global counter
    counter = 0

    # pim_perf_results_devicePIM_DEVICE_BANK_LEVEL_rank1_BPR1_SPB1_rows32_cols4096_vf32.csv
    if EXIST_TEST:
        DEVICE_TYPES = [PimDeviceEnum.PIM_DEVICE_BANK_LEVEL]
        RANKS = [1]
        BANKS_PER_RANKS = [1]
        SUBARRAYS_PER_BANK = [1]
        NUM_ROWS = [32]
        NUM_COLS = [4096]
        VF = [32]


    COMBINE = [DEVICE_TYPES, RANKS, BANKS_PER_RANKS, SUBARRAYS_PER_BANK, NUM_ROWS, NUM_COLS]

    POOL_SIZE = 8

    if COUNT_COMBINATIONS:
        POOL_SIZE = 1

    def worker(combination):
        # Check if valid
        (device_type, ranks, bpr, spb, num_rows, num_cols) = combination

        if COUNT_COMBINATIONS or is_valid_pim_config(device_type = device_type, ranks = ranks, bpr = bpr, spb = spb, num_rows = num_rows, num_cols = num_cols):

            print("VALID CONFIG", combination)
            # Loop over vector sizes
            for vf in VF:
                if not COUNT_COMBINATIONS:
                    evaluate_config(device_type = device_type, ranks = ranks, bpr = bpr, spb = spb, num_rows = num_rows, num_cols = num_cols, vf = vf)
                else:
                    global counter
                    counter += 1

        else:
            print("INVALID CONFIG", combination)

    pool = concurrent.futures.ThreadPoolExecutor(max_workers=POOL_SIZE)
    for idx, combination in enumerate(itertools.product(*COMBINE)):
        (device_type, ranks, bpr, spb, num_rows, num_cols) = combination
        pool.submit(worker, combination)

    pool.shutdown(wait=True)
    print("Completed compiling pool...")
    print(f"Number of possible combinations {counter} ")



def get_csv_name(device_type = PimDeviceEnum.PIM_DEVICE_BANK_LEVEL, ranks = 1, bpr = 1, spb = 1, num_rows = 1, num_cols = 1, vf = 1, config_file = None):

    pim_config = PIM_CONFIG(device_type = device_type, num_ranks = ranks, num_banks_per_rank = bpr, num_subarray_per_bank = spb, num_rows = num_rows, num_cols = num_cols, vf = vf, config_file = config_file)
    cpp_eval_template = get_template(ranks = ranks, bpr = bpr, spb = spb, rows = num_rows, cols = num_cols, device_type_str =  get_device_type_name(device_type), config_file = config_file)

    LOG_DIR = "./perf_logs"
    pim_config.set_work_dir(LOG_DIR)

    # First check if file already exists, if so we can early exit
    result_path = pim_config.get_perf_csv_output_path()
    return result_path




def evaluate_config(device_type = PimDeviceEnum.PIM_DEVICE_BANK_LEVEL, ranks = 1, bpr = 1, spb = 1, num_rows = 1, num_cols = 1, vf = 1, config_file = None):

    print("evaluate_config ivoked")
    pim_config = PIM_CONFIG(device_type = device_type, num_ranks = ranks, num_banks_per_rank = bpr, num_subarray_per_bank = spb, num_rows = num_rows, num_cols = num_cols, vf = vf, config_file = config_file)
    print("config object created")
    cpp_eval_template = get_template(ranks = ranks, bpr = bpr, spb = spb, rows = num_rows, cols = num_cols, device_type_str = get_device_type_name(device_type), config_file = config_file)
    print("Eval template:", cpp_eval_template)

    LOG_DIR = "./perf_logs"
    pim_config.set_work_dir(LOG_DIR)

    # First check if file already exists, if so we can early exit
    result_path = pim_config.get_perf_csv_output_path()
    print("result_path:", result_path)
    if os.path.exists(result_path):
        print(f"{result_path} already exists ... early exit")
        return True


    PREFIX = get_random_tempfile_name()
    CPP_FILE_NAME = f"{PREFIX}_test.cpp"
    with open(CPP_FILE_NAME, "w+") as CppFile:
        CppFile.write("// Automatically generated file")
        CppFile.write(cpp_eval_template)

    if not os.path.exists(LOG_DIR):
        os.mkdir(LOG_DIR)

    FUSED_LOG_PATH = f"./{PREFIX}_fused_log.txt"
    UNFUSED_LOG_PATH = f"./{PREFIX}_unfused_log.txt"

    SETTINGS = [
        ("UNFUSED", UNFUSED_LOG_PATH),
        ("FUSED", FUSED_LOG_PATH),
    ]

    BINARY_NAME = f"{PREFIX}.out"

    CLEAN_UP_FILES = [FUSED_LOG_PATH, UNFUSED_LOG_PATH, BINARY_NAME, CPP_FILE_NAME, BINARY_NAME]

    for target, fpath  in SETTINGS:
        try:
            # Compile with fused implementation
            with open(fpath, "w+") as LogFile:
                COMPILE_CMD = f"g++ {CPP_FILE_NAME} -D{target}=1 -DVF={vf} -L./ -lpimeval -o {BINARY_NAME}"

                cmd = f"rm {BINARY_NAME}"
                sb.call(cmd, shell = True)
                compile_start = time.time()
                cmd = COMPILE_CMD
                print(cmd, "to", fpath)
                sb.call(cmd, shell = True)
                compile_end = time.time()
                cmd = f"./{BINARY_NAME}"
                return_code = sb.call(cmd, stdout = LogFile, stderr = LogFile)
                exec_end = time.time()
                compile_time = compile_end - compile_start
                exec_time = exec_end - compile_end
                print(f"Compilation took {compile_time} seconds and execution took {exec_time} seconds")

                if return_code != 0:
                    print("Errored out!")
                    for fname in CLEAN_UP_FILES:
                        rm_cmd = f"rm {fname}"
                        print(rm_cmd)
                        sb.call(rm_cmd, shell = True)
                    return False
        except Exception as e:
            print(e)

            for fname in CLEAN_UP_FILES:
                rm_cmd = f"rm {fname}"
                print(rm_cmd)
                sb.call(rm_cmd, shell = True)
            with open("ErrorLog.txt", "a+") as ErrFile:
                ErrFile.write(f"Failed for {pim_config.get_perf_csv_name()}\n")
            return False


    print("Processing Logs to generate CSV!")
    pim_config.generate_perf_csv(fused_stats_path = FUSED_LOG_PATH, unfused_stats_path =  UNFUSED_LOG_PATH)


    for fname in CLEAN_UP_FILES:
        rm_cmd = f"rm {fname}"
        print(rm_cmd)
        sb.call(rm_cmd, shell = True)

    return True















if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Utility for generating pIM Fused Cost Models for different PIM configurations")
    parser.add_argument("-g","--generate-pim-cost",  action="store_true", help="Invoke PIMeval framework to generate stats csv for various PIM configuration and vectorization factors")
    args = parser.parse_args()

    if args.generate_pim_cost:
        gen_cost_csv()


