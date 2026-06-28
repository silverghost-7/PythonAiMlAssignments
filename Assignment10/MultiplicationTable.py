def Multiplication(Num):
    for i in range(10):
        print(Num*(i+1),end=" ")

def main():
    No = int(input("Enter number:"))
    Multiplication(No)

if (__name__=="__main__"):
    main()