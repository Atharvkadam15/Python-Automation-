import sys


def main():
  
  if(len(sys.argv) == 2):
    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
      print("help")
    elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
      print("Usage")
    else:    
      DirectoryName = sys.argv[1]
      print("DirectoryName is : ",DirectoryName)

  else:
    print("invaild number of arguments") 
    print("please use --h or --u for more info") 
                            

if __name__ == "__main__":
  main()