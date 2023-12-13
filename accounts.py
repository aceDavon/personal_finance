class BalanceException(Exception):
    pass


class account():
    def __init__(self, acctName, initial_deposit):
        self.acctName = acctName
        self.balance = initial_deposit

    def is_viable_transaction(self, amount):
        if amount >= self.balance:
            raise BalanceException("Insufficient funds 🤕")

    def get_acct_balance(self):
        return (f"${self.balance:.2f}\n")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\n Deposit successful.. \n {self.acctName}'s balance now: {
              self.get_acct_balance()}")
        
    def withdraw(self, amount):
        try:
            self.is_viable_transaction(amount)
            print(f"\n ******************** \n")
            self.balance -= amount
            print(f"\n Withdrawal Successful.. 🚀 \n {self.acctName}'s balance now: {self.get_acct_balance()}\n")
            print(f"\n ******************** \n")
        except BalanceException as error:
            print(f" Withdrawal not successful: {error} \n")

    def transfer(self, amount, acct):
        try:
            self.is_viable_transaction(amount)
            print("********************************")
            self.withdraw(amount)
            acct.deposit(amount)
            print(f"\n Transfer successful.. 🤙🏽 \n Yor Balance now: {self.get_acct_balance()}")
            print("********************************")
        except BalanceException as error:
            print(f"Transfer Failed: {error}")

class interest_acct(account):
    def __init__(self, acctName, initial_deposit):
        super().__init__(acctName, initial_deposit)
        self.balance = initial_deposit * 1.05

    def deposit(self, amount):
        self.balance += amount * 1.05
        print(f" Deposit successful.. \n {self.acctName}'s balance: {self.balance} \n")

    def withdraw(self, amount):
        try:
            self.is_viable_transaction(amount * 1.05)
            self.balance -= amount * 1.05
            print(f"\n Withdrawal Successful.. 🚀 \n{self.acctName}'s balance now: {self.get_acct_balance()}\n")
        except BalanceException as error:
            print(f" withdrawal failed: {error}")

