def main():
    Num1 = int(input("Enter first number:"))
    Num2 = int(input("Enter second number:"))
    Num3 = int(input("Enter third number:"))
    # Return true if number is odd
    Odd = lambda no1,no2,no3 : no1 if (no1>no2 and no1>no3) else (no2 if (no2>no3) else no3)
    print("Maximum Number:", Odd(Num1, Num2, Num3))

if (__name__=="__main__"):
    main()