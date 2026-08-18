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

   
def main():
  ret = calculatechecksum("demoX.txt")
  print ("checksum of file is : ",ret)


if __name__ == "__main__":
  main()