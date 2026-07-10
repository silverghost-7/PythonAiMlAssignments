import multiprocessing,os

def SumEven(No):
    Sum = 0
    for i in range(2,No+1,2):
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
    MData = p.map(SumEven,Data)
    p.close()
    p.join()

if (__name__=="__main__"):
    main()