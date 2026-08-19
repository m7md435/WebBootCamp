class student:
    pass

print(student)
print(type(student))

class Student:
    pass
student_one = Student()
student_two = Student()

print(student_one)
print(student_one is student_two)


class Student:
    def __init__(self, name,  score): # constructor
        self.name = name
        self.score = score

student_one = Student("sara", 95)
print(student_one.name)
print(student_one.score)


class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")

student_one = Student("omar")
student_one.introduce()  # Output: Hello, my name is omar.


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

sara = Student("sara", 92)
omar = Student("omar", 81)

sara.score = 95

print(f"{sara.name} scored {sara.score}")  # Output: sara scored 95
print(f"{omar.name} scored {omar.score}")  # Output: omar scored 81
print(omar is sara)  # Output: False
print( isinstance(omar, Student))  # Output: True


class Student:
    academy ="tuwaiq academy"

    def __init__(self, name):
        self.name = name

sara = Student("sara")

print(Student.academy)  # Output: tuwaiq academy
print(sara.academy)  # Output: tuwaiq academy


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display_results(self):
        print(f"{self.name} scored {self.score}")

student_one = Student("lina", 88)
student_one.display_results()  # Output: lina scored 88 


class Counter:
    def __init__(self):
        self.Value = 0

    def increment(self):
        self.Value += 1

counter = Counter()
counter.increment()
counter.increment()

print(counter.Value)  # Output: 2


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle = Rectangle(5, 3)
print(rectangle.area())  # Output: 15


class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance


    def withdraw(self, amount):
        if amount <=  0 and amount >= self.balance:
            return False

        self.balance -= amount
        return True 
account = BankAccount(500)
print(account.withdraw(200))  # Output: True
print(account.balance)  # Output: 300


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return f"Student Name: {self.name}, Score: {self.score}"

student = Student("sara", 95)
print(student)  # Output: Student Name: sara, Score: 95



class counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

first = counter()
second = counter()

first.increment()

print(first.value)  # Output: 1
print(second.value)  # Output: 0


class Student:
    def __init__(self, name):
        self.name = name
     

    def greeting(self):
        print(f"Hello, {self.name}.")

student = [
    Student("sara"),
    Student("omar"),
    Student("ali")
]

for student in student:
    student.greeting()

class Student:
    pass

student = Student()

print(type(student))
print(type(student) is Student)  # Output: True
print(isinstance(student, Student))  # Output: True



class Student:
    def __init__(self, name, score):
        self.name = name
        self._score = score

student = Student("sara", 95)

print(student.name)  # Output: sara
print(student._score)  # Output: 95 


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score  

    def average_score(self):
        return sum(self.score) / len(self.score)

    def add_score(self, score):
        if 0 <= score <= 100:
            self.score.append(score)
        else:
            raise ValueError("Score must be between 0 and 100.")

student = Student("sara", [80 , 90])
student.add_score(100)
print(f"{student.name}'s average score is: {student.average_score():.2f}")  # Output: sara's average score is: 90.00    