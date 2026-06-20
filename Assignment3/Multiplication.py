def Multiplication(num1,num2):
    return num1*num2

def main():
    print("Enter first number:")
    num1 = int(input())

    print("Enter second number:")
    num2 = int(input())

    Result = Multiplication(num1,num2)
    print("Multiplication:",Result)

if (__name__=="__main__"):
    main()