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

    Duplicate={}



    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
       for fname in FileName:
          fname=os.path.join(FolderName,fname)

          Checksum = calculatechecksum(fname)


          if Checksum in Duplicate:
             Duplicate[Checksum].append(fname)
          else:
             Duplicate[Checksum] = [fname]

    return Duplicate   



def DeleteDuplicate(DirectoryName):
   myDict= FindDuplicate(DirectoryName)

   
   result = list ( filter ( lambda x : len(x) > 1 , myDict.values() ) )

   count = 0 
   totalDeleted = 0

   for value in result:
      for subvalue in value:
          count = count + 1
          if (count > 1 ):
             os.remove(subvalue)
             totalDeleted = totalDeleted + 1
      count = 0
      
   print("total deleted files : ",totalDeleted)


def main():
   data = DeleteDuplicate("Test")
   


if __name__ == "__main__":
  main()