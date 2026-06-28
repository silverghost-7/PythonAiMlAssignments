def Sum(Num):
    if (Num==1):
        return 1
    else:
        return Num + Sum(Num-1)

def main():
    No = int(input("Enter number:"))
    print(Sum(No))
if (__name__=="__main__"):
    main()