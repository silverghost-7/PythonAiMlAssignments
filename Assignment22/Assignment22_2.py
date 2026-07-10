import multiprocessing,os

def Factorial(No):
    Fact = 1
    for i in range(2,No+1):
        Fact = Fact * i
    print(f"PID: {os.getpid()}, Input: {No}, Factorial: {Fact}")
    return Fact


def main():
    Count = int(input("Enter number of elements:"))
    Data = list()
    MData = list()
    for i in range(Count):
        Data.append(int(input()))

    p = multiprocessing.Pool()
    MData = p.map(Factorial,Data)
    p.close()
    p.join()
    print("Result:",MData)

if (__name__=="__main__"):
    main()