import os, shutil
import time # For pausing
import datetime

"""
This script does read arguments passed when calling the script, takes 3 parameters that is the paths of the directoriesas follow:
*source_path is the working directory a.k.a where is the file located and is the first argument to be passed to the script.
*dest_path is the destination for the renamed file, is the second argument to be passed and is the files that were renamed with timestamp.
*backup_path is the original files copied from source_path before the renaming a.k.a the original files "untouched".

calling the script example: python c:source c:dest c:backup

"""

# define the source, destination and backup paths

#source_path = sys.argv[1]
#dest_path = sys.argv[2]
#backup_path = sys.argv[3]


source_path = r'/Users/n1tk/Desktop/test'
dest_path = r'/Users/n1tk/Desktop/dest'
backup_path = r'/Users/n1tk/Desktop/backup'

# Function to rename multiple files 
def main():

    # Passed parameters to the script
    print("The following paths will be used, for source: " + source_path +
          " Destination: " + dest_path + " Original: "
          + backup_path)

    # get the working directory
    gcwd = os.getcwd()
    print("Current working directory is:", gcwd)
    absWorkingDir = os.path.abspath(os.path.dirname(__file__))
    #absWorkingDir = os.path.abspath(source_path)  # get the absolute working directory path for the build of the paths for files.
    print(absWorkingDir)
    sourceFilename = os.path.join(absWorkingDir, source_path)  # need to decide if we do something with the source path file ...
    print(sourceFilename)
    destFilename = os.path.join(sourceFilename, dest_path)  # here the renamed files the path are copied to.
    print(destFilename)
    backupFilename = os.path.join(sourceFilename, backup_path)  # here the original files the path are moved to.
    print(backupFilename)

    # changing the directory to match the source_path
    os.chdir(sourceFilename)

    # verify the path using getcwd()
    cwd = os.getcwd()

    # print the current directory
    print("Current working directory is:", cwd)

    # check if folder/directory is not empty
    if len(os.listdir(sourceFilename) ) == 0:
        print("Directory is empty")
    else:    
        print("Directory is not empty ... renaming starting ... ")
        time.sleep(1)

        # Function to generate the timestamp and append to file name
        def timeStamped(filename, fmt='%Y%m%d-%H%M%S-{fname}'):

            """
            This creates a timestamped filename so we don't overwrite our good work
            invoke separate the function with
            fname = timeStamped('myfile.xls')
            Result: 2013 - 05 - 23 - 08 - 20 - 43 - myfile.xls
            get the current time so can use for the name of the files
            timestr = time.strftime("%Y%m%d-%H%M%S")
            print(timestr)
            """
            return datetime.datetime.now().strftime(fmt).format(fname=filename)

        # itterating thru the files in the current directory and count the amount of files renamed and moved to new location.
        i = 0
        count = 0

        # Get the full, absolute file paths.
        for filename in os.listdir(sourceFilename):
            # new_name = os.path.join(sourceFilename,timeStamped(filename))
            new_name = os.path.join(destFilename, timeStamped(filename))
            backup_name = os.path.join(backupFilename, filename)
            print('The filename is:', new_name)
             # rename the file
            # if item is a file, copy it
            if os.path.isfile(filename):
                shutil.copy(filename, new_name)
                shutil.move(filename, backup_name)

            i += 1
            count +=1 # variable will increment every loop iteration

            # Rename the files.
            print('Renaming "%s" to "%s"...' % (filename, timeStamped(filename)))

            # Move the files.
            print('Moved "%s" to "%s"...' % (filename, backup_name))

            # Print the total files renamed
            print("Renamed and moved a total of: " , count , 'files')

  
# Driver Code
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 


