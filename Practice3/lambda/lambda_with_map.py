# Using lambda with map()
numbers = [1, 2, 3, 4]

# Multiply each number by 2
doubled = list(map(lambda x: x * 2, numbers))

print("Doubled numbers:", doubled)