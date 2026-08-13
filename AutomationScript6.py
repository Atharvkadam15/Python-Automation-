import sys

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
      DirectoryName = sys.argv[1]
      print("DirectoryName is : ",DirectoryName)

  else:
    print("invaild number of arguments") 
    print("please use --h or --u for more info") 


  print(Border)
  print(" Thank You for using Marvellous Automation Script ")
  print(Border)  
                            

if __name__ == "__main__":
  main()