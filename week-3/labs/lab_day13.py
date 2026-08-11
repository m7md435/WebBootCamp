import math
#lab 1 

students = ["sara", "john", "mike", "lisa"]

for student in students:
    print(student)


iterable = enumerate(students)
print(next(iterable))

#lab 2

set_col = {"abdullah", "mohammed", "sara", "dalal"}
tuple_col = (11, 22, 33, 44, 55, 66)
dict_col = {"name": "sara", "age": 22, "has_car": True}
list_col = ["abc", 33 , (33 ,33)]
for c in dict_col.values():
    print(type(c))
print(set_col)
print(tuple_col)
print(dict_col)
print(list_col)
print(type(set_col))
print(type(tuple_col))
print(type(dict_col))
print(type(list_col))

#lab 3

cars = ["bmw", "audi", "toyota", "honda"]

print(cars[3])
print(cars[-1])
print(cars[1:3])
print(cars[::-1])

#lab 4
tasks = [" Read email", "open ticket"]
tasks[0] = "login " 
tasks.append("check notifications")
tasks.insert(1, "review tasks")
tasks.pop(3)
print(tasks)

#lab 5

nums = [1, 2, 3, 4, 5]

print(sum(nums))
print(len(nums))
print(max(nums))
print(min(nums))
print(sorted(nums))
print(math.sqrt(max(nums)))
print(math.pow(2, 3))
print(math.__doc__)
print(nums.pop(3))
print(sorted(nums, reverse=True))

#lab 6

skills = {"python", "django", "flask", "fastapi", "java"}

skills.add("css")
skills.add("html")  
skills.discard("java")
print(skills)

