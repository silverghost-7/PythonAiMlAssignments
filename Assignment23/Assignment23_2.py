import multiprocessing,os

def SumOdd(No):
    Sum = 0
    for i in range(1,No+1,2):
        Sum = Sum + i
    print(f"PID:{os.getpid()} Input:{No} Sum:{Sum}")
    return Sum


def main():
    Count = int(input("Enter number of elements:"))
    Data = list()
    MData = list()
    for i in range(Count):
        Data.append(int(input()))

    p = multiprocessing.Pool()
    MData = p.map(SumOdd,Data)
    p.close()
    p.join()

if (__name__=="__main__"):
    main()