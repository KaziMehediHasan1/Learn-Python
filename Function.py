def check_func(name,age):
    print("my name is", name, "and age is", age)
    
check_func("Kazi",24)
check_func("Kazi",24)

# tuple function
def mult(*names):
    return names

ans = mult("kazi","mehedi","shakil","raju")
print(list(ans))

# lambda
secure = lambda x,y: x*y
print(secure(3,4))

# defualt value
def sum(a,b=4):
    print(a+b)
    
sum(30,100)
    