from multiprocessing.pool import ThreadPool
from functools import reduce

def Sum(Data):
    Res = reduce(lambda No1,No2:No1+No2, Data)
    return Res

def Product(Data):
    Res = reduce(lambda No1,No2:No1*No2, Data)
    return Res

def main():
    Count = int(input("Enter number of elements: "))
    Data = list()
    for i in range(Count):
        Data.append(int(input()))
    Result1 = 0
    Result2 = 0
    
    pool = ThreadPool(processes=2)
    Result1 = pool.apply_async(Sum,(Data,))
    Result2 = pool.apply_async(Product,(Data,))
    
    print("Sum:",Result1.get())
    print("Product:",Result2.get())

if (__name__=="__main__"):
    main()