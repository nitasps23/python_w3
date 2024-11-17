# Multiline Strings

poem = """Down the lane winding between & behind houses, I find the cottage
I rented after I left Michael, he painted it bright yellow, decades later
it's the same color, Mike with stars of paint in his curly black hair..."""

print(poem)

# Strings are Arrays

a = "Hello, World!"
print(a[2])     # Square brackets can be used to access elements of the string


# Looping Through a String

for x in "banana":
    print(x)

# Check String

# to check if a certain phrase or character is present in a string

txt = "The best things in life are free!"
print("free" in txt)

# Use it in an if statement:

txt = "The best things in life are free!"

if "free" in txt:
    print("Yes, 'free' is present.")


# Check if NOT

txt = "The best things in life are free!"

print("expensive" not in txt)

# Use it in an if statement:

if "expensive" not in txt:
    print("Yes, 'expensive' is not present")


# Slicing Strings

b = "Hello, World!"
print(b[2:5])

print(b[:5])    # leaving out the start index, the range will start at the first character

print(b[2:])    # leaving out the end index, the range will go to the end

print(b[-5:-2]) # Use negative indexes to start the slice from the end of the string

# Modify Strings

a = "Hello, World!"

print(a.upper())    # Upper Case

print(a.lower())    # Lower Case

a = " Hello, World! " # Whitespace is the space before and/or after the actual text, and very often you want to remove this space
print(a)

print(a.strip())    # strip() method removes any whitespace from the beginning or the end

# Replace String

a = "Hello, World!"

print(a.replace("H", "J"))

# Split String

# split() method returns a list where the text between the specified separator becomes the list items.

a = "Hello, World!"

print(a.split(",")) 


# Concatenate Strings

a = "Hello"
b = "World"

c = a + " " + b
print(c)

# Format Strings

#  we cannot combine strings and numbers 

age = 36
# txt = "My name is John, I am " + age      <--- error
# print(txt)

# we can combine strings and numbers by using the format() method

age = 38
txt = "My name is Nita, and I am {}"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders

quantity = 3
itemno = 567
price = 49.95

my_order = "I want {} pieces of item {} for {} dollars."
print(my_order.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders

quantity = 3
itemno = 567
price = 49.95
my_order = " I want to pay {2} dollars for {0} pieces of item {1}."

print(my_order.format(quantity, itemno, price))


# Escape Characters

# to insert characters that are illegal in a string, use an escape character.

# An escape character is a backslash \ followed by the character you want to insert

# txt = "We are the so-called "Vikings" from the north." 
# You will get an error if you use double quotes inside a string that are surrounded by double quotes

txt = "We are the so-called \"Vikings\" from the north."

print(txt)

# Escape Characters
# Other escape characters used in Python:

txt = 'It\'s alright.'      # Single Quote
print(txt)

txt = "This will insert one \\ (backslash)."    # Backslash
print(txt)

txt = "Hello\nWorld!"   # 	New Line
print(txt) 

txt = "Hello\rWorld!"   # Carriage Return
print(txt)

txt = "Hello\tWorld!"   # Tab	
print(txt)

txt = "Hello \bWorld!"  # Backspace
print(txt) 

# \f	Form Feed

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 