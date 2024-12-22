print("OE:6")
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance:.2f}")

    def __display_balance(self):
        print(f"Current Balance: {self.__balance:.2f}")

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if isinstance(balance, float) and balance >= 0:
            self.__balance = balance
        else:
            print("Error: Balance must be a non-negative float.")

account = BankAccount("123456789", 1000.00)
account.deposit(500.00)
account.withdraw(200.00)
account.set_balance(-100.00)
account.set_balance(1500.00)
account.display_account_info()