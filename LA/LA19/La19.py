print("LA:19")

class Burger:
    def __init__(self, bun, patty, cheese, toppings):
        self.bun = bun
        self.__patty = patty
        self.__cheese = cheese
        self.__toppings = toppings

    def __str__(self):
        toppings_str = ', '.join(self.__toppings) if self.__toppings else "No toppings"
        return f"A burger with a {self.bun} bun, {self.__patty} patty, {self.__cheese} cheese, topped with {toppings_str}."

    def get_ingredients(self):
        return {
            "patty": self.__patty,
            "cheese": self.__cheese,
            "toppings": self.__toppings
        }

burger1 = Burger("Sesame", "Beef", "Cheddar", ["Lettuce", "Tomato", "Pickles"])

try:
    print(burger1.__patty)
except AttributeError as e:
    print(e)

print(burger1.get_ingredients())
