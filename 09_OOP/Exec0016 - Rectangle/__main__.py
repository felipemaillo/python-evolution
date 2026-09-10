from rectangle import Rectangle

def main():
  rectangle1 = Rectangle()
  rectangle1.base = 12
  rectangle1.height = 4
  print(rectangle1.dimensions)

  rectangle2 = Rectangle(9, 4)
  print(rectangle2.dimensions)

  rectangle3 = Rectangle()
  rectangle3.dimensions = (10, 7)
  print(rectangle3.dimensions)

if __name__ == "__main__":
  main()
