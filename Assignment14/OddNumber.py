def main():
    Num = int(input("Enter first number:"))
    # Return true if number is odd
    Odd = lambda no : no%2!=0
    print("Number is","Odd" if Odd(Num) else "Even")

if (__name__=="__main__"):
    main()