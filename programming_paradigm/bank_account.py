class BankAccount():
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        new_amount = amount + self.account_balance
        return new_amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            new_amount = self.account_balance - amount
            return True
        else:
            new_amount = amount
            return False

    def display_balance(self):
        print(f"Current Balance: $[amount]")
