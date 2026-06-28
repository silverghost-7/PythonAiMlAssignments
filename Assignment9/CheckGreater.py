def ChkGreater(No1, No2):
    if (No1 > No2):
        return No1
    else:
        return No2

def main():
    Num1 = int(input("Enter first number:"))
    Num2 = int(input("Enter second number:"))
    print(ChkGreater(Num1, Num2),"is greater")

if (__name__=="__main__"):
    main()