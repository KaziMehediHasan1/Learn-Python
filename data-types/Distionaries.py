thisDict ={
    "name":"kazi mehedi hasan",
    "age":24,
    "isStudent":False,
    "FavouritesColors":["red","blue","white"]
}

# print(type(thisDict["FavouritesColors"]),"check dict")
# using method to make dict()
makeDict = dict(name="kazi Mehedi",age=24,isStudent=False)
# print(makeDict,"check make dict")
# print(makeDict.get("name"),"specific value")
# print(makeDict.keys())
# print(thisDict.values())
# thisDict["age"] = 30; change value
# thisDict["FavouritesColors"] = ["green"] ;
# thisDict["FavouritesColors"] = "green"
# print(thisDict.items())

"""if "agee" not in thisDict:
    print("yeah, not have this keys")
elif "age" in thisDict:
    print("not yet") """

#  update dict pair

thisDict.update({"age":25})
print(thisDict,"upadate")