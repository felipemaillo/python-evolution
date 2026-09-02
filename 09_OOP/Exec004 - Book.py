# Exec 04
from rich import print
from time import sleep

class Book:
  current_page = 1

  def __init__(self, title, page_count):
    self.title = title
    self.page_count = page_count
    print(f'You just opened the book {self.title} which has {self.page_count} pages in total.\nYou are now on page 1')

  def turn_pages(self, qty):
    for i in range(0,qty,1):
      sleep(0.3)
      if ((self.current_page) < self.page_count):
        self.current_page += 1
        print(f'[blue]Pg{self.current_page}[/] [yellow]>[/]',end=' ')

        if (i + 1 == qty):
          sleep(0.3)
          print(f'You turned {qty} pages and are now on page {self.current_page}')
      else:
        sleep(0.3)
        print(f'You finished reading the book [red]{self.title}[/]. [green]CONGRATULATIONS!![/]')
        break

book = Book('The Art of War',20)
book.turn_pages(5)
book.turn_pages(10)
book.turn_pages(50)
