def EvenNumbers(Num):
    for i in range(0,Num,2):
        print(i,end=" ")


def main():
    No = int(input("Enter number:"))
    EvenNumbers(No)

if (__name__=="__main__"):
    main()