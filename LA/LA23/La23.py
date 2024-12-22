print("LA 23")
class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
    def introduce(func):
        def introduce(*args, **kwargs):
            print("introducing...")
            result = func(*args, **kwargs)
            print("this character is amazing!..")
            return result
        return introduce
    @introduce        
    def character_intro(self):
        print(f"i am {self.name} and i can use {self.ability}.")
naruto = AnimeCharacter("john paul","barbie")
naruto.character_intro()
