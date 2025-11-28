python_object={
    "name":"Kazi Mehedi Hasan",
    "roll":683304,
    "section":"A",
    "dept":"CST",
    "num":"018843356835",
    "subject":["math","iit","english","hardware"]  
}
python_object["Color"] =["green","red"]
# python_object.update({"color","white"})
# python_object.pop("Color")
# python_object.popitem()
# del python_object["subject"]
# python_object.clear()
print(python_object.get("name"))
for key,value in python_object.items():
    print(key,value,"check")