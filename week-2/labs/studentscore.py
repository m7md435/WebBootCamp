name = input("Enter your name: ").strip()
score = int(input("Enter your score: "))
course = input("Enter your course: ").strip
confirm_name = name.isalpha() and len(name) > 0
confirm_score = score >= 0 and score <= 100


if confirm_name and confirm_score:
    if score >= 90:
        print("Excellent")

    elif score >= 80:
        print("Good")
    else:
        print("Needs Improvement")
else:
    print("Invalid input. Please enter valid data.")

if course not in ["math", "science", "english"]:
    print("Invalid course. Please enter a valid course.")