def IsPerfectNumber(Num):
    Sum = 0
    for i in range(1,int(Num/2+1)):
        if (Num%i==0):
            Sum = Sum + i
    return Sum==Num

def main():
    No = int(input("Enter number:"))
    if (IsPerfectNumber(No)):
        print("Perfect number")
    else:
        print("Not perfect number")

if (__name__=="__main__"):
    main()