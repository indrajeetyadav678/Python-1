class Bank:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount to withdraw must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount} successfully.")
            self.current_balance()

    def deposit(self, amount):
        if amount <= 0:
            print("Amount to deposit must be greater than 0.")
        else:
            self.balance += amount
            print(f"Deposited {amount} successfully.")
            self.current_balance()

    def current_balance(self):
        print(f"Current Balance: {self.balance}")


# Get user input for account number and initial balance
account_number = input("Enter account number: ")
initial_balance = float(input("Enter initial balance: "))

# Create an instance of the Bank class
bank_account = Bank(account_number, initial_balance)

# Example usage
bank_account.withdraw(100)  # Withdraw 100 from the account
bank_account.deposit(500)   # Deposit 500 to the account
