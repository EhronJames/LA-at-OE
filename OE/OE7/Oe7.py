print("OE:7")
class TekkenChar:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper(*args, **kwargs):
            print("Introducing.")
            func(*args, **kwargs)
            print("This character is amazing!")
        return wrapper

a = TekkenChar("Nina", "Fatal Judgement")

def character_intro():
    print(f"I am {a.name} and I can use {a.ability}.")

character_intro = a.introduce(character_intro)

character_intro()
