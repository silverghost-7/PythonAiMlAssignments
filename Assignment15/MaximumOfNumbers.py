from functools import reduce

Maximum = lambda No1,No2 : No1 if No1>No2 else No2

def main():
    Count = int(input("Enter number of elements:"))
    Data = list()
    for i in range(Count):
        Data.append(int(input()))
    print("Input data:",Data)
    Result = reduce(Maximum,Data)
    print("Maximum:",Result)

if (__name__=="__main__"):
    main()