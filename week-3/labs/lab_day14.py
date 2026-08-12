numbers = [1, 2, 3, 4, 5] # exeprtion

squares = [
    number ** 2 
    for number in numbers
    if number % 2 == 1 # clause
    ]
print(squares) #[1, 9, 25]

prices = [100, 200, 300, 400]

scores = [42 , 65, 78, 90, 55]

passing_scores = [
    score 
    for score in scores
    if score >= 60
]
print(passing_scores) #[65, 78, 90]












# name =10
# name = "sara"
# print(name)
# students = None
# print(id(students)) # unique and immutable object 
# # for has counter and while has condition  
