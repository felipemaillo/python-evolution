from abc import ABC, abstractmethod
import random
from rich import print
from rich.panel import Panel

class Character(ABC):

  def __init__(self,name,health):
    self.name = name
    self.health = health
    self.attacks = []

  def attack(self,target,power):
    if self.health > 0 and target.health > 0:
      damage = random.randint(0,power)
      target_current_health = target.health
      target.take_damage(damage)

      content = f'Attacked [blue]{target.name}[/][yellow]({target_current_health}[/]) '
      content += f'with a [red]{random.choice(self.attacks)}[/] of power {power}.\n'
      content += f'[blue]{target.name}[/] took [red]{damage} damage[/] '
      content += f'and their remaining health is [yellow]{target.health}[/].' if target.health > 0 else f'and [red]DIED[/]'
    else:
      if self.health <= 0:
        content = f'The character [green]{self.name}[/] is [red]DEAD[/] and cannot attack.'
      if target.health <= 0:
        content = f'The character [blue]{target.name}[/] is [red]DEAD[/] and cannot receive attacks.'

    print(Panel(content,title=f'Attack from [green]{self.name}[/][blue]({self.health})[/]',expand=False))

  def take_damage(self,damage):
    self.health -= damage

    if self.health < 0:
      self.health = 0

  @abstractmethod
  def heal(self):
    pass
