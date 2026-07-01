Square = lambda No : No*No

def main():
    Count = int(input("Enter number of elements:"))
    Data = list()
    for i in range(Count):
        Data.append(int(input()))
    print("Input data:",Data)
    Result = list(map(Square,Data))
    print("Square of numbers:",Result)

if (__name__=="__main__"):
    main()