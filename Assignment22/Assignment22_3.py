import multiprocessing,os

def ChkPrime(Num):
    for i in range(2,int(Num/2)+1):
        if (Num%i==0):
            return False
    return True

def CountPrime(No):
    Count = 0
    for i in range(1,No+1):
        if (ChkPrime(i)):
            Count = Count + 1
    return Count


def main():
    Count = int(input("Enter number of elements:"))
    Data = list()
    MData = list()
    for i in range(Count):
        Data.append(int(input()))

    p = multiprocessing.Pool()
    MData = p.map(CountPrime,Data)
    p.close()
    p.join()
    print("Result:",MData)

if (__name__=="__main__"):
    main()