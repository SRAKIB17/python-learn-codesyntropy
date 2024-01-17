
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p01 = Student(name="Prome", age=23)
p01.age = 28
print(p01.age)
del Student
p02 = Student(name="X", age=25)
