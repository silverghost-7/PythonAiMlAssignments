def Factorial(no):
    if (no==1):
        return 1
    else:
        return no * Factorial(no-1)

def main():
    num = int(input("Enter number:"))
    print(Factorial(num))

if (__name__=="__main__"):
    main()