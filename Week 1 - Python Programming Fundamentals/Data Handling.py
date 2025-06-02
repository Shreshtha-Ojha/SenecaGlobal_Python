
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
data = {'name': 'abcd', 'age': 5, 'is_active': True}
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
data = {'name': 'Shreshtha', 'age': 30, 'skills': ['Python', 'AI']}
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


#MultiThreading
#Before using threading
import threading
import time
def func(seconds):
  time.sleep(seconds)
time1 = time.perf_counter()
func(4)
func(2)
func(1)
time2 = time.perf_counter()
print(time2-time1)          #Output = 7.001504637999972

#After using multithreading
import threading
import time
def func(seconds):
  time.sleep(seconds)
time1 = time.perf_counter()
t1 = threading.Thread(target = func , args=[4])
t2 = threading.Thread(target = func , args=[2])
t3 = threading.Thread(target = func , args=[1])
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
time2 = time.perf_counter()
print(time2-time1)                        #Output = 4.001969119000023

#Multiprocessing
from multiprocessing import Process

def task1():
    print("Task 1 running")

def task2():
    print("Task 2 running")

if __name__ == "__main__":
    p1 = Process(target=task1)
    p2 = Process(target=task2)

    p1.start()
    p2.start()                #Task 1 running
                              #Task 2 running
                              #Both processes finished.
    p1.join()
    p2.join()
    print("Both processes finished.")

#Using Pool Process
from multiprocessing import Pool

def square(n):
    return n * n

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])
        print(results)                                #Output: [1,4,9,16,25]



