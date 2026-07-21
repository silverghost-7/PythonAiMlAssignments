import schedule,time,os,sys,datetime

def DisplayInformation(dirPath):
    for FolderName,SubFolders,FileNames in os.walk(dirPath):
        print("Directory Scanned: ",FolderName)
        print("Total Files: ",len(FileNames))
        print("Total Subdirectories: ",len(SubFolders))
        print("Scan Time: ",datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
        break

def main():
    if (len(sys.argv)!=2):
        print("Error: Wrong number of arguments")
    elif (os.path.exists(sys.argv[1])==False):
        print("Error: '",sys.argv[1],"' directory does not exist")
    elif (os.path.isdir(sys.argv[1])==False):
        print("Error: '",sys.argv[1],"' is not a directory")
    else:
        schedule.every().minute.do(DisplayInformation,sys.argv[1])
        while(True):
            schedule.run_pending()
            time.sleep(1)

if (__name__=="__main__"):
    main()