class is_viable_transaction(Exception):
  pass

class account():
  def __init__(self, acctName, initial_deposit):
    self.acctName = acctName
    self.balance = initial_deposit

  def get_acct_balance(self):
    print(f"\n {self.acctName}'s balance: {self.balance}\n")