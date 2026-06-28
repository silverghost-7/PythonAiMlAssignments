def SumDigits(Num):
    Sum = 0
    while(Num!=0):
        Sum = Sum + (Num%10)
        Num = int(Num/10)
    print(Sum)

def main():
    No = int(input("Enter number:"))
    SumDigits(No)

if (__name__=="__main__"):
    main()