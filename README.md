# Code & File Repository for PHYS399

This repository contains Python and C++ code files used in the **PHYS399 class**.

## How to Clone the Repository

1. Open a terminal on your computer.
2. Navigate to the directory where you want to clone the project.
3. Run the following command:

   ```bash
   git clone https://github.com/kyoshiha/phys399.git
   cd phys399
   ```

## Environment Setup (Conda)

We use a dedicated conda environment named phys399 for this course.
The setup script setup.sh will create and configure it for you.
	1.	Make sure Anaconda or Miniconda is installed.
	2.	In the project directory, run:
   ```bash
   source setup.sh
   ```

This will execute the following steps:
   ```bash
   conda env create -f environment.yml
   conda activate phys399
   python -m ipykernel install --user --name phys399 --display-name "Python (phys399)"
   ```
After this, Jupyter Notebook / JupyterLab will allow you to select the kernel Python (phys399).

## Notes

If you already have an environment named phys399, you may need to remove it first:
  ```bash
  conda env remove -n phys399
  ```
The environment file environment.yml specifies all required dependencies for the course.
