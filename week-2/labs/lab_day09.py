#lab 1
age = 20
if age >= 18:
    print("welcome")
print("code completed")

#lab 2
temprature = 31
if temprature >= 31:
    print("It's a hot outside")
else:
    print("It's a cold outside")

#lab 3
score = 2000

if score >= 90:
    print(" A")
elif score >= 80:
    print("B")
elif score >= 70:
    print(" C")
else:
    print("you need to improve ")

#lab 4
is_active = True
is_verified = True
role = "editor"
is_blocked = False

if is_active and is_verified:
    print("account is ready")

if role == "admin" or role == "editor":
    print("you can edit")

if not is_blocked:
    print("user is not blocked")

else:
    print("user is blocked")

#lab 5
account_active = True
has_permission = True

if account_active :
    if has_permission:
        print("Access granted")
    else:
        print("Access denied")
else:
    print("Account is not active")

#lab 6
name = "Faisal"
cart = []
balance = 990

if name:
    print("name has a value")

if not cart:
    print("cart is empty, please add items")
print(bool(cart))

#lab 7
name = input("Enter your name: ").strip()

if not name:
    print("Invalid input. Please enter a valid name.")
elif not name.replace(" ", "").isalpha():
    print("must contain letters.")
else:
    print(f"Hello, {name}!")

#lab 8
age_text = input("Enter your age: ").strip()
if age_text.isdigit():
    age =int(age_text)
    print(f"You will be {age + 5} years old in 5 years.")
else:
    print("Enter number.")

#lab 9

is_verified = False
score_text = input("Enter a number between 0 and 100: ")

if score_text.isdigit():
    score = int(score_text)

    if 0 <= score <= 100:
        print("Valid score")
        is_verified = True
    else:
        print("Invalid score.")
else:
    print("Please enter a number.")

#lab 10

membership = ["Admin", "Editor", "Viewer"]

current_membership = input("Enter your membership role: ").strip().lower

if current_membership.title() in membership:
    print("you are allowed to view the content")
    print(current_membership)
else:
    print("please contanct the admin team")
    print(current_membership)

#lab 11

command = input("Enter a command: ").strip().lower()

match command:
    case "start":
        print("....starting system")
    case "stop":
        print("stopping system....")
    case "status":
        print("system is up and running👌")
    case _:
        print("invalid command")
        