# f = open("demo.txt","r") 
# f = open("demo.txt","w") 
# f = open("demo.txt","a") 
"""# data = f.read(5)
lineOne = f.readline()
lineTwo = f.readline()
print(lineOne)
print(lineTwo)
f.close()"""

"""writefile=f.write("\nI will move to next.js")
print(writefile)
f.close()"""

with open("sample.txt","w+") as f:
    f.write("I am write in sample.txt file")
    f.write("\nI am write sample.txt file in python file system related somethings..")
    f.seek(0)
    read_sample = f.read()
    # print(read_sample)
    f.close()
    print("Filename:",f.name)
    print("isClosed?:",f.closed)
    print("Mode?:",f.mode)