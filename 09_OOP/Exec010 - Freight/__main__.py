from rich import print
from rich.table import Table
from truck import Truck
from drone import Drone
from motorcycle import Motorcycle

def main():
  distance = 100

  trip = [Motorcycle(distance),Truck(distance),Drone(distance)]

  freights = Table(title=f'[ Freight Table ]')
  freights.add_column('Distance')
  freights.add_column('Type')
  freights.add_column('Freight')
  for item in trip:
    freights.add_row(f'{distance}Km',f'{type(item).__name__}',item.calculate_freight())
  print(freights)

if __name__ == "__main__":
  main()