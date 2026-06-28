def Factorial(Num):
    if (Num==1):
        return 1
    else:
        return Num * Factorial(Num-1)


def main():
    No = int(input("Enter number:"))
    print(Factorial(No))

if (__name__=="__main__"):
    main()