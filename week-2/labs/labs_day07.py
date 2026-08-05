Lab 1: Variable Assignment
student_name = "Ammar"
student_name = "Sarah"

print(student_name)  # overwrite = Sarah


Student_name = "Ammar"
student_name = "Sarah"
#Case Sensitivity
print(student_name)  # output = Sarah
print(Student_name)  # output = Ammar


Lab 2: Variable Assignment and Data Types
student_name = "Mada"
student_age = 20
course = "Web Development bootcamp"
registered = True

MAX_CLASS_SIZE = 25
MAX_CLASS_SIZE = 15  # overwrite = 15

print(f"""\n
Welcome {student_name} to the {course} course!
You are {student_age} years old
Registered status: {registered}
Maximum class size: {MAX_CLASS_SIZE}
""")


printing the data types of the variables
student_name, student_age, student_is_registered = "YES", 20, True


print(type(student_age))
print(type(student_name))
print(type(student_is_registered))

print(isinstance(student_name, str))  # True
print(isinstance(student_age, int))   # True
print(isinstance(student_is_registered, bool))  # True

#Lab 3: Casting and Type Conversion

age = input("Enter your age ")
if (isinstance(age, str)):
    print("You entered an invalid age")
else:
    print("Your are", int(age), "years old")