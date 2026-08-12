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