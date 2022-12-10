# Strings are Arrays
print("====Strings are Arrays====")
"""Get the character at position 1 (remember that the first character 
has the position 0):"""
a = "Hello, World!"
print(a[1])

# Looping Through a String
print("====Looping Through a String====")
"""Since strings are arrays, we can loop through the characters in a string, 
with a for loop."""
for x in "banana":
  print(x)

# String Length
print("====String Length====")
"""To get the length of a string, use the len() function"""
a = "Hello, World!"
print(len(a)) #hasilnya 13 karena terdiri dari 13 karakter termasuk spasi

# Check String
print("====Check String====")
"""To check if a certain phrase or character is present in a string, 
we can use the keyword in."""
txt = "The best things in life are free!"
print("free" in txt)

"""Use it in an if statement:"""
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Check if NOT
print("====Check if NOT====")
"""To check if a certain phrase or character is NOT present in a string, 
we can use the keyword not in."""
txt = "The best things in life are free!"
print("expensive" not in txt)

"""Use it in an if statement:"""
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# Slicing Strings
print("====Slicing Strings====")
"""You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, 
to return a part of the string."""
"""Get the characters from position 2 to position 5 (not included):"""
b = "Hello, World!"
print(b[2:5])

"""Slice From the Start"""
b = "Hello, World!"
print(b[:5])

# Slice To the End
b = "Hello, World!"
print(b[2:])

# Negative Indexing
"""Use negative indexes to start the slice from the end of the string:"""
"""Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):"""
b = "Hello, World!"
print(b[-5:-2])

# Upper Case
print("====Upper Case====")
"""The upper() method returns the string in upper case:"""
a = "Hello, World!"
print(a.upper())

# Lower Case
print("====Lower Case====")
"""The lower() method returns the string in lower case:"""
a = "Hello, World!"
print(a.lower())

# Remove Whitespace
print("====Remove Whitespace====")
"""The strip() method removes any whitespace from the beginning or the end:"""
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace String
print("====Replace String====")
"""The replace() method replaces a string with another string:"""
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
print("====Split String====")
"""The split() method splits the string into substrings if it finds 
instances of the separator:"""
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# String Concatenation
print("====String Concatenation====")
"""Merge variable a with variable b into variable c:"""
a = "Hello"
b = "World"
c = a + b
print(c)

# To add a space between them, add a " "
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String Format
print("====String Format====")
"""Use the format() method to insert numbers into strings:"""
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

"""You can use index numbers {0} to be sure the arguments are placed in 
the correct placeholders:"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escape Character
print("====Escape Character====")
"""To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
An example of an illegal character is a double quote inside a string that is surrounded 
by double quotes"""

# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Other escape characters used in Python:
print("====Single Quote (\')====")
txt = 'It\'s alright.'
print(txt) 

print("====Backslash (\\)====")
txt = "This will insert one \\ (backslash)."
print(txt)

print("====New Line (\n)====")
txt = "Hello\nWorld!"
print(txt)

print("====Carriage Return (\r)====")
txt = "Hello\rWorld!"
print(txt)

print("====Tab (\t)====")
txt = "Hello\tWorld!"
print(txt)

print("====Backspace (\b)====")
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)

print("====Form Feed (\f)====")


print("====Octal value (\ooo)====")
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)

# Hex value (\xhh)
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

print("====capitalize()====")
# Converts the first character to upper case
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

print("====casefold()====")
# Converts string into lower case
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

print("====center()====")
# Returns a centered string
txt = "banana"
x = txt.center(20)
print(x)

print("====count()====")
# Returns the number of times a specified value occurs in a string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

print("====encode()====")
# Returns an encoded version of the string
txt = "My name is Ståle"
x = txt.encode()
print(x)

print("====endswith()====")
# Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

print("====expandtabs()====")
# Sets the tab size of the string
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

print("====find()====")
# Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

print("====format()====")
# Formats specified values in a string
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

print("====format_map()====")
# Formats specified values in a string


print("====index()====")
# Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

print("====isalnum()====")
# Returns True if all characters in the string are alphanumeric
txt = "Company12"
x = txt.isalnum()
print(x)

print("====isalpha()====")
# Returns True if all characters in the string are in the alphabet
txt = "CompanyX"
x = txt.isalpha()
print(x)

print("====isdecimal()====")
# Returns True if all characters in the string are decimals
txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)

print("====isdigit()====")
# Returns True if all characters in the string are digits
txt = "50800"
x = txt.isdigit()
print(x)

print("====isidentifier()====")
# Returns True if the string is an identifier
txt = "Demo"
x = txt.isidentifier()
print(x)


print("====islower()====")
# Returns True if all characters in the string are lower case
txt = "hello world!"
x = txt.islower()
print(x)

print("====isnumeric()====")
# Returns True if all characters in the string are numeric
txt = "565543"
x = txt.isnumeric()
print(x)

print("====isprintable()====")
# Returns True if all characters in the string are printable
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

print("====isspace()====")
# Returns True if all characters in the string are whitespaces
txt = "   "
x = txt.isspace()
print(x)

print("====istitle()====")
# Returns True if the string follows the rules of a title\
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)


print("====isupper()====")
# Returns True if all characters in the string are upper case
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

print("====join()====")
# Joins the elements of an iterable to the end of the string
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

print("====ljust()====")
# Returns a left justified version of the string
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

print("====lower()====")
# Converts a string into lower case
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

print("====lstrip()====")
# Returns a left trim version of the string
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

print("====maketrans()====")
# Returns a translation table to be used in translations
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))

print("====partition()====")
# Returns a tuple where the string is parted into three parts
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

print("====replace()====")
# Returns a string where a specified value is replaced with a specified value
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

print("====rfind()====")
# Searches the string for a specified value and returns the last position of where it was found
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

print("====rindex()====")
# Searches the string for a specified value and returns the last position of where it was found
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

print("====rjust()====")
# Returns a right justified version of the string
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")

print("====rpartition()====")
# Returns a tuple where the string is parted into three parts
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

print("====rsplit()====")
# Splits the string at the specified separator, and returns a list
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

print("====rstrip()====")
# Returns a right trim version of the string
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

print("====split()====")
# Splits the string at the specified separator, and returns a list
txt = "welcome to the jungle"
x = txt.split()
print(x)

print("====splitlines()====")
# Splits the string at line breaks and returns a list
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

print("====startswith()====")
# Returns true if the string starts with the specified value
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

print("====strip()====")
# Returns a trimmed version of the string
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

print("====swapcase()====")
# Swaps cases, lower case becomes upper case and vice versa
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

print("====title()====")
# Converts the first character of each word to upper case
txt = "Welcome to my world"
x = txt.title()
print(x)

print("====translate()====")
# Returns a translated string
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

print("====upper()====")
# Converts a string into upper case
txt = "Hello my friends"
x = txt.upper()
print(x)

print("====zfill()====")
# Fills the string with a specified number of 0 values at the beginning
txt = "50"
x = txt.zfill(10)
print(x)



