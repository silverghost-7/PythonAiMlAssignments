def main():
    num = int(input())
    Sum=0
    while(num>0):
        Sum = Sum + num%10
        num = int(num/10)
    print("Sum:",Sum)

if (__name__=="__main__"):
    main()