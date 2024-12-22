print("LA:3")
class character:
    def __init__(self, name):
        self.name = name

    def describe(self, role):
        print(f"{self.name} is a {role} hero.")
hero = character("Chou")
hero.describe("Fighter")
