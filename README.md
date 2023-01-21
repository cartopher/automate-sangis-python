# Python for GIS Data Automation: Downloading Large Datasets
The python script uses the twill package to programmatically access and download large GIS datasets from a website. 

### Overview of twill's Python API ###  
The Python package twill, is based on `requests` and `lxml` packages and is described as a simplified scripting language developed for programmatic or automated website navigation through a command-line interface. You may use twill to navigate websites that employ forms, cookies, and other standard Web features. Moreover, twill provides excellent support for both MySQL and PostgreSQL database management tasks.

## Installation

In this documentation, I am walking you through how to configure and run this project using PyCharm IDE. I will add more walkthroughs using Jupyter Notebooks and Virtual Studio Code later and will provide links for those walkthroughs here.

In this section, you will learn how to install a conda environment from a .yml file that contains a list of desired Python packages.

*__Note__: If you prefer to use an existing virtual environment, all you need to do is run the ‘pip install twill’ command.*

The list of commands used:
````
cd {repository path}
conda env create -f environment.yml
conda env list
conda activate sangisdownload
conda list
````
To download the `automate-sangis-python` repository and install the `sangisdownload` environment, you will need to follow these steps: 

__1.__ Download `automate-sangis-python` repository (ZIP) to your preferred directory and extract its contents. 
- This repository contains all the modules to run the automation process, in addition to a file called `environment.yml`, which contains a list of required packages and dependencies that are all installed during the environment creation process, as described below.

__2.__ Open the Anaconda Terminal on your computer.
- To create the environment required to run this project, you must set your directory to where you downloaded the `automate-sangis-python` project using cd to change directories. 

__3.__ In the Terminal, set your directory using cd to change directories (e.g., `cd C:/Users/name/PycharmProjects/automate-sangis-python-main`). 

__4.__ Once you are in the directory, you can create your environment. To do this run: 
`conda env create -f environment.yml`. 
- This process will take no more than 3 minutes as all of the packages found in the `sangisdownload` environment need to be downloaded and installed.

__5.__ Confirm the environment was created by printing a list of all conda environments available on your machine by running: `conda env list`. 

__6.__ Once the environment is installed, you can activate it by running: `conda activate sangisdownload`. 

__7.__ View a list of all Python packages installed in this environment, run: `conda list`.

__8.__ Navigate to the directory where you saved and extracted the repository and open the `automate-sangis-python-main` as a new project in PyCharm.

*__Important Note__: After opening the project in PyCharm, a pop-up message on the lower right corner of the screen notifies you that "__Python 3.# (sangisdownload) has been configured as a project interpreter"__.  If this is the case, you can skip the entire __'Getting Set Up with PyCharm'__ section and go straight to the __'Script Overview'__ section. 

__9.__ Open the `sangis_credentials.py` Python file (located on the left of the PyCharm screen) and input your username and password used to access the SanGIS/SANDAG GIS Data Warehouse website. See below: 

````
# Store credentials into string variables
username = 'INPUT EMAIL'
password = 'INPUT PASSWORD'
````

__10.__ Next, open the `sangis_download.py` module and analyze the code. 
- Refer to the __Script Overview__ section to help guide your understanding of the main module's logic. 

Upon completing the steps above, you have successfully downloaded the entire project repository, created an environment, installed all required packages, and opened the project with all the correct configurations. If, for any reason, you need to add the project interpreter manually, proceed to the __'Getting Set Up using PyCharm'__ section and follow the instructions. 

## Getting Set Up using PyCharm

The next step is to __Add a New Python Intrepreter__ for this project. 

__1.__ On the lower right corner of your PyCharm screen, click where it says __'Python 3.# (base)'__, to open a drop-down menu and select __'Add New Interpreter'__, and then select __'Add Local Intrepreter...'__. 
- The window for __'Add Python Interpreter'__ will pop up and you will see a list of Interpreters/Environments on the left. 

__2.__ Select `Conda Environment` and a list of configuration options will appear. 

__3.__ At the top of the list where it says __'Interpreter:'__, select the down arrow on the right of this setting and a dropdown menu appears. 

- The window for __'Add Python Interpreter'__ will pop up, and you will notice a list of Interpreters/Environments on the left. 

__4.__ At the top of the list where it says __'Interpreter:'__, select the down arrow on the right of this setting, and a dropdown menu appears. 

__5.__ Locate the environment you created for this project (`sangisdownload`) and select it. 

- Leave all the other settings as default unless you want to specify your __'Python version'__ for this project. 

__Important:__ It is recommended that you use Python versions 3.7-3.10 to execute this project successfully. 

__6.__ Press __'OK'__ to apply these settings. 

- It may take a moment for PyCharm to apply the new Interpreter. 

You are now ready to run the code. The following two sections will assist you in becoming acquainted with the entire project and its contents so that you have a better understanding of the overall workflow.

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
  
__1.__ The "date-stamped" output directory is generated and named after the year and month in which the main module is executed (for example, `2022_09`), this means a new date-stamped output directory will be created and named after every month.

__2.__ In the case of the `Current` output directory, the extracted contents from the previous download month are replaced every month; however, this occurs only if the extracted files have the same name.

__3.__ Lastly, if for any reason the main module is ran more than once a month, all downloaded files with the same name in both the `YYYY_MM` and `Current`  output directories will be overwritten.

In short, __*every month*__, we want to __*archive*__ the previous months __*unextracted*__ zipped files in a `YYYY_MM` output directory, and we want to __*overwrite*__ the __*extracted*__ contents in the `Current` output directory.

This might not be very clear now, but it will make more sense after we review the entire program's functionality below. 

## Script Overview

### Important Imports
*__Notice__ the bottom import is called `sangis_credentials`; this is the name of the Python file that contains our login credentials for accessing the SanGIS/SANDAG GIS Data Warehouse website. Importing the module allows us to access and use those variables in our main module. We carry out this process in the `login_credentials()` method below.*

````
# import packages
import os
import time
import zipfile
from twill.commands import *
from twill import browser

# import sangis_credentials.py module
import sangis_credentials

def login_credentials():
    """Browses to data source website,
       Call the 'sangis_credentials' module to input login credentials"""
    # Talk to the web browser directly,
    go('https://rdw.sandag.org/Account/Login')
    showforms()

    # input login credentials
    fv("1", "ctl00$MainContent$Email", sangis_credentials.username)
    fv("1", "ctl00$MainContent$Password", sangis_credentials.password)
    submit('0')
````
### Class Object & Constructor Method  
Create a SanGISDownload Class Object & Encapsulate all Methods and Variables.
````
class SanGISDownload:
    directory = None
    filename = None
    current_month_folder = None

    # create class constructor with two arguments
    def __init__(self, directory, filename):
        """SanGISDownload  Class Constructor,
           :param self: pass 'self' to access variables coming from the constructor,
           :param directory: output file path (string),
           :param filename: output filename(s) (string)"""

        # initialize class variables
        self.directory = directory
        self.filename = filename
````
### build_directory() Method   
Now that we have created our Class Constructor,, we are free to accesss and modify our Class Objects Attributes in our Methods.
For out first Class Method, we will build out directories to ensure all ZIP files are downloaded and organized into specific output directories.
````
 def build_directory(self):
        """Creates "date-stamped" subdirectories,
           Changes the current working directory to output file path,
           :current_month_folder: a Class Variable containing the file path to the date-stamped subdirectories"""

        # modify attribute properties
        directory_path = self.directory
        # store the current year and month to a variable
        current_month = time.strftime("%Y_%m")

        # create a new directory (folder) if it does not already exist
        if os.path.isdir(directory_path + current_month):
            print("Directory already exists")
        else:
            print("Creating directory for you")
            os.mkdir(directory_path + current_month)

        # change the current working directory to the date-stamped subdirectory,
        os.chdir(directory_path + current_month)

        # assign the current working directory
        directory = os.getcwd()

        # reassign the current working directory to a class variable
        self.current_month_folder = directory

        # Print the new current working directory
        print(directory)    
````
### process_download() Method  
Class Method for Downloading ZIP File(s).
````
    def process_download(self):
        """Browsing while logged in,
           Initialize the download process"""

        # navigate to the zip file download page
        go("gisdtview.aspx?dir=Parcel")
        go("GetFSFile.aspx?dir=Parcel&Name=" + self.filename)

        # create a file object,
        # open file for writing in binary format,
        # overwrite the file if it exists,
        # if the file does not exist, create new file for writing
        with open(self.filename, "wb") as bf:
            bf.write(browser.dump)
````
### extract_zipfile() Method  
Class Method for extracting ZIP file(s).
````    
    def extract_zipfile(self):
        """Creates a new folder directory specifically for extraction,
           Extracts ZIP file contents to new directory"""
        # pass filename with path to extract
        # open file using read permission that we want to extract it
        myzip = zipfile.ZipFile(
            self.current_month_folder + "\\" + self.filename, 'r')

        # extract zip file contents to a new folder
        myzip.extractall(self.directory + "Current")

        # close the zip file
        myzip.close()

        # display the filename
        print(self.filename)
````        
### process_sangis() Method  
Here, we build a Class Method to Handle Exceptions (errors) that occur during our Runtime (execution) of the program. We Handle these Expections gracefully using Try and Exception Statements. For Example, if the Try Block Raises an Exception, the Except Block will Return the Exception that may be caused by the Try Block.  
````
    def process_sangis(self):
        """try block: contains the code that may cause the exception,
           except block: returns the exception that may be caused by the try block."""
        try:
            self.build_directory()
        except Exception as e:
            print("Exception when trying to change directory.")
            print(print(str(e)))
            return

        try:
            login_credentials()
        except Exception as e:
            print("Exception when trying to go to the specified URL.")
            print(print(str(e)))
            return

        try:
            self.process_download()
        except Exception as e:
            print("Exception when trying to download ZIP file.")
            print(print(str(e)))
            return

        try:
            self.extract_zipfile()
        except Exception as e:
            print("Exception when trying to extract ZIP file.")
            print(print(str(e)))
            return
````
### main() Method  
We define the main method and use it to run each line serially from the top of the entire module.  

__Important:__ Be sure to modify the directory paths to reflect your own (e.g., `C:/Users/name/PycharmProjects/automate-sangis-python-main/output/Parcels`). Failure to do so would raise an exception as it would return the following message __'Exception when trying to change directory.'__ and the code will not execute.
````
def main():
    directory1 = '{INPUT DIRECTORY PATH}'
    download1 = SanGISDownload(directory1, "Assessor_Book.zip")
    download1.process_sangis()

    # display the first directory
    print(directory1)
    print('Download 1: Complete!')

    directory2 = '{INPUT DIRECTORY PATH}'
    download2 = SanGISDownload(directory2, "PARCELS_EAST.zip")
    download2.process_sangis()

    # display the second directory
    print(directory2)
    print("Download 2: Complete!")


if __name__ == '__main__':
    main()
````

## Conclusion
We conclude this demonstration by running the program to see that we've successfully downloaded and extracted two ZIP files (`Assessor_Book.zip`, and `PARCELS_EAST.zip`) into our preferred file locations on our operating system. I just shared with you a valuable tool to help simplify your workflow processes by removing complex steps in your data collection and handling management processes to improve workflow efficiency and power up productivity.
