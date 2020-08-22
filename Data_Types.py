
# PYTHON FUNDAMENTALS

# Alyssa Falshaw
# August 16th, 2020


# DATA TYPES: refers to how a given value is classified

# Primitive data types

# Boolean Values - Assesses true value of something. True and False (uppercase T and F)

is_hungry = True
has_freckles = False

# Numbers - Integers (whole numbers), floating point numbers (decimal numbers), and complex numbers

age = 35 # storing an int
weight = 160.57 # storing a float

# Strings - literal text

name = "Joe Blue"

# Composite types: collections composed of the above primitive types

# Tuples - Type of data that is immutable (can't be changed after creation) and can hold a group of values. Can contain mixed data types

dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])		# output: Bruce
dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)

# Lists - Type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.

empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']

# Dictionaries - Group of key-value pairs. Elements are indexed by unique keys which are used to access values.

empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists
new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
print(new_person)
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}

# Common Functions

# type() : find a value or variable's data type

print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>

# len() : For data types that have a length attribute (eg. lists, dictionaries, tuples, strings), can use the len function to get the length

print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# output: 11

# Type Casting or Explicit Type Conversion

# cast the number as a string, then we will be able to "add" the two values together

print("Hello" + 42)			# output: TypeError
print("Hello" + str(42))		# output: Hello 42

# treat a string input as a number

total = 35
user_val = "26"
total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61