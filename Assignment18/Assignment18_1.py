from functools import reduce

def main():
    count = int(input("Number of elements:"))
    NumList = list()
    for i in range(count):
        NumList.append(int(input()))
    print("Sum:",reduce(lambda num1,num2:num1+num2,NumList))

if (__name__=="__main__"):
    main()