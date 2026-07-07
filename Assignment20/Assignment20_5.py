import threading
from functools import reduce

def DisplayNumbers():
    print("Thread 1:")
    for i in range(1,51):
        print(i,end=" ")

def DisplayNumbersReverse():
    print("\nThread 2:")
    for i in range(50,0,-1):
        print(i,end=" ")

def main():
    t1 = threading.Thread(target=DisplayNumbers)
    t2 = threading.Thread(target=DisplayNumbersReverse)

    t1.start()
    t1.join()

    t2.start()
    t2.join()
    
if (__name__=="__main__"):
    main()