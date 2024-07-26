'''
This is a note for Module 3 of Python Intermediate. 
This is a Multi-line String comment. 

LESSON 3: Python Sets

# There are four collection data types in the Python programming language: List, Tuple, Set, and Dictionary.

https://www.w3schools.com/python/python_sets.asp 

# SET Methods
https://www.w3schools.com/python/python_sets_methods.asp 

# ? Set Comprehension
https://www.geeksforgeeks.org/comprehensions-in-python/


'''

# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Sets are written with curly brackets.

thisset = {"apple", "banana", "cherry"}
print(thisset)
# True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
# False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

print(len(thisset))

# Set items can be of any data type: String, int and boolean data types

myset = {"apple", "banana", "cherry"}
print(type(myset))

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# To Add Set Items
thisset.add("orange")
print(thisset)

# To Add Items from another
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# To Remove Items and discard will not raise an error if not available
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)