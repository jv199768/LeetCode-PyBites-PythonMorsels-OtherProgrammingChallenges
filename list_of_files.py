#import the os module.
import os

#Get path of current working directory
cwd = os.getcwd()


#List all files in current working directory
current_files = os.listdir(cwd)

#Create list to store file information as dictionaries
list_of_files = []

#Iterate through all the files in the current working directory
for files in current_files:
    path = os.path.join(cwd,files)

    #Check to see if file is an existing file and not a directory
    if os.path.isfile(path):

        #Let's create a dictionary that includes the filename and size.
        file_data = {
            'path': path,
            'size': os.path.getsize(path)
        }

        #Create list of dictionaries of files
        list_of_files.append(file_data)

#Print list of dictionaries
for file_data in list_of_files:
    print(file_data)
