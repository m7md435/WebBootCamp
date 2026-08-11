students =[
    {"name": "sara", "score": (99, 65, 100) , "skills": {"git", "python"}},
    {"name": "omar", "score": (88, 50, 60), "skills": {"java", "c++"}},
    {"name": "ali", "score": (20, 70, 80), "skills": {"html", "css"}}
]

for student in students:
    average_score = sum(student["score"]) / len(student["score"])
    student["skills"].add("sql")
    print(f"Name: {student['name']}, Average Score: {average_score:.2f}, Skills: {student['skills']}")
