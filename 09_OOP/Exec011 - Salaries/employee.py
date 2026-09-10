from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Employee(ABC):
  minimum_wage = 1612
  social_security_tax = 7.5

  def __init__(self,name = None):
    self.name = name
    self.gross_salary = 0
    self.salary = 0

  def analyze_salary(self):
    print(Panel(f'The salary of [green]{self.name}[/] [yellow]({type(self).__name__})[/] is [blue]¢ {self.salary:,.2f}[/] and corresponds to [red]{self.salary / Employee.minimum_wage:,.1f} minimum wages[/].',title='Salary Analysis', style='white', expand=False))

  @abstractmethod
  def calculate_salary(self):
    pass
