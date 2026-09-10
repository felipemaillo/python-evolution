from bank_account import BankAccount

def main():
  account = BankAccount('123-5', 'Felipe', 1000)
  account.deposit(1000)
  account.withdraw(50)
  account.name = 'Maillo'

if __name__ == "__main__":
  main()
