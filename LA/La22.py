print("LA: 22")
class BdayParty:
    def __init__(self, theme, foods, special_dish):
        self.theme = theme
        self.foods = foods
        self.__special_dish = special_dish

    def print_foods(self):
        print(f"Theme: {self.theme}")
        print("Foods:")
        for food in self.foods:
            print(f"- {food}")
        self.__secret_dish()

    def __secret_dish(self):
        print(f"Secret Dish: {self.__special_dish}")

p1 = BdayParty("Spiderman",["Burger", "Coke","Chips"], "Cookies" )
p2 = BdayParty("Halloween",["Cake", "7up", "hatdog"],"Egg")
p3 = BdayParty("Xmas", ["Sinigang", "Rc", "adobo"], "adobo")

p1.print_foods()
print()
p2.print_foods()
print()
p3.print_foods()
print()