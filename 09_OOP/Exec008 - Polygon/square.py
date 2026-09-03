from polygon import Polygon

class Square(Polygon):

  def __init__(self,side = 1):
    super().__init__(4)
    self.side = side

  def perimeter(self):
    print(f'The square perimeter is {(self.side * 4):,.2f}m')

  def area(self):
    print(f'The square area is {(self.side ** 2):,.2f}mm2')
