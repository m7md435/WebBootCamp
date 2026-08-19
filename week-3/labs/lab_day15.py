#Lab 1
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for number in numbers:
    squared_numbers.append(number  2)

print(squared_numbers)

#comprehension
squared_numbers = [
    number  2 
    for number in numbers
]
print(squared_numbers)


#Lab 2
prices = [10, 25, 40]

prices_with_vat = [
    round(price * 1.15, 2)
    for price in prices
]
print(prices_with_vat)


#Lab 3
names = ["SaRa", "ArEeJ", "Mashael", "nasser"]

lower = [
    name.lower()
    for name in names
]

upper = [
    name.upper()
    for name in names
]

titled = [
    name.title()
    for name in names
]

print(lower)
print(upper)
print(titled)


#Lab 4
c_temp = [20, 33, 15, 1]

f_temp = [
    (temp * 1.8) + 32
    for temp in c_temp
    if temp > 0
]

print(f_temp)


#Lab 5
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = []
for row in nested_list:
    for item in row:
        flattened_list.append(item)

print(flattened_list)

#comprehension
comp_flattened_list = [
    colomn
    for row in nested_list
    for colomn in row
]

print(comp_flattened_list)


#Lab 6
scores = [45, 55, 65, 75, 86, 95]
passing_scores = [
    "pass" if score >= 60 else "fail"
    for score in scores
]

print(passing_scores)


#Lab 7
skills = ["PYTHON", "Git", "python", "Javascript", "SQL", "git"]
skills_set = {
    skill.lower()
    for skill in skills
}
print(skills_set)


#Lab 8
list_name = ["Sara", "Dalal", "Nouf", "Taif"]

counted_chars = [
    {
        "name": name,
        "count": len(name)
    }
    for name in list_name
]

print(counted_chars)


#Lab 9
new_names = ["Mada", "Khadija", "Sara", "Ahmed"]

upp = (
    name.upper()
    for name in new_names

)
print(next(upp)) #MADA
print(next(upp)) #KHADIJA
print("-" * 10) 
for x in upp:
    print(x)     #SARA, AHMED
#guide practice 

from copy import deepcopy
students = [
    {"name": "Sara", "score": [90, 80, 85]},
    {"name": "Omar", "score": [85, 90, 95]},
    {"name": "Ahmed","score": [30, 55, 50]},
]

avg_students = [
    {
        "name": student["name"],
        "average": sum(student["score"]) / len(student["score"])
    }
    for student in students
]

filter_student = [
    student
    for student in avg_students
    if student["average"] >= 60
]

rep_index = {
    student["name"]: student
    for student in filter_student
}

backup = deepcopy(rep_index)

rep_index["Ahmed"] = {
    "name": "Ahmed",
    "average": 100
}

print(rep_index)
print(backup)
#slides 

from copy import deepcopy
numbers = range(1_000_000)

total = sum(

    number ** 2
    for number in numbers

)

print(total)


items = ["Python", "Git"]
items.append("Django")

name = "sara"
name = name.title().strip()

print(id(items))
print(id(name))


original = ["Python", "Git"]
alias = original

alias.append("Django")

print(original)
print(id(original))
print(alias)
print(id(alias))
print(original is alias)


original = ["Python", "Git"]
clone = original.copy()

clone.append("Django")

print(original)  # ['Python', 'Git'] #if there is a list it will be mutable
print(id(original))
print(clone)  # ['Python', 'Git', 'Django']
print(id(clone))
print(original is clone)  # False


#Shallow Copy
original = [["Sara", 90], ["Omar", 80]]
clone = original.copy()

clone[0][1] = 95

print(original)
print(id(original))
print(clone)
print(id(clone))
print(original[0] is clone[0])  # True


#Deep Copy
original = [["Sara", 90], ["Omar", 85]]
clone = deepcopy(original)

clone[0][1] = 95

print(original)
print(id(original))
print(clone)
print(id(clone))
print(original[0] is clone[0])  # False


names = ["Sara", "Omar", "Ahmed"]

# searches items one by one O(n)
print("Ahmed" in names)

name_set = set(names)

# Average membership time O(1)
print("Ahmed" in name_set)


students = [
    {"id": 101, "name": "Sara"},
    {"id": 102, "name": "Omar"},
]

studnets_by_id = {
    student["id"]: student
    for student in students
}

print(studnets_by_id[102]["name"])