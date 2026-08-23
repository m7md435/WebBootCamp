class Course:
    def __init__(self, course_code, title, assigned_teacher=None, enrolled_students=None):
        self.course_code = course_code
        self.title = title
        self.assigned_teacher = assigned_teacher
        self.enrolled_students = enrolled_students if enrolled_students is not None else []

    def add_student(self, student_id):
        if student_id not in self.enrolled_students:
            self.enrolled_students.append(student_id)

    def remove_student(self, student_id):
        if student_id in self.enrolled_students:
            self.enrolled_students.remove(student_id)

    def display_info(self):
        teacher = self.assigned_teacher if self.assigned_teacher else "Not assigned"
        students = ", ".join(self.enrolled_students) if self.enrolled_students else "None"
        return f"{self.course_code} | {self.title}\nTeacher: {teacher} | Students: {students}"
