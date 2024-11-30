# Python Tuples

mytuple = ("apple", "banana", "cherry")

thistuple = ("apple", "banana", "cherry")
print(thistuple)

print(len(thistuple))

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Access Tuples

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Negative Indexing

print(thistuple[-1])

# Range of Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])

# Range of Negative Indexes

#Negative indexing means starting from the end of the tuple.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Check if Item Exists

thistuple = ("apple", "banana", "cherry")
if 'apple' in thistuple:
    print("yes, apple is in the fruits tuple.")


# Update Tuples

# Tuples are unchangeable, meaing that you cannot change, add, or remove items once the tuple is created.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x = ("apple", "banana", "cherry")

y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Add Items
# Once a tuple is created, you cannot add items to it.

# thistuple = ("apple", "banana", "cherry")
# thistuple.append("orange")  # this is error

# print(thistuple)


# Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")

y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)


# Remove Items

# You cannot remove items in a tuple.

# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")

y = list(thistuple)
y.remove("apple")

thistuple = tuple(y)

print(thistuple)

# The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")

del thistuple

# print(thistuple) # #this will raise an error because the tuple no longer exists


# Unpack Tuples

# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

fruits = ("apple", "banana", "cherry")

# extract the values back into variables. This is called "unpacking":

# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#The number of variables must match the number of values in the tuple, if not, you must use an asterix to collect the remaining values as a list.

# Using Asterix*

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# If the asterix is added to another variable name than the last, 
# Python will assign values to the variable until the number of values left matches the number of variables left.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# Loop Tuples

# You can loop through the tuple items by using a for loop.

thistuple = ("apple", "banana", "cherry")

for x in thistuple:
    print(x)


# Loop Through the Index Numbers

# Use the range() and len() functions to create a suitable iterable.

thistuple = ("apple", "banana", "cherry")

for i in range(len(thistuple)):
    print(thistuple[i])

# Using a While Loop

# Print all items, using a while loop to go through all the index numbers:

thistuple = ("apple", "banana", "cherry")

i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1


# Join Tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples

fruits = ("apple", "banana", "cherry")

mytuple = fruits * 2
print(mytuple)