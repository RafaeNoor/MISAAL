#!/bin/bash
#
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --job-name=test_vec_add
#SBATCH --account=25sp-cs526d-eng   # <- replace "account_name" with an account available to you
#SBATCH --partition=eng-instruction
#SBATCH --output=o.%j
#SBATCH --constraint=G8358
#SBATCH --time=03:00:00
##SBATCH --error=e_check_prop.%j
##SBATCH --mail-user=is16@illinois.edu     # <- replace "NetID" with your University NetID
##SBATCH --mail-type=BEGIN,END
#
# End of embedded SBATCH options
#

python test_vec_add.py

