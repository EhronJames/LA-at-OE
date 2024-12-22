print("lA:24")
from abc import ABC, abstractmethod

class GameChar(ABC):
    
    @abstractmethod
    def attack(self):
        pass


class Warrior(GameChar):
    def attack(self):
        print("Swings sword!")

class Mage(GameChar):
    def attack(self):
        print("Casts a fireball!")

class Archer(GameChar):
    def attack(self):
        print("Shoots an arrow!")


class Healer(GameChar):
    def attack(self):
        print("Casts healing spell on ally!")


def main():
    warrior = Warrior()
    mage = Mage()
    archer = Archer()
    healer = Healer()

    warrior.attack()
    mage.attack()
    archer.attack()
    healer.attack()

if __name__ == "__main__":
  main()
