from polygon import Polygon
from math import pi

class Circle(Polygon):

  def __init__(self,radius = 1):
    super().__init__(0)
    self.radius = radius

  def perimeter(self):
    print(f'The circle perimeter is {(2 * pi * self.radius):,.2f}cm')

  def area(self):
    print(f'The circle area is {(pi * (self.radius ** 2)):,.2f}cm2')
