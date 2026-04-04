# Using __init__ constructor

class Student:
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old.")

student1 = Student("Asyl", 17)
student1.introduce()