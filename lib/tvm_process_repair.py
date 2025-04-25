import json
import os

target = "x86"

int_file = f"RepairRelavanceIntermediates_{target}_intermediate_results.py"
v4_file = f"RepairRelavanceV4_{target}_intermediate_results.py"

files = [int_file, v4_file]

def process_path(path):
    print(path)

    if not os.path.exists(path):
        return {}

    data = {}

    with open(path, "r") as ReadFile:
        data = json.load(ReadFile)

    result_data = {}


    for key in data:
        tokens = key.split("+")
        src_inst = tokens[0]
        target_inst = tokens[1]

        if not src_inst in result_data:
            result_data[src_inst] = []

        result_data[src_inst].append(target_inst)

    return result_data


def merge_dict(d1, d2):

    merged = {}

    for key in d1:
        d1_result = d1[key]

        d2_result = []

        if key in d2:
            d2_result = d2[key]

        merged[key] = list(set(d1_result + d2_result))

    for key in d2:
        if key in d1:
            continue

        merged[key] = d2[key]

    return merged

starting_dict = {}

for f in files:
    result = process_path(f)
    starting_dict = merge_dict(result, starting_dict)

print(json.dumps(starting_dict, indent = 4))

with open(f"tvm_repair_forward_map_{target}.json", "w+") as OutFile:
    OutFile.write(json.dumps(starting_dict, indent = 4))
