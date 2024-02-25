price = 0.0

quantity = int(input("Enter the quantity of the item: "))

if quantity > 10000:
  price = 10.0
elif quantity > 5000:
  price = 20.0
else:
  price = 30.0

extendedPrice = quantity * price
tax = extendedPrice * 0.07
total = extendedPrice + tax

print(f"Extended Price: ${extendedPrice}")
print(f"tax: ${tax}")
print(f"Total: ${total}")

