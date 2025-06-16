# Get input from user
user_input = input("Enter your name:")

# Convert input to boolean
is_valid = bool(user_input)

# Check the condition
if is_valid == False:  # or simply `if not is_valid:`
    print("Please enter your name.")
else:
    print(f"Hello {user_input}.")