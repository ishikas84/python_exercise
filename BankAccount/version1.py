class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def transfer(self, account, amount):
        self.balance -= amount
        account.balance += amount

    def __repr__(self):
        return f"BankAccount(balance={self.balance})"
