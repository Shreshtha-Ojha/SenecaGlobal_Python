
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

#File not found error
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
