class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    # Overriding parent method
    def speak(self):
        print("Meow")

cat1 = Cat()
cat1.speak()