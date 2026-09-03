from circle import Circle
from square import Square

def main():
  circle = Circle(12)
  circle.perimeter()
  circle.area()

  print('')

  square = Square(20)
  square.perimeter()
  square.area()

if __name__ == "__main__":
  main()