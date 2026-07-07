import threading
from functools import reduce

def Even(Data):
    Sum = 0
    FData = list(filter(lambda No:No%2==0,Data))
    Sum = reduce(lambda No1,No2:No1+No2,FData)
    print(f"Sum of Even elements:{Sum}")

def Odd(Data):
    Sum = 0
    FData = list(filter(lambda No:No%2!=0,Data))
    Sum = reduce(lambda No1,No2:No1+No2,FData)
    print(f"Sum of Odd elements:{Sum}")

def main():
    Count = int(input("Enter number of elements:"))
    Data = list()
    for i in range(Count):
        Data.append(int(input()))
    t1 = threading.Thread(target=Even,name="EvenList",args=(Data,))
    t2 = threading.Thread(target=Odd,name="OddList",args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if (__name__=="__main__"):
    main()