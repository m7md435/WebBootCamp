class Student:
    def __init__(self, student_id, name, age, enrolled_courses=None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.enrolled_courses = enrolled_courses if enrolled_courses is not None else []

    def enroll_course(self, course_code):
        if course_code not in self.enrolled_courses:
            self.enrolled_courses.append(course_code)

    def drop_course(self, course_code):
        if course_code in self.enrolled_courses:
            self.enrolled_courses.remove(course_code)

    def display_info(self):
        courses = ", ".join(self.enrolled_courses) if self.enrolled_courses else "None"
        return f"{self.student_id} | {self.name} | Age {self.age}\nCourses: {courses}"
