from character import Character
from random import randint
from rich import print
from rich.panel import Panel

class Mage(Character):
  max_health = 0

  def __init__(self,name,health):
    super().__init__(name,health)
    self.max_health = health
    self.attacks = ['Fire Ball','Dark Magic','Lightning']

  def heal(self):
    current_health = self.health

    if self.health > 0:
      healing = randint(0,100)

      if (self.health + healing) > self.max_health:
        healing = self.max_health - self.health

      self.health += healing

      content = f'Cast a healing spell and recovered [green]{healing}[/] health points.\n'
      content += f'Current health is [yellow]{self.health}[/]'
    else:
      content = f'The character [green]{self.name}[/] is [red]DEAD[/] and cannot heal.'

    print(Panel(content,title=f'Character [green]{self.name}[/][blue]({current_health})[/]',expand=False))