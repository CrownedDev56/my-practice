# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).


people = ['John', 'Will', 'Janet', 'Karen']

# s\Simple forloop
'''for person in people:
    print('Name: ', person)'''

#break out
for person in people:
    print('Name: ', person)
    if person == 'Janet':
        break

# Continue
for person in people:
    if person =='Janet':
        continue
    print('Current person: ', person)

# Range

for i in range(len(people)):
    print('Current person: ', people[i])


for i in range(0,10):
    print('Number: ', i )


# While loops execute a set of statements as long as a condition is true.

count = 0
while count <=10:
    print('count:', count)
    count +=1
