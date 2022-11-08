# Automate SanGIS using Python  
Manually downloading countless files onto our operating systems is repetitive, inefficient, and expensive. But it doesn't have to be that way. Python offers a way to cut costs considerably by streamlining and automating these time-consuming processes. In this demonstration, I outline how to use Python's `twill` package to access and navigate the SanGIS/SANDAG GIS Data Warehouse website so we can download and extract multiple ZIP files to our operating system. While at the same time, we automate how we want our output directories structured each time we run the program, making it easy to locate the files we are looking for, lending itself nicely to code reproducibility. The script below is modularized and thoroughly explains how each process is executed so that you can quickly learn how to implement it into your project activities.

### Overview of twill's Python API ###  
The Python package twill, is based on `requests` and `lxml` packages and is described as a simplified scripting language developed for programmatic or automated website navigation through a command-line interface. You may use twill to navigate websites that employ forms, cookies, and other standard Web features. Moreover, twill provides excellent support for both MySQL and PostgreSQL database management tasks.

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

__1.__ Download `automate-sangis-python` repository (ZIP) to your preferred directory and extract its contents. 
- This repository contains all the modules to run the automation process and a file called `environment.yml`, which includes the instructions to install the environment. 

__2.__ Open the Anaconda Terminal on your computer.
- To create the environment required to run this project, you must set your directory to where you downloaded the `automate-sangis-python` project using cd to change directories. 

__3.__ In the Terminal, set your directory using cd to change directories (e.g., ` cd C:\Users\name\PycharmProjects\automate-sangis-python-main\automate-sangis-python-main`). 

__4.__ Once you are in the directory, you can create your environment. To do this run: 
`conda env create -f environment.yml`. 

__5.__ Confirm the environment was created by printing a list of all conda environments available on your machine by running: `conda env list`. 

__6.__ Once the environment is installed, you can activate it by running: `conda activate downloadsangis`. 

__7.__ View a list of all Python packages installed in this environment, run: `conda list`.

Upon completing the following steps, you have successfully downloaded the entire repository and created an environment containing the `twill` package and all of its dependencies required to execute the code successfully. 

## Package Overview

#### Modules #####
| Module | Description |  
| --- | --- |  
| `sangis_download.py` | The main module that runs the entire process |  
| `sangis_credentials.py` | A module used to secure sensative information from being visible |  
| `__init__.py` | A module used to mark directories on a disk as Python package directories |  

#### Directories ####

| Parent Output  | Description |  
| --- | --- |  
| `output`  | The parent directory that contains multiple subdirectories |  
| `Parcels` | A subdirectory of the output used for storing and extracting parcel files |  

#### Subdirectories ####

| Child Output | Description |  
| --- | --- |  
| `YYYY_MM`  | A generated subdirectory, and the download working directory for unextracted zipped files |  
| `Current` | A generated subdirectory, and the download working directory for extracted zipped files |  
  
  
__Important__: There are a few instances you should keep in mind about the child output directories.  
  
  
__1.__ The "date-stamped" output directory is generated and named after the year and month in which the main module is executed (for example, __2022_09__), this means a new date-stamped output directory will be created and named after every month.

__2.__ In the case of the __'Current'__ output directory, the extracted contents from the previous download month are replaced every month; however, this occurs only if the extracted files have the same name.

__3.__ Lastly, if for any reason the main module is ran more than once a month, all downloaded files with the same name in both the __'YYYY_MM'__ and __'Current'__  output directories will be overwritten.

In short, __*every month*__, we want to __*archive*__ the previous months __*unextracted*__ zipped files in a __*YYYY_MM*__ output directory, and we want to __*overwrite*__ the __*extracted*___ contents in the __'Current'__ output directory.

This might not be very clear now, but it will make more sense after we review the entire program's functionality below. 

