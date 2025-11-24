from PIM_TUNER_UTILS import get_full_pim_result_stats_from_pim_log_files
import pandas as pd
import os
import glob

log_dir = "dse_logs"
benchmark = "histogram"

compute_files_hist = glob.glob(f"{log_dir}/*{benchmark}*_compute_log")
print(compute_files_hist)


global_dict = {}

for file in compute_files_hist:
    try:
        config_base_name = os.path.basename(file).split("_compute_log")[0]
        print(config_base_name)
        compute_file = file
        data_movement_file = file.replace("compute_log","data_log")
        stats = get_full_pim_result_stats_from_pim_log_files( compute_file, data_movement_file)
        global_dict[config_base_name] = stats
        print(stats)
    except:
        continue

df = pd.DataFrame(global_dict).transpose()
print(df)
df.to_csv(f'{benchmark}_dse.csv', index=True)

