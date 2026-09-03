# Exec 03
from rich import print
from rich.panel import Panel

class Barbecue:
  price_kg = 82.40
  standard_consumption = 400
  total_cost = 0
  price_per_person = 0
  meat_amount = 0

  def __init__(self, qty_people):
    self.qty_people = qty_people

  def calculate(self):
    self.meat_amount = (self.standard_consumption * self.qty_people) / 1000
    self.total_cost = self.meat_amount * self.price_kg
    self.price_per_person = self.total_cost / self.qty_people

    content = f'[white]For a barbecue with [green]{self.qty_people}[/] people, you will need to buy [green]{self.meat_amount} Kg[/] of meat.'
    content += f'\nThe total cost is [red]¢ {self.total_cost:,.2f}[/] and the cost per person is [red]¢ {self.price_per_person:,.2f}[/]'
    print(Panel(content,title='BBQ Calculator', style='blue',expand=False))

barbecue = Barbecue(15)
barbecue.calculate()
