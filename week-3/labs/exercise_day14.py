#list comperhension , odd numbers
numbers = [1, 2, 3, 4, 5] #name of this line expression

squares = [               #squares comperhension
    number ** 2
    for number in numbers
    if number % 2 == 1    #name of this line clause
]

print(squares) #[1, 9, 25]


prices = [10, 25, 40]     #name of this line expression

prices_with_vat = [
    round(price * 1.15, 2)
    for price in prices   #name of this line clause
]

print(prices_with_vat) #[11.5, 28.75, 46.0]


scores = [42, 67, 91, 58, 75]

passing_scores = [
    score                 #expression
    for score in scores   #clause
    if score >= 60        #Filter
]

print(passing_scores)  # [67, 91, 75]

raw_names = [" sara ", " ", "omar", "  lina  "]
cleaned_names = [
    name.strip().title()  # expression
    for name in raw_names
    if name.strip() # clause
]
print(cleaned_names)  # ["sara", "omar", "lina"]

for name in raw_names:
    print(name.strip())
    
numbers = [1, 2]
letters = ["a", "b"]
combined = [
    (number, letter)  # expression
    for number in numbers
    for letter in letters  # clause
    ]
print(combined)  # [(1, "a"), (1, "b"), (2, "a"), (2, "b")]

scores = [42, 67, 91]
labels = [
    "pass" if score >= 60 else "retry"  # expression
    for score in scores               # clause
]
print(labels)  # ["retry", "pass", "pass"]    

email = [
    "SARA@example.Com",
    "omar@example.com",
    "lina@school.sa"
]
domain = {
    email.split("@")[1].lower() 
    for email in email}
print(domain)  # {"example.com"}

numbers = range(1, 6)

squares = {
    number : number ** 2
    for number in numbers
}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

