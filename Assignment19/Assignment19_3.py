from functools import reduce

FilterCondition = lambda No : No>=70 and No<=90

Transform = lambda No : No+10

Product = lambda No1,No2 : No1*No2

def main():
    Data = list()
    Count = int(input("Enter number of elements:"))
    for i in range(Count):
        Data.append(int(input()))

    FData = list(filter(FilterCondition,Data))
    print("List after filter =",FData)
    MData = list(map(Transform,FData))
    print("List after map =",MData)
    Res = reduce(Product,MData)
    print("Output of reduce =",Res)

if (__name__=="__main__"):
    main()