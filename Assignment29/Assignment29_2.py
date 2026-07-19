import os,sys

def main():
    if (len(sys.argv)<2):
        print("Error:Please provide file name")
        return
    
    fObj = None
    try:
        fObj = open(sys.argv[1],"r")
    except FileNotFoundError as e:
        print(e)
        return

    Count = 0
    while(True):
        str = fObj.readline()
        if (str == ""):
            break
        print(str,end="")
if (__name__=="__main__"):
    main()