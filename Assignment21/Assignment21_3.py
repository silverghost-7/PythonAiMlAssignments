import threading
from functools import reduce

Count = 0
lock = threading.Lock()

def Increment():
    with lock:
        global Count
        Count = Count + 1

def PrintEven():
    global Count
    while (Count<10):
        if (Count%2==0):
            print(f"Thread name: {threading.current_thread().name}  Count:{Count}")
            Increment()

def PrintOdd():
    global Count
    while (Count<10):
        if (Count%2!=0):
            print(f"Thread name: {threading.current_thread().name}  Count:{Count}")
            Increment()

def main():

    t1 = threading.Thread(target=PrintEven,name="PrintEven")
    t2 = threading.Thread(target=PrintOdd,name="PrintOdd")

    t1.start()
    t2.start()

if (__name__=="__main__"):
    main()