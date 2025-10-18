#!/bin/bash
mkdir results
for f in data/run000*.csv; do
#for f in data/run*.csv; do
    echo "Processing $f"
    python3 analyze.py "$f" > "results/$(basename $f .csv).txt"
done
