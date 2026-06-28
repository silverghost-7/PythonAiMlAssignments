def Factors(Num):
    for i in range(1,int(Num/2+1)):
        if (Num%i==0):
            print(i,end=" ")
    print(Num)

def main():
    No = int(input("Enter number:"))
    Factors(No)

if (__name__=="__main__"):
    main()