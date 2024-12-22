print("La:20")

class LumpiaWrapper:
    def __init__(self, main_ingredient, onion, carrot):
        self.main_ingredient = main_ingredient
        self._onion = onion
        self.__carrot = carrot

    def __str__(self):
        return (
            f"Ang lumpia ko ay may {self.main_ingredient}, "
            f"{self._onion} kilo ng sibuyas, at {self.__carrot} kilo ng karot."
        )

    def get_carrot(self):
        return self.__carrot


shanghai = LumpiaWrapper("baboy", 1, 2)
print(shanghai.get_carrot())
print(shanghai)