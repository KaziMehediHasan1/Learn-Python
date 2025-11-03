thisDict ={
    "name":"kazi mehedi hasan",
    "age":24,
    "isStudent":False,
    "FavouritesColors":["red","blue","white"]
}

# just showing keys
"""for x in thisDict:
    save = x
    if "age" in save:
         print("have this");
    else:
         print("nothing yet")"""

# line by line shows all values
"""
for x in thisDict:
    save = x
    print(thisDict[save])"""

#  line by line shows all values
"""for x in thisDict.values():
    print(x,"values")
        """

# both get using items() method
"""for x,y in thisDict.items():
    print("key -->", x,  "value -->", y)"""




# copy dict using many ways 
"""copyOne = dict(thisDict);
print(copyOne,"copy dict")"""

copyTwo = thisDict.copy();
print(copyTwo,"copy way")
   