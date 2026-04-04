# Parent class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Child class
class Dog(Animal):
    pass

dog1 = Dog()
dog1.speak()