## Exercise 4.1
print("==== Exercise 4.1 ====")
x = 15
y = 4

# Output: x + y = 19
print('x + y =', x+y)

# Output: x - y = 11
print('x - y =', x-y)

# Output: x * y = 60
print('x * y =', x*y)

# Output: x / y = 3.75
print('x / y =', x/y)

# Output: x // y = 3
print('x // y =', x//y)

# Output: x ** y = 50625
print('x ** y =', x**y)

## Exercise 4.2
print("\n==== Exercise 4.2 ====")
x = 15
x = 10
y = 12

# Output: x > y is False
print('x > y is', x>y)

# Output: x < y is True
print('x < y is', x<y)

# Output: x == y is False
print('x == y is', x==y)

# Output: x != y is True
print('x != y is', x!=y)

# Output: x >= y is False
print('x >= y is', x>=y)

# Output: x <= y is True
print('x <= y is', x<=y)

## Exercise 4.3
print("\n==== Exercise 4.3 ====")
x = True
y = False

print('x and y is', x and y)

print('x or y is', x or y)

print('not x is', not x)

## Exercise 4.4
print("\n==== Exercise 4.4 ====")
# Strings
str1 = "Hello"
str2 = "World"

# Concat
result = str1 + " " + str2

# Output
print(result)

## Exercise 4.5
print("\n==== Exercise 4.5 ====")
# String
str = "HA"

# Replicate
result = str * 3

# Output
print(result)

## Exercise 4.6
print("\n==== Exercise 4.6 ====")
# Strings
needle = "lo"
haystack = "Hello World"

# Check
if needle in haystack:
    print(needle, "is present in the string", haystack)
else:
    print("Not found")

## Exercise 4.7
print("\n==== Exercise 4.7 ====")
# Strings
needle = "HA"
haystack = "Hello World"

# Check
if needle in haystack:
    print(needle, "is present in the string", haystack)
else:
    print("Not found")

## Exercise 4.8
print("\n==== Exercise 4.8 ====")
# String
str = "Jane Doe"

# Character
ch = str[1]

# Output
print(ch)   #a

## Exercise 4.9
print("\n==== Exercise 4.9 ====")
# String
str = "Hello World"

# Substring
substr = str[3:5]

# Output
print(substr)   #lo

## Exercise 4.10
print("\n==== Exercise 4.10 ====")
# string
str = "Hello World"

# Skip
new_str = str[0::2]
print(new_str)

## Exercise 4.11
print("\n==== Exercise 4.11 ====")
# String
str = "Hello World"

# Reverse
result = str[::-1]

# Output
print(result)

## Exercise 4.12
print("\n==== Exercise 4.12 ====")
#!/usr/bin/python

a = 60          # 60 = 0011 1100
b = 13          # 13 = 0000 1101
c = 0

c = a & b      # 12 = 0000 1100
print("Line 1 - Value of c is ", c)

c = a | b      # 61 = 0011 1101
print("Line 2 - Value of c is ", c)

c = a ^ b      # 49 = 0011 0001
print("Line 3 - Value of c is ", c)

c = ~a         # 61 = 0011 1101
print("Line 4 - Value of c is ", c)

c = a << 2      # 240 = 1111 0000
print("Line 5 - Value of c is ", c)

c = a >> 2      # 15 = 0000 1111
print("Line 6 - Value of c is ", c)

