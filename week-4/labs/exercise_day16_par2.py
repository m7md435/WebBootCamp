class Student:
        def __init__(self, name, score):
            self.name = name
            self.score = score

        def add_score(self, score):
             if score >= 0 and score <= 100:
                self.score.append(score)

        def average_course_score(self):
                if len(self.score) == 0:
                    return 0
                return sum(self.score) / len(self.score)
class course:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        

    

    def __str__(self):
        for student in self.students:
            print(f"Student Name: {student.name}, Score: {student.score} , Average Score: {student.average_course_score():.2f}")

course1 = course()
student1 = Student("sara", [80, 90])
student2 = Student("omar", [70, 85])
course1.add_student(student1)
course1.add_student(student2)
student1.add_score(100)

course1.__str__()