print("LA:7")
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Toyota", "Red")
print(f"Car 1 Brand: {car1.brand}, Color: {car1.color}")
car1.color = "Black"
print(f"Car 1 Updated Color: {car1.color}")
car2 = Car("Honda", "Green")
print(f"Car 2 Brand: {car2.brand}, Color: {car2.color}")
