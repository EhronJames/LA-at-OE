print("LA:9")
class Car:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"This car is a {self.brand}."

my_car = Car("Ford")
print(my_car)

del my_car

try:
    print(my_car)
except NameError as e:
    print(e)