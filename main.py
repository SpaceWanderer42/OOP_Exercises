# EX1
# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# modelX = Vehicle(240, 18)
# print(modelX.max_speed, modelX.mileage)

# EX2
# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle): #doar preia clasa vehicle, nu adauga nimic suplimentar (cam banal)
#     pass
#
# School_Bus = Bus("School Volvo", 180, 12)
# print("Vehicle Name: ", School_Bus.name, "| Speed:", School_Bus.max_speed, "| Mileage: ", School_Bus.mileage)

# EX3
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
#
#
# class Bus(Vehicle):
#     def seating_capacity(self, capacity=50):
#         return super().seating_capacity(capacity=50)
#
# School_Bus = Bus("School Volvo", 180, 12)
# print(School_Bus.seating_capacity())
#

# EX4

# class Vehicle:
#
#     color = "white"
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#
# class Bus(Vehicle):
#     pass
#
# class Car(Vehicle):
#     pass
#
# School_Bus = Bus("School Volvo", 180, 12)
# print("Color: ", School_Bus.color, "| Name: ", School_Bus.name, "| Speed: ", School_Bus.max_speed, "| Mileage: ", School_Bus.mileage)
#
# car = Car("Audi Q5", 240, 18)
# print("Color: ", car.color, "| Name: ", car.name, "| Speed: ", car.max_speed, "| Mileage: ", car.mileage)

# EX5

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
#     def fare(self):
#         return self.capacity * 100
#
# class Bus(Vehicle):
#     def fare(self):
#         amount = super().fare()
#         amount += amount * 10 / 100
#         return amount
#
# School_Bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is: ", School_Bus.fare())

# EX6

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
# class Bus(Vehicle):
#     pass
#
# School_Bus = Bus("School Volvo", 12, 50)
#
# #Which class a given Bus object belongs to
#
# print(type(School_Bus))

# EX7

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
# class Bus(Vehicle):
#     pass
#
# School_Bus = Bus("School Volvo", 12, 50)
#
# #Checks if School_Bus is also an instance of Vehicle class
#
# print(isinstance(School_Bus, Vehicle))

# ---------------------------------------------------------------------

# Exercise 3: Write a program, to create a child class Teacher
# that will inherit the properties of Parent class Staff

# class Staff:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
#
#     def show_details(self):
#         print("Name: ", self.name)
#         print("Age: ", self.age)
#         print("Role: ", self.role)
#         print("Department: ", self.dept)
#
#
# class Teacher(Staff):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Teacher", "Science", 25000)
#
#
# teacher = Teacher("Emily", 30)
#
# teacher.show_details()

# Exercise 4: Write a Program, to create a class and using the
# class instance print all the writable attributes of that object.

# display all instances using __dict__
# (that returns a dictionary of all the attributes available for that object.)

# print(teacher.__dict__)

# t = [0, 0, 0]
#
# t[0] = Teacher("Raj", 45)
# t[1] = Teacher("M", 70)
# t[2] = Teacher("S", 50)
#
# t[0] = t[0].show_details()
# t[1] = t[1].show_details()
# t[2] = t[2].show_details()
#
# for i in t:
#     print(t)

# print(isinstance(teacher, Teacher))
# print(isinstance(teacher, Staff))

# Clasa cu atribut privat

class Teacher():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary  # atribut privat

    def show_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

        print("Salary: ", self.__salary)  # accesare atribut privat in interiorul clasei -> in exterior la apelare va crapa


teacher = Teacher("Vaiadena", 36, 100000)

teacher.show_details()

# print(teacher.__salary) prostie =)))

# m-am oprit la operator overload de pe techgeekbuzz
