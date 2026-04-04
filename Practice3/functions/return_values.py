# Example 1: Returning a value
def multiply(a, b):
    
    return a * b

result = multiply(4, 5)
print("Multiplication result:", result)


# Example 2: Passing list as argument
def count_elements(items):
    
    return len(items)

numbers = [1, 2, 3, 4, 5]
print("List length:", count_elements(numbers))