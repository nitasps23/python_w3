# Python Operators

# Operators are used to perform operations on variables and values

# Python divides the operators in the following groups:

# Arithmetic operators

x = 5
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)    # Modulus
print(x ** y)   # Exponentiation
print(x // y)   # #the floor division // rounds the result down to the nearest whole number

# Assignment operators

x = 5

print(x)

x += 3      # x = x + 3

print(x)

x = 5

x -= 3      # x = x - 3

print(x)

x = 5

x *= 3      # x = x * 3

print(x)

x = 5

x /= 3      # 	x = x / 3

print(x)

## x /= 3	x = x / 3
## x %= 3	x = x % 3
## x //= 3	x = x // 3
## x **= 3	x = x ** 3
## x &= 3	x = x & 3
## x |= 3	x = x | 3
## x ^= 3	x = x ^ 3
## 	x >>= 3	x = x >> 3
## x <<= 3	x = x << 3

# Comparison operators : Comparison operators are used to compare two values

x = 5
y = 3

print(x == y)

x = 5
y = 3

print(x != y)

x = 5
y = 3

print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


# Logical operators : Logical operators are used to combine conditional statements

x = 5

print(x > 3 and x < 10)
print(x > 3 or x < 4)
print(not(x > 3 and x < 10))

# Identity operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y



# Membership operators : Membership operators are used to test if a sequence is presented in an object

x = ["apple", "banana"]

print("banana" in x)
print("orange" not in x)

# Bitwise operators : Bitwise operators are used to compare (binary) numbers

# & 	AND	Sets each bit to 1 if both bits are 1
# |	OR	Sets each bit to 1 if one of two bits is 1
# ^	XOR	Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT	Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

