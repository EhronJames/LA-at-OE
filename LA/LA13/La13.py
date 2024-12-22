print("LA:13")
class Animal():
    def __init__(self,fish,klase):
        self.fish = fish
        self.klase = klase

    def describeFish(self):
        print(f"{self.fish}, {self.klase}")
class fish(Animal):
    def __init__(self,fish,can_swim):
        super().__init__(fish,type)
        self.can_swim = can_swim

fizz = fish("tahong", True)
fizz.describeFish()
print(fizz.can_swim)
