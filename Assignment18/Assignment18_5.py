from MarvellousNum import ChkPrime
from functools import reduce

def ListPrime(Data):
    FData = list(filter(ChkPrime, Data))
    print(FData)
    return reduce(lambda no1,no2:no1+no2, FData)

def main():
    count = int(input("Number of elements:"))
    print("Input elements:")
    NumList = list()
    for i in range(count):
        NumList.append(int(input()))
    print("Sum:",ListPrime(NumList))

if (__name__=="__main__"):
    main()