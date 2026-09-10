class Rectangle:

  def __init__(self, base = 1, height = 1):
    self._base = None
    self._height = None
    self._area = None

    self.base = base
    self.height = height

  @property
  def base(self):
    return self._base

  @base.setter
  def base(self, base):
    if (not isinstance(base, float) and not isinstance(base, int)) or (base <= 0):
      raise ValueError('Invalid value for the base.')

    self._base = base

  @property
  def height(self):
    return self._height

  @height.setter
  def height(self, height):
    if (not isinstance(height, float) and not isinstance(height, int)) or (height <= 0):
      raise ValueError('Invalid value for the height.')

    self._height = height

  @property
  def area(self):
    self._area = self._base * self._height
    return self._area

  @area.setter
  def area(self):
    raise PermissionError('The area cannot be set manually.')

  @property
  def dimensions(self):
    return f'Height: {self.height}\nBase: {self.base}\nArea: {self.area}'

  @dimensions.setter
  def dimensions(self, dimensions:tuple):
    if len(dimensions) != 2:
      raise SyntaxError('To set the dimensions, only the Base and the Height must be provided.')

    if (isinstance(dimensions[0], float) or isinstance(dimensions[0], int)) and (dimensions[0] > 0):
      self.base = dimensions[0]
    else:
      raise TypeError('The base must be a float or an integer and greater than zero.')

    if (isinstance(dimensions[1], float) or isinstance(dimensions[1], int)) and (dimensions[1] > 0):
      self.height = dimensions[1]
    else:
      raise TypeError('The height must be a float or an integer and greater than zero.')
