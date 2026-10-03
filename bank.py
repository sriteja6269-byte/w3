class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.balance)



account = BankAccount("Sri Teja", 5000)

account.display_balance()

account.deposit(2000)
account.display_balance()

account.withdraw(1500)
account.display_balance()

account.withdraw(7000)