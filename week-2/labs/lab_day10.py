#lab 1

for attempts in range(3):
    print("Attempt", attempts + 1)

#lab 2

for num in range(2, 11, 2):
    print(num)

#lab 3

for secondstolaunch in range(10, 0, -1):
    print(f"T-:{secondstolaunch}")

#lab 4

course = "python"
for letter in course:
    print(letter)

#lab 5 
students = ["shahad", "khadija", "yamam"]
for student in students:
    print(f" Progressing student is: {student}") 

#lab 6

for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")
    print("----------------------")


#lab 7

numbers = [1, 2, 3, 4, 5]
even_counter = 0
for number in numbers:
    if number % 2 == 0:
        even_counter += 1

print(f"Total even numbers is: {even_counter}")


#lab 8

prices = [10, 20, 30, 40, 50]
total = 0

for price in prices:
    total += price

print(f"Total price is: {total} Vat: {total * 1.15:.2f}")


#lab 9

count = 1
while count < 5:
    count += 1
    print(f"Count.... {count}")
print("loop completed")


#lab 10
message = "Please enter your age: "
age_text = input(message).strip()
while not age_text.isdigit():
    age_text = input(message).strip()
age = int(age_text)
print(f"Your age is: {age}")

#lab 11

password = input("Enter the password please: ")
while password != "python123":
    password = input("Incorrect password. Please enter the password: ")
print("Password accepted. Welcome to the system!")

#lab 12
for score in [80, 55, 45 ,90 ]:
    if score < 50:
        pass
    print(f"if passed the: {score}")

for record in [80, 55, 45 ,90 ]:
    if record < 50:
        continue
    print(f"if passed the: {record}")

for record in [80, 55, 45 ,90 ]:
    if record < 50:
        break
    print(f"if passed the: {record}")

#lab 13

for row in range( 1, 4):
    for column in range(1, 4):
        print(f"{row} X  {column} = {row * column}")

