import schedule,time,datetime,sys,os

def Backup(fileNameRead, dirPath):
    fObj_read = open(fileNameRead,"r")
    backupFileName = str(datetime.datetime.now().replace(microsecond=0).strftime("%d_%m_%Y_%H_%M_%S"))
    backupFileName = "Data_"+backupFileName
    backupFileName = backupFileName.replace("-","_")
    backupFileName = backupFileName.replace(" ","_")
    backupFileName = backupFileName.replace(":","_")
    backupFileName = backupFileName = backupFileName + ".txt"
    fObj_write = open(dirPath+"/"+backupFileName,"w")
    Data = fObj_read.readline()
    while(Data!=""):
        fObj_write.write(Data)
        fObj_write.flush()
        Data = fObj_read.readline()
    
    fObj_read.close()
    fObj_write.close()


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