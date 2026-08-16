class Student:
        def __init__(self, name, score):
            self.name = name
            self.score = score

        def add_score(self, score):
             if score >= 0 and score <= 100:
                self.score.append(score)

class course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        

    def average_course_score(self):
        if len(self.students) == 0:
            return 0
        return sum(student.score) / len(student.score)

    def __str__(self):
        return f"Course Name: {self.name}, Number of Students: {len(self.students)}, Average Course Score: {self.average_course_score():.2f}"

course1 = course("Python")
student1 = Student("sara", [80, 90])
student2 = Student("omar", [70, 85])
course1.add_student(student1)
course1.add_student(student2)
student1.add_score(100)


for student in course1.students:
    print(f"Student Name: {student.name}, Score: {student.score} , Average Score: {course1.average_course_score():.2f}")