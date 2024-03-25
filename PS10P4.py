def ticket(miles):
  if miles >= 30:
      train_tix = 12.00
  elif 20 <= miles <= 29:
      train_tix = 10.00
  elif 10 <= miles <= 19:
      train_tix = 8.00
  else:
      train_tix = 5.00
  return train_tix
    
  
total_ticket_price = 0

r = input("Do you want to begin the program? (Yes/No)  ")
while r == "Yes":
  last_name = input("Enter your last name: ")
  miles = int(input("Enter the number of miles to Downtown Chicago: "))

  train_tix = ticket(miles)
  print(f"The ticket price is: {train_tix}")

  total_ticket_price += train_tix


  r = input("Do you want to continue with the program? (Yes/No): ")
print(f"The total ticket price is: {total_ticket_price}")



