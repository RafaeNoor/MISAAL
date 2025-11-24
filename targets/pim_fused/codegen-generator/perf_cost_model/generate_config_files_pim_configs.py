from GenPimFusedCost import evaluate_config
import os
import glob
import concurrent.futures
import sys

pim_eval_path = "/home/arnoor2/pim-eval/PIMeval-PIMbench-2.0/"

config_files_root_path = os.path.join(pim_eval_path, "configs", "asplos")

config_files = glob.glob(f"{config_files_root_path}/*.cfg")

dse_files_root_path = os.path.join(pim_eval_path,"configs/asplos/Design-Space/bank-simd/")

config_files += glob.glob(f"{dse_files_root_path}/*.cfg")

#config_files = glob.glob(f"{dse_files_root_path}/*.cfg")
#config_files = glob.glob("aquabolt_cost_model/*.cfg")
config_files = ['/home/arnoor2/pim-eval/PIMeval-PIMbench-2.0/configs/asplos/PIMeval_Bank_Rank20.cfg']

print("Config Files", config_files)

#VFS = [pow(2,i) for i in range(3, 25)]

VFS = [32768*2]

def worker(datum):
    cfg , VF = datum
    evaluate_config(config_file = cfg, vf = VF)

POOL_SIZE = 8

if True:
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=POOL_SIZE)
    for VF in  VFS:
        for cfg in config_files:
            if "AiM" in cfg:
                continue

            pool.submit(worker, (cfg, VF))
    pool.shutdown(wait=True)

else:
    for VF in  VFS:
        for cfg in config_files:
            if "AiM" in cfg:
                continue
            worker((cfg, VF))


