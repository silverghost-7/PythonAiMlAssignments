def main():
    num = int(input("Enter number:"))
    IsPrime = True
    for i in range(2,int(num/2+1)):
        if (num%i==0):
            IsPrime = False
            break
    if (IsPrime):
        print("It is Prime Number")
    else:
        print("It is not Prime Number")

if (__name__=="__main__"):
    main()