import schedule,time,datetime

def Display():
    print("Coding kar..!")

def main():
    schedule.every(30).minutes.do(Display)
    while(True):
        schedule.run_pending()
        time.sleep(60)

if (__name__=="__main__"):
    main()