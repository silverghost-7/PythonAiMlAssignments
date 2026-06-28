def Area(Radius):
    return 3.14*Radius*Radius

def main():
    R = int(input("Enter radius:"))
    print("Area of circle:",Area(R))

if (__name__=="__main__"):
    main()