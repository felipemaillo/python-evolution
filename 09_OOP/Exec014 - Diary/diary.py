class Diary:

  def __init__(self, password = '1234'):
    self.__secrets = []
    self.__password = password

  @property
  def password(self):
    raise ValueError('Viewing the password is not allowed!')

  @password.setter
  def password(self, password):
      self.__password = password

  def change_password(self, old_password, new_password):
    if old_password == self.__password:
      self.password = new_password
    else:
      raise ValueError('Invalid password!')

  def write(self, msg):
    if isinstance(msg, str) and len(msg) > 0:
      self.__secrets.append(msg)

  def read(self, password = None):
    if password == self.__password:
      for secret in self.__secrets:
        print(f'- {secret}')
    else:
      raise ValueError('Invalid password!')
