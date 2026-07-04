def ChkNum(num):
    return num%2==0

def main():
    no = int(input("Input : "))
    if (ChkNum(no)):
        print("Even number")
    else:
        print("Odd number")

if (__name__=="__main__"):
    main()