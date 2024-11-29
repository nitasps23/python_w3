# Python Lists

thislist = ["apple", "banana", "cherry"]

print(thislist)

# List items are ordered, changeable, and allow duplicate values.

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# To determine how many items a list has, use the len() function

print(len(thislist))

# List items can be of any data type:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list1 = ["abc", 34, True, 40, "male"]


# type()

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# The list() Constructor

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Python Collections (Arrays)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered and changeable. No duplicate members.

# Access List Items

thislist = ["apple", "banana", "cherry"]

print(thislist[1])      # The first item has index 0.


# Negative Indexing

print(thislist[-1])     # -1 refers to the last item, -2 refers to the second last item etc.


# Range of Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])        # start at index 2 (included) and end at index 5 (not included).

print(thislist[:4])     # By leaving out the start value, the range will start at the first item:

print(thislist[2:])     # By leaving out the end value, the range will go on to the end of the list:

# Range of Negative Indexes

print(thislist[-4:-1])      # returns the items from "orange" (-4) to, but NOT including "mango" (-1):

# Check if Item Exists

thislist = ["apple", "banana", "cherry"]

if 'apple' in thislist:
    print("Yes, 'apple' is in the fruits list.")

# Change List Items

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrent"
print(thislist)

# Change a Range of Item Values

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ['blackcurrent', 'watermelon']
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, 'watermelon')
print(thislist)

# Add List Items
# Append Items - add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]
thislist.append('orange')
print(thislist)

# Insert Items

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, 'orange')
print(thislist)


# Extend List

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)
print(thislist)


# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# Remove List Items
# The remove() method removes the specified item.

thislist = ["apple", "banana", "cherry"]
thislist.remove('banana')
print(thislist)

# Remove Specified Index
#The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# If you do not specify the index, the pop() method removes the last item.

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely.

thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List
# The list still remains, but it has no content.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Loop Lists
# You can loop through the list items by using a for loop:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)


# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number

thislist = ["apple", "banana", "cherry"]

for i in range(len(thislist)):
    print(thislist[i])

# Using a While Loop
# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.
# Remember to increase the index by 1 after each iteration.

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Looping Using List Comprehension

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]     # Without list comprehension
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)

# The Syntax

# newlist = [expression for item in iterable if condition == True]

# Condition
# a filter that only accepts the items that valuate to True.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]

print(newlist)

# The condition is optional and can be omitted:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]     # With no if statement:
newlist = [x for x in fruits]

print(newlist)

# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc.
# You can use the range() function to create an iterable:

newlist = [x for x in range(10)]
print(newlist)

# Same example, but with a condition:

newlist = [x for x in range(10) if x < 5]
print(newlist)

# Expression
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]

print(newlist)

newlist = ['hello' for x in fruits]

print(newlist)

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
# "Return the item if is not banana, if it is banana return orange".
newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

# Sort Lists

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()

print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


# Sort Descending
# use the keyword argument reverse = True:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse= True)

print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse= True)

print(thislist)

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.

# The function will return a number that will be used to sort the list (the lowest number first):

def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)

print(thislist)

# Case Insensitive Sort

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# if you want a case-insensitive sort function, use str.lower as a key function:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key= str.lower)

print(thislist)

# Reverse Order

# reverse() method reverses the current sorting order of the elements.

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Copy Lists

# You cannot copy a list simply by typing list2 = list1
# Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# Another way to make a copy is to use the built-in method list().

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)

print(mylist)


# Join Lists

# There are several ways to join, or concatenate, two or more lists
# One of the easiest ways are by using the + operator.

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# Another way to join two lists are by appending all the items from list2 into list1, one by one:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# Or you can use the extend() method, which purpose is to add elements from one list to another list:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


# List Methods

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list