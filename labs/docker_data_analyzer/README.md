# Docker Lab 2: Python Data Analyzer

## Overview
In this lab, you'll containerize a Python application that analyzes CSV data files, performs statistical operations, and generates reports.



## Files Structure
```
data_analyzer/
├── src/
│   ├── analyzer.py
│   ├── utils.py
│   └── __init__.py
├── data/
│   └── sample.csv
├── requirements.txt
└── README.md
```



### Create Dockerfile

Your task is to create a Dockerfile that:
- Uses an appropriate Python base image
- Installs the required dependencies 
- Sets up the application files
- Creates appropriate directories for data and output
- Uses volumes for data input and output
- Sets environment variables
- Runs the data analyzer when the container starts

## Lab Tasks

1. Create a Dockerfile that containerizes the Python data analyzer application
2. Build and run the Docker container
3. Verify the analysis works by checking the output directory
4. Experiment with different environment variables
5. Improve the Dockerfile for production use
