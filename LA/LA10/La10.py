print("LA:10")
class vehicle():
    def __init__(self,brand,model,fuel):
        self.brand = brand 
        self.model = model
        self.fuel = fuel

    def describeVehicle(self):
        print(f"{self.brand} {self.model} {self.fuel}")
class Car(vehicle):
    pass
ford = Car("ford","focus", "pula")
ford.describeVehicle()

class Motor(vehicle):
    pass
honda = Motor("Kawasaki", "barako", "green")
honda.describeVehicle()
