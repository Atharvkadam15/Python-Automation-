import sys
import os
import time
import schedule

def DirectoryScanner(DirectoryPath = "marvellous"): 
  Border = "-"*40
  timeStamp = time.ctime()
  LogFileName = "marvellous%s.log"%(timeStamp) #unique
  LogFileName = LogFileName.replace(" ","_")
  LogFileName = LogFileName.replace(":","_")

  Ret = False 

  Ret = os.path.exists(DirectoryPath)

  if Ret == False:
    print("Marvellous Automation error : There is no such Directory with name ",DirectoryPath)
    return 

  Ret = os.path.isdir(DirectoryPath)

  if (Ret == False):
    print("Marvellous Automation error : It is not a Directory with name ",DirectoryPath)
    return

  print("LogFile gets Created with name : ",LogFileName)

  fobj = open(LogFileName,"w")

  fobj.write( Border +"\n")
  fobj.write(" Marvellous Automation Script ")
  fobj.write("\n"+Border +"\n")


  fobj.write("Marvellous Automation Script \n")

  fobj.write("Files from the directory are : \n")

  for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
    for fname in FileName:
      fobj.write(fname + "\n")

  fobj.write( Border +"\n")
  fobj.write(" LogFile gets created at : "+timeStamp)
  fobj.write("\n"+ Border +"\n")

  fobj.close()


def main():
  Border = "-"*40
  print(Border)
  print(" Marvellous Automation Script ")
  print(Border)

  if(len(sys.argv) == 2):
    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
      print("This automation script is used to travel the directory ")
      print("for better info please use --u flag ")
    elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
      print("please execute the script as ")
      print("python Filename.py DirectoryName ")
      print("DirectoryName should be absolute path")
    else:    
     schedule.every(1).minute.do( DirectoryScanner , sys.argv[1] )

     while True:  #Counter 
       schedule.run_pending()
       time.sleep(1)
      

  else:
    print("invaild number of arguments") 
    print("please use --h or --u for more info") 

  print(Border)
  print(" Thank You for using Marvellous Automation Script ")
  print(Border)  
                            
if __name__ == "__main__":
  main()