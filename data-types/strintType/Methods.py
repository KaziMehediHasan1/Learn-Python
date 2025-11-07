# count 
a ="Kazi Mehedi Hasan, Father Names Kazi, Mothers Names Kazi, Always Kazi Names"
print(a.count("Names"))

#capitalized 
b = "kazi, Mehedi, hasan, koi jabe, janina, tobe next e se valo korbo r o, se prepared valo korar jonno, struggle korar jonno"
print(b.capitalize())

# find - get postion
c = "Kazi Mehedi Hasan"
print(c.find("Hasan"))

# startswith()
print(a.startswith(" Kazi")) #True

# endswith()
print(a.endswith("Names"))

# find position -- find()
print(a.find("Kazi"),"find holo kina..")

# isalnum()
print(c.isalnum(),"isalnum")

# 1 str.upper()
name = "kazi mehedi hasan"
uppercaseString = name.upper()
print(uppercaseString)  # Output: "KAZI MEHEDI HASAN"

# 2 str.lower()
name1 = "KAZI MEHEDI HASAN"
lowercaseString = name1.lower()
print(lowercaseString)  # Output: "kazi mehedi hasan"

# 3 str.capitalize()
name2 = "kazi mehedi hasan"
capitalizedString = name2.capitalize()
print(capitalizedString)  # Output: "Kazi mehedi hasan"

# 4 str.title()
name3 = "kazi mehedi hasan"
titleString = name3.title()
print(titleString)  # Output: "Kazi Mehedi Hasan"

# 5 str.replace()
text1 = "hello world"
print(text1.replace("world", "Python"))

# 6 str.split()
spliteFun = "hellow-python-vaiya"
print(spliteFun.split("-"))

# 7 str.join()
joinFun = ['hellow', 'python', 'vaiya']
print("-".join(joinFun))

# 8 str.strip()
stripFun = " Hello World "
print(stripFun.strip())
print(stripFun)

print(stripFun.lstrip(),"38")
print(stripFun.rstrip(),"38")