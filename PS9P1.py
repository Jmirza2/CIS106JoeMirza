def CompExtPrice(qty, unitPrice):
  extPrice = qty * unitPrice


  if extPrice > 10000.00:
    discount = extPrice * 0.10
  else:
    discount = 0.0

  return extPrice
    
total_extPrice = 0.0
r = input("Do you want to compute extended price? (Yes or No): ")

while r == "Yes":
  qty = float(input("Enter quantity: "))
  unitPrice = float(input("Enter unit price: "))
  extPrice = CompExtPrice(qty, unitPrice)
  total_extPrice = total_extPrice + extPrice
  print("Extended price: $", extPrice)
  r = input("Do you want to compute extended price? (Yes or No): ")
  print("Total extended price: $", total_extPrice)