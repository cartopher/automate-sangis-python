# Empower Your GIS Workflow with Automated Data Retrieval

In this documentation, I will outline how to automate and streamline the repetitive, inefficient, and costly process of manually downloading multiple files from the web onto our operating systems. Rather than downloading files over HTTP with Python Requests, I will explain an alternative solution for accessing, navigating, downloading, and extracting multiple files while automating the output directory structure for easy file retrieval and code reproducibility.

## Overview of twill's Python API

Twill is a Python package that allows for automating web browsing tasks. It allows you to script interactions with a web browser, such as filling out forms, navigating pages, and clicking links. Twill can be used for tasks such as web scraping, functional testing of web applications, and automating repetitive tasks on websites. It uses a command-line interface and a Python API to interact with a web browser, and can be used to automate interactions with web pages in a way that mimics a human user. It is also designed to work well with other Python packages such as Beautiful Soup for parsing HTML and lxml for parsing XML. Twill can be installed using pip package installer by running "pip install twill" in the command line.

For more about the 'twill' package, see:
- [twill Project Description](https://pypi.org/project/twill/)
- [twill Overview](https://twill-tools.github.io/twill/overview.html)
- [twill’s Python API](https://twill-tools.github.io/twill/python-api.html#python-api)

## Project Structure

In this project, we aimed to automate the process of downloading and storing multiple GIS files from the SanGIS/SANDAG GIS Data Warehouse. For your reference, I have outlined the project structure with descriptions for the modules and directories within the project package.

### Top Level Folders

**Content Root**
- Contains the entire repository

### Namespace Package

**automate-file-downloads-main**
- Contains a collection of modules and subdirectories for the project
- Important: You will import the content root (top folder) into PyCharm. Do not import the namespace package!

### Environments

- environments.yml: A list of packages and dependencies that are installed and configured for the project
- requirements.txt: A list of packages for the project
- PyCharm should automatically set up the Anaconda Virtual Environment and configure the interpreter when you import the automate-file-downloads-main folder as the content root. If this does not happen, refer to the instructions for manual setup in the sections below.

### Modules

- automate_downloads.py: The main module that runs the entire project
- __init__.py: A module used to mark directories on a disk as Python package directories
- credentials.py: A module used to secure sensitive information from being visible within the main module
  - Important: Please note that a more secure way of storing your credentials is to save them in a configuration file and then invoke them as parameters in your code. If you do not already have one, you will need to register for a SanGIS/SANDAG GIS Data Warehouse account ([Register Here](https://rdw.sandag.org/Account/Register)). Once registered, you will need to store your account login credentials as variables in the credentials.py to prevent them from being displayed in the main module.

See below:

```
# store credentials into variables
email = 'INPUT EMAIL'
password = 'INPUT PASSWORD'
```

### Directories

**Root Directory**
- output: The output directory that contains multiple subdirectories

**Parent Directory**
- Parcels: A subdirectory of the output used for storing and extracting parcel zip files
- After executing the script, both child folders (see directly below) are created for both parent folders (see above).

**Child Directories**
- YYYY_MM: A generated output subdirectory of Parcels, and the download working directory for unextracted zip files
- Current: A generated output subdirectory of Parcels, and the download working directory for extracted zip files
- The YYYY_MM output subdirectory, also referred to as the "date-stamped" output subdirectory, is generated and named based on the year and month in which the main module is run (for example, 2023_02). This results in the creation of a new date-stamped output subdirectory each month the script is executed.
- The Current output subdirectory is where the contents of the previously extracted files from the previous month are replaced with the newer versions from the current month, but only if the file names are identical.
- To summarize, every month, we want to archive the previous month's unextracted zip files in a YYYY_MM output subdirectory, and we want to overwrite the extracted contents in the Current output subdirectory. This process will be clearer after reviewing the overall function of the program.

## Getting Started

1. Download automate-file-downloads repository to your downloads folder on your computer and extract its contents.
 - Important: A new window may open after you extract the file. You MUST exit this window before proceeding to step 2.
 
2. Open the content root (repository) automate-file-downloads-main as a new project in PyCharm.
 - Tip: From the downloads folder, right-click automate-file-downloads-main and select 'Open with' and choose 'PyCharm'.
 - When you open a project in PyCharm, it will first look for a virtual environment associated with that project and set the interpreter accordingly. This process, which includes activating the environment and installing any necessary packages and dependencies, may take a few minutes. A successful setup will be indicated by the message "Python 3.* (base) (2) has been configured as a project interpreter" in the bottom-right corner of the PyCharm window.
 - If you need to manually set up the project, proceed to the next section titled "Manually Setting the Project."
 - If not, you have successfully set up the project and can proceed to the "Script Overview" section to begin analyzing the script.

# Manually Activating the Project Environment

## List of commands used in this section:

```shell
cd {repository path}
conda env create -f environment.yml
conda env list
conda activate sangisdownload
conda list
```

The following steps explain how to download the repository and set up the virtual environment from the `.yml` file using the Anaconda prompt. The `environment.yml` contains a list of packages and dependencies required to execute this project.

1. Download the `automate-file-downloads` repository to your downloads folder and extract its contents.
2. Open the Anaconda prompt on your computer.
3. Use the `cd` command in Anaconda prompt to navigate to your project directory (e.g., `cd C:/Users/name/PycharmProjects/automate-sangis-python-main`).
4. Create your environment by running: `conda env create -f environment.yml`.
   Note: This process may take up to 3 minutes.
5. Verify that the environment was created by running: `conda env list`.
6. Activate the environment by running: `conda activate sangisdownload`.
7. Check that all necessary packages and dependencies have been installed by running: `conda list`.

# Manually Configuring the PyCharm Interpreter

The next steps explain how to add a new Python interpreter for this project in PyCharm.

1. Go to your project directory (downloads) and open the `automate-file_downloads-main` as a new project in PyCharm by right-clicking on the repository and selecting the option to "Open with PyCharm."
2. In the lower right corner of your PyCharm screen, open the drop-down menu by clicking on the "Python 3.# (base)" text, then select the option "Add New Interpreter." From there, choose "Add Local Interpreter...". A window will appear, allowing you to select the "Conda Environment" option on the left to view the configuration options.
3. In the top of the list, there is an "Interpreter:" option. By clicking the arrow on the right of this setting, you can view a drop-down menu of available virtual environments. Select the environment you created for this project (sangisdownload) from this list. Unless you have a specific reason to do so, you can leave all the other settings as the default.
   Note: Only Python versions 3.7-3.10 will execute this project successfully.
4. Click 'OK' to confirm these settings. This process may take a moment to complete, but afterwards, your PyCharm is ready to run the code with the new interpreter.

# Script Overview

The code below is a Python script that uses the `twill` package to automate the process of logging into a website. The script imports the `twill` package, along with the `os`, `time`, and `zipfile` packages, and a module named `sangis_credentials`.

The script defines a function called `login_credentials()`, which uses the `twill` package's `go()` and `showforms()` functions to navigate to the login page of a website, and the `fv()` and `submit()` functions to fill in and submit the login form. The script uses the `sangis_credentials` module to import the login credentials and fill in the form fields with them.

```python
import os  # For interacting with the operating system
import time  # For sleeping to wait for the page to load
import zipfile  # For handling zip files
from twill.commands import *  # For importing all the commands from twill package
from twill import browser  # For importing the browser object from twill package

import credentials  # For importing login credentials

def login_credentials():
    """
    Logs in to the website using the login credentials from the 'sangis_credentials' module
    """
    go('https://rdw.sandag.org/Account/Login')  # Navigate to the login page
    showforms()  # Display the forms on the current page

    fv("1", "ctl00$MainContent$Email", credentials.email)  # Input the email in the form field
    fv("1", "ctl00$MainContent$Password", credentials.password)  # Input the password in the form field
    submit('0')  # submit the login form
```

The code below is a Python class named `SanGISDownload` that's used to download files from a website. The class contains three class variables: `directory`, `filename`, and `current_month_folder`, which are used to store the directory where the files will be saved, the name of the file, and the current month folder respectively.

The class also has an `__init__` method, which is called when an instance of the class is created. The method accepts two parameters: `directory` and `filename`. The parameters passed to the method are assigned to the class variables, `self.directory` and `self.filename`. These class variables are then used to specify the location and the name of the file that will be downloaded.

It's worth mentioning that the `current_month_folder` class variable is not being used in the `__init__` method; it's being left as `None`.

```python
class SanGISDownload:
    """
    A class used to download files from a website
    """
    directory = None  # Variable to store the directory where the files will be saved
    filename = None  # Variable to store the name of the file
    current_month_folder = None  # Variable to store the current month folder

    def __init__(self, directory, filename):
        """
        Initialize the class variables with the provided directory and filename
        """
        self.directory = directory  # Assign the directory to the class variable
        self.filename = filename  # Assign the filename to the class variable
```

The code below is a method named `change_directory` that's added to the class `SanGISDownload`. The method is used to change the current working directory to a new directory.

The method starts by defining a variable `directory_path` that's assigned the value of the class variable `self.directory`. This variable is used to store the path to the directory where the files will be saved.

It then creates a variable `current_month` that's assigned the current month using the `time.strftime()` function. The function takes a format string as an argument, in this case `%Y_%m`, that returns a string representing the date in the format of "year_month" (e.g., "2021_01").

It then checks if the directory `directory_path + current_month` already exists using the `os.path.isdir()` function. If the directory exists, it prints "Directory already exists." else it creates a new directory using the `os.mkdir()` function with the directory path of `directory_path + current_month` and prints "Creating directory for you."

The method then changes the current working directory to the new directory using `os.chdir()` function and passing the directory path of `directory_path + current_month`. It then gets the current working directory using `os.getcwd()` and assigns the value to a variable `directory`.

It then assigns the value of the variable `directory` to the class variable `self.current_month_folder`.

Finally, it prints the current working directory, which should be the new directory that was

 just created.

```python
    def change_directory(self):
        """
        Method to change the current working directory to a new directory
        """
        directory_path = self.directory  # Get the directory path from the class variable

        current_month = time.strftime("%Y_%m")  # Get the current month

        # Check if the directory already exists
        if os.path.isdir(directory_path + current_month):
            print("Directory already exists.")
        else:
            print("Creating directory for you.")
            os.mkdir(directory_path + current_month)  # Create the new directory

        os.chdir(directory_path + current_month)  # Change the current working directory

        directory = os.getcwd()  # Get the current working directory

        self.current_month_folder = directory  # Assign the current working directory to the class variable

        print(directory)  # Print the current working directory
```

The method below is used to download and save a file from a website. It starts by navigating to the webpage containing the file using the `go()` command from the `twill` package. It takes two arguments, the first one is the URL of the webpage and the second one is the file name, in this case `self.filename`, which is passed as a parameter when creating an instance of the class.

It then opens a new file with the specified name and writes the contents of the webpage to the file using `with open(self.filename, "wb") as bf:`. It opens the file in binary write mode and assigns it to the variable `bf`. The contents of the webpage is written to the file using the `bf.write()` method, passing the `browser.dump` variable as an argument.

```python
    def process_download(self):
        """
        Method to download and save a file from a website
        """
        # Navigate to the webpage containing the file
        go("gisdtview.aspx?dir=Parcel")
        go("GetFSFile.aspx?dir=Parcel&Name=" + self.filename)

        # Open a new file with the specified name and write the contents of the webpage to the file
        with open(self.filename, "wb") as bf:
            bf.write(browser.dump)
```

The method below is used to extract the contents of a zip file. It starts by opening the zip file with the specified name, in this case `self.filename`, and reads it using the `zipfile.ZipFile()` method. The first argument passed to this method is the name of the zip file and the second argument is the mode in which the file should be opened, in this case, it is `r` for read mode.

It then extracts all the contents of the zip file to the specified directory, which is `self.directory + "Current"`, using the `myzip.extractall()` method. The contents of the zip file are extracted to the directory `Current` which is a subdirectory of the directory passed as an argument when creating an instance of the class.

It then closes the zip file using the `myzip.close()` method and prints the name of the zip file using the `print()` function.

```python
    def extract_zipfile(self):
        """
        Method to extract the contents of a zip file
        """
        # Open the zip file with the specified name and read it
        myzip = zipfile.ZipFile(
            self.current_month_folder + "\\" + self.filename, 'r')
        # Extract all the contents of the zip file to the specified directory
        myzip.extractall(self.directory + "Current")
        # Close the zip file
        myzip.close()
        # Print the name of the zip file
        print(self.filename)
```

The `process_sangis()` method below is a function that performs the entire process of creating the directory, logging in to the website, downloading and extracting the zip file. In this method, each step of the process is wrapped in a try-except block. The try block contains the code that may cause the exception, while the except block returns the exception that may be caused by the try block. This allows the program to continue running even if an exception is encountered, rather than crashing, and gives the user an informative message of what went wrong.

```python
    def process_sangis(self):
        """
        Method to perform the entire process of creating the directory, 
        logging in to the website, downloading and extracting the zip file
        """
        try:
            self.change_directory()
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
```

The code below defines a `main` function that performs the following actions:

1. It creates a variable `directory1` and assigns a string of the directory path where the files will be saved.
2. It creates an instance of the `SanGISDownload` class and assigns it to the variable `download1`. It passes the `directory1` variable and a string `Parcels_South.zip` as arguments to the class constructor.
3. It calls the `process_sangis` method on the `download1` object to perform the entire process of creating the directory, logging in to the website, downloading, and extracting the zip file.
4. It prints the `directory1` variable to display the first directory.
5. It repeats steps 1-4 with a new variable `directory2` and a different file name `PARCELS_EAST.zip`.
6. If the file name is `__main__` is the current file's name then it calls the main function.

The main function creates two instances of the `SanGISDownload` class, passing different directory paths and filenames as arguments, and calls the `process_sangis()` method on each instance. As a result, it downloads and extracts two different zip files to the specified directories. It also prints the directory path of each downloaded file.

```python
def main():
    # Input the directory path where the files will be downloaded
    directory1 = '{INPUT DIRECTORY PATH}'
    # Initialize an object of the SanGISDownload class and pass the directory path and the file name
    download1 = SanGISDownload(directory1, "Parcels_South.zip")
    # Call the process_sangis method to perform the download and extraction of the file
    download1.process_sangis()

    # Display the first directory path
    print(directory1)
    print('Download 1: Complete!')

    # Input the directory path where the files will be downloaded
    directory2 = '{INPUT DIRECTORY PATH}'
    # Initialize an object of the SanGISDownload class and pass the directory path and the file name
    download2 = SanGISDownload(directory2, "PARCELS_EAST.zip")
    # Call the process_sangis method to perform the download and extraction of the file
    download2.process_sangis()

    # Display the second directory path
    print(directory2)
    print("Download

 2: Complete!")


if __name__ == '__main__':
    main()
```
We conclude this demonstration by executing the program to confirm that we have successfully downloaded and extracted two ZIP files, `Parcels_South.zip` and `PARCELS_EAST.zip`, into the desired directories on our system (Note: the execution process may take a few minutes to finish). This tool simplifies the workflow process by eliminating tedious steps in data collection and storage, ultimately improving efficiency and increasing productivity.
