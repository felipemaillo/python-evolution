from abc import ABC, abstractmethod

class Transport(ABC):
  def __init__(self,distance):
    self.distance = distance
    self.freight = 0

  @abstractmethod
  def calculate_freight(self):
    pass
