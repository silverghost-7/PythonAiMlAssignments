import threading

def Even(No):
    Sum = 0
    for i in range(1,int(No/2),2):
        if (No%i==0):
            Sum = Sum + i
    print(f"Sum of Even factors:{Sum}")

def Odd(No):
    Sum = 0
    for i in range(2,int(No/2),2):
        if (No%i==0):
            Sum = Sum + i
    print(f"Sum of Odd factors:{Sum}")  

def main():
    No = int(input("Enter number:"))
    t1 = threading.Thread(target=Even,name="EvenFactor",args=(No,))
    t2 = threading.Thread(target=Odd,name="OddFactor",args=(No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if (__name__=="__main__"):
    main()