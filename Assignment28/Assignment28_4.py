import sys

def main():
    if (len(sys.argv)<2):
        print("Error:Please provide file name")
        return
    
    fObj_read = None
    fObj_write = None
    try:
        fObj_read = open(sys.argv[1],"r")
        fObj_write = open(sys.argv[2],"w")
    except FileNotFoundError as e:
        print(e)
        return

    Count = 0
    while(True):
        str = fObj_read.readline()
        if (str == ""):
            break
        fObj_write.write(str)

if (__name__=="__main__"):
    main()