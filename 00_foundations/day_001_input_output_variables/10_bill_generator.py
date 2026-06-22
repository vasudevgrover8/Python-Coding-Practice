# Input: Item name, quantity, and price per item
# Process: Multiply quantity by price per item
# Output: Item details and total bill

item_name = input("Enter the name of the item: ")
quantity = int(input("Enter the quantity of the item: "))
price_per_item = float(input("Enter the price per item: "))

total_bill = quantity * price_per_item

print("Item:", item_name)
print("Quantity:", quantity)
print("Price per item:", price_per_item)
print("Total bill:", total_bill)
