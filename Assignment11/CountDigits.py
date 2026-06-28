def CountDigits(Num):
    count = 0
    while(Num!=0):
        count = count+1
        Num=int(Num/10)
    print(count)

def main():
    No = int(input("Enter number:"))
    CountDigits(No)

if (__name__=="__main__"):
    main()