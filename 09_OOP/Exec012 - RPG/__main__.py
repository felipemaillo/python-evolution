from warrior import Warrior
from mage import Mage

def main():
  warrior = Warrior("Kratos",2000)
  mage = Mage("Merlin",100)

  warrior.attack(mage,1000)
  mage.heal()

  mage.attack(warrior,1000)
  warrior.heal()

if __name__ == "__main__":
  main()