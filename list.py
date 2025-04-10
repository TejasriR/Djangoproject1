'What is a list in Python?'
'''Answer: A list[] is a mutable, ordered collection of items that can store elements of different
data types.'''

'How do you create a list in Python?'
my_list=[10,20,30,"apple",4.5]
print(my_list)

' How do you access elements in a list?'
print(my_list[0])
print(my_list[-1])
'''In Python, lists are ordered collections, which means each item in the list has an index starting from 0. You can access any 
element by referring to its index inside square brackets [].'''

'How do you modify an element in a list?'

my_list[1] = 100
print(my_list)

'''output = [10, 100, 30, 'apple', 4.5]'''

'1. How do you add elements to a list?'

print(my_list) #output = [10, 100, 30, 'apple', 4.5]

#append() – adds to the end
#insert() – adds at specific index
#extend() – merges another list

my_list.append(50) 
print(my_list)      #output = [10, 100, 30, 'apple', 4.5, 50]

my_list.insert(6,'banana') 
print(my_list)      #output = [10, 100, 30, 'apple', 4.5, 50, 'banana']

my_list.extend([6,7])
print(my_list)      #[10, 100, 30, 'apple', 4.5, 50, 'banana', 6, 7]

'How do you remove elements from a list?'

#remove() – removes by value
#pop() – removes by index
#del – deletes by index or slice

my_list.remove(30)
print(my_list)   #output = [10, 100, 'apple', 4.5, 50, 'banana', 6, 7]

my_list.pop(6)
print(my_list) # output = [10, 100, 'apple', 4.5, 50, 'banana', 7]

del my_list [1:3]
print(my_list) #output = [10, 4.5, 50, 'banana', 7]

'What is list comprehension in Python?'
''' A concise way to create a new list from an existing iterable.'''
squares = [x**2 for x in range(5)]
print(squares)
