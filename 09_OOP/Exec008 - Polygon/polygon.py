from abc import ABC, abstractmethod

class Polygon(ABC):
  def __init__(self,num_sides):
    self.num_sides = num_sides

  @abstractmethod
  def perimeter(self):
    pass

  @abstractmethod
  def area(self):
    pass
