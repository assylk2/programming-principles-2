class Flyer:
    def fly(self):
        print("Can fly")

class Swimmer:
    def swim(self):
        print("Can swim")

# Multiple inheritance
class Duck(Flyer, Swimmer):
    pass

duck1 = Duck()
duck1.fly()
duck1.swim()