import sys
import os
import hashlib

def calculatechecksum(filename):
   fobj=open(filename,"rb")

   hobj = hashlib.md5()

   buffer = fobj.read(1000)

   while(len(buffer)>0):
     hobj.update(buffer)
     buffer = fobj.read(1000)

   fobj.close()

   return hobj.hexdigest()

   
def main():
  ret = calculatechecksum("demo.txt")
  print ("checksum of file is : ",ret)


if __name__ == "__main__":
  main()