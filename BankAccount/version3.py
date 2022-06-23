import uuid


class BankAccount:
    accounts = []

    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError(f"Cannot open account with {balance} balance")
        self.balance = balance
        self.number = uuid.uuid4()
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        if amount < 0:
            raise ValueError(f"Can't deposit {amount}")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError(f"Can't withdraw {amount}")
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError(f"Can't withdraw {amount} with {self.balance} balance")

    def transfer(self, account, amount):
        if amount < 0:
            raise ValueError(f"Can't withdraw {amount}")
        if amount > self.balance:
            raise ValueError(f"Can't withdraw {amount} with {self.balance} balance")
        self.balance -= amount
        account.balance += amount

    def __repr__(self):
        return f"{type(self).__name__}(balance={self.balance})"
