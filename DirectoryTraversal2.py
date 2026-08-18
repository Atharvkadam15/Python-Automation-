import os
def main():
  for FolderName , SubFolder , FileName in os.walk("marvellous"):
    print("Folder name : ",FolderName)

    for subf in SubFolder:
      print("SubFolder name : ",subf)


if __name__ == "__main__":
  main()