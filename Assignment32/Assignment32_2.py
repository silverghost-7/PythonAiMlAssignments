import schedule,datetime,time,sys,os

def LogInformation(FilePath):
    Exists = os.path.exists(FilePath)
    timeNow = datetime.datetime.now()
    fileName = "FileSizeLog.txt"
    fObj = open(fileName,"a")
    if (Exists):
        fObj.write("File path: "+FilePath+"\n")
        fObj.write("File Size in bytes: "+str(os.path.getsize(FilePath))+"\n")
    else:
        fObj.write("File details not available\n")
    fObj.write("Scan Time: "+timeNow.replace(microsecond=0).strftime("%d-%m-%Y %I:%M:%S %p")+"\n")
    fObj.write("\n")
    fObj.flush()
    fObj.close()


def main():
    if (len(sys.argv)!=2):
        print("Error: Wrong number of arguments")
    elif(os.path.exists(sys.argv[1])==False):
        print("Error: File does not exist")
    else:
        schedule.every(30).seconds.do(LogInformation,sys.argv[1])
        while(True):
            schedule.run_pending()
            time.sleep(10)

if (__name__=="__main__"):
    main()