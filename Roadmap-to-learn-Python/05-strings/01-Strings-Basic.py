# Strings in python are surrounded by either single quotation marks, or double quotation marks.
print("Hello")
print('Hello') #'hello' is the same as "hello".

# Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Assign String to a Variable
a = "Hello"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Another way of printing multiline strings
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Strings are Arrays
a = "Hello, World!"
print(a[1])

# Looping through strings
for x in "banana":
  print(x)

# String Length
a = "Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)

# Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt: #Print only if "free" is present:
  print("Yes, 'free' is present.")

# Check if NOT present
txt = "The best things in life are free!"
print("expensive" not in txt)  # prints true if "expensive" is not in txt

