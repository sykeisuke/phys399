#!/bin/bash
conda env create -f environment.yml
conda activate phys399
python -m ipykernel install --user --name phys399 --display-name "Python (phys399)"

echo "======================================"
echo "PHYS399 environment has been installed"
echo "Activate with: conda activate phys399"
echo "Then launch Jupyter Notebook or Lab."
echo "======================================"
