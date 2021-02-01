
# Lesson 1: Python Variables
print("Lesson 1")
# 1.1 How to create variables
print("1.1 How to create variables")
x = 5
y = "John"
print(x)
print(y)
x = 4  # x is of type int
print(x)
x = "Sally"  # x is now of type str
print(x)
# 1.2 How to specify the data type of a variable
print("1.2 How to specify the data type of a variable")
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)
# 1.3 How to get the data type of a variable
print("1.3 How to get the data type of a variable")
x = 5
y = "John"
print(type(x))
print(type(y))
# 1.4 How to assign values to multiple variables in one line
print("1.4 How to assign values to multiple variables in one line")
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# 1.5 How to assign the same string to multiple variables
print("1.5 How to assign the same string to multiple variables")
x = y = z = "Orange"
print(x)
print(y)
print(z)
# 1.6 How to extract the values into variables
print("1.6 How to extract the values into variables")
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
# 1.7 How to combine both text and a variable
print("1.7 How to combine both text and a variable")
x = "awesome"
print("Python is " + x)
x = "Python is "
y = "awesome"
z = x + y
print(z)
x = 5
y = 10
print(x + y)
