import sys
import os
import hashlib

def calculatechecksum(filename):
   fobj=open(filename,"rb")

   hobj = hashlib.md5()

   buffer = fobj.read(1024)

   while(len(buffer)>0):
     hobj.update(buffer)
     buffer = fobj.read(1024)

   fobj.close()

   return hobj.hexdigest()

def FindDuplicate(DirectoryName):

    ret = False

    ret = os.path.exists(DirectoryName)

    if ret == False:
       print("Path is invaild")
       return 


    ret = os.path.isdir(DirectoryName)

    if ret == False:
       print("it is not a directory")   
       return

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
       for fname in FileName:
          fname=os.path.join(FolderName,fname)

          Checksum = calculatechecksum(fname)

          print(f"{fname} : {Checksum}")
        

     
def main():
    FindDuplicate("Test")


if __name__ == "__main__":
  main()