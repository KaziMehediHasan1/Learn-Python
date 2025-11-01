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
"""thisDict.update({"age":25})
print(thisDict,"upadate")"""

# remove items in dict
'''thisDict.pop("age")
print(thisDict,"removed keys values pair")'''

# removed last items in dict
"""thisDict.popitem();
print(thisDict,"last items removed")"""

# clear full dict
"""thisDict.clear();
print(thisDict,"clear all dict items")"""


# make nested dict 
makeTwoDic = {
    "one":thisDict,
    "two":makeDict
};
# print(makeTwoDic["one"],"check nested dic has created?")


# get loop through the keys and values
for x,obj in makeTwoDic.items():
    print(x,"key values")

    for y in obj:
        print(y + ":",obj[y], "values")