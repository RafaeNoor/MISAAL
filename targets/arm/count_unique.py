import json
import glob

files = glob.glob("EqClassEqualDepthV4*intermediate_results.py")
files += glob.glob("LowerSwizzles*.py")

print(files)

count = 0

for f in files:
    with open(f, "r") as PatFile:
        dict_ = json.load(PatFile)
        count += len([key for key in dict_])

print("Total count:", count)

