from rich import print
from coffee import Coffee
from milk import Milk
from tea import Tea

def main():
  coffee = Coffee()
  coffee.prepare()
  print('-' * 50)

  milk = Milk()
  milk.prepare()
  print('-' * 50)

  tea = Tea()
  tea.prepare()
  print('-' * 50)

if __name__ == "__main__":
  main()