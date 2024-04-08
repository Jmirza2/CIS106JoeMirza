def compute(qty, price, discount_rate):
  discount_amount = qty * price * discount_rate
  discount_price = price - discount_amount
  return discount_amount, discount_price

qty = int(input("Enter the quantity: "))
price = float(input("Enter the price: "))
discount_rate = float(input("Enter the discount rate: "))


discount_amount, discount_price = compute(qty, price, discount_rate)



print(f'Quantity: {qty}')
print(f'Price: ${price:.2f}') 

print(f'Discount amount: ${discount_amount:.2f}')
print(f'Discounted price: ${discount_price:.2f}')


