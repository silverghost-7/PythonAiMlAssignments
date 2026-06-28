def OddNumbers(Num):
    for i in range(1,Num,2):
        print(i,end=" ")

def main():
    No = int(input("Enter number:"))
    OddNumbers(No)

if (__name__=="__main__"):
    main()