class BankAccount:
    def __init__(self, accountnumber, name, balance):
        self.accountNumber = accountnumber
        self.name = name
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print("The balance available is " + str(self.balance))


    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance " + str(self.balance))
        else:
            self.balance -= amount
            print("The remaining balance is " + str(self.balance))


    def bankfees(self):
        if self.balance < 1000:
            fee_charge = (5/100)*self.balance
            self.balance -= fee_charge
            print("The penality charge is " + str(fee_charge))
            print("The available balance is " + str(self.balance))


    def display(self):
        print("Account Details \n")
        print(self.accountNumber)
        print(self.name)
        print(self.balance)






kartheesh = BankAccount(123456789, "kartheesh", 500)
kartheesh.bankfees()
kartheesh.display()