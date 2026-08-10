#lab 1

course = "Web development Bootcamp"
duration = 12
def type(course):
    print("opps!")
print(course)
print(duration)
print(type(course))
print(globals())


#lab 2

building = "Tuwaiq Academy"
cohort_size = 20

print (f"Welcome to {building} building, we have {cohort_size} students in this cohort.")
print("Tuwaiq" in building)
print("cohort_size" in globals())
print(globals()["building"])

#lab 3
location = "global"
def outter(): 
    location = "outter"  
    print(f"from {location} ")
    def inner():
        location = "inner"
        print(f"from {location} ")
    inner()
    
outter()

#lab 4
location = 0
def outter(): 
    location = 1   
    print(f"from {location} ")
    def inner():
        nonlocal location
        location += 2
        print(f"from {location} ")
    inner()
    
outter()

#lab 5

def printer():
    print("welcome")

def desk():
    printer()

def room():
    desk()

def house():
    room()

def city():
    house()

def country():
    city()

country()

#lab 6

language = "Python"

def show_lang(language):
    print(f"Language is: {language}")

show_lang("Dart")
print(f"Language is: {language}")


#lab 7
rate = 0.15
def getTotal(amount):
    total = amount * rate + amount
    return total
print(f"Total: {getTotal(200):.2f}")    
print(round(getTotal(200), 2))

#lab 8
def inspect_order(item, qty):
    subtotal = 25 * qty
    print(locals())
    print(locals()["subtotal"])
inspect_order("Coffee", 10)