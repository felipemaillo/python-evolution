# Exec 07
from rich import print
from rich.panel import Panel
import subprocess

class RemoteControl:
  on = False
  current_channel = 1
  current_volume = 1
  channel_min = 1
  channel_max = 5
  volume_min = 1
  volume_max = 5

  def __init__(self):
    self.display()

  def clearDisplay(self):
    subprocess.run(['clear'], shell=True)

  def display(self):
    self.clearDisplay()

    if not (self.on):
      print(Panel("[red]The TV is off[/]",title='[ TV ]', style='white',expand=False))
    else:
      channels = ''
      for channel in range(self.channel_min, self.channel_max + 1):
        if channel == self.current_channel:
          channels += f'[white on yellow] {self.current_channel} [/]'
        else:
          channels += f' {channel} '

      volumes = ''
      for volume in range(self.volume_min, self.volume_max + 1):
        if volume <= self.current_volume:
          volumes += f'[white on green]  [/]'
        else:
          volumes += '  '

      print(Panel(f'CHANNEL = {channels}\nVOLUME  = {volumes} ',title='[ TV ]', style='white',expand=False))

    print(f'< CH{self.current_channel} >',end='   ')
    print(f'- VOL{self.current_volume} +',end=' ')

    self.command(input(' '))

  def command(self,command):
    if command == '@': self.turnOnOff()
    if command == '<': self.channel('d')
    if command == '>': self.channel('a')
    if command == '-': self.volume('d')
    if command == '+': self.volume('a')
    if command == '0': exit()

    self.display()

  def turnOnOff(self):
    self.on = False if (self.on) else True

  def channel(self,type):
    if not (self.on):
      return

    if (type == 'a'):
      self.current_channel = self.current_channel + 1 if self.current_channel < self.channel_max else self.channel_min
    else:
      self.current_channel = self.current_channel - 1 if self.current_channel > self.channel_min else self.channel_max

  def volume(self,type):
    if not (self.on):
      return

    if (type == 'a'):
      self.current_volume = self.current_volume + 1 if self.current_volume < self.volume_max else self.volume_max
    else:
      self.current_volume = self.current_volume - 1 if self.current_volume > self.volume_min else self.volume_min

remote = RemoteControl()
