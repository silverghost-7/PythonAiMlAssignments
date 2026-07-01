from functools import reduce

Addition = lambda No1,No2 : No1+No2

def main():
    Count = int(input("Enter number of elements:"))
    Data = list()
    for i in range(Count):
        Data.append(int(input()))
    print("Input data:",Data)
    Result = reduce(Addition,Data)
    print("Addition:",Result)

if (__name__=="__main__"):
    main()