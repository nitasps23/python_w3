# Python Dictionaries

thisdict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}

# Dictionaries are used to store data values in key:value pairs

# unordered, changeable and does not allow duplicates.

print(thisdict)

# Dictionary Items

thisdict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}

print(thisdict['brand'])

# Dictionaries cannot have two items with the same key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}

print(thisdict)

# Dictionary Length

print(len(thisdict))

# Dictionary Items - Data Types

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)

# type()

print(type(thisdict))


# Access Items

# access the items of a dictionary by referring to its key name, inside square brackets:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict['model']
print(x)

# a method called get() that will give you the same result

x = thisdict.get('model')
print(x)

# Get Keys

# keys() method will return a list of all the keys in the dictionary.

x = thisdict.keys()
print(x)

# Add a new item to the original dictionary, 
# and see that the value list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x)

car['color'] = 'white'

print(x)


# Get Values

# values() method will return a list of all the values in the dictionary.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()
print(x)

# Make a change in the original dictionary, 
# and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x)

car['year'] = 2020

print(x)

# Add a new item to the original dictionary, 
# and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x)

car['color'] = 'red'
print(x)

# Get Items

# items() method will return each item in a dictionary, as tuples in a list.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()
print(x)

# Add a new item to the original dictionary, 
# and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x)

car['year'] = 2020

print(x)

# Add a new item to the original dictionary, 
# and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x)

car['color'] = 'red'

print(x)


# Check if Key Exists

# determine if a specified key is present in a dictionary use the in keyword:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

if 'model' in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


# Change Items

# change the value of a specific item by referring to its key name

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict['year'] = 2018

print(thisdict)


# Update Dictionary

# update() method will update the dictionary with the items from the given argument.

# argument must be a dictionary, or an iterable object with key:value pairs.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.update({'year': 2020})

print(thisdict)


# Add Items

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict['color'] = 'red'
print(thisdict)

# Update Dictionary

# update() method will update the dictionary with the items from a given argument. 
# If the item does not exist, the item will be added

# argument must be a dictionary, or an iterable object with key:value pairs

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.update({'color': 'red'})

print(thisdict)

# Remove Items

# pop() method removes the item with the specified key name

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.pop('model')
print(thisdict)

# popitem() method removes the last inserted item 
# (in versions before 3.7, a random item is removed instead

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.popitem()
print(thisdict)

# del keyword removes the item with the specified key name

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

del thisdict['model']
print(thisdict)


# del keyword can also delete the dictionary completely:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

del thisdict
# print(thisdict) # #this will cause an error because "thisdict" no longer exists


# clear() method empties the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.clear()
print(thisdict)


# Loop Dictionaries

# loop through a dictionary by using a for loop

# When looping through a dictionary, the return value are the keys of the dictionary, 
# but there are methods to return the values as well.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Print all key names in the dictionary, one by one
for x in thisdict:
    print(x)

# Print all values in the dictionary, one by on

for x in thisdict:
    print(thisdict[x])


# You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
    print(x)


# You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
    print(x)


# Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
    print(x, y)


# Copy Dictionaries

# Make a copy of a dictionary with the copy() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict = thisdict.copy()
print(mydict)


# Another way to make a copy is to use the built-in function dict()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict = dict(thisdict)
print(mydict)


# Nested Dictionaries

# A dictionary can contain dictionaries, this is called nested dictionaries.

# Create a dictionary that contain three dictionaries:

myfamily = {
    'child1': {
        'name': 'Emil',
        'year': 2004
    },
    'child2': {
        'name': 'Tobias',
        'year': 2007
    },
    'child3': {
        'name': 'Linus',
        'year': 2011
    }
}

print(myfamily)


# Or, if you want to add three dictionaries into a new dictionary:

# Create three dictionaries, 
# then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
    'child1': child1,
    'child2': child2,
    'child3': child3
}

print(myfamily)

# Access Items in Nested Dictionaries

# use the name of the dictionaries, starting with the outer dictionary:

# Print the name of child 2:

print(myfamily["child2"]['name'])