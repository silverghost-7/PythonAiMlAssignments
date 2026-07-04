def main():
    Num1 = int(input("Enter first number:"))
    Num2 = int(input("Enter second number:"))
    Min = lambda no1,no2 : no2 if no1>no2 else no1
    print("Maximum number:",Min(Num1,Num2))

if (__name__=="__main__"):
    main()