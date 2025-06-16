# Remove list items using the `remove()` method
mylist = ["apple", "banana", "cherry", "Orange"]
mylist.remove("banana")
print(mylist)  # Output: ['apple', 'cherry', 'Orange']

# Remove the first occurrence of "banana"
mylist = ["apple", "banana", "cherry", "banana", "Orange"]
mylist.remove("banana")
print(mylist)  # Output: ['apple', 'cherry', 'banana', 'Orange']

# Remove Specified Index
mylist = ["apple", "banana", "cherry", "Orange"]
del mylist[1]  # Removes the item at index 1
print(mylist)  # Output: ['apple', 'cherry', 'Orange']

# Remove the last item using the `pop()` method
mylist = ["apple", "banana", "cherry", "Orange"]
last_item = mylist.pop()  # Removes the last item and returns it
print(mylist)  # Output: ['apple', 'banana', 'cherry']
print("Removed item:", last_item)  # Output: Removed item: Orange

# The del keyword also removes the specified index
mylist = ["apple", "banana", "cherry", "Orange"]
del mylist[1]  # Removes the item at index 1
print(mylist)  # Output: ['apple', 'cherry', 'Orange']

# del keyword can also delete the list completely
mylist = ["apple", "banana", "cherry", "Orange"]
del mylist  # Deletes the entire list
# print(mylist)  # Uncommenting this line will raise an error since mylist is deleted

# Clear the list using the `clear()` method
mylist = ["apple", "banana", "cherry", "Orange"]
mylist.clear()  # Removes all items from the list
print(mylist)  # Output: []