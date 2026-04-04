class School:
    # Class variable (shared by all objects)
    school_name = "KBTU"

    def __init__(self, student_name):
        # Instance variable
        self.student_name = student_name

student1 = School("Asyl")
student2 = School("Dana")

print(student1.school_name)
print(student2.school_name)

# Modifying instance variable
student1.student_name = "Ali"
print(student1.student_name)