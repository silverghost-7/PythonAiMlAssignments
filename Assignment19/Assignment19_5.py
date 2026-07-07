from functools import reduce

def ChkPrime(No):
    for i in range(2,int(No/2)):
        if (No%i==0):
            return False
    return True

Transform = lambda No : No*2

Maximum = lambda No1,No2 : No1 if (No1>No2) else No2 

def main():
    Data = list()
    Count = int(input("Enter number of elements:"))
    for i in range(Count):
        Data.append(int(input()))

    FData = list(filter(ChkPrime,Data))
    print("List after filter =",FData)
    MData = list(map(Transform,FData))
    print("List after map =",MData)
    Res = reduce(Maximum,MData)
    print("Output of reduce =",Res)

if (__name__=="__main__"):
    main()