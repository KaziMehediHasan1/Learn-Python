"""try:
    first_variable = 10 / 0
    print(first_variable)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")"""
    
    
import os
"""
try:
     directory_content=os.listdir("new_file")
     print(directory_content)
except FileNotFoundError:
    print("Error: 'listdir' does not return a context manager.")
"""

"""try:
    with open("calc.txt","r") as file:
        content = file.read()
        data = len(content) + 10
        print(data,"check")
        print(content)
except FileNotFoundError:
    print("Error: The file 'calc.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")"""
    
# Finally block example
