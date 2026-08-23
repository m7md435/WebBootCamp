# Unit 2 School Management System

This is a Python console application for managing students, courses, and teachers.

## Features

- Add students, courses, and teachers
- Enroll student in course
- Drop student from course
- Assign teacher to course
- View students and courses
- View one student's courses
- View one course's students
- Save and load data using JSON files
- Handle errors and log them to `logs.txt`

## Folder Structure

```text
school_system/
├── main.py
├── models/
│   ├── student.py
│   ├── course.py
│   ├── teacher.py
│   └── school.py
├── utils/
│   ├── file_handler.py
│   ├── validators.py
│   └── logging.py
└── data/
    ├── students.json
    ├── courses.json
    └── teachers.json
```

## Use Case Diagram
![](https://github.com/m7md435/WebBootCamp/blob/17e2ce3be9389aa4b39d1e45f6c57a87299ed6b9/project-unit-2/use%20case%20diagram-2026-08-23-135750.png)
## Class Diagram
![](https://github.com/m7md435/WebBootCamp/blob/4272a24962e1b29df621e1b993e586f316fc76a0/project-unit-2/class%20diagram-2026-08-23-140220.png)
## Activity Diagram for the Add Student Scenario
![](https://github.com/m7md435/WebBootCamp/blob/cfb44ea0e69c94685b5e7ebed9b054597ecd38c6/project-unit-2/activity%20diagram-2026-08-23-135947.png)
## How to Run

From the workspace root (`project-unit-2`):

```powershell
python school_system/main.py
```

## Data Files

The app stores data in:

- `school_system/data/students.json`
- `school_system/data/courses.json`
- `school_system/data/teachers.json`

Data is loaded when the app starts and saved when you choose **Save and Exit** from the menu.
