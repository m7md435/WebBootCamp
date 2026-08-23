from models.course import Course
from models.student import Student
from models.teacher import Teacher
from utils.file_handler import load_data as read_json
from utils.file_handler import save_data as write_json
from utils.logging import log_error


class School:
    def __init__(self, data_folder):
        self.data_folder = data_folder
        self.students = {}
        self.courses = {}
        self.teachers = {}

    def add_student(self, student):
        if student.student_id in self.students:
            raise ValueError("A student with that ID already exists.")
        self.students[student.student_id] = student

    def add_course(self, course):
        if course.course_code in self.courses:
            raise ValueError("A course with that code already exists.")
        self.courses[course.course_code] = course

    def add_teacher(self, teacher):
        if teacher.teacher_id in self.teachers:
            raise ValueError("A teacher with that ID already exists.")
        self.teachers[teacher.teacher_id] = teacher

    def enroll_student(self, student_id, course_code):
        if student_id not in self.students:
            raise ValueError("Student not found.")
        if course_code not in self.courses:
            raise ValueError("Course not found.")
        student = self.students[student_id]
        course = self.courses[course_code]
        if course_code in student.enrolled_courses or student_id in course.enrolled_students:
            raise ValueError("Student is already enrolled in that course.")
        student.enroll_course(course_code)
        course.add_student(student_id)

    def drop_course(self, student_id, course_code):
        if student_id not in self.students:
            raise ValueError("Student not found.")
        if course_code not in self.courses:
            raise ValueError("Course not found.")
        student = self.students[student_id]
        course = self.courses[course_code]
        if course_code not in student.enrolled_courses:
            raise ValueError("Student is not enrolled in that course.")
        student.drop_course(course_code)
        course.remove_student(student_id)

    def assign_teacher(self, teacher_id, course_code):
        if teacher_id not in self.teachers:
            raise ValueError("Teacher not found.")
        if course_code not in self.courses:
            raise ValueError("Course not found.")
        self.courses[course_code].assigned_teacher = teacher_id

    def display_students(self):
        if not self.students:
            print("No students found.")
            return
        for student in self.students.values():
            print(student.display_info())
            print("-" * 30)

    def display_courses(self):
        if not self.courses:
            print("No courses found.")
            return
        for course in self.courses.values():
            print(course.display_info())
            print("-" * 30)

    def load_data(self):
        try:
            student_records = read_json(self.data_folder / "students.json")
            course_records = read_json(self.data_folder / "courses.json")
            teacher_records = read_json(self.data_folder / "teachers.json")
            self.students = {
                record["student_id"]: Student(
                    record["student_id"],
                    record["name"],
                    record["age"],
                    record.get("enrolled_courses", []),
                )
                for record in student_records
            }
            self.courses = {
                record["course_code"]: Course(
                    record["course_code"],
                    record["title"],
                    record.get("assigned_teacher"),
                    record.get("enrolled_students", []),
                )
                for record in course_records
            }
            self.teachers = {
                record["teacher_id"]: Teacher(
                    record["teacher_id"], record["name"], record["subject"]
                )
                for record in teacher_records
            }
        except (KeyError, TypeError, ValueError) as error:
            log_error(f"Missing or invalid field in saved data: {error}")
            self.students = {}
            self.courses = {}
            self.teachers = {}

    def save_data(self):
        student_records = [student.__dict__ for student in self.students.values()]
        course_records = [course.__dict__ for course in self.courses.values()]
        teacher_records = [teacher.__dict__ for teacher in self.teachers.values()]
        write_json(self.data_folder / "students.json", student_records)
        write_json(self.data_folder / "courses.json", course_records)
        write_json(self.data_folder / "teachers.json", teacher_records)
