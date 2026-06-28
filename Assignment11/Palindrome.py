def ReverseNumber(Num):
    Res = 0
    while(Num!=0):
        Res = (Res*10) + (Num%10)
        Num = int(Num/10)
    return Res

def main():
    No = int(input("Enter number:"))
    if (No==ReverseNumber(No)):
        print("Palindrome")
    else:
        print("Not Palindrome")

if (__name__=="__main__"):
    main()