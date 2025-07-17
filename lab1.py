class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)

class CheckingAccount(Account):
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return True
        return False

acc1 = SavingsAccount("Jainil", 9000, 0.05)
acc2 = CheckingAccount("Manish", 500, 200)

acc1.deposit(200)
acc1.apply_interest()

acc2.withdraw(600)
acc2.deposit(150)

print(f"{acc1.owner}'s balance: {acc1.get_balance()}")
print(f"{acc2.owner}'s balance: {acc2.get_balance()}")
