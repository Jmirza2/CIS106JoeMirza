price_per_share = int(input("Enter Price Per Share: "))
current_Stock = int(input("Enter Current Stock Price: "))
quantity = int(input("Enter Quantity: "))

change_in_value = (current_Stock - price_per_share) * quantity

print("Change in value totals to : ", change_in_value)

