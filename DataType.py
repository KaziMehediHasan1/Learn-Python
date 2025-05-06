# text-type------> str
# number-type-----> float, complex,int
# sequence-type ----> list, tuple, range
# Mapping Type--->	dict
# Set Types------>	set, frozenset
# Boolean Type---->	bool
# Binary Types---->	bytes, bytearray, memoryview
# None Type----> NoneType



# INTEGER DATA TYPE    
number_type = 10
# print(type(number_type)) #check data type.
# print(number_type)

# TEXT DATA TYPE(STRING)
MyName = "Kazi Mehedi Hasan"
# print(type(MyName))
# print(MyName)

floatingType = 5.50
# print(type(floatingType)) #it's a float data type
# print(floatingType)

complexType = 5j
complexText = complexType + 9
# print(type(complexType)) # complex data types
# print(complexText)

# TYPE CONVENTION 
conventionOne = float(number_type) # number type to float!
# print(conventionOne)

conventionTwo = int(floatingType)
# print(conventionTwo)

conventionThree = complex(number_type) 
print(conventionThree)

## note : complex not convert to int and float types!
