def main():
    num = int(input("Enter number:"))
    Sum = 0
    for i in range(1,int(num/2+1)):
        if (num%i==0):
            Sum=Sum+i
    print(Sum)

if (__name__=="__main__"):
    main()