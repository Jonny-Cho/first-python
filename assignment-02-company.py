class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Workmate(Human):
    position = "대리"

human1 = Workmate("조준희", "27", "남")
print(human1.name)
print(human1.position)