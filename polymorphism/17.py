class BankAccount:
    def calculate_interest(self):
        print("Calculating interest")

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings Account interest: 5%")

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Current Account interest: 2%")

for account in [SavingsAccount(), CurrentAccount()]:
    account.calculate_interest()