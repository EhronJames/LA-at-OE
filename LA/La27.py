print("La;27")
from abc import ABC, abstractmethod

class NinjaTurtles(ABC):
    def __init__(self, real_name, __alias):
       self.real_name = real_name
    @property
    @abstractmethod
    def __init__(self, real_name):
        pass

class Leonardo (NinjaTurtles):
     def __init__(self, real_name, __alias):
        self.real_name = real_name 
        self.__alias = __alias
     @property
     def alias(self):
        return self.__alias

class MichaelAngelo (NinjaTurtles):
     def __init__(self, real_name, __alias):
        self.real_name = real_name 
        self.__alias = __alias
     @property
     def alias(self):
        return self.__alias     

class Donatello (NinjaTurtles):
     def __init__(self, real_name, __alias):
        self.real_name = real_name 
        self.__alias = __alias
     @property
     def alias(self):
        return self.__alias

class Raphael (NinjaTurtles):
     def __init__(self, real_name, __alias):
        self.real_name = real_name 
        self.__alias = __alias
     @property
     def alias(self):
        return self.__alias

if __name__ == "__main__":
    epo = Leonardo ("Leonardo", "roldd")
    epo1 = MichaelAngelo ("MichaelAngelo", "zakss")
    epo2 = Donatello ("Donatello", "Mhasdf")
    epo3 = Raphael ("Raphael", "palku")
    print(epo.alias)
    print(epo1.alias)
    print(epo2.alias)
    print(epo3.alias)
    import sominebsit2b

Leonardo = sominebsit2b.Leonardo ("Leonardo", "roldd")
MichaelAngelo = sominebsit2b.MichaelAngelo ("MichaelAngelo", "zakss")
Donatello = sominebsit2b.Donatello ("Donatello", "Mhasdf")
Raphael = sominebsit2b.Raphael ("Raphael", "oalku")

print(Leonardo.alias)
print(MichaelAngelo.alias)
print(Donatello.alias)
print(Raphael.alias)