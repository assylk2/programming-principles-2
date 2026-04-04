# Example 1: Positional arguments
def add_numbers(a, b):

    print("Sum:", a + b)

add_numbers(5, 3)


# Example 2: Default argument
def power(base, exponent=2):

    print("Result:", base ** exponent)

power(4)        # uses default exponent
power(4, 3)     # custom exponent