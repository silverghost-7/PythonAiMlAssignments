import schedule,time

def main():
    Message = input("Enter message: ")
    Interval = int(input("Enter interval in seconds: "))

    if (Interval <= 0):
        print("Error: Invalid interval (should be greater than 0)")

    schedule.every(Interval).seconds.do(lambda Msg:print(Msg),Message)
    while(True):
        schedule.run_pending()
        time.sleep(1)

if (__name__=="__main__"):
    main()