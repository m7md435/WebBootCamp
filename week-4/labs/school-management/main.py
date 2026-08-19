from pathlib import Path
import json
class StudentNotFoundError(Exception):
    pass

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

data_file = data_dir / "students.json"


students = [
    {"name": "Sara", "score": 95},
    {"name": "ali", "score": 85},
      {"name": " ", "score": 90},
        {"name": "Ahmed", "score": 110}  ]

with open(data_file, "w") as file:
    json.dump(students, file, indent=4)

try:
    with open(data_file, "r") as file:
        students = json.load(file)

    for student in students:
        if "name" not in student or "score" not in student:
            raise StudentNotFoundError(f"Invalid student record: {student}")

        if not isinstance(student["name"], str) or not student["name"].strip():
            raise StudentNotFoundError(f"Invalid name: {student['name']!r}. Name must be a non-empty string.")

        if not 0 <= student["score"] <= 100:
            raise StudentNotFoundError(f"Invalid score for {student['name']!r}: {student['score']}. Score must be between 0 and 100.")

except json.JSONDecodeError:
    print("Invalid JSON")

except StudentNotFoundError as e:
    print("Error:", e)