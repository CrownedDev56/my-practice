# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create List
numbers = [1,2,3,4,5]
# using a constuctor
'''numbers = list((1,2,3,4,5))'''

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Get Value
print(fruits[2])

# Get len

print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Grapes')

# Insert into specific position
fruits.insert(2, 'Strawberries')

# Remove from position

fruits.pop(1)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)



print(fruits)
