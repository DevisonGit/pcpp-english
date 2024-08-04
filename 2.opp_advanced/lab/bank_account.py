class AccountException(Exception):
    """Base class for other exceptions"""
    pass

class InvalidAccountNumberChangeException(AccountException):
    """Raised when there is an attempt to change the account number"""
    def __init__(self, message="Account number cannot be changed."):
        self.message = message
        super().__init__(self.message)

class NegativeBalanceException(AccountException):
    """Raised when there is an attempt to set a negative balance"""
    def __init__(self, message="Balance cannot be negative."):
        self.message = message
        super().__init__(self.message)

class NonZeroBalanceException(AccountException):
    """Raised when there is an attempt to delete an account with a non-zero balance"""
    def __init__(self, message="Cannot delete account with non-zero balance."):
        self.message = message
        super().__init__(self.message)

class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        raise InvalidAccountNumberChangeException()

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise NegativeBalanceException()
        self._balance = value

    def deposit(self, amount):
        if amount > 100000:
            print("Auditing: Large deposit detected.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > 100000:
            print("Auditing: Large withdrawal detected.")
        if self.balance - amount < 0:
            raise NegativeBalanceException("Insufficient funds for this withdrawal.")
        self.balance -= amount

    def __del__(self):
        if self.balance != 0:
            raise NonZeroBalanceException()

# Test case 1: Setting the balance to 1000
account = BankAccount("1234567890")
account.balance = 1000
print(f"Balance after setting to 1000: {account.balance}")

# Test case 2: Trying to set the balance to -200
try:
    account.balance = -200
except NegativeBalanceException as e:
    print(e)

# Test case 3: Trying to set a new value for the account number
try:
    account.account_number = "0987654321"
except InvalidAccountNumberChangeException as e:
    print(e)

# Test case 4: Trying to deposit 1,000,000
account.deposit(1000000)
print(f"Balance after depositing 1,000,000: {account.balance}")

# Test case 5: Trying to delete the account attribute containing a non-zero balance
try:
    del account
except NonZeroBalanceException as e:
    print(e)
