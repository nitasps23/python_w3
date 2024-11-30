# Python Arrays

# Python does not have built-in support for Arrays, 
# but Python Lists can be used instead.

# use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, 
# like the NumPy library.

# Arrays are used to store multiple values in one single variable:

# import numpy


cars = ["Ford", "Volvo", "BMW"]

print(cars)

# An array is a special variable, 
# which can hold more than one value at a time

# An array can hold many values under a single name, 
# and you can access the values by referring to an index number.

# refer to an array element by referring to the index number.

cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

print(x)


# Modify the value of the first array item:

cars[0] = 'toyota'
print(cars)

# The Length of an Array

cars = ["Ford", "Volvo", "BMW"]

x = len(cars)
print(x)

# Looping Array Elements

# use the for in loop to loop through all the elements of an array.

cars = ["Ford", "Volvo", "BMW"]

for x in cars:
    print(x)


# Adding Array Elements

# use the append() method to add an element to an array.

cars.append('honda')

print(cars)

# Removing Array Elements

# use the pop() method to remove an element from the array.

cars.pop(1)

print(cars)

# use the remove() method to remove an element from the array.

cars = ["Ford", "Volvo", "BMW"]

cars.remove('Volvo')

print(cars)


# The list's remove() method only removes the first occurrence of the specified value.

