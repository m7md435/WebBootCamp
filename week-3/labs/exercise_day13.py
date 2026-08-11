# #exercise 1

# name = input(" Enter youre name: ")

# for i in name:
#     print(i)

# #exercise 2

# students = ["Ali", "Ahmed", "Hassan", "Hussain", "Fatima"]
# print(students)
# print(students[0])
# print(type(students))

# #exercise 3

# colors = ["red", "green", "blue", "yellow"]
# print(colors[0])
# print(colors[1])
# print(colors[-1])

# #exercise 4

# numbers = [10, 20, 30, 40, 50]
# print(numbers[1:4])
# print(numbers[:3])
# print(numbers[::2])
# print(numbers[::-1])

# #exercise 5

# tasks = ["plan", "code"]

# tasks[0] = "design"
# tasks.append("test")
# tasks.insert(1, "review")

# print(tasks)

# #exercise 6

# scores = [88, 72, 95, 81]
# scores.remove(72)
# last = scores.pop()
# scores.sort()

# print(scores)
# print(last)

# #exercise 7

# students = ["sarah", "omar", "lina"]

# for student in students:
#     print(student)

# for index, student in enumerate(students):
#     print( index, student)

# #exercise 8

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[0])
# print(matrix[1][2]) # output: 6

# #exercise 9

# locations = (24.7136, 46.6753)  # Riyadh coordinates

# print(locations[0])  
# print(locations[-1])  

# # locations[0] = 25.0  # This will raise an error since tuples are immutable    

# #exercise 10

# student = ("sarah", 22, "python", "has laptop", "has internet")

# name, age, course, *other = student

# print(name)
# print(age)
# print(course)
# print(other)

# #exercise 11

# skills = {"python", "git", "python"}

# skills.add("Django")

# print(skills)
# print("git" in skills)  # Output: True
# print(len(skills))  # Output: 3

# #exercise 12

# backend = {"python", "django", "sql"}
# frontend = {"html", "css", "javascript", "sql"}

# print(backend | frontend) # Output: {'python', 'django', 'sql', 'html', 'css', 'javascript'}
# print(backend & frontend) # Output: {'sql'}
# print(backend - frontend) # Output: {'python', 'django'}

# #exercise 13

# student = {
#     "name": "sara",
#     "age": 22,
#     "course": "python",
# }

# print(student["name"])  # Output: sara

# #exercise 14

# student = {
#     "name": "sara",
#     "score": 90
# }

# student["score"] = 95
# student["grade"] = "A"

# email = student.get("email", "Not set")
# grade = student.pop("grade")

# print(student)

# #exercise 15
# student = {
#     "name": "sara",
#     "score": 95
# }

# for key in student:
#     print(key)

# for key, value in student.items():
#     print(key, value)

# #exercise 16 # you can use these operators with lists, tuples, sets, and dictionaries

# name = ["sara", "omar"]
# skills = ["python", "git"]
# student = {"name": "sara", "skills": 95}

# print(len(name))
# print("python" in skills)
# print("name" in student) #check keys
# print( 95 in student.values()) #check values

# #exercise 17

# students = [
#     {"name": "sara", "score": 95},
#     {"name": "omar", "score": 88},
# ]

# for student in students:
#     print(f"{student['name']} scored {student['score']}")

