class Student:
        def __init__(self, name, score):
            self.name = name
            self.score = score

        def add_score(self, score):
             if score >= 0 and score <= 100:
                self.score.append(score)

        def __str__(self):
            return f"Student Name: {self.name}, Score: {self.score} Average Score: {self.average_score():.2f}"

        def average_score(self):
            if len(self.score) == 0:
                return 0
            return sum(self.score) / len(self.score)


course = [
    Student("sara", [99, 65, 100]),
    Student("omar", [88]),
    Student("ali", [20,  80])

]
for student in course:
    student.add_score(90)
    print(student)