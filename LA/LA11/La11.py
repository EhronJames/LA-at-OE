print("LA:11")
class phone():
    def __init__(self,brand,model):
        self.brand = brand 
        self.model = model

    def describePhone(self):
        print(f"{self.brand} {self.model}")
class Android(phone):
    def __init__(self,brand,model):
        phone.__init__(self,brand,model)
apol = Android("tulphone","samsong")
apol.describePhone()
