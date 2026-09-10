class Thermostat:

  min_temperature = 16
  max_temperature = 30

  def __init__(self, show_progress:bool = False):
    self.__temperature = 24
    self.show_progress = show_progress

  @property
  def f_temperature(self):
    return (f'{self.__temperature}°C')

  @property
  def temperature(self):
    return self.__temperature

  @temperature.setter
  def temperature(self, value):

    if (value % 0.5) != 0:
      raise ValueError(f'The temperature {value}°C is invalid')

    while True:
      if self.show_progress:
        print(f'{self.__temperature} > ', end='')

      if self.__temperature > value:
        self.__temperature -= 0.5
      else:
        self.__temperature += 0.5

      if self.__temperature == value:
        if self.show_progress:
          print(f'{self.__temperature}')
        break

      if self.__temperature <= self.min_temperature:
        self.__temperature = self.min_temperature
        print(f'{self.__temperature}')
        break

      if self.__temperature >= self.max_temperature:
        self.__temperature = self.max_temperature
        print(f'{self.__temperature}')
        break
