# Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Extend List
thislist.extend(["kiwi", "mango", "papaya"])
print(thislist)  # Output: ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'papaya']

# Insert Items
thislist.insert(1, "blueberry")
print(thislist)  # Output: ['apple', 'blueberry', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'papaya']


# Add Any Iterable
thislist.extend(("pineapple", "grapefruit"))
print(thislist)  # Output: ['apple', 'blueberry', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'papaya', 'pineapple', 'grapefruit']

