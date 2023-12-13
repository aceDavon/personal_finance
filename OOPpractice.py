from accounts import *

david = account(acctName="David", initial_deposit=1000)
mary = account(acctName="mary", initial_deposit=2000)
davon= interestAcct("Davon", 400)

david.get_acct_balance()
david.deposit(amount=820)
davon.deposit(400)
david.withdraw(4000)
david.withdraw(400)
david.transfer(2000, mary)
david.transfer(200, mary)
mary.get_acct_balance()
davon.withdraw(100)
