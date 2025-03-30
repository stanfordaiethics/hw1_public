# CS 281. Homework 1. Machine Bias

## Setting the environment

Follow the steps below to install anaconda and create the environment for running the starter code.

1. Download anaconda from https://www.anaconda.com/ and install
2. Create a new environment that has all the dependencies installed, e.g., if you decide to name this new
   environment `cs281-hw1`, run the command

```bash
conda create -n cs281-hw1 python=3.8 -y
conda activate cs281-hw1
cd hw1_public
pip install -r requirements.txt  # Run this from root of the repo.
```

## Starter Code
All starter code related to the first homework is in `hw1.ipynb`. Your code should directly go in this file.

You should include your responses to the free-form questions in the jupyter notebook, within a markdown cell.

To launch the notebook, simply run
```bash
conda activate cs281-hw1
cd hw1_public
jupyter notebook hw1.ipynb
```

## Submission

To submit your work to gradescope, export your jupyter notebook, `hw1.ipynb` as a PDF file. You can do this by navigating to `File > Save and Export Notebook As > PDF`. For coding and written questions, make sure your final answer is clearly visible in the PDF you submit. 
<!-- Running the following will generate hw1.zip which contains hw1.ipynb
```bash
bash make_submission.sh
``` -->
Submit the PDF file to Gradescope.


