

class BankAccount():

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        self.balance -= amount
        return self.balance






Arnold = BankAccount()
Arnold.deposit(100)
Arnold.withdraw(20)
Arnold.deposit(10000)
Arnold.withdraw(2000)
print(Arnold.balance)


