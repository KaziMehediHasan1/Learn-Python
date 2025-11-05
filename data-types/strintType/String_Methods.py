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