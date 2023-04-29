"""ex_5_4.py"""
import numpy as np
from pathlib import Path

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root

# Use these predefined paths.  Note: automated tests expect these paths
# Changing these paths will cause tests to fail.

root_dir = get_repository_root()
data_dir = root_dir / "data"
output_dir = root_dir / "outputs"
input_file = data_dir / "ex_5_4-data.csv"
output_file = output_dir / "ex_5_4-processed.csv"

aray1 = np.loadtxt(input_file)

# fd = np.where(fd<0, 0, fd)
for i in range(len(aray1)):
    if aray1[i]<0:
        aray1[i]=0


np.savetxt(output_file, aray1, fmt='%.2e')
