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

"""class Student:
    def __init__(self, fullname,marks):
        self.name = fullname
        self.marks =  marks
        print("adding new student")

s1 = Student("Mehedi Hasan",98)
print(f"{s1.name} result is {s1.marks}")"""

"""class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    @staticmethod    
    def name_func():
        print("your names")
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
            print("hi", self.name, "your avg score is:", sum/len(self.marks))
            # print(len(self.marks),"sum")
            
        
s1 = Student("Mehedi",[88,90,95])
del s1.name
print(s1.name,"Check")
# print(s1.get_avg())
# print(s1.name_func())"""


"""class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.clutch =True
        self.acc = True
        print("Car started...")
        
car1 =Car()
car1.start()"""

"""class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no =acc
        
    # debit method
    def debit(self,amount):
        self.balance -= amount
        print("Tk",amount, "was debited")
        print("total balance =", self.get_balance())
           
    # credit method
    def credit(self, amount):
        self.balance += amount
        print("tk",amount, "was credited")
        print("total balance =", self.get_balance())
        
    def get_balance(self):
        return self.balance
        
        
acc1 = Account(10000, 12345)
# print(acc1.balance)
# print(acc1.account_no)
acc1.debit(1000)
acc1.credit(10000) """       

class Student:
    def __init__(self,name):
        self.name =name
        
s1 = Student("mehedi")
print(s1.name)
del s1.name
try:
    print(f"After deletion: {s1.name}")

except AttributeError:
    print("Error: The 'name' attribute no longer exists on this object.")
        