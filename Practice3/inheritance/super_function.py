class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        # Call parent constructor
        super().__init__(name)
        self.grade = grade

student1 = Student("Asyl", 12)
print(student1.name, student1.grade)