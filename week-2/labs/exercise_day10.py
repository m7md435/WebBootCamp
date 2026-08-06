numbers = int(input("Enter a number between 1 and 100: "))
total = 0
count = 0

for number in range(1, numbers + 1):
    if number % 2 == 0:
        print(f"{number} is an even number")
        total += number
        count += 1
    else:
        print(f"{number} is an odd number")

print(f"count of even numbers: {count}")
print(f"total of even numbers: {total}")