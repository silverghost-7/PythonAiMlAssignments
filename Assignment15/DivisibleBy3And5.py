IsDivisible = lambda No : No%3==0 and No%5==0

def main():
    Count = int(input("Enter number of elements:"))
    Data = list()
    for i in range(Count):
        Data.append(int(input()))
    print("Input data:",Data)
    Result = list(filter(IsDivisible,Data))
    print("Numbers divisble by 3 and 5:",Result)

if (__name__=="__main__"):
    main()