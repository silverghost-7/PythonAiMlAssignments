def main():
    Num1 = int(input("Enter first number:"))
    Num2 = int(input("Enter second number:"))
    Multiplication = lambda no1,no2 : no1*no2
    print("Multiplication:",Multiplication(Num1,Num2))

if (__name__=="__main__"):
    main()