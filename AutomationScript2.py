import sys


def main():
  
  if(len(sys.argv) != 2):
    DirectoryName = sys.argv[1]
    print("DirectoryName is : ",DirectoryName)

  else:
    print("invaild number of arguments")  

  DirectoryName = sys.argv[1]
  
                            

if __name__ == "__main__":
  main()