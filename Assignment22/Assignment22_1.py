import multiprocessing

def SumSquare(No):
    Sum = 0
    for i in range(1,No):
        Sum = Sum + i**2
    return Sum


def main():
    Count = int(input("Enter number of elements:"))
    Data = list()
    MData = list()
    for i in range(Count):
        Data.append(int(input()))

    p = multiprocessing.Pool()
    MData = p.map(SumSquare,Data)
    p.close()
    p.join()
    print("Result:",MData)

if (__name__=="__main__"):
    main()