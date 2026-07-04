from Arithmatic import Add,Sub,Mult,Div
def main():
    no1 = int(input("Enter first number:"))
    no2 = int(input("Enter second number:"))

    print("Addition:",Add(no1,no2))
    print("Subtraction:",Sub(no1,no2))
    print("Multiplication:",Mult(no1,no2))
    print("Division:",Div(no1,no2))
if (__name__=="__main__"):
    main()