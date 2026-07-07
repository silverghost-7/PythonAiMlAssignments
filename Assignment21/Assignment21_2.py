import threading
from functools import reduce

def Maximum(Data):
    Res = reduce((lambda No1,No2 : No1 if (No1 > No2) else No2), Data)
    print(f"Maximum:{Res}")

def Minimum(Data):
    Res = reduce((lambda No1,No2 : No1 if (No1 < No2) else No2), Data)
    print(f"Minimum:{Res}")

def main():
    Count = int(input("Enter number of elements: "))
    Data = list()
    for i in range(Count):
        Data.append(int(input()))

    t1 = threading.Thread(target=Maximum, args=(Data,))
    t2 = threading.Thread(target=Minimum, args=(Data,))

    t1.start()
    t2.start()

if (__name__=="__main__"):
    main()