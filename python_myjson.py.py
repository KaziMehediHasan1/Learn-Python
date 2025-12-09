"""
- read_json: Read JSON data from a file or string and convert it into a Python dictionary.
- write_json : Write a Python dictionary to a file in JSON format.
- validate_json: Validate a JSON string against a specified schema.
- merge_json: Merge two JSON objects into one, with options for handling conflicts.
- pretty_print_json: Print JSON data in a human-readable format with indentation.
- convert_json_to_yaml: Convert JSON data to YAML format.
- convert_yaml_to_json: Convert YAML data to JSON format.
"""

import json

# python dictionary -- Json string
"""person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"]
}

person_json = json.dumps(person,indent=4)
# print(person_json)
"""


# Json string -- python dictionary
"""person_json = '''{
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": false,
    "titles": ["engineer", "programmer"]
}'''

person_dict = json.loads(person_json)
print(person_dict["titles"][0])"""

# Python dictionary -- Json string + file write
"""person_json = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"]
}
with open("person.json","w") as file:
    json.dump(person_json,file,indent=4)"""
    
#  json file -- python dictionary read
with open("person.json","r") as file:
    person_dict = json.load(file)
    print(person_dict)