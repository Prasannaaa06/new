# Typecasting: (A process of converting from one data type to another)
#              str(),int(),float(),bool()

age = 25
name = "Harish"
distance = 5.5
is_student = True
number=5

# Let us try to convert the inter to float
#age=float(age)
#print(f"You are {age} years old.")

# Let us try to convert float datatype into integer
distance = int(distance)
print(f"The distance between Paris to Tambaram is {distance}km.")

# Let us try to convert the integer to string

age = str(age)
print(f"you are {age}years old.")

# Let us perform mathematical function which the converted string from integer

print(number+distance) # When you add a string to integer is throws up an error , only integers and float can be performed mathematical functions.

# # Let us try to convert the string to boolean

name = bool(name)
print(name)