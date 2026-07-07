import threading

def ChkPrime(No):
    for i in range(2,int(No/2)+1):
        if (No%i==0):
            return False
    return True

def Prime(Data):
    Str = ""
    for element in Data:
        if (ChkPrime(element)):
            Str = Str + " " + str(element)
    print(f"Prime numbers:{Str}")

def NotPrime(Data):
    Str = ""
    for element in Data:
        if (ChkPrime(element)==False):
            Str = Str + " " + str(element)
    print(f"Not Prime numbers:{Str}")

def main():
    Count = int(input("Enter number of elements: "))
    Data = list()
    for i in range(Count):
        Data.append(int(input()))

    t1 = threading.Thread(target=Prime, args=(Data,))
    t2 = threading.Thread(target=NotPrime, args=(Data,))

    t1.start()
    t2.start()

if (__name__=="__main__"):
    main()