import schedule,datetime,time

def CreateFile():
    timeNow = datetime.datetime.now()
    fileName = "File_"+str(timeNow.replace(microsecond=0).strftime("%d_%m_%Y_%H_%M_%S"))
    fObj = open(fileName,"w")
    fObj.write("File name: "+fileName+"\n")
    fObj.write("Creation date: "+timeNow.replace(microsecond=0).strftime("%d-%m-%Y")+"\n")
    fObj.write("Creation date: "+timeNow.replace(microsecond=0).strftime("%I:%M:%S %p")+"\n")
    fObj.flush()
    fObj.close()


def main():
    schedule.every().minute.do(CreateFile)
    while(True):
        schedule.run_pending()
        time.sleep(10)

if (__name__=="__main__"):
    main()