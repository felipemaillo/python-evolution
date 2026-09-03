from abc import ABC, abstractmethod

class HotDrink(ABC):

  def prepare(self):
    print('--- Starting Preparation ---')
    self.boil_water()
    self.mix()
    self.serve()
    print('--- Drink Ready ---')

  def boil_water(self):
    print(f'1. Boiling water at 100 degrees Celsius.')

  @abstractmethod
  def mix(self):
    pass

  @abstractmethod
  def serve(self):
    pass
