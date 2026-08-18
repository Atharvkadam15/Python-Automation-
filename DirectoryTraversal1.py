import os
def main():
  for FolderName , SubFolder , FileName in os.walk("marvellous"):
    print(FolderName)

if __name__ == "__main__":
  main()