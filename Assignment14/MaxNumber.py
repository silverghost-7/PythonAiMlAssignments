def main():
    Num1 = int(input("Enter first number:"))
    Num2 = int(input("Enter second number:"))
    Max = lambda no1,no2 : no1 if no1>no2 else no2
    print("Maximum number:",Max(Num1,Num2))

if (__name__=="__main__"):
    main()