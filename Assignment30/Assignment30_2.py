import schedule,time,datetime

def Display():
    print(datetime.datetime.now())

def main():
    schedule.every().minute.do(Display)
    while(True):
        schedule.run_pending()
        time.sleep(10)

if (__name__=="__main__"):
    main()