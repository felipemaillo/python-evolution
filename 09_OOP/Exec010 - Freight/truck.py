from transport import Transport

class Truck(Transport):
  factor = 1.20

  def __init__(self,distance):
    super().__init__(distance)

  def calculate_freight(self):
    if self.distance >= 50:
      self.freight = (self.distance * Truck.factor)
      content = f'¢ {(self.freight):,.2f}'
    else:
      content = 'The minimum distance for this type of freight is 50 KM'

    return content