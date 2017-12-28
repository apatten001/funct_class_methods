

class BankAccount():

    def __init__(self,):
        self.balance = 0


    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        self.balance -= amount
        return self.balance

# here I am inheriting the BankAccount class to use info in the next class


class MinimalBalance(BankAccount):

    def __init__(self,minimal_balance):
        BankAccount.__init__(self)
        self.minimal_balance = minimal_balance

    def withdraw(self,amount):

        if self.balance - amount < self.minimal_balance:
            print("Im sorry, you have insufficient funds!" + " " + " Your balance is: $" + str(self.balance))
        else:
            BankAccount.withdraw(self,amount)


AJ = MinimalBalance(10)

AJ.deposit(70.23)
AJ.withdraw(100)

