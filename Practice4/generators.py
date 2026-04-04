# Iterators example

mytuple = ("apple", "banana", "cherry")

myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


# Looping through iterator

mystr = "banana"

for x in mystr:
    print(x)


# Create your own iterator

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)


# Generator example

def mygenerator():
    yield 1
    yield 2
    yield 3

for value in mygenerator():
    print(value)