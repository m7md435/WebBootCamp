from pathlib import Path

from models.course import Course
from models.school import School
from models.student import Student
from models.teacher import Teacher, add_teacher, assign_teacher
from utils.logging import log_error
from utils.validators import validate_age, validate_name, validate_text


DATA_FOLDER = Path(__file__).resolve().parent / "data"


def add_student(school):
    student_id = validate_text(input("Student ID: "), "Student ID")
    name = validate_name(input("Name: "))
    age = validate_age(input("Age: "))
    school.add_student(Student(student_id, name, age))
    print("Student added successfully.")


def add_course(school):
    course_code = validate_text(input("Course code: "), "Course code")
    title = validate_text(input("Course title: "), "Course title")
    school.add_course(Course(course_code, title))
    print("Course added successfully.")


def enroll_student(school):
    student_id = validate_text(input("Student ID: "), "Student ID")
    course_code = validate_text(input("Course code: "), "Course code")
    school.enroll_student(student_id, course_code)
    print("Student enrolled successfully.")


def drop_course(school):
    student_id = validate_text(input("Student ID: "), "Student ID")
    course_code = validate_text(input("Course code: "), "Course code")
    school.drop_course(student_id, course_code)
    print("Student dropped the course successfully.")


def view_student_courses(school):
    student_id = validate_text(input("Student ID: "), "Student ID")
    if student_id not in school.students:
        raise ValueError("Student not found.")
    student = school.students[student_id]
    print(f"{student.student_id} | {student.name}")
    if not student.enrolled_courses:
        print("Courses: None")
        return
    print("Courses:")
    for course_code in student.enrolled_courses:
        course = school.courses.get(course_code)
        title = course.title if course else "Unknown course"
        print(f"- {course_code} | {title}")


def view_course_students(school):
    course_code = validate_text(input("Course code: "), "Course code")
    if course_code not in school.courses:
        raise ValueError("Course not found.")
    course = school.courses[course_code]
    print(f"{course.course_code} | {course.title}")
    if not course.enrolled_students:
        print("Students: None")
        return
    print("Students:")
    for student_id in course.enrolled_students:
        student = school.students.get(student_id)
        name = student.name if student else "Unknown student"
        print(f"- {student_id} | {name}")


def print_menu():
    print("\nSCHOOL MANAGEMENT SYSTEM")
    print("\n1. Add student")
    print("2. Add course")
    print("3. Enroll student")
    print("4. View students")
    print("5. View courses")
    print("6. Add teacher")
    print("7. Drop course")
    print("8. View student courses")
    print("9. View course students")
    print("10. Assign teacher")
    print("11. Save and Exit")


def main():
    school = School(DATA_FOLDER)
    school.load_data()
    actions = {
        "1": lambda: add_student(school),
        "2": lambda: add_course(school),
        "3": lambda: enroll_student(school),
        "4": school.display_students,
        "5": school.display_courses,
        "6": lambda: add_teacher(school, validate_name, validate_text),
        "7": lambda: drop_course(school),
        "8": lambda: view_student_courses(school),
        "9": lambda: view_course_students(school),
        "10": lambda: assign_teacher(school, validate_text),
    }

    while True:
        print_menu()
        choice = input("\nChoose an option: ").strip()
        if choice == "11":
            school.save_data()
            print("Data saved. Goodbye!")
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid option. Please choose a menu number.")
            continue
        try:
            action()
        except (ValueError, KeyError) as error:
            log_error(str(error))
            print(f"Error: {error}")
        except Exception as error:
            log_error(f"Unexpected error: {error}")
            print("An unexpected error occurred. The program is still running.")


if __name__ == "__main__":
    main()
