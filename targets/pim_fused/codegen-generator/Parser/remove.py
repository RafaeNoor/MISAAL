import glob
import subprocess as sb

files = glob.glob("test_test_enum*.rkt")
files += glob.glob("verify_test_enum*.rkt")
print(len(files))

for f in files:
    sb.call(f"rm {f}", shell = True)
