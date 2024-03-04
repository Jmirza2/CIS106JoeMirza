user = input("Do you want to do this program? ")
total_discount = 0

while user == "yes" or user == "Yes":
    quantity = float(input("Enter a quantity: "))
    price = float(input("Enter a price of an item: "))
    extended_Price = quantity * price
    if extended_Price > 10000.00:
      discount = extended_Price * .25
    else:
      discount = extended_Price * 0.10

    total_discount = total_discount + discount
    print("Extended Price: ", extended_Price)
    print("Discount Amount: ", discount)
    print("Total: ", extended_Price - discount)

    user = input("Do you want to continue? ")

print("Total discount for all orders: ", total_discount)
 


