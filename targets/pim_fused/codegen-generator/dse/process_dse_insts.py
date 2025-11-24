import glob
import json

log_dir = 'dse_logs'

benchmark = "histogram"

header_files = glob.glob(f"{log_dir}/*{benchmark}*header.h")
print("Num headers: ", len(header_files))

def create_histogram(data):
    histogram = {}
    for file_, ops in data.items():
        for op in ops:
            if op not in histogram:
                histogram[op] = 0
            histogram[op] += 1
    return histogram

distribution = {}

for file_ in header_files:
    print(file_)

    with open(file_, "r") as File:
        content = File.readlines()

    ops = set()

    for line in content:
        line = line.strip()
        if line.startswith("test_") or line.startswith("comb"):
            op_name = line.split("(")[0]
            ops.add(op_name)
    distribution[file_] = list(ops)



print(json.dumps(distribution, indent = 4))

histogram = create_histogram(distribution)
print(json.dumps(histogram, indent = 4))


