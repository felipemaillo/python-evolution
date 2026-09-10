from transport import Transport

class Motorcycle(Transport):
  factor = 0.50

  def __init__(self,distance):
    super().__init__(distance)

  def calculate_freight(self):
    self.freight = (self.distance * Motorcycle.factor)
    return f'¢ {(self.freight):,.2f}'