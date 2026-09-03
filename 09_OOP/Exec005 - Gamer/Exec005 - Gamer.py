# Exec 05
from rich import print
from rich.panel import Panel

class Gamer:
  favorites = []

  def __init__(self, name, nickname):
    self.name = name
    self.nickname = nickname

    print(f'The Gamer {self.name} with nickname {self.nickname} has been registered.')

  def add_favorite(self,title):
    self.favorites.append(title)
    self.favorites = sorted(self.favorites,key=str.lower)

  def profile(self):
    content = f'Real name: [black on white]{self.name}[/]'
    content += f'\n\nFavorite games: '
    for i in range(len(self.favorites)):
      content += f'\n:video_game: {self.favorites[i]}'

    print(Panel(content,title=f'Player: {self.nickname}', style='white',expand=False))

gamer = Gamer('Feipe Maillo','Gemini Saga')
gamer.add_favorite('Silent Hill')
gamer.add_favorite('Resident Evil')
gamer.add_favorite('Horizon Zero Dawn')
gamer.profile()
