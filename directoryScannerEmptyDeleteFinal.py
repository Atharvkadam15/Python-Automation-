######################################################
#
# Importing required libraries
#
#######################################################

import sys
import os
import time
import schedule

######################################################
#
# Function Name :       directoryScanner
# Input:                Name of Directory
# Description:          Delete all empty files periodically
# Date:                 19/07/2026
# Author:               Babakhalid Isaq Patel
#
#######################################################

def directoryScanner(DirectoryPath):
    Border = "-"*50

    timeStamp = time.ctime()
    logFileName = "Marvellous_%s.log"%(timeStamp)
    logFileName = logFileName.replace(" ", "_").replace(":","_")

    ret = False
    ret = os.path.exists(DirectoryPath)

    if ret == False:
        print("Marvellous Automation Error : There is no such directory with name", DirectoryPath)
        return
    
    ret = os.path.isdir(DirectoryPath)
    if ret == False:
        print("Marvellous Automation Error : It is not a directory with name", DirectoryPath)
        return
    
    


    print("Log File gets created with Name :", logFileName)

    fobj = open(logFileName,"w")
    fobj.write(Border+"\n")
    fobj.write("Marvellous Automation Script \n")
    fobj.write(Border+"\n\n")

    fobj.write("Files from the directory are : \n\n")
    fobj.write(Border+"\n")

    totalFiles = 0
    emptyFiles = 0


    for folderName, SubFolder, FileName in os.walk(DirectoryPath):
        for fName in FileName:
            totalFiles = totalFiles + 1
            fName = os.path.join(folderName, fName)
            fobj.write(f"{fName} : {os.path.getsize(fName)} bytes \n")

            if(os.path.getsize(fName) == 0):
                emptyFiles = emptyFiles + 1
                os.remove(fName)


    fobj.write(Border+"\n")
    fobj.write(f"Total files scanned : {totalFiles}\n")
    fobj.write(f"Total empty files found and deleted : {emptyFiles}")

    fobj.write(Border+"\n")
    fobj.write("Log File gets created at :"+timeStamp)
    fobj.write("\n"+Border+"\n")


    fobj.close()

######################################################
#
# Function Name :       main
# Input:                Command Line Arguments
# Description:          It controls the script
# Date:                 19/07/2026
# Author:               Babakhalid Isaq Patel
#
#######################################################

def main():
    Border = "-"*50
    print(Border)
    print("       Marvellous Automation Script         ")
    print(Border)


    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to travel the directory")
            print("For better usage please check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as  ")
            print("pyhton3 FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
        else:
            schedule.every(1).minute.do(directoryScanner,  sys.argv[1])
            while True:
                schedule.run_pending()
                time.sleep(1)
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

    print(Border)
    print(" Thank you for using Marvellous Automation Script ")
    print(Border)

######################################################
#
# Starter of the automation script
#
#######################################################
if __name__ == "__main__":
    main()