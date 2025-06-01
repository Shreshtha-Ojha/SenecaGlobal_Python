
#Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

try:
    number = int("abc")
except ValueError:
    print("Error: Invalid literal for int().")
except TypeError:
    print("Error: Type mismatch.")

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"Result is {result}")
finally:
    print("Execution completed.")

#Custom exceptions
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print(f"Caught an exception: {e}")


#Serialization/Deserialization

import pickle
data = {'name': 'Alice', 'age': 25, 'is_active': True}
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)
with open('data.pkl', 'rb') as f:
    loaded_data = pickle.load(f)

print(loaded_data)
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")

import json
data = {'name': 'Shreshtha', 'age': 30, 'skills': ['Python', 'Data Science']}
json_str = json.dumps(data)

# Deserialize 
data_back = json.loads(json_str)

print(json_str)
print(data_back)

import yaml

data = {'name': 'Ojha', 'age': 2, 'languages': ['English', 'Hindi']}

# Serialize
yaml_str = yaml.dump(data)

# Deserialize 
data_back = yaml.safe_load(yaml_str)

print(yaml_str)
print(data_back)
