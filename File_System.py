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

# with open("sample.txt","w+") as f:
#     f.write("I am write in sample.txt file")
#     f.write("\nI am write sample.txt file in python file system related somethings..")
#     f.seek(0)
#     read_sample = f.read()
#     # print(read_sample)
#     f.close()
#     print("Filename:",f.name)
#     print("isClosed?:",f.closed)
#     print("Mode?:",f.mode)

"""import os
os.remove("demo.txt")"""

# Creating a directory
# Reading a directory
# Writing to a file in a directory
# Renaming a directory
# Deleting a directory
# Read Files names from directory and print list

"""import os

# os.mkdir("new_file/text.txt") create
dir = os.listdir(".")
for folderOr_FileNames in dir:
    full_path = os.path.join(".", folderOr_FileNames)
    # print(full_path)
    # if os.path.isdir(full_path):
    #     print(full_path,"it is a directory")
        
    if os.path.isfile(full_path):
        print(full_path,"it is a file")
    
    # print(folderOr_FileNames)"""
    
# create zip file
# extract from zip file
# make zip from directory

import zipfile , shutil

# create zip file 
"""with zipfile.ZipFile("new.zip","w") as zip:
    zip.write("Loop.py")
    zip.write("List.py")"""
    
# Extract Zip file 
"""with zipfile.ZipFile("new.zip","r") as zip:
    zip.extractall()
    extract_file = zip.namelist()
    print(extract_file) """

# make zip from dir
# shutil.make_archive("zip_file","zip","new_file")

# csv file 
import csv 
"""
data = [
    ["Name","Salary","Designation","Department","Location"],
    ["John Doe","50000","Software Engineer","IT","New York"],
    ["Jane Smith","60000","Data Analyst","Marketing","San Francisco"],
    ["Sam Brown","55000","Product Manager","Product","Chicago"]
]

with open("new.csv","w") as file:
   csv_file = csv.writer(file)
   csv_file.writerows(data)
   print("CSV file created successfully")"""
   
with open("new.csv","r") as file:
    csv_file = csv.reader(file)
    for row in csv_file:
        print(row)