import schedule,time,datetime

def main():
    schedule.every().monday.at("09:00").do(lambda : print("Start your weekly goals"))
    schedule.every().wednesday.at("17:00").do(lambda : print("Review your weekly progress"))
    schedule.every().friday.at("18:00").do(lambda : print("Weekly work completed"))
    while(True):
        schedule.run_pending()
        time.sleep(10*60)

if (__name__=="__main__"):
    main()