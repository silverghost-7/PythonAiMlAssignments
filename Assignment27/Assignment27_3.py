class Numbers:
    def __init__(self, Num):
        self.Value = Num

    def ChkPrime(self):
        for i in range(2,int(self.Value/2+1)):
            if (self.Value%i==0):
                return False
        return True
    
    def ChkPerfect(self):
        Sum = 0
        for i in range(1,int(self.Value/2+1)):
            if (self.Value%i==0):
                Sum = Sum + i
        return Sum==self.Value
    
    def Factors(self):
        Facts = list()
        for i in range(1,int(self.Value/2+1)):
            if (self.Value%i==0):
                Facts.append(i)
        return Facts
    
    def SumFactors(self):
        Sum = 0
        for i in range(1,int(self.Value/2+1)):
            if (self.Value%i==0):
                Sum = Sum + i
        return Sum

def main():
    while (True):
        No = int(input("Enter Number(-1 to exit):"))
        if (No == -1):
            break
        obj = Numbers(No)
        print(f"{No} is {"Prime" if obj.ChkPrime() else "not prime"}")
        print(f"{No} is {"perfect" if obj.ChkPerfect() else "not perfect"}")
        print("Factors:",obj.Factors())
        print("Sum of Factors:",obj.SumFactors())

if (__name__=="__main__"):
    main()