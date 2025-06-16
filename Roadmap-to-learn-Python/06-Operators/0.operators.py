# Operators are used to perform operations on variables and values.
#Python divides the operators in the following groups:
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operator
# Identity operators
# Membership operators
# Bitwise operators


# Arithmetic operators :

# '+' performs Addition
print ("Sum of 10 and 5 :",10+5)
# '-' performs Subtraction
print ("Subtraction of 10 and 5 :",10-5)
# '/' performs Division
print ("Division of 10 and 5 :",10/5)
# '*' performs Multiplication
print ("Product of 10 and 5 :",10*5)
# '%' finds Modulus, calculates the remainder of a division operation.
print ("Modulus of 10 and 5 :",10%5)
# '**' finds Exponentiation
print ("10 power 5 :",10**5)
# '//' performs floor division
print ("Floor Division of 15 and 2 :",15//2)

''' Assignment Operators '''

# '=' used to assign the values
x = 5
# '+=' a shorthand for addition assignment
x+=x
print(x)
# '-=' a shorthand for subtraction assignment
x-=x
print(x)
# same for all operators for reference visit : https://www.w3schools.com/python/python_operators.asp


''' Comparison Operators '''

# '==' comparison operator
x = 5
y = 6
print (x==y)

# try every comparison operator by urself
'''
'!=' Not equal operator
'>'	Greater than
'<'	Less than
'>=' Greater than or equal to
'<=' Less than or equal to
'''

''' Logical Operators '''

# 'and' Returns True if both statements are true
x = 10
y = 6
z =8
print(x>y and x>z)

# 'or' Returns True if one of the statements is true
x = 7
y = 8
z = 2
print(x>y or x>z)

# 'not' Reverse the result, returns False if the result is true
x = 8
y = 6
z = 15
print(not(x < y and y < z))

''' Identity Operators '''

# 'is'	Returns True if both variables are the same object
x = ["apple","honey","peanut butter"]
y = ["orange","lemon","grapes"]
x = z
print(y is x)
print(z is x)

# 'is not' Returns True if both variables are not the same object
x = ["apple","honey","peanut butter"]
y = ["orange","lemon","grapes"]
x = z
print(y is not x)
print(z is not x)
