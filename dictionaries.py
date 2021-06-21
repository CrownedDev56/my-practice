# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Simple dictionary

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30}

# Using a constructor
person2 = dict( 
    first_name= 'John',
    last_name= 'Doe',
    age= 30)



# Access value
print(person['first_name'])
print(person.get('last_name'))

# Add key/Value
person['phone'] = '555-555-5555'

# Get Keys
print(person.keys())

# Get Items
print(person.items())


#make copy
person3 = person.copy()
person3['city'] = 'Boston'


# Remove item
del(person['age'])
person.pop('phone')

# clear
person.clear

# Get length
print(len(person3))

# List of dict

people = [
    {'name':'Marth', 'age': 40},
    {'name':'Bob', 'age': 20}
]

print(people[1]['name'])