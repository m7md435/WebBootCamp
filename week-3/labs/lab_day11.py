#lab 1
def greet():
    print("Hello, welcome to the program!")

greet()

#lab 2
def show_menu():
    print("1- Coffee")
    print("2- Tea")
    print("3- Zatar")

show_menu()
print(" Outside the call")
show_menu()

#lab 3
#_() lmda function
print("Line one ")
def gotoFunc():
    print(" From within the GoTo")
print(" Where is line 2?")
gotoFunc()
print("i am up here")

#lab 4
def greet_student(name):
    print(f"Hello, {name}! Welcome to the program.")

greet_student("Sarah")

#lab 5
def show_booking(destination, nights = 1):
    if nights.isdigit():
        nights = int(nights)
    else:
        print("Invalid input for nights. Using default value of 1.")
        nights = 1
    print(f"""You are traveling to {destination} 
    and staying for {nights} n
    ights.""")

show_booking("Paris", 5)
show_booking("New York", 2)

#lab 6
def getVat(total, rate = 0.15):
    """ this function calculates the VAT for a given total amount and rate. """
    vat = total + (total * rate)
    return vat
print(getVat(100))
print(getVat(100, 0.05))
print(getVat.__doc__)
help(getVat)
print(getVat.__name__)
