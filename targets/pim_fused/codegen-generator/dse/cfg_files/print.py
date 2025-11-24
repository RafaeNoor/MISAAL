import glob

files = glob.glob("*.cfg")
for f in files:
    print(f.split(".")[0])

