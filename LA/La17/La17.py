print("LA:17")
class Player():
    def __init__(self, name, health, attack_dmg):
        self.name = name
        self.health = health
        self.attack_dmg = attack_dmg
    def basic_attack(self, target):
        target.health = target.health - self.attack_dmg
        print(f"{self.name} attack's {target.name} has {self.attack_dmg} dmg.")
        print(f"{self.name}, has left {target.health} health.")
ling = Player("ling", 200, 40)
lance = Player("lance", 220, 44)
while ling.health > 0 and lance.health > 0:
    ling.basic_attack(lance)
    if lance.health <= 0:
        print(f"{lance.name} has been defeated! {ling.name} wins!")
        break
    lance.basic_attack(ling)
    if ling.health <= 0:
        print(f"{ling.name} has been defeated! {lance.name} wins!")
