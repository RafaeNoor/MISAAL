import glob
import pandas as pd
import os
import sys
import json
import argparse

class PimPerfAnalyzer:
    def __init__(self, pim_csvs_dir: str):
        self.pim_csvs_dir = pim_csvs_dir
        self.pim_csvs = glob.glob(os.path.join(pim_csvs_dir, "*.csv"))

        self.perf_data = {}


    def get_different_vf_data(self, device_name: str, rank: str, bpr: str, spb: str, rows: str, cols: str):
        # Index into self.perf_data[device_name][rank][bpr][spb][rows][cols]

        # convert rank, bpr, spb, rows, cols to str
        rank = str(rank)
        bpr = str(bpr)
        spb = str(spb)
        rows = str(rows)
        cols = str(cols)
        vf_data = {}
        # Assert keys exist in required order
        assert device_name in self.perf_data, "Device name not found"

        assert rank in self.perf_data[device_name], "Rank not found"
        assert bpr in self.perf_data[device_name][rank], "BPR not found"
        assert spb in self.perf_data[device_name][rank][bpr], "SPB not found"
        assert rows in self.perf_data[device_name][rank][bpr][spb], "Rows not found"
        assert cols in self.perf_data[device_name][rank][bpr][spb][rows], "Cols not found"
        vf_data = self.perf_data[device_name][rank][bpr][spb][rows][cols]
        return vf_data

    def gen_misaal_perf_json(self):
        """
        Generate a JSON file with the following format
        {
            "op_name" : {
                "vf" : {
                    "energy_improvement" : 0.0,
                    "perf_improvement" : 0.0
                }
            }
        }
        """
        print(f"Generating MISAAL cost model for {len(self.perf_data)} devices")
        for device_name in self.perf_data.keys():
            for rank in self.perf_data[device_name].keys():
                for bpr in self.perf_data[device_name][rank].keys():
                    for spb in self.perf_data[device_name][rank][bpr].keys():
                        for rows in self.perf_data[device_name][rank][bpr][spb].keys():
                            for cols in self.perf_data[device_name][rank][bpr][spb][rows].keys():
                                print(f"Processing {device_name} rank{rank} bpr{bpr} spb{spb} rows{rows} cols{cols}")
                                vf_data = self.perf_data[device_name][rank][bpr][spb][rows][cols]
                                vectorization_factors = list(vf_data.keys())

                                op_dict = {}
                                print(f"    Processing vectorization factors {vectorization_factors}")
                                for vf in vectorization_factors:
                                    print(f"    Processing vectorization factor {vf}")
                                    # Get data for this VF
                                    df = vf_data[vf]
                                    # print column names
                                    # Group by operation name and get first row of improvements
                                    grouped = df.groupby('OP_NAME').agg({
                                        'Energy (mJ)_IMPROVEMENT': 'first',
                                        'Execution Time (ms)_IMPROVEMENT': 'first',
                                        'Energy (mJ)_FUSED': 'first',
                                        'Execution Time (ms)_FUSED': 'first',
                                        'Energy (mJ)_UNFUSED': 'first',
                                        'Execution Time (ms)_UNFUSED': 'first',
                                    }).reset_index()
                                    #     Column names: ['OP_NAME', 'Energy (mJ)_FUSED', 'Energy (mJ)_UNFUSED', 'Energy (mJ)_IMPROVEMENT', 'Execution Time (ms)_FUSED', 'Execution Time (ms)_UNFUSED', 'Execution Time (ms)_IMPROVEMENT', 'GOPS/W_FUSED', 'GOPS/W_UNFUSED', 'GOPS/W_IMPROVEMENT', '%R_FUSED', '%R_UNFUSED', '%R_IMPROVEMENT', '%W_FUSED', '%W_UNFUSED', '%W_IMPROVEMENT', '%L_FUSED', '%L_UNFUSED', '%L_IMPROVEMENT']
                                    # Convert to dictionary format
                                    for _, row in grouped.iterrows():
                                        if row['OP_NAME'] not in op_dict:
                                            op_dict[row['OP_NAME']] = {}
                                        op_dict[row['OP_NAME']][vf] = {
                                            "energy_improvement": row['Energy (mJ)_IMPROVEMENT'],
                                            "perf_improvement": row['Execution Time (ms)_IMPROVEMENT'],
                                            "fused": {
                                                "energy": row['Energy (mJ)_FUSED'],
                                                "perf": row['Execution Time (ms)_FUSED'],

                                            },
                                            "unfused": {
                                                "energy": row['Energy (mJ)_UNFUSED'],
                                                "perf": row['Execution Time (ms)_UNFUSED'],

                                            }
                                        }

                                SUMMARY_DIR_PATH = "./MISAAL_COST_MODEL"
                                if not os.path.exists(SUMMARY_DIR_PATH):
                                    os.makedirs(SUMMARY_DIR_PATH)
                                fpath = os.path.join(SUMMARY_DIR_PATH, f"{device_name}_rank{rank}_bpr{bpr}_spb{spb}_rows{rows}_cols{cols}.json")
                                print(f"Writing MISAAL cost model to {fpath}")
                                with open(fpath, "w+") as f:
                                    json.dump(op_dict, f, indent=4)



    def measure_impact_of_vf_changes(self):

        SUMMARY_DIR_PATH = "./VF_Summary"
        if not os.path.exists(SUMMARY_DIR_PATH):
            os.makedirs(SUMMARY_DIR_PATH)

        for device_name in self.perf_data.keys():
            for rank in self.perf_data[device_name].keys():
                for bpr in self.perf_data[device_name][rank].keys():
                    for spb in self.perf_data[device_name][rank][bpr].keys():
                        for rows in self.perf_data[device_name][rank][bpr][spb].keys():
                            for cols in self.perf_data[device_name][rank][bpr][spb][rows].keys():
                                print(f"Processing {device_name} rank{rank} bpr{bpr} spb{spb} rows{rows} cols{cols}")
                                vf_data = self.get_different_vf_data(device_name, rank, bpr, spb, rows, cols)
                                vectorization_factors = list(vf_data.keys())
                                if len(vectorization_factors) < 2:
                                    print(f"Only one vectorization factor found for {device_name} rank{rank} bpr{bpr} spb{spb} rows{rows} cols{cols}")
                                    continue
                                print(f"Vectorization Factors: {vectorization_factors}")
                                vf_impact_df = self.check_if_vf_changes_speedup(vf_data)
                                #print(vf_impact_df)
                                vf_impact_df.to_csv(os.path.join(SUMMARY_DIR_PATH, f"{device_name}_rank{rank}_bpr{bpr}_spb{spb}_rows{rows}_cols{cols}.csv"), index=False)
                                #sys.exit()


    def check_if_vf_changes_speedup(self, vf_data):
        # vf_data is a dictionary of dataframes
        op_dict = {}
        op_names = []
        vectorization_factors = list(vf_data.keys())
        for vf in vectorization_factors[:1]:
            op_names = vf_data[vf]['OP_NAME'].unique().tolist()




        for op_name in op_names:
            op_dict[op_name] = {}
            for vf in vectorization_factors:
                op_vf_data = vf_data[vf][vf_data[vf]['OP_NAME'] == op_name]
                energy_improvement = op_vf_data['Energy (mJ)_IMPROVEMENT'].values[0]
                perf_improvement = op_vf_data['Execution Time (ms)_IMPROVEMENT'].values[0]
                op_dict[op_name][vf] = {
                    'energy_improvement': energy_improvement,
                    'perf_improvement': perf_improvement
                }

            # check if the speedup is different for different VFs
            # if it is, return True
            # if it is not, return False
            for vf in vectorization_factors:
                op_vf_data = op_dict[op_name][vf]


        """
        {'2':                  OP_NAME  Energy (mJ)_FUSED  Energy (mJ)_UNFUSED  ...  %L_FUSED  %L_UNFUSED  %L_IMPROVEMENT
0  comb_0_fused_pim_op_0           0.000064             0.000062  ...      2.96        1.35        0.456081
        """



        NEW_HEADERS = ["OP_NAME"]
        for vf in vectorization_factors:
            NEW_HEADERS.append(f"Fusion_Energy_Improvement_vf{vf}")
            NEW_HEADERS.append(f"Fusion_Perf_Improvement_vf{vf}")


        # Create a new dataframe with the new headers
        new_df = pd.DataFrame(columns=NEW_HEADERS)
        for op_name in op_dict.keys():
            new_row = [op_name]
            for vf in vectorization_factors:
                new_row.append(op_dict[op_name][vf]['energy_improvement'])
                new_row.append(op_dict[op_name][vf]['perf_improvement'])

            #entry = {NEW_HEADERS[0]: op_name}
            entry = {}
            for i in range(0, len(NEW_HEADERS)):
                entry[NEW_HEADERS[i]] = new_row[i]
            #print("new_row: ",new_row)
            #print("entry: ",entry)
            new_df = new_df.append(entry, ignore_index=True)



        return new_df









    def process_perf(self):
        print(f"Processing {len(self.pim_csvs)} PIM CSV files")
        for pim_csv in self.pim_csvs:
            #print(pim_csv)
            file_name = os.path.basename(pim_csv)
            file_name_example = "pim_perf_results_devicePIM_DEVICE_BANK_LEVEL_rank1_BPR1_SPB4_rows16_cols4096_vf32.csv"
            config_file_name_example = "pim_perf_results_config_bank-simd_mem-gddr_ranks-20_banks-32_subarr-32_rows-1024_cols-1024_vf32768.csv"

            if "config" in file_name:
                device_name = file_name.split("_rank")[0].split("config_")[-1]
                rank = file_name.split("ranks-")[-1].split("_")[0]
                bpr = file_name.split("banks-")[-1].split("_")[0]
                spb = file_name.split("subarr-")[-1].split("_")[0]
                rows = file_name.split("rows-")[-1].split("_")[0]
                cols = file_name.split("cols-")[-1].split("_")[0]
                vf = file_name.split("_vf")[1].split(".csv")[0]
            else:
                device_name = file_name.split("_rank")[0].split("_device")[1]
                #print("Device Name: ",device_name)


                rank = file_name.split("_rank")[1].split("_BPR")[0]

                #print("Rank: ",rank)
                bpr = file_name.split("_BPR")[1].split("_SPB")[0]
                #print("BPR: ",bpr)
                spb = file_name.split("_SPB")[1].split("_rows")[0]
                #print("SPB: ",spb)
                rows = file_name.split("_rows")[1].split("_cols")[0]
                #print("Rows: ",rows)
                cols = file_name.split("_cols")[1].split("_vf")[0]
                #print("Cols: ",cols)
                vf = file_name.split("_vf")[1].split(".csv")[0]
                #print("VF: ",vf)

            if device_name not in self.perf_data:
                self.perf_data[device_name] = {}
            if rank not in self.perf_data[device_name]:
                self.perf_data[device_name][rank] = {}
            if bpr not in self.perf_data[device_name][rank]:
                self.perf_data[device_name][rank][bpr] = {}
            if spb not in self.perf_data[device_name][rank][bpr]:
                self.perf_data[device_name][rank][bpr][spb] = {}
            if rows not in self.perf_data[device_name][rank][bpr][spb]:
                self.perf_data[device_name][rank][bpr][spb][rows] = {}
            if cols not in self.perf_data[device_name][rank][bpr][spb][rows]:
                self.perf_data[device_name][rank][bpr][spb][rows][cols] = {}
            if vf not in self.perf_data[device_name][rank][bpr][spb][rows][cols]:
                self.perf_data[device_name][rank][bpr][spb][rows][cols][vf] = pd.read_csv(pim_csv)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Utility for analyzing PIM performance")
    parser.add_argument("-g","--generate-misaal-cost", action="store_true", help="Generate MISAAL cost model")
    parser.add_argument("-m","--measure-vf-changes", action="store_true", help="Measure the impact of vectorization factor changes")
    args = parser.parse_args()

    pim_csvs_dir = "./perf_logs"
    analyzer = PimPerfAnalyzer(pim_csvs_dir)
    analyzer.process_perf()

    if args.measure_vf_changes:
        analyzer.measure_impact_of_vf_changes()

    if args.generate_misaal_cost:
        analyzer.gen_misaal_perf_json()






