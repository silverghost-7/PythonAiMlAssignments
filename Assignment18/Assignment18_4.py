def main():
    count = int(input("Number of elements:"))
    Search = int(input("Element to search:"))
    NumList = list()
    for i in range(count):
        NumList.append(int(input()))
    print("Frequency:",len(list(filter(lambda no:no==Search,NumList))))

if (__name__=="__main__"):
    main()