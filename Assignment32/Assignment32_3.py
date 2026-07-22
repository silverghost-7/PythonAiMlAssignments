import schedule,datetime,time,sys,os

def DisplayFileInformation(FilePath):
    if (os.path.exists(FilePath)==False):
        print("File does not exist\n")
    elif (os.path.getsize(FilePath)==0):
        print("File is empty\n")
    else:
        try:
            fObj = open(FilePath,"r")
            print("File contents:")
            Data = fObj.readline()
            while(Data!=""):
                print(Data)
                Data = fObj.readline()
        except PermissionError:
            print("Permission is denied")
        except:
            print("Cannot read file")
        finally:
            fObj.close()

def main():
    if (len(sys.argv)!=2):
        print("Error: Wrong number of arguments")
    else:
        schedule.every().minute.do(DisplayFileInformation,sys.argv[1])
        while(True):
            schedule.run_pending()
            time.sleep(10)

if (__name__=="__main__"):
    main()