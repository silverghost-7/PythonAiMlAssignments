import schedule,time,os,sys,datetime

def CreateLogFile():
    timeNow = datetime.datetime.now()
    fileName = "MarvellousLog_"+str(timeNow.replace(microsecond=0).strftime("%d_%m_%Y_%H_%M_%S"))
    fObj = open(fileName,"w")
    fObj.write("Log file created successfully.\n")
    fObj.write("Creation time: "+timeNow.replace(microsecond=0).strftime("%d-%m-%Y %I:%M:%S %p")+"\n")


def main():
    schedule.every(10).minutes.do(CreateLogFile)
    while(True):
        schedule.run_pending()
        time.sleep(10)

if (__name__=="__main__"):
    main()