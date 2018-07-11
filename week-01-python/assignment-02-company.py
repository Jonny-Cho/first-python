class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Workmate(Human):
        def __init__(self, name, age, gender, position):
            super().__init__(name, age, gender)
            self.position = position

human1 = Workmate("Jonny", 27, "Male", "대리")
print(human1.__dict__)