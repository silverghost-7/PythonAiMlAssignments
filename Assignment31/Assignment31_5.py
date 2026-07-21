import schedule,time,os,sys,datetime

def LogInformation(dirPath):
    fObjLog = open("DirectoryCountLog.txt","a")
    for FolderName,SubFolders,FileNames in os.walk(dirPath):
        fObjLog.write("Directory Scanned: "+FolderName+"\n")
        fObjLog.write("Total Files: "+str(len(FileNames))+"\n")
        fObjLog.write("Scan Time: "+datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")+"\n")
        fObjLog.write("\n")
        break

def main():
    if (len(sys.argv)!=2):
        print("Error: Wrong number of arguments")
    elif (os.path.exists(sys.argv[1])==False):
        print("Error: '",sys.argv[1],"' directory does not exist")
    elif (os.path.isdir(sys.argv[1])==False):
        print("Error: '",sys.argv[1],"' is not a directory")
    else:
        schedule.every(5).minutes.do(LogInformation,sys.argv[1])
        while(True):
            schedule.run_pending()
            time.sleep(10)

if (__name__=="__main__"):
    main()