print("LA: 14")
class Spiderman:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describeSpiderman(self):
        print(f"{self.name},{self.age}")

class Tobey(Spiderman):
    def __init__(self, age, movieTitle):
        super().__init__('Tobey', age)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, age, movieTitle):
        super().__init__('Andrew', age)
        self.movieTitle = movieTitle

class Tom(Spiderman):
    def __init__(self, age, movieTitle):
        super().__init__('Tom', age)
        self.movieTitle = movieTitle

tobey = Tobey(age=47, movieTitle="Spiderman1")
andrew = Andrew(age=40, movieTitle="Spiderman2")
tom = Tom(age=28, movieTitle="No Home")

print(f"{tobey.name.upper()} - {tobey.movieTitle}")
print(f"{andrew.name.upper()} - {andrew.movieTitle}")
print(f"{tom.name.upper()} - {tom.movieTitle}")
