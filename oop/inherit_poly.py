# del keyword for deleting propertise
"""
class Student:
    def __init__(self,name):
        self.name = name
        
s1 = Student("Mehedi")
print(s1.name)
del s1.name
print(s1.name)

"""



# private class
"""class Account:
    def __init__(self,acc_no,acc_pass):
        self.account = acc_no
        self.__account_password = acc_pass # when write double _,_ underscore use in the propertise or methods, then your call thats private.
        
    def reset_pass(self):
        print(self.__account_password)
        
acc1 = Account(12345,5569894)
print(acc1.account)
print(acc1.reset_pass())"""

# inheritence - single inheritence
class Car:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")
        
class ToyotaCar(Car):
    def __init__(self,name):
       self.name = name
       
        
car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

# print(car1.name)
# print(car1.start())

# inheritence - multi-level inheritence - # super method
class Foutuner(ToyotaCar):
    def __init__(self,type,name):
        self.type = type
        super().__init__(name)
        super().start()
      
        
        
four1 = Foutuner("builder","fortune model")
# print(four1.start())
# print(four1.type)
print(four1.name)

# inheritence - multiple inheritence
class A:
    varA = "welcome class A"
class B:
    varB = "welcome class B"
class C(A,B):
    varC = "welcome class C"
    
class1 = C()
# print(class1.varC)
# print(class1.varB)
# print(class1.varA)

