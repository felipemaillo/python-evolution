from hashlib import sha256
from pwinput import pwinput

class BankAccount:

  def __init__(self, account_number:int, name:str = None, balance:float = 0, key:str = None):
    print('Creating the account...')

    self._account_number = account_number
    self._holder = name
    self.__balance = balance

    if key is None:
      self.__hash = self.ask_password()
    else:
      self.__hash = sha256(key.encode('utf-8')).hexdigest()

    print(f'Account {self._account_number} created successfully. Current balance: ¢ {self.__balance:,.2f}')

  def __str__(self):
    return f'{self.name}, the balance of your account {self._account_number} is ¢ {self.__balance:,.2f}'

  @property
  def name(self):
    if self.validate_password(self.ask_password()):
      return self._holder
    else:
      raise ValueError('Invalid password.')

  @name.setter
  def name(self, name):
    self._holder = name

  def deposit(self, value: float):
    print('Making deposit...')
    self.__balance += value
    print(f'Deposit into account {self._account_number} completed successfully. Current balance: ¢ {self.__balance:,.2f}')

  def withdraw(self, value: float, key: str = ''):
    print('Making withdrawal...')

    can_withdraw: bool = False
    if key != '':
      can_withdraw = self.validate_password(sha256(key.encode('utf-8')).hexdigest())
    else:
      can_withdraw = self.validate_password(self.ask_password())

    if can_withdraw:
      if (value <= self.__balance):
        self.__balance -= value
        print(f'Withdrawal from account {self._account_number} completed successfully. Current balance: ¢ {self.__balance:,.2f}')
      else:
        print(f'Insufficient balance in account {self._account_number}. Current balance: ¢ {self.__balance:,.2f}')
    else:
      raise ValueError('Invalid password.')

  def validate_password(self, key) -> bool:
    return True if self.__hash == key else False

  def ask_password(self) -> str:
    while True:
      password = pwinput(prompt="Enter your password: ", mask="*")

      if len(password) < 4:
        print('The password must be 4 characters or more.')
      else:
        break

    return sha256(password.encode('utf-8')).hexdigest()
