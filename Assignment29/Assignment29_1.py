import os,sys

def main():
    if (len(sys.argv)<2):
        print("Error: Please provide file name")
        return
    
    if (os.path.exists(sys.argv[1])):
        print("File exists")
    else:
        print("File does not exist")

if (__name__=="__main__"):
    main()