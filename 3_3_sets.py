# Python Sets

# unordered and unindexed
# unchangeable, and do not allow duplicate values.

myset = {'apple', 'banana', 'cherry'}

print(myset)

# Once a set is created, you cannot change its items, 
# but you can add new items.
# Duplicate values will be ignored:


myset = {'apple', 'banana', 'cherry', 'apple'}
print(myset)

print(len(myset))

# Set Items - Data Types
# Set items can be of any data type:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# A set can contain different data types:

set1 = {"abc", 34, True, 40, "male"}

# type()

print(type(myset))

# The set() Constructor

# Using the set() constructor to make a set:

thisset = set(('apple', 'banana', 'cherry'))    # # note the double round-brackets

print(thisset)

# Access Set Items

# cannot access items in a set by referring to an index or a key
# you can loop through the set items using a for loop

thisset = {'apple', 'banana', 'cherry'}

for x in thisset:
    print(x)

print('banana' in thisset)

# Add Set Items

# Once a set is created, you cannot change its items, 
# but you can add new items.

# Add an item to a set, using the add() method:

thisset = {'apple', 'banana', 'cherry'}

thisset.add('orange')

print(thisset)


# Add Sets

# add items from another set into the current set, 
# use the update() method.

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# Add Any Iterable

# Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ['kiwi', 'orange']

thisset.update(mylist)

print(thisset)


# Remove Set Items

# use the remove(), or the discard() method.

thisset = {"apple", "banana", "cherry"}

thisset.remove('banana') # If the item to remove does not exist, remove() will raise an error.

print(thisset)


thisset = {"apple", "banana", "cherry"}

thisset.discard('banana')  # If the item to remove does not exist, discard() will NOT raise an error.

print(thisset)

# use the pop(), method to remove an item, but this method will remove the last item. 
# Remember that sets are unordered, so you will not know what item that gets removed

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# clear() method empties the set

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}

del thisset

#print(thisset)

# Loop Sets

# loop through the set items by using a for loop:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)


# Join Sets

# union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Both union() and update() will exclude any duplicate items.

# Keep ONLY the Duplicates

# intersection_update() method will keep only the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# intersection() method will return a new set, 
# that only contains the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z)

# Keep All, But NOT the Duplicates

# symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

# symmetric_difference() method will return a new set, 
# that contains only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
print(z)