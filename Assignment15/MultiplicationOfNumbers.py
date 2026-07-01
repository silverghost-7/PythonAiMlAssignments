from functools import reduce

Multiplication = lambda No1,No2 : No1*No2

def main():
    Count = int(input("Enter number of elements:"))
    Data = list()
    for i in range(Count):
        Data.append(int(input()))
    print("Input data:",Data)
    Result = reduce(Multiplication,Data)
    print("Multiplication:",Result)

if (__name__=="__main__"):
    main()