import sys,os,datetime,schedule,time        

fLogger = None

def InitLogger():
    global fLogger
    if (os.path.exists("Log")==False or os.path.isdir("Log")==False):
        os.mkdir("Log")
    if (fLogger==None):
        time = str(datetime.datetime.date(datetime.datetime.now()))
        logFileName = "Log/Log"+time+".txt"
        if (os.path.exists(logFileName)):
            fLogger = open(logFileName,"a")
        else:
            fLogger = open(logFileName,"w")
        fLogger.flush()
        
def IsValidPath(DirName):
    if (os.path.exists(DirName)==False or os.path.isdir(DirName)==False):
        return False
    return True

def RemoveEmptyFiles(DirName):
    global fLogger
    InitLogger()
    
    for FolderName, SubFolders, FileNames in os.walk(DirName):
        for fName in FileNames:
            fAbsPath = os.path.join(FolderName,fName)
            if (os.path.getsize(fAbsPath)==0):
                fLogger.write("Removed file"+fAbsPath+"\n")
                fLogger.flush()
                os.remove(fAbsPath)
    fLogger.close()
    fLogger = None

def main():
    if (len(sys.argv)!=2):
        print("Error: Wrong number of arguments")
    elif (sys.argv[1]=="--h" or sys.argv[1]=="--H"):
        print("This program removes all empty files")
        print("Please run with '--u' for usage")
    elif (sys.argv[1]=="--u" or sys.argv[1]=="--U"):
        print("Run command as:\npython3 AutomationScript1.py <directory path>}")
        print("<directory path>:Absolute path of directory")
    else:
        if (IsValidPath(sys.argv[1])==False):
            print("Error: There is no directory with name '"+sys.argv[1]+"'\n")
        else:
            schedule.every(5).seconds.do(RemoveEmptyFiles, sys.argv[1])
            #RemoveEmptyFiles(sys.argv[1])

    while(True):
        schedule.run_pending()
        time.sleep(5)

if (__name__=="__main__"):
    main()