import os
def main():
  for FolderName , SubFolder , FileName in os.walk("marvellous"):
    print("Folder name : ",FolderName)

    for subf in SubFolder:
      print("SubFolder name : ",subf)

    for fname in FileName:
         print("Filename : ",FileName)
if __name__ == "__main__":
  main()