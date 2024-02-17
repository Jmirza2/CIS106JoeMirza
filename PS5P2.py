item = input("Enter your item: ")
quantity = int(input("Enter the quantity: "))

if item == 'A':
  unit_Price = 10.00
else: 
  unit_Price = 20.00

extendPrice = unit_Price * quantity

print("Item: " , item)
print("Unit Price: " , unit_Price)
print("Extended Price: " , extendPrice)