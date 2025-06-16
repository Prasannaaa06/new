# Changing the list items

mylist = ["apple", "banana", "cherry", "Orange"]
# Changing the value of the first item
mylist[0] = "kiwi"
print(mylist)  # Output: ['kiwi', 'banana', 'cherry', 'Orange'] 

# Change a Range of Item Values
mylist[1:3] = ["blackcurrant", "watermelon"]
print(mylist)  # Output: ['kiwi', 'blackcurrant', 'watermelon', 'Orange']

# Insert Items
mylist.insert(2, "grape")
print(mylist)  # Output: ['kiwi', 'blackcurrant', 'grape', 'watermelon', 'Orange']

