# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#Simple tuple
fruit_tuple = ('Apple', 'Orange', 'Mango')

# Constructor
'''fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))'''

# Get single value

'''print(fruit_tuple[1])'''

# Cannot Change value

'''fruit_tuple[1] = 'Grape'''

# Tuples with one value should have trailing comma otherwise it will display as a string
fruit_tuple_2 =('Apple',)

#Get lenght of tuple
'''print(len(fruit_tuple))'''

# Delete tuple
del fruit_tuple_2
'''print(fruit_tuple_2)'''

'''print(fruit_tuple)'''




# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruit_set ={'Apple', 'Orange','Mango'}

#Check if value is in set
print('Apple' in fruit_set)


# Add to set

fruit_set.add('Grape')

# Remove from set
fruit_set.remove('Grape')

# Clear set
fruit_set.clear()

# Delete Set
del fruit_set

print(fruit_set)
