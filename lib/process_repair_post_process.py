import json
import os

target = "x86"

pass_path = "RepairRelavancePostProcess_PASS_{}_VERSION_V4.json".format(target)
fail_path = "RepairRelavancePostProcess_FAIL_{}_VERSION_V4.json".format(target)
error_path = "RepairRelavancePostProcess_ERROR_{}_VERSION_V4.json".format(target)

def process_path(path, category):

    if not os.path.exists(path):
        return

    data = {}

    with open(path, "r") as ReadFile:
        data = json.load(ReadFile)

    result_data = {}

    print("*****", category)

    for key in data:
        tokens = key.split("+")
        src_inst = tokens[0]
        target_inst = tokens[1]

        if not src_inst in result_data:
            result_data[src_inst] = []

        result_data[src_inst].append(target_inst)

    print(json.dumps(result_data, indent = 4))



process_path(pass_path, "PASS")
#process_path(fail_path, "FAIL")
#process_path(error_path, "ERROR")
