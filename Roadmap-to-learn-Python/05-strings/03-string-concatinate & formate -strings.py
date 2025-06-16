# To concatenate, or combine, two strings you can use the + operator.

a = "Hello"
b = "World"
c = a + b
print(c) # Merging variable  a and b together

# To concatenate, or combine, two strings you can use the + operator with a space in between use " ".

d = a + " " + b
print(d) # Merging variable  a and b together with a space in between

# String Format
'''
age = 36
txt = "My name is John, I am " + age
print(txt) # This will raise an error because age is an integer, not a string'''

# F-Strings

age = 36
txt = (f"My name is John, I am {age}")
print(txt) # This will work because f-strings automatically convert the integer to a string 

# Placeholders and Modifiers

price = 59
txt = (f"The price is $ { price} dollars")
print(txt) # This will work because f-strings automatically convert the integer to a string

# Formatting strings

age = 36
name = "John"
print(f"My name is {name} and I am {age} years old.") 

# another way to format strings
print("My name is {} and I am {} years old.".format(name, age))

# using % operator
print("My name is %s and I am %d years old." % (name, age))

# using f-string with expressions
print(f"My name is {name.upper()} and I am {age + 5} years old.")  # name in uppercase, age incremented by 5

# A placeholder can contain Python code, like math operations
print(f"The sum of 4 and 5 is {4 + 5}.")  # outputs: The sum of 4 and 5 is 9

# Using escape characters
print("He said, \"Hello!\"")  # using backslash to escape double quotes

# Using triple quotes for multi-line strings
multi_line_string = """This is a multi-line string.
It can span multiple lines."""
print(multi_line_string)

# Using raw strings to ignore escape characters
raw_string = r"This is a raw string. \n It will not interpret escape characters."   
print(raw_string)  # outputs: This is a raw string. \n It will not interpret escape characters.



# Splitting and joining strings
text = "  Hello, World!  "  # a string with leading and trailing spaces
words = text.split(",")  # splits the string into a list  
print(words)  # outputs: ['  Hello', 'World!  ']
joined_text = " - ".join(words)  # joins the list into a string with " - " as separator
print(joined_text)  # outputs: '  Hello - World!  '

# Checking for substrings
print("Hello" in text)  # checks if "Hello" is in the text, outputs: True
print("Python" not in text)  # checks if "Python" is not in the text, outputs: True

# Finding the index of a substring

print(text.find("World"))  # finds the index of "World", outputs: 8

# Counting occurrences of a substring   

print(text.count("o"))  # counts how many times "o" appears in the text, outputs: 2

# Checking if a string starts or ends with a specific substring

print(text.startswith("  Hello"))  # checks if the text starts with "  Hello", outputs: True

print(text.endswith("World!  "))  # checks if the text ends with "World!  ", outputs: True
