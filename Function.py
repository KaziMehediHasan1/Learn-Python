"""def check_func(name,age):
    print("my name is", name, "and age is", age)
    
check_func("Kazi",24)
check_func("Kazi",24)"""

# tuple function
"""def mult(*names):
    return names

ans = mult("kazi","mehedi","shakil","raju")
print(list(ans))"""

# lambda
"""secure = lambda x,y: x*y
print(secure(3,4))"""

# defualt value
"""def sum(a,b=4):
    print(a+b)
    
sum(30,100)"""

# variable length arguments
"""def vla(*args):
    for ag in args:
        print(ag)
        if(type(ag)=="str"):
            print(ag)
    
vla(45,60,"kazi",True,3.4)"""

# dectionary
"""def dict_fun(**args):
    print(args["degree"])
    
dict_fun(
    name="Kazi",
    age=50,
    degree="Diploma"
)"""

# return once
"""def One_Return_Func(a,b=400):
    sum = a+b
    return sum

result = One_Return_Func(30)
print(result)"""

# multifle return
"""def calc(a,b=40):
    sum = a+b,
    sub= a-b,
    if a % 2 == 0:
        return "it's even"   
    return sum,sub

result = calc(34)
print(result)"""

"""def validate(pw):
    if len(pw) < 6:
        return False, "Password too short ❌"
    return True, "Password OK ✔️"

status, msg = validate("123456")
print(status, msg)
"""

# lambda function
"""result = lambda a,b:a+b;
print(result(3,5))"""

# 