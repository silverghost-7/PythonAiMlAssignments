IsLenghValid = lambda Str : len(Str)>5

def main():
    Count = int(input("Enter number of elements:"))
    Data = list()
    for i in range(Count):
        Data.append(input())
    print("Input data:",Data)
    Result = list(filter(IsLenghValid,Data))
    print("List of valid strings:",Result)

if (__name__=="__main__"):
    main()