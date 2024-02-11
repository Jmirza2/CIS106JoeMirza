price_per_share = float(input("Enter Price Per Share: "))
current_Stock = float(input("Enter Current Stock Price: "))
quantity = float(input("Enter Quantity: "))

change_in_value = (current_Stock - price_per_share) * quantity

print("Change in value totals to : ", change_in_value)
