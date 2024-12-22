print("LA:18")
class Burger:
    def __init__(self, bun, patty, cheese, toppings):
        self.bun = bun
        self.patty = patty
        self.cheese = cheese
        self.toppings = toppings

    def __str__(self):
        toppings_str = ', '.join(self.toppings) if self.toppings else "No toppings"
        return f"A burger with a {self.bun} bun, {self.patty} patty, {self.cheese} cheese, topped with {toppings_str}."

burger1 = Burger("Sesame", "Beef", "Cheddar", ["Lettuce", "Tomato", "Pickles"])
burger2 = Burger("Whole Wheat", "Chicken", "Swiss", ["Avocado", "Onions", "Bacon"])
burger3 = Burger("Pretzel", "Veggie", "American", ["Mushrooms", "Spinach", "Mustard"])

print(burger1)
print(burger2)
print(burger3)
