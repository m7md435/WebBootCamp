#part 1
import csv
with open("student.csv", 
          "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Course"])
    writer.writerow(["Alice", "Math"])
    writer.writerow(["Bob", "Science"])

#part 2

import json

students = [
    {"name": "Sara", "score": "92"},
    {"name": "Ali", "score": "85"}
]

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=2)

with open("students.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

print(loaded[0]["name"])  

#part 3

try:
    score = int(input("Enter your score: "))
except ValueError as er:
    print("Enter a whole number.")
    print(er)
print("program continues...")

#part 4
from pathlib import Path

try:
    text = Path("students.txt").read_text(encoding="utf-8")

except FileNotFoundError:
    print("student file not found")
except Exception:
    print("student file cannot be read.")

#part 5
#else and finally run if the try runs without error
from pathlib import Path

path = Path("students.txt")

try:
    text = path.read_text(encoding="utf-8")

except OSError as error:
    print("Load failed:", error)

else:
    print(text)
finally: #runs no matter what happens
    print("Load attempted finished")

#part 6
def validate_score(score):
   if not 0 <= score <= 100:
       raise ValueError("Score must be between 0 and 100.")
   return score

try:
    score = validate_score(120)
except ValueError as error:
    print("Invalid score:", error)

#part 7
class studentNotfoundError(Exception):
    pass

def find_student(name, students):
    for student in students:
        if student["name"] == name:
            return student
    raise studentNotfoundError(name)

students = [
    {"name": "Sara"},]

try:
    print(find_student("Ali", students))
except studentNotfoundError as error:
    print("missing student:", error)  