class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Deposit successful.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print("Current balance:", self.__balance)


# Create a BankAccount object
account = BankAccount(1000)

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(200)

# Display balance
account.display_balance()
