def main():
    Num = int(input("Enter first number:"))
    # Return true if number is even
    Divisible = lambda no : no%5==0
    print("Number is","divisible by 5" if Divisible(Num) else "not divisible by 5")

if (__name__=="__main__"):
    main()