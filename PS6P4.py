num_tix = int(input("Enter number of concert tickets: "))
# 3 

price_per_tix = 0

if num_tix >=25:
  price_per_tix = 50
elif 10 <= num_tix <= 24:
  price_per_tix = 60
elif 5 <= num_tix <= 9:
  price_per_tix = 70
elif num_tix < 5:
  price_per_tix = 75


total_price = num_tix * price_per_tix
# 3 * 75 = 225

print(f"Number of tickets: {num_tix}")
print(f"Price per ticket: ${price_per_tix}")
print(f"Total price: ${total_price}")

