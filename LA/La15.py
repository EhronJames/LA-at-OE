print("LA: 15")
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Bark")

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Meow")

class Bird:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Chirp")

def animal_sounds(animal):
    animal.speak()


dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")
animals = [dog, cat, bird]


for animal in animals:
    animal_sounds(animal)