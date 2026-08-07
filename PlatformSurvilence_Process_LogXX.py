import psutil
import sys
import os
import time
import schedule


def ProcessScan():
  listprocess = []
  for proc in psutil.process_iter():
    info = proc.as_dict(attrs=["pid", "name" ,"username" ,"status"])
    info["cpu_percent"] = proc.cpu_percent(None)
    info["memory_percent"] = proc.memory_percent()

    listprocess.append(info)

  return listprocess



def PlatformSurvilence(FolderName):
  Border = "-"*50

  ret = False

  ret = os.path.exists(FolderName)

  if(ret == True):
    ret = os.path.isdir(FolderName)
    if(ret == False):
      print("Unable to proceed as Directory name is but not a directory")
      return
  else:
    os.mkdir(FolderName)
    print("Directory for the log file gets creates successfully")

  timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

  FileName = os.path.join(FolderName, "Marvellous_%s.log" %timestamp)
  fobj = open(FileName,"w")
  print(f"Log file gets successfully created with name {FileName}")

  fobj.write(Border+"\n")
  fobj.write("--- Marvellous Platform Survillence System ---\n")
  fobj.write("Log file gets created at : "+timestamp+"\n")
  fobj.write(Border+"\n\n")

  fobj.write("------------- System Report -------------\n")

  # CPU Information
  fobj.write("Number of Active CPU Cores : %s \n" %psutil.cpu_count())
  fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
  fobj.write(Border+"\n")

  # RAM Information
  memory = psutil.virtual_memory()
  fobj.write("RAM Usage : %s %%\n" %memory.percent)
  fobj.write("Total RAM Available : %s\n" %memory.total)
  fobj.write(Border+"\n")

  # Network Usage
  netobj = psutil.net_io_counters()

  fobj.write("Network Usage Report \n")
  fobj.write("Sent : %.2f MB\n" %(netobj.bytes_sent / (1024*1024)))
  fobj.write("Received : %.2f MB\n" %(netobj.bytes_recv / (1024*1024)))
  fobj.write(Border+"\n")

  # Prcess Log
  Data = ProcessScan()

  for info in Data:
   # fobj.write(f"{info}")
    fobj.write("PID : %s\n" %info.get("pid"))
    fobj.write("Name : %s\n" %info.get("name"))
    fobj.write("User name : %s\n" %info.get("username"))
    fobj.write("Status : %s\n" %info.get("status"))
    fobj.write("CPU Usage : %.2f\n" %info.get("cpu_percent"))
    fobj.write("Memory Usage : %.2f\n" %info.get("memory_percent"))    
    fobj.write(Border+"\n")


  fobj.write(Border+"\n")
  fobj.write("------------- End of Log File -------------\n")
  fobj.write(Border+"\n")

  fobj.close()

def main():
  Border = "-"*50
  print(Border)
  print("--- Marvellous Platform Survillence System ---")
  print(Border)


  # --h & --u handling
  if (len(sys.argv)==2):
     if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
       print("This Automation script used to perform ")
       print("1 : It fetch the information of running processes ")
       print("2 : It fetch the information of about the RAM")
       print("3 : It fetch the information of primary storage as RAM ")
       print("4 : It fetch the information of Secondary storage as HDD ")
       print("5 : It fetch information about the microprocessor")
       print("6 : It gets auto schedulled periodically")
       print("7 : It maintains all records into log file ")
       print("8 : it sends the log files through mail periodically")


     elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
       print("Use the automation script as : ")
       print("python {sys.argv[0]} Time_Interval Folder_Name")
       print("Time_Interval : Time in minutesfor perodically")
       print("Folder_Name : the name of folder where log files get stores")
     else:
       print("Unable to proceed as arguments are not matching")
       print("Please use --h or --u flag for getting more details")
     
  #Actual Project code
  elif(len(sys.argv)==3):

   # print("CPU Usage : ",psutil.cpu_percent())     
    print("Scheduler Started Successfully")
    print("Press Ctrl + C to abort the Automation script")
    schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvilence, sys.argv[2])

    while True:
      schedule.run_pending()
      time.sleep(1)
     
  else:
    print("Invalid number of argument")
    print("Unable to proceed as arguments are not matching ")
    print("Please use --h or --u flag for getting more details")

  print(Border)
  print("--- Thank You for using Automation System ---")
  print(Border)

if __name__ == "__main__":
  main()