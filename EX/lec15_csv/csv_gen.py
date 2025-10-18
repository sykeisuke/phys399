#!/usr/bin/env python3
import os
import numpy as np
import pandas as pd

OUT_DIR = "data/"
N_FILES = 1000          
N_ROWS = 100            
N_COLS = 2              
LOW, HIGH = 1, 10000    

os.makedirs(OUT_DIR, exist_ok=True)

rng = np.random.default_rng(42)  

for i in range(1, N_FILES + 1):
    fname = os.path.join(OUT_DIR, f"run{i:04d}.csv")
    arr = rng.integers(LOW, HIGH + 1, size=(N_ROWS, N_COLS))
    df = pd.DataFrame(arr, columns=["val1", "val2"])
    df.to_csv(fname, index=False)

print(f"Done: generated {N_FILES} files in {OUT_DIR}")

