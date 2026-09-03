from transport import Transport

class Drone(Transport):
  factor = 9.50

  def __init__(self,distance):
    super().__init__(distance)

  def calculate_freight(self):
    if self.distance <= 10:
      self.freight = (self.distance * Drone.factor)
      content =  f'¢ {(self.freight):,.2f}'
    else:
      content = 'The maximum distance for this type of freight is 10 KM'

    return content