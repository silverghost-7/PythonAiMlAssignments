def IsDivisible(No):
    return No%3==0 and No%5==0

def main():
    Num = int(input("Enter number:"))
    if (IsDivisible(Num)):
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")

if (__name__=="__main__"):
    main()