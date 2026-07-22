import schedule,time,sys,os,shutil

def validateDir(DirPath):
    if (not os.path.exists(DirPath) or not os.path.isdir(DirPath)):
        return False
    return True

def CopyFiles(SourceDir, DestDir):
    fLog = open("FileCopyLog.txt","a")
    if (not validateDir(SourceDir)):
        print("Error: Source directory is not valid")
    elif (not validateDir(DestDir)):
        print("Error: Destination directory is not valid")
    else:
            for FolderName,SubFolders,FileNames in os.walk(SourceDir):
                for fName in FileNames:
                    if (fName.endswith(".txt")):
                        try:
                            filePath = os.path.join(FolderName,fName)
                            shutil.copy2(filePath,DestDir+"/"+fName)
                            fLog.write("File Copied: "+filePath+"\n")
                        except PermissionError:
                            print("Permission is denied: "+filePath)
                        except shutil.SameFileError:
                            print("File already present: "+filePath)
                        except:
                            print("Error copying file: "+filePath)
    fLog.write("\n\n")
    fLog.close()
    print()
    print()

def main():
    if (len(sys.argv)!=3):
        print("Error: Wrong number of arguments")
    elif (not validateDir(sys.argv[1])):
        print("Error: Source directory is not valid")  
    elif (not validateDir(sys.argv[2])):
        print("Error: Destination directory is not valid")
    else:
        schedule.every(10).minutes.do(CopyFiles,sys.argv[1],sys.argv[2])
        while(True):
            schedule.run_pending()
            time.sleep(60)

if (__name__=="__main__"):
    main()