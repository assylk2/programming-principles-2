from functools import reduce

nums = [1, 2, 3, 4, 5]

# map (умножить на 2)
mapped = list(map(lambda x: x * 2, nums))
print(mapped)

# filter (только чётные)
filtered = list(filter(lambda x: x % 2 == 0, nums))
print(filtered)

# reduce (сумма)
total = reduce(lambda x, y: x + y, nums)
print(total)