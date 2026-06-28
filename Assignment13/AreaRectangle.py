def Area(Length,Width):
    return Length*Width

def main():
    Len = int(input("Enter length:"))
    Wid = int(input("Enter width:"))
    print("Area of rectangle:",Area(Len,Wid))

if (__name__=="__main__"):
    main()