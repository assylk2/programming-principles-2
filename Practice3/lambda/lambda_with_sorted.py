# Using lambda with sorted()

students = [
    {"name": "Ali", "grade": 85},
    {"name": "Asyl", "grade": 95},
    {"name": "Dana", "grade": 78}
]

# Sort by grade
sorted_students = sorted(students, key=lambda student: student["grade"])

print("Sorted by grade:", sorted_students)