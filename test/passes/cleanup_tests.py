#!/usr/bin/env python3
import os
import shutil
import glob

def cleanup_test_artifacts(test_dir):
    """
    Clean up test artifacts in the given directory.
    This includes:
    - __pycache__ directories
    - work directory
    - .log files
    - .json files
    - .rkt files
    
    Args:
        test_dir: The directory to clean up
    """
    # Remove __pycache__ directories
    pycache_dirs = glob.glob(os.path.join(test_dir, "**/__pycache__"), recursive=True)
    for pycache in pycache_dirs:
        if os.path.exists(pycache):
            print(f"Removing {pycache}")
            shutil.rmtree(pycache)
    
    # Remove work directory
    work_dir = os.path.join(test_dir, "work")
    if os.path.exists(work_dir):
        print(f"Removing {work_dir}")
        shutil.rmtree(work_dir)
    
    # Remove .log files
    log_files = glob.glob(os.path.join(test_dir, "*.log"))
    for log_file in log_files:
        if os.path.exists(log_file):
            print(f"Removing {log_file}")
            os.remove(log_file)
    
    # Remove .json files
    json_files = glob.glob(os.path.join(test_dir, "*.json"))
    for json_file in json_files:
        if os.path.exists(json_file):
            print(f"Removing {json_file}")
            os.remove(json_file)

    # Remove .rkt files
    rkt_files = glob.glob(os.path.join(test_dir, "*.rkt"))
    for rkt_file in rkt_files:
        if os.path.exists(rkt_file):
            print(f"Removing {rkt_file}")
            os.remove(rkt_file)

if __name__ == "__main__":
    # Get the directory containing this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("Cleaning up all test artifacts...")
    cleanup_test_artifacts(current_dir)
    print("Cleanup complete!") 