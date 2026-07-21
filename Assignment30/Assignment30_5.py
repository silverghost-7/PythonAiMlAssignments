import schedule,time,datetime

def WriteToFile():
    fileName = "Marvellous.txt"
    fObj = open(fileName,"a")
    fObj.write("Task executed at: "+str(datetime.datetime.now())+"\n")
    fObj.flush()
    fObj.close()

def main():
    schedule.every(5).minutes.do(WriteToFile)
    while(True):
        schedule.run_pending()
        time.sleep(60)

if (__name__=="__main__"):
    main()