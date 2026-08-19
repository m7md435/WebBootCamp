# #lab 1
# class Ticket:
#     def __init__(self, name ,status = "open"):
#         self.name = name
#         self.status = status
#     def newStatus(self, status):
#         self.status = status
# myTicket = Ticket("1000", "in progress")
# myTicket2 = Ticket("1001", "pending")
# print(myTicket.status)
# print(f"Ticket {myTicket2.name} is {myTicket2.status}")

# #lab 2

# class Greeter:
#     def __init__(self, massage):
#         self.massage = massage
#     def greet(self , user):
#         self.user = user

#         return f"Hello {self.user}, {self.massage}"

# mygreeter = Greeter("Welcome to the tuwaiq")
# mymsg = mygreeter.greet("salam")
# print(mymsg)

# #lab 3

# class Welcome:
#     def __init__(self, name):
#         self.name = name
#     def welcome(self):
#         print(f"Hello {self.name}")

# students = [  Welcome("Sara"),
#              Welcome("Mohammed"),
#              Welcome("khadija"),  # Added missing comma
#              Welcome("Omar")
# ]

   

# for student in students:
#     student.welcome()

# #LAB 4
# from pathlib import Path
# path = Path("home") / "students" / "students.txt"
# path.parent.mkdir(parents=True, exist_ok=True)

# print(path.is_dir())
# print(path.suffix)
# print(path.name) 
# print(path.is_file()) 

# #lab 5
# class Food:
#     def __init__(self, name):
#         self.name = name
#     def showName(self):
#         return self.name

# class Fruites(Food):
#     newName = "     Fa    "
#     def __init__(self, name, cal):
#         super().__init__(name)
#         self.cal = cal

#     def stripName(newName):
#          return newName.strip()
# myFruit = Fruites("Apple", 200)
# print(myFruit.showName())  # Output: Apple
# print(Fruites.stripName(Fruites.newName))  # Output: Fa
