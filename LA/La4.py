print("LA:4")
class character:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return "{hero.name} is a {self.role} hero. "

    
hero = character("Chou", "fighter")
print(hero)