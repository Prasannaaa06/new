# Shopping cart program

item = input("What item do you like to buy? :")
price = float(input("Enter the price of the item :"))
quantity = int(input("How many items do you like to buy? :"))

total_price = quantity * price

print(f"The total payable amount for the purchase of {item} is {total_price}")