import multiprocessing,os

def CountOdd(No):
    Count = 0
    for i in range(1,No+1,2):
        Count = Count + 1
    print(f"PID:{os.getpid()} Input:{No} Odd Count:{Count}")
    return Count


def main():
    Count = int(input("Enter number of elements:"))
    Data = list()
    MData = list()
    for i in range(Count):
        Data.append(int(input()))

    p = multiprocessing.Pool()
    MData = p.map(CountOdd,Data)
    p.close()
    p.join()
    print("Result:",MData)

if (__name__=="__main__"):
    main()