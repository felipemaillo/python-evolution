# Exec 02
from rich import print
from rich.panel import Panel

class Product:

  def __init__(self, name, price):
    self.name = name
    self.price = price

  def label(self):
    content = f'[white]{self.name.center(30,' ')}\n{'-' * 30}\n{self.price.center(30,'-')}[/]'
    print(Panel(content,title='Product', style='blue',expand=False))

product1 = Product('Macbook','¢ 1600,00')
product1.label()
