# Trying Numeric Data type - Using Python as a Calculator (Data Types + Functions)

def calculator():
    while True:
        a = int(input("Enter a number: "))
        op = input("Enter the operation symbol (+, -, *, /, //, %): ")
        b = int(input("Enter a number: "))

        if op == '+':
            print("Result:", a + b)
        elif op == '-':
            print("Result:", a - b)
        elif op == '*':
            print("Result:", a * b)
        elif op == '/':
            if b != 0:
                print("Result:", a / b)
            else:
                print("Error: Division by zero")
        elif op == '//':
            if b != 0:
                print("Result:", a // b)
            else:
                print("Error: Division by zero")
        elif op == '%':
            if b != 0:
                print("Result:", a % b)
            else:
                print("Error: Division by zero")
        else:
            print("Invalid operator!")

        ch = input("Do you wish to continue? (yes/no): ").lower()
        if ch != 'yes':
            print("Thank You")
            break

calculator()


#Exploring the mutability charectoristics of Lists and Tuples
def add(p,q):
  p+=y
  return p

a = [1,2,3]
b=(8,9)
result1 = add(a, [4,5])
result2 = add(b, (6,7))

print(result1)                                #output: [1,2,3,4,5]
print("value of a after operation: ", a)      #output: value of a after operation: [1,2,3,4,5]
print(result2)                                #output: (8,9,6,7)
print("value of b after operation: ", b)      #output: valuse of b after operation: (8,9)


# Learning the decorator design pattern

def greet(func):
  def modified(*args, **kwargs):                # use of *args and **kwargs - used to add any number of non-keyword and keyword arguments respectively
    print("Hi")
    func(*args, **kwargs)
    print("Thank you for using this function")
  return modified    

@greet
def add(a,b):
  print(a+b)

a= int(input())
b=int(input())
add(a,b)  

#Exploring Logging Decorator
#A logging decorator is a Python decorator used to automatically log function calls, arguments, return values, or execution time — without modifying the function’s core logic.

import logging
logging.basicConfig(level=logging.INFO)
def log_func(func):
  def decorated(*args, **kwargs):
    logging.info(f"Calling{func.__name__} with args {args} and kwargs {kwargs}")
    result = func(*args, **kwargs)
    logging.info(f"{func.__name__} returned {result}")
    return result
  return decorated

@log_func
def add(a,b):
  return a+b

add(10,5)    

# Here the output is 15. but if we change the 81 and 83, we can print the actual operations happening due to logging. By default these opertions are not printed.

import logging
logging.basicConfig(level=logging.INFO)
def log_func(func):
  def decorated(*args, **kwargs):
    print(f"Calling{func.__name__} with args {args} and kwargs {kwargs}")      #INFO:Calling add with args (10, 5) and kwargs {}
    result = func(*args, **kwargs)
    print(f"{func.__name__} returned {result}")                                #INFO:add returned 15
    return result
  return decorated

@log_func
def add(a,b):
  return a+b
add(10,5)  


#Using the logging function with time calculation
import time

def log_t(func): 
    def decorated(*args, **kwargs):
        start = time.time()
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} returned {result} in {end - start:.4f}s")
        return result
    return decorated

@log_t
def hi():
    print("Hello World")
hi()



#Generators
# They compute the result during execution instead of first computing all and then printing. This ensures the reult to start printing faster and less load on the interpreter.
def my_gen():
  for i in range (500):
    yield i

gen = my_gen()
print(next(gen))      #prints the immediate next number in the order

for i in gen:
  print(i)


#iterators require the knowledge of class. Will come back to this after completing the other topics until OO concepts.

"""Important Question
Iterators and Generators
Question:
Implement a generator function called chunk_reader(file_path: str, chunk_size: int) that lazily reads a text file line-by-line and yields chunks of chunk_size lines at a time. Also, implement a custom iterator class ReverseList that iterates over a list in reverse order.

Requirements:

Use a generator to avoid loading the entire file into memory.

The iterator class should raise StopIteration correctly.

Include a usage example for both."""



