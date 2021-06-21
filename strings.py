# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = 'Tafadzzz'
age = 25

# Concatenate
'''print('Hello ' + name + ' i am ' + str(age))'''

# String Formatting

# Arguments by position
'''print('{2},{1},{0}'.format('a', 'b', 'c'))'''

# Arguments by name
'''print('My name is {name} and i am {age}'.format(name= name, age = age))'''

# F-strings
'''print(f'My name is {name} and i am {age}')'''

# String Methods
s = 'hello there World'

# Capitalize first letter
print(s.capitalize())

# All uppercase
print(s.upper())

# All lower
print(s.lower())

# Swap Case
print(s.swapcase())

# Get Length
print(len(s))

# Replace
print(s.replace('World', 'everyone'))

# Count
sub = "h"
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Fine position
print(s.find('r'))


# Is all alphanumberic
print(s.isalnum())

# Is all Alphabetic
print(s.isalpha())

# Is all Numeric
print(s.isnumeric())

