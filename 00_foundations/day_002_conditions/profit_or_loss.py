#Input: Cost and selling price
#Process: Subtract and compare the output with zero and then display accordingly
#Output: Profit or loss and value

cost = int(input("Enter the cost price: "))
selling_price = int(input("Enter the selling price: "))
total = selling_price - cost

if total > 0:
    print("Profit: ", total)
elif total < 0:
    print("Loss: ", cost - selling_price)
else:
    print("No profit no loss")