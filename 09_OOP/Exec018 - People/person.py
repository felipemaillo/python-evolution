from abc import ABC
from datetime import date

class Person(ABC):

  def __init__(self, name:str, birth_year:int):
    self._name = name
    self._birth_year = None
    self.birth_year = birth_year

  @property
  def birth_year(self):
    return self._birth_year

  @birth_year.setter
  def birth_year(self, year:int):
    if 1900 <= year <= date.today().year:
      self._birth_year = year
    else:
      raise ValueError(f'Year {year} is invalid.')

  @property
  def age(self):
    return date.today().year - self._birth_year

  @age.setter
  def age(self, age):
    raise PermissionError('Age cannot be changed manually.')
