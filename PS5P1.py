quantityItem = int(input('Enter the quantity of the item: '))
if quantityItem >= 1000:
  unitPrice = 3.00
else:
  unitPrice = 5.00

extendedPrice = quantityItem * unitPrice
tax = extendedPrice * 0.07
total = extendedPrice + tax

print("Quantity: ", quantityItem)
print("Unit Price: ", unitPrice)
print("Extended Price: ", extendedPrice)
print("Tax: ", tax)
print("Total: ", total)
