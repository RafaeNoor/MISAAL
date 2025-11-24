import glob
import os, time


test_files = glob.glob("./test_*.rkt")
test_files += glob.glob("./verify_*.rkt")
print("Files to remove", len(test_files))

import subprocess as sb

for file in test_files:
    is_older_than_hour = (time.time() - os.path.getctime(file)) > 3600
    if is_older_than_hour:
        sb.run(f"rm {file}", shell = True)
