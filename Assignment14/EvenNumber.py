def main():
    Num = int(input("Enter first number:"))
    # Return true if number is even
    Even = lambda no : no%2==0
    print("Number is", "Even" if Even(Num) else "Odd")

if (__name__=="__main__"):
    main()