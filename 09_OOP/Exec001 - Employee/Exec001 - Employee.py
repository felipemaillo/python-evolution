# Exec 01
from rich import print
from rich.panel import Panel

class Employee:
  company = 'Stefanini Group'

  def __init__(self, name, department, role):
    self.name = name
    self.department = department
    self.role = role

  def introduce(self):
    print(Panel(f'[white]Hello, my name is {self.name}, I work in the {self.department} department as a {self.role} at {self.company}[/] :+1:',title='Employee', style='blue',expand=False))


employee1 = Employee('Maria','Administration','Director')
employee1.introduce()

employee2 = Employee('Pedro','IT','Programmer')
employee2.introduce()
