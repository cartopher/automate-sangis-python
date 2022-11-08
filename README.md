# Automate SanGIS using Python  
Manually downloading countless files onto our operating systems is repetitive, inefficient, and expensive. But it doesn't have to be that way. Python offers a way to cut costs considerably by streamlining and automating these time-consuming processes. In this demonstration, I outline how to use Python's "twill" package to access and navigate the SanGIS/SANDAG GIS Data Warehouse website so we can download and extract multiple ZIP files to our operating system. While at the same time, we automate how we want our output directories structured each time we run the program, making it easy to locate the files we are looking for, lending itself nicely to code reproducibility. The script below is modularized and thoroughly explains how each process is executed so that you can quickly learn how to implement it into your project activities.

### Overview of twill's Python API ###  
The Python package "twill," is based on requests and lxml packages and is described as a simplified scripting language developed for programmatic or automated website navigation through a command-line interface. You may use twill to navigate websites that employ forms, cookies, and other standard Web features. Moreover, twill provides excellent support for both MySQL and PostgreSQL database management tasks.

For more about the 'twill' package, see:  
twill Project Description (https://pypi.org/project/twill/)  
twill Overview (https://twill-tools.github.io/twill/overview.html)  
twill’s Python API (https://twill-tools.github.io/twill/python-api.html#python-api)

## Installation

You will learn how to install a conda environment from a .yml file that contains a list of desired Python packages.

*__Note__: If you prefer to use an existing virtual environment, all you need to do is run the ‘pip install twill’ command.*

The list of commands used:
````
cd {repository path}
conda env create -f environment.yml
conda env list
conda activate sangisdownload
conda list
````
To download the automate-sangis-python repository and install the downloadsangis environment, you will need to follow these steps:

Download 'automate-sangis-python' repository (ZIP) to your preferred directory.
- This repository contains all the modules to run the automation process and a file called 'environment.yml,' which includes the instructions to install the environment.
Open the Anaconda Terminal on your computer.
 In the Terminal, set your directory using cd to change directories (e.g., C:\Users\name\PycharmProjects\automate-sangis-python-main\automate-sangis-python-main).
Once you are in the directory, you can create your environment. To do this run: 
conda env create -f environment.yml.
 Confirm the environment was created by printing a list of all conda environments available on your machine by running: conda env list.
Once the environment is installed, you can activate it using:  conda activate downloadsangis.
 To view a list of all Python packages installed in this environment, run: conda list.
