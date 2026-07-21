import schedule,time,datetime,sys,os,shutil

def Backup(fileNameRead, dirPath):
    fObj_read = open(fileNameRead,"r")
    backupFileName = str(datetime.datetime.now().replace(microsecond=0).strftime("%d_%m_%Y_%H_%M_%S"))
    backupFileName = "Data_"+backupFileName
    backupFileName = backupFileName.replace("-","_")
    backupFileName = backupFileName.replace(" ","_")
    backupFileName = backupFileName.replace(":","_")
    backupFileName = backupFileName = backupFileName + ".txt"
    shutil.copy2(fileNameRead,dirPath+"/"+backupFileName)    
    fObjLog = open("backup_log.txt","a")
    fObjLog.write("Backup completed successfully at "+datetime.datetime.now().replace(microsecond=0).strftime("%d-%m-%Y %I:%M:%S %p")+"\n")


def main():
    if (len(sys.argv)!=3):
        print("Error: Wrong number of arguments")
    elif (os.path.exists(sys.argv[1])==False):
        print("Error: File to be backed up does not exist")
    elif (os.path.exists(sys.argv[2])==False):
        print("Error: '",sys.argv[2],"' directory does not exist")
    elif (os.path.isdir(sys.argv[2])==False):
        print("Error: '",sys.argv[2],"' is not a directory")
    else:
        schedule.every().hour.do(Backup,sys.argv[1],sys.argv[2])
        while(True):
            schedule.run_pending()
            time.sleep(60)

if (__name__=="__main__"):
    main()