def PrimeNumber(Num):
    for i in range(2,int(Num/2+1),1):
        if (Num%i==0):
            return False
    return True

def main():
    No = int(input("Enter number:"))
    if (PrimeNumber(No)):
        print("Prime number")
    else:
        print("Not a prime number")

if (__name__=="__main__"):
    main()