class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount
        BankAccount.ROI = BankAccount.ROI+1

    def Display(self):
        print(f"Name: {self.Name} Amount: {self.Amount}")

    def Deposit(self, Amt):
        self.Amount = self.Amount + Amt

    def Withdraw(self, Amt):
        self.Amount = self.Amount - Amt

    def CalculateInterest(self):
        return (self.Amount * BankAccount.ROI) / 100

def main():
    obj1 = BankAccount("ABC",100)
    obj1.Display()
    obj1.Deposit(10)
    obj1.Display()
    obj1.Withdraw(5)
    obj1.Display()
    print("Interest: ",obj1.CalculateInterest())

    obj1 = BankAccount("DEF",50)
    obj1.Display()
    obj1.Deposit(10)
    obj1.Display()
    obj1.Withdraw(5)
    obj1.Display()
    print("Interest: ",obj1.CalculateInterest())


if (__name__=="__main__"):
    main()