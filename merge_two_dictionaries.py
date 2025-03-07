#9. Write a Python code to merge two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
#**dict1 and **dict2 unpack the key-value pairs from dict1 and dict2.
#The {} braces create a new dictionary that includes all the key-value pairs from both dict1 and dict2.

merged = {**dict1, **dict2}
print("final mearged data",merged) #{'a': 1, 'b': 3, 'c': 4}