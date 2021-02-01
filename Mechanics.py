print("Hello, World!")
# when you are done, end the program with exit()
# this is called comments you can use them to write message in code without them playing any effect
"""
Same thing here
"""
'''
And this
'''

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

# Lesson 2: Using Functions
print("Lesson 2: Using Functions")

x = "awesome"


def myfunc1():
    print("Python is " + x)


myfunc1()


def myfunc2():
    global x
    x = "fantastic"


myfunc2()

print("Python is " + x)
x = "awesome"


def myfunc3():
    global x
    x = "fantastic"


myfunc3()

print("Python is " + x)

# Lesson 3: Data Types
print("Lesson 3: Data Types")
# Lesson 4: Python Numbers
print("Lesson 4: Python Numbers")

# Lesson 5: Casting
print("Lesson 5: Casting")
x = int(1)  # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3
print(x)
print(y)
print(z)
x = float(1)  # x will be 1.0
y = float(2.8)  # y will be 2.8
z = float("3")  # z will be 3.0
w = float("4.2")  # w will be 4.2
print(x)
print(y)
print(z)
print(w)
x = str("s1")  # x will be 's1'
y = str(2)  # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x)
print(y)
print(z)

# Lesson 6: Python Strings
print("Lesson 6")
# 6.1 How to print out Strings
print("6.1 How to print out Strings")
a = "Hello"
print(a)
# 6.2 How to print comments
print("6.2 How to print comments")
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# 6.3 How to print out the String length
print("6.3 How to print out the String length")
a = "Hello, World!"
print(len(a))
# 6.4 How to print out the letters of the string in a loop
print("6.4 How to print out the letters of the string in a loop")
for x in "banana":
    print(x)
# 6.5 How to check if a certain phrase or character is present in a string
print("6.6 How to check if a certain phrase or character is present in a string")

txt = "The best things in life are free!"
print("free" in txt)
# 6.6 How to check if a certain phrase or character is NOT present in a string
print("6.6 How to check if a certain phrase or character is NOT present in a string")
txt = "The best things in life are free!"
print("expensive" not in txt)
# 6.7 How to cut Strings
print("6.7 How to cut Strings")
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])
# 6.8 How to modify Strings
a = "Hello, World!"
print(a.upper())  # Upper Case
print(a.lower())  # Lower Case
print(a.strip())  # removes any ending blank spaces
print(a.replace("H", "J"))  # replaces a string with another string
print(a.split(","))  # splits the string into substrings
# 6.9 How to concatenate Strings
print("6.9 How to concatenate Strings")
a = "Hello"
b = "World"
c = a + b
print(c)
a = "Hello"
b = "World"
c = a + " " + b
print(c)
# 6.10 How to format your strings
print("6.10 How to format your strings")
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))  # using {}, format(age) makes that {} into that variable
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))  # you can use multiple and ordering matters
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))  # you can use index to locate the spots yourself
# 6.11 How to escape characters
print("6.11 How to escape characters")
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
# 6.12 List of String methods you can test out.
print("6.12 List of String methods you can test out.")
"""capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""
# Lesson 7: Python Booleans
# 7.1 How to return true or false
print("7.1 How to return true or false")
print(10 > 9)  # true
print(10 == 9)  # false
print(10 < 9)  # false
# 7.2 How to use true/false to find if s statement is true using if/else
print("7.2 How to use true/false to find if s statement is true using if/else")
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

# 7.3 How evaluate any value
print("7.3 How evaluate any value")
print(bool("Hello"))
print(bool(15))
x = "Hello"
y = 15
# 7.4 What values are true
print("7.4 What values are true")
"""
Most Values are True:
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""
print("Examples")
print(bool(x))
print(bool(y))
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
# 7.5 What values are false
print("7.5 What values are false")
"""
Some Values are False
In fact, there are not many values that evaluate to False, except empty values, 
such as (), [], {}, "", the number 0, and the value None. And of course the value 
False evaluates to False.
"""
print("Examples")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print("PROXY")


class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))

# 7.6 How to use functions to return boolean
print("7.6 How to use functions to return boolean")


def myFunction():
    return True


print(myFunction())

if myFunction():  # if it returns true
    print("YES!")
else:  # if it returns false
    print("NO!")

x = 200
print(isinstance(x, int))
# Lesson 8 Python math operators
print("Lesson 8 Python math operators")
# 8.1 Arithmetic Operators
print("8.1 Arithmetic Operators")
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 % 5)
print(10 ** 5)
print(10 // 5)
"""
+	Addition	    x + y	
-	Subtraction	    x - y	
*	Multiplication	x * y	
/	Division	    x / y	
%	Modulus	        x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
"""
# 8.2 Assignment Operators
print("8.2 Assignment Operators")
x = 5
print(x)
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
x %= 3
print(x)
x //= 3
print(x)
x **= 3
print(x)
x = 5
x &= 3
print(x)
x |= 3
print(x)
x ^= 3
print(x)
x >>= 3
print(x)
x <<= 3
print(x)
"""
Operator:	Example:	Same As:
=	        x = 5	    x = 5	
+=	        x += 3	    x = x + 3	
-=	        x -= 3	    x = x - 3	
*=	        x *= 3	    x = x * 3	
/=	        x /= 3	    x = x / 3	
%=	        x %= 3	    x = x % 3	
//=	        x //= 3	    x = x // 3	
**=	        x **= 3	    x = x ** 3	
&=	        x &= 3	    x = x & 3	
|=	        x |= 3	    x = x | 3	
^=	        x ^= 3	    x = x ^ 3	
>>=	        x >>= 3	    x = x >> 3	
<<=	        x <<= 3	    x = x << 3
"""
# 8.3 Comparing Operators
print("8.3 Comparing Operators")
x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
"""
==	Equal	                    x == y	
!=	Not equal	                x != y	
>	Greater than	            x > y	
<	Less than	                x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	    x <= y	
"""
# 8.4 Logical Operators
print("8.4 Logical Operators")
x = 5
print(3 < x < 10)
print(x > 3 or x < 4)
print(not (x > 3 and x < 10))
"""
and 	Returns True if both statements are true	                x < 5 and  x < 10	
or	    Returns True if one of the statements is true	            x < 5 or x < 4	
not	    Reverse the result, returns False if the result is true	not (x < 5 and x < 10)
"""
# 8.5 Identity Operators
print("8.5 Identity Operators")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
print(x is not z)
# returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate the difference between "is not" and "!=": this comparison returns False because x is equal to y
"""
is 	        Returns True if both variables are the same object	        x is y	
is not	    Returns True if both variables are not the same object	    x is not y
"""
# 8.6 Membership Operators
print("8.6 Membership Operators")
x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list
x = ["apple", "banana"]
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list
"""
in 	    Returns True if a sequence with the specified value is present in the object	    x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y
"""
# Lesson 9: List(aka Arrays)
print("Lesson 9: List(aka Arrays)")
# 9.1 How to make a list
print("9.1 How to make a list")
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
# 9.2 How to check for list length
print("9.2 How to check for list length")
print(len(thislist))
# 9.3 List data types can be int, String, and boolean and all be in the same list
print("9.3 List data types can be int, String, and boolean and all be in the same list")
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
list4 = ["abc", 34, True, 40, "male"]
print(list4)
# 9.4 How to define the list data type
print("9.4 How to define the list data type")
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
# 9.5 Using the list constructor to make a list
print("9.5 Using the list constructor to make a list")
thislist = list(("apple", "banana", "cherry"))
print(thislist)
# 9.6 How to access a index of a list
print("9.6 How to access a index of a list")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
# 9.7 How to check if an Item exist
print("9.7 How to check if an Item exist")
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
# 9.8 How to change the value of a specific item
print("9.8 How to change the value of a specific item")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1] = "blackcurrant"
print(thislist)
# 9.9 How to change a Range of Item Values
print("9.9 How to change a Range of Item Values")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:4] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:1] = ["blackcurrant", "watermelon"]
print(thislist)
# 9.10 How to insert items
print("9.10 How to insert items")
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
# 9.11 How to append Items
print("9.11 How to append Items")
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# 9.12 How to extend the list
print("9.12 How to extend the list")
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
# 9.13 How to remove a specific item
print("9.13 How to remove a specific item")
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# 9.14 How to remove a specific index
print("9.14 How to remove a specific index")
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop()  # pop() with no idex removes the last
print(thislist)
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# 9.15 How to delete the list
print("9.15 How to delete the list")
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # del thislist would ALSO delete the entire list
# 9.16 How to use Loops in list
print("9.16 How to use Loops in list")
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
# 9.17 How to use While Loops in a list
print("9.17 How to use While Loops in a list")
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
# 9.18 How to Loop using List Comprehension
print("9.18 How to Loop using List Comprehension")
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
# 9.19 How to use list comprehension
print("9.19 How to use list comprehension")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print("Prints out words that contain a")
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print("Prints out words that is not apple")
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print("Prints out the list since there are no conditions")
print(newlist)

newlist = [x for x in range(10)]
print("Iterable: Prints out the numbers up to 10")
print(newlist)

newlist = [x for x in range(10) if x < 5]
print("Prints out the numbers up to 10 but only for those less than 5")
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print("Turns all the list into uppercase")
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print("Makes all the list 'Hello'")
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print("uses conditions to solves problems: if banana exist, replace it with orange")
print(newlist)
# 9.20 How to Sort Lists
print("9.20 How to Sort Lists")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print("Sorts alphabetically")
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print("Sorts in size order")
print(thislist)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print("Printing in reverse")
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print("Printing in reverse")
print(thislist)

print("This sorts the list based on how close the number is to 50")


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print("this sorts by caps too: Caps go first")
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print("this sorts by lowercase first instead")
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print("this prints in reverse")
print(thislist)

# 9.21 How to copy list
print("9.21 how to copy lists")
print("This is how you copy list into another variable")
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

print("You can also use the list() method")
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# 9.22 How to join list together
print("9.22 How to join list together")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

print("You can use for loop to combine one by one")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

print("The extend() method, which purpose is to add elements from one list to another list")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# 9.23 List methods
print("9.23 List methods")
"""
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""
# Lesson 10 Python Tuples
print("Lesson 10 Python Tuples")
print("One of the data types like list set and dictionaries that dont change its contents")
thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print("Finding the length of the tuple")
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

print("To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not "
      "recognize it as a tuple.")
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))