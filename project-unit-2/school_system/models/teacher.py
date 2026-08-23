class Teacher:
    def __init__(self, teacher_id, name, subject):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject

    def display_info(self):
        return f"{self.teacher_id} | {self.name}\nSubject: {self.subject}"


def add_teacher(school, validate_name, validate_text):
    teacher_id = validate_text(input("Teacher ID: "), "Teacher ID")
    name = validate_name(input("Name: "))
    subject = validate_text(input("Subject taught: "), "Subject")
    school.add_teacher(Teacher(teacher_id, name, subject))
    print("Teacher added successfully.")


def assign_teacher(school, validate_text):
    teacher_id = validate_text(input("Teacher ID: "), "Teacher ID")
    course_code = validate_text(input("Course code: "), "Course code")
    school.assign_teacher(teacher_id, course_code)
    print("Teacher assigned successfully.")
