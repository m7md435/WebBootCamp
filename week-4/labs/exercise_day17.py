#part 1
# from pathlib import Path

# data_file = Path("data") / "student.txt"

# print(data_file)
# print(data_file.name)
# print(data_file.suffix)

#part 2

# from pathlib import Path
# data_dir = Path("data")
# data_dir.mkdir(exist_ok=True)

# data_file = data_dir / "students.txt"
# print(data_dir.is_dir())
# print(data_file.exists())

# #part 3

# from pathlib import Path

# path = Path("notes.txt")

# with path.open("r", encoding = "utf-8") as file:
#     content =file.read()

# print(content)
# print(file.closed)

# #part 4

# from pathlib import Path

# path = Path("notes.txt")

# with path.open("r", encoding = "utf-8") as file:
#     text =file.read()

# same_text = path.read_text(encoding= "utf-8")

# print(text == same_text)

# #part 5

# from pathlib import Path

# path =Path("student.txt")

# with path.open("r", encoding="utf-8") as file:
#     for line in file:
#         name =line.strip()
#         if name:
#             print(name)

# #part 6

# from pathlib import Path

# path =Path("student.txt")

# with path.open("w", encoding="utf-8") as file:
#     count = file.write("sara\nali\n")

# print(count)

# #part 7
# from pathlib import Path
# path = Path("activity.log")

# with path.open("a", encoding="utf-8") as file:
#     file.write("student enrolled: sara\n")

# print("Activity saved")

# #part 8
# from pathlib import Path

# name = ["sara", "محمد", "ali"]
# text ="\n".join(name) +"\n"
# Path("student.txt").write_text(
#     text,
#     encoding="utf-8"
# )