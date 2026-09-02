# Exec 06
from rich import print

class Pen:
  """
  Available colors: 'yellow','blue','red' and 'green'
  """
  colors = ['yellow','blue','red','green']
  selected_color = colors[1]
  capped = True

  def uncap(self):
    if (self.capped):
      self.capped = False
    else:
      print('The pen is already uncapped.')

  def cap(self):
    if not (self.capped):
      self.capped = True
    else:
      print('The pen is already capped.')

  def write(self,phrase):
    if (self.capped):
      print('You need to uncap the pen before writing.')
    else:
      print(f'[{self.selected_color}]{phrase}[/]',end='')

  def line_break(self,qty_lines = 1):
    print('\n' * qty_lines, end='')

  def change_color(self, color):
    if (color not in self.colors):
      print('The selected color does not exist.')
      print(f'Available colors are: {self.colors}')
    else:
      self.selected_color = color

pen = Pen()
pen.uncap()
pen.write('Test')
pen.change_color('yellow')
pen.write('Test')
pen.line_break(1)
pen.change_color('green')
pen.write('Test')
