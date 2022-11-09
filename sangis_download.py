# import packages
import os
import time
import zipfile
from twill.commands import *
from twill import browser

# import sangis_credentials.py module
import sangis_credentials


# method for accessing the SanGIS/SANDAG GIS Data Warehouse website
def login_credentials():
    """Browses to data source website,
         Call the 'sangis_credentials' module to input login credentials,"""
    # Talk to the web browser directly,
    go('https://rdw.sandag.org/Account/Login')
    showforms()

    # input login credentials
    fv("1", "ctl00$MainContent$Email", sangis_credentials.username)
    fv("1", "ctl00$MainContent$Password", sangis_credentials.password)
    submit('0')


# create a SanGISDownload class object & encapsulate all methods and variables
class SanGISDownload:
    directory = None
    filename = None
    current_month_folder = None

    # create SanGISDownload class constructor, with two arguments, and initialize class variables
    def __init__(self, directory, filename):
        """SanGISDownload  Class Constructor,
           :param self: pass 'self' to access variables coming from the constructor
           :param directory: output file path (string)
           :param filename: output filename(s) (string)"""

        # initialize class variables
        self.directory = directory
        self.filename = filename

    # create a class method for creating and structuring output subdirectories
    def change_directory(self):
        """Creates "date-stamped" subdirectories
           Changes the current working directory to output file path
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

        # print the new current working directory
        print(directory)

    # class Method downloading ZIP file(s)
    def process_download(self):
        """Browsing while logged in,
           Initiatize the download process,"""

        # navigate to the zip file download page
        go("gisdtview.aspx?dir=Parcel")
        go("GetFSFile.aspx?dir=Parcel&Name=" + self.filename)

        # create a file object,
        # open file for writing in binary format,
        # overwrite the file if it exists,
        # if the file does not exist, create new file for writing
        with open(self.filename, "wb") as bf:
            bf.write(browser.dump)

    # class Method to extract zip file(s)
    def extract_zipfile(self):
        """Creates a new folder directory specifically for extraction,
              Extracts ZIP file contents to new directory """
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

    # when an error occurs, this class method catches and handles the exception,
    def process_sangis(self):
        """ try block: contains the code that may cause the exception.
              except block: returns the exception that may be caused by the try block."""
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


# define the main method, so it runs each line serially from the top of the entire module
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
