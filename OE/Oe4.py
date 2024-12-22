print("OE:4")
class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} attacks {target.name}! {target.name}'s remaining health is {target.health}.")

    def special_move(self):
        pass

    def defend(self, attacker):
        damage_taken = max(attacker.power // 2, 1)
        self.health -= damage_taken
        print(f"{self.name} defends! {self.name} takes {damage_taken} damage. Remaining health: {self.health}")


class Warrior(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def special_move(self):
        print(f"{self.name} uses Shield Bash!")
        self.power *= 2


class Mage(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def special_move(self):
        print(f"{self.name} casts Fireball!")
        self.power = 100


class Archer(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def special_move(self):
        print(f"{self.name} shoots a Piercing Arrow!")
        self.power = self.health


class Monster(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def special_move(self):
        print(f"{self.name} roars and gains extra health!")
        self.health += 50


def simulate_battle():
    warrior = Warrior("Warrior", 200, 30)
    mage = Mage("Mage", 150, 20)
    archer = Archer("Archer", 120, 25)
    monster = Monster("Monster", 300, 15)

    characters = [warrior, mage, archer]
    for character in characters:
        character.attack(monster)
        character.special_move()

    monster.attack(warrior)
    monster.attack(mage)
    monster.attack(archer)

    print("\nPolymorphism in action:")
    for character in characters + [monster]:
        character.special_move()

simulate_battle()