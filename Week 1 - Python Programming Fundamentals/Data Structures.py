#Lists
'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.'''
class Solution:
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


'''Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.'''


class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[k-1]:
                nums[k]=nums[i]
                k+=1
        return k   


'''You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''
class Solution(object):
    def maxProfit(self, prices):
      max_p = 0
      min_p = float('inf')

      for p in prices:
        if p<min_p:
            min_p = p
        else:
            p = p-min_p
            max_p = max(max_p , p)    
      return max_p      


'''Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.'''
class Solution(object):
    def sortedSquares(self, nums):
        sq = []
        for i in nums:
           sq.append(i**2)
        return sorted(sq)   


'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.'''

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1  
        return res
#Tuple
'''Reverse a Tuple'''
inp_t = eval(input("Enter numbers: "))            #input: 4,5,6,7,8
rev = inp_t[::-1]
print(rev)                                        #output: (8,7,6,5,4)

'''Find Tuples with All Elements Divisible by a Given Number'''
def tdk(t,k):
  return [tup for tup in t if all(elem%k==0 for elem in tup)]

t= eval(input("Enter tuple pairs: "))            # Input: Enter tuple pairs: [(10,30),(45 , 43), (34,75)]
k=int(input("Enter a number: "))                 # Input: k=2
result = tdk(t,k)
print(result)                                     #Output: [(10, 30)]

# Dictionaries
person = {"name": "Shreshtha", "age": 10}
print(person)                                  #Output: {"name": "Shreshtha", "age": 10}
person['City'] = "Hyderabad"
print(person)                                  #Output: {"name": "Shreshtha", "age": 10, "City": "Hyderabad"}
for key, value in person.items():
    print(f"{key}: {value}")
print(person.keys())                           # Output: dict_keys(['name', 'age', 'City'])
print(person.values())                         # Output: dict_values(['Shreshtha', 10, 'Hyderabad'])

'''Merge Two Dictionaries by Adding Values for Common Keys'''
from collections import Counter

dict1 = {'a':100 , 'b': 200, 'c':300}
dict2 = {'d':400, 'e':500 , 'c': 50}
merged = dict(Counter(dict1)+Counter(dict2))
print(merged)                                    #Output:{'a': 100, 'b': 200, 'c': 350, 'd': 400, 'e': 500}
dict1.update(dict2)
print(dict1)                                     # Output: {'a': 100, 'b': 200, 'c': 50, 'd': 400, 'e': 500}



#String Manipulation
'''Concatenating two strings'''
a = "Hi"
b = "Shreshtha"
print(a+' '+b)        #Output Hi Shreshtha

'''Accessing Characters in a String'''
word = "chocolate"
out1 = word[3]
out2= word[5]
print(out1)        #output h
print(out2)        #output l

''' Replacing Part of a String'''
sen = "I cannot code in Python"
new_sen = sen.replace("cannot", "can")
print(new_sen)                            #output I can code in python

'''Finding the length of a string'''
word = "Chocolate"
n = len(word)
print(n)                    #output 9

'''Converting Numbers to Strings'''
num = 100
print("I am", num, "years old")



'''Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.'''

class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        map_s_to_t = {}
        map_t_to_s = {}

        for char_s, char_t in zip(s, t):
            if char_s in map_s_to_t:
                if map_s_to_t[char_s] != char_t:
                    return False
            else:
                map_s_to_t[char_s] = char_t

            if char_t in map_t_to_s:
                if map_t_to_s[char_t] != char_s:
                    return False
            else:
                map_t_to_s[char_t] = char_s

        return True


'''You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

 '''
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or s == s[::-1]:
            return s
        
        temp = s + "#" + s[::-1]

        lps = [0] * len(temp)
        for i in range(1, len(temp)):
            j = lps[i - 1]
            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]
            if temp[i] == temp[j]:
                j += 1
            lps[i] = j
        to_add = s[lps[-1]:][::-1]  
        return to_add + s

           
# Formatting

object = 'Chocolate'
object2 = "milk"
print(f"I like {object} and {object2}")        #output I like Chocolate and milk

print("My name is {name} and I am {age} years old.".format(name="Shreshtha", age=100))  #output My name is Shreshtha and I am 100 years old.

pi = 3.14159265
print(f"the most commonly used value of pi is {pi: .2f}")      # output: the most commonly used value of pi is 3.14

number = 8943769237847
print(f"The number with appropriate commas is : {number:,}")   #output: The number with appropriate commas is : 8,943,769,237,847

# In-built Methods
x = 100                                         
print("Type of x:", type(x))                #output : Type of x: <class 'int'>      
print("Length of 'hello':", len("hello"))   #output: Length of 'hello':5
print("ID of x:", id(x))                    #output: ID of x: 10754024

print("int('25'):", int("25"))               #output: int('25'): 25
print("float('3.14'):", float("3.14"))       #output: float('3.14'): 3.14
print("str(100):", str(100))                 #output: str(100): 100
print("bool(0):", bool(0))                   #output: bool(0): False
print("bool(1):", bool(1))                   #output: bool(1): True
print("list('abc'):", list("abc"))           #output: list('abc'): ['a', 'b', 'c']
print("tuple([1, 2, 3]):", tuple([1, 2, 3])) #Output: tuple([1, 2, 3]): (1, 2, 3)
print("set([1, 2, 2, 3]):", set([1, 2, 2, 3]))                    #output: set([1, 2, 2, 3]): {1, 2, 3}
print("dict([('a', 1), ('b', 2)]):", dict([('a', 1), ('b', 2)]))  #output: dict([('a', 1), ('b', 2)]): {'a': 1, 'b': 2}


print("abs(-5):", abs(-5))                    #output: abs(-5): 5
print("round(3.456, 2):", round(3.456, 2))    #output: round(3.456 , ): 3.46
print("pow(2, 3):", pow(2, 3))                #output: pow(2,3): 8
print("sum([1, 2, 3]):", sum([1, 2, 3]))      #output: sum([1,2,3]): 6
print("min(5, 2, 7):", min(5, 2, 7))          #output: min(5,2,7): 2  
print("max(5, 2, 7):", max(5, 2, 7))          #output: max(5,2,7): 7


l = ['a', 'b', 'c']
print("enumerate(l):", list(enumerate(l)))        #output: enumerate(l): [(0, 'a'), (1, 'b'), (2, 'c')]
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
print("zip(nums1, nums2):", list(zip(nums1, nums2)))        #output: zip(nums1, nums2): [(1, 4), (2, 5), (3, 6)]
print("sorted([3, 1, 2]):", sorted([3, 1, 2]))              #output: sorted([3, 1, 2]): [1, 2, 3]
print("reversed([1, 2, 3]):", list(reversed([1, 2, 3])))    #output: reversed([1,2,3]): [3,2,1]
print("range(3):", list(range(3)))                          #output: range(3): [0,1,2]
print("all([1, 2, 3]):", all([1, 2, 3]))                    #output: all([1,2,3]): True
print("any([0, False, 5]):", any([0, False, 5]))            #output: any([0, False, 5]): True

expression = "3 + 5 * 2"
print("eval(expression):", eval(expression))            #output: eval(expression): 13
code = "for i in range(2): print('Executed:', i)"
exec(code)                                              #Output:Executed: 0  \n  Executed: 1
compiled_code = compile("2 + 3", "<string>", "eval")
print("compile + eval:", eval(compiled_code))            #output: compile + eval: 5


#Searching and Sorting using python
#Linear Search
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

#Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

#Sorting
arr = [5, 2, 9, 1]
sorted_arr = sorted(arr)  # Returns a new list
arr.sort()                # Sorts the original list


#bubble sort
def bbsort(arr):
  n=len(arr)
  for i in range(n):
    swapped = False
    for j in range(0,n-i-1):
      if arr[j]>arr[j+1]:
        swapped = True
        arr[j], arr[j+1] = arr[j+1], arr[j]
    if not swapped:
      break
  return arr

arr = eval(input("Enter array: "))
bbsort(arr)


#QuickSort
def qksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        middle = []
        right = []

        for x in arr:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)

        return qksort(left) + middle + qksort(right)
arr = eval(input("Enter array: "))
qksort(arr)


#Selection Sort
def ssort(arr):
    n = len(arr)
    for i in range(n):
        mini = i
        for j in range(i+1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr
arr = eval(input("Enter array: "))
ssort(arr)


#heap sort (max heap)
def heapify(arr,n,i):
  l = i
  left = 2*i +1
  right = 2*1+2
  if left<n and arr[left]>arr[l]:
    l = left
  if right<n and arr[right]>arr[l]:
    l = right
  if l!=i:
    arr[i], arr[l]=arr[l], arr[i]
    heapify(arr, n, l)

def heapsort(arr):
  n = len(arr)
  for i in range(n//2-1 , -1,-1):
    heapify(arr,n,i)
  for i in range(n-1,0,-1):
    arr[i],arr[0] = arr[0] , arr[i]
    heapify(arr,n,0)
  return arr  

arr = eval(input("Enter a list: "))
heapsort(arr)   

#Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_idx = right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])

    return merged


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




