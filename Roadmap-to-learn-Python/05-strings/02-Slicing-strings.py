# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string. 



a = "Good morning!"         
print(a[0:4])  # prints from index 0 to 3

print(a[5:])   # prints from index 5 to the end   

print(a[:5])   # prints from the beginning to index 4

print(a[-6:-1])  # prints from index -6 to -2 (last character is excluded)

print(a[-6:])  # prints from index -6 to the end

print(a[:-1])  # prints from the beginning to the second last character

print(a[::2])  # prints every second character