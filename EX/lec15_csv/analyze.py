#!/usr/bin/env python3
import sys
import pandas as pd
import os

if len(sys.argv) < 2:
    print("Usage: python3 analyze.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]
if not os.path.exists(input_file):
    print(f"Error: {input_file} not found")
    sys.exit(1)

df = pd.read_csv(input_file)

if df.shape[1] < 2:
    print(f"Error: {input_file} must have at least two columns")
    sys.exit(1)

df["sum"] = df.iloc[:, 0] + df.iloc[:, 1]
mean_sum = df["sum"].mean()

print(f"{os.path.basename(input_file)}: mean(sum) = {mean_sum:.2f}")
