# Example 1: *args (multiple positional arguments)
def sum_all(*numbers):
    
    total = 0
    for num in numbers:
        total += num
    return total

print("Sum:", sum_all(1, 2, 3, 4))


# Example 2: **kwargs (keyword arguments)
def print_user_info(**info):
    
    for key, value in info.items():
        print(f"{key}: {value}")

print_user_info(name="Asyl", age=17, city="Almaty")