"""class MyClass:
    student = "30"
    teacher = "5"
    
classOne = MyClass()
print(classOne.student)
print(classOne.teacher)"""

"""class Student:
    name = "kazi"
     
s1 = Student()
print(s1.name)"""

"""class Car:
    color = "blue"
    brand = "toyota"
    
carOne = Car()
print(carOne.color)
print(carOne.brand)"""

class Student:
    def __init__(self, fullname,marks):
        self.name = fullname
        self.marks =  marks
        print("adding new student")

s1 = Student("Mehedi Hasan",98)
print(f"{s1.name} result is {s1.marks}")