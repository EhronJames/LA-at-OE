print("LA:12")
class toy():
    def __init__(self,name, price):
        self.name = name
        self.price = price

    def describeToy(self):
        print(f"{self.name} {self.price}")
class car(toy):
    def __init__(self,name,price):
        super().__init__(name,price)

Car = car("asd", "dsa")
Car.describeToy()
