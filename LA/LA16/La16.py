print("LA:16")
class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def operate(self):
        print("Operating!")

class WashingMachine(Appliance):
    def operate(self):
        print("Washing clothes!")

class Refrigerator(Appliance):
    def operate(self):
        print("Keeping food cold!")

class Microwave(Appliance):
    def operate(self):
        print("Heating food!")


washing_machine = WashingMachine("Shingshing", "dsadsa")
refrigerator = Refrigerator("Ref", "asdasd")
microwave = Microwave("Micro", "zxczxc")


appliances = [washing_machine, refrigerator, microwave]


for appliance in appliances:
    appliance.operate()
