class BankAccount:
    ROI = 10.5

    def __init__(self,AccountHolderName,AccountBalance):
        self.Name = AccountHolderName
        self.Amount = AccountBalance
    
    def Display(self):
        print("Enter Account Holder Name : ",self.Name)
        print("Enter Account Balance : ",self.Amount)

    def Deposit(self):
        value1 = float(input("Enter Deposit Amount : "))
        self.Amount =self.Amount + value1
    
    def Withdraw(self):
        value2 = float(input("Enter Withdraw Amount : "))
        if value2 <= self.Amount:
            self.Amount = self.Amount - value2
        else :
            print("Insufficient Balance")

    def CaluculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest

obj1 = BankAccount("Sachin",10000)
obj2 = BankAccount("Sagar",50000)

print("-------First Account Holder-----")
obj1.Display()

obj1.Deposit()
obj1.Display()

obj1.Withdraw()
obj1.Display()

print("Interest is : ",obj1.CaluculateInterest())

print("="*30)

print("-------First Second Holder-----")
obj2.Display()

obj2.Deposit()
obj2.Display()

obj2.Withdraw()
obj2.Display()

print("Interest is : ",obj2.CaluculateInterest())

