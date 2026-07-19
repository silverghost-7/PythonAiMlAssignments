import sys

def main():
    if (len(sys.argv)<2):
        print("Error:Please provide file name")
        return
    
    fObj1 = None
    fObj2 = None
    try:
        fObj1 = open(sys.argv[1],"r")
        fObj2 = open(sys.argv[2],"r")
    except FileNotFoundError as e:
        print(e)
        return

    Count = 0
    while(True):
        str1 = fObj1.readline()
        if (str1 == ""):
            break
        str2 = fObj2.readline()
        if (str1 != str2):
            print("Failure")
            return
        
    print("Success")

if (__name__=="__main__"):
    main()