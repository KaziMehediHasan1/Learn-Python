## SINGLE VARIABLE
x = "kazi"
# print(x)
##-----------------------------##

## MULTI VARIABLE 
x = y = z = "Hello World", #same value assigning to x,y,z
# print(y, x),

##-----------------------------##
## GLOBAL VARIABLE DECLARATION
def myFunc():
    global x ## now it's global variable, it get out of function !
    x = "Mehedi Hasan"
    # print(x)
myFunc()

print(x) ## call global variable 


##----------------------------##

