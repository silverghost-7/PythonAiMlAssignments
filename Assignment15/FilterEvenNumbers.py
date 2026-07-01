IsEven = lambda No : No%2==0

def main():
    Count = int(input("Enter number of elements:"))
    Data = list()
    for i in range(Count):
        Data.append(int(input()))
    print("Input data:",Data)
    Result = list(filter(IsEven,Data))
    print("List of even numbers:",Result)

if (__name__=="__main__"):
    main()