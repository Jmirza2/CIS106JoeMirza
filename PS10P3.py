def out_of_door_price(msrp, make, model, electric_vehicle_code):
  if make == "Honda" and model == "Accord":
      percent_off = 0.10
  elif make == "Toyota" and model == "Rav4":
      percent_off = 0.15
  elif electric_vehicle_code == "Y":
      percent_off = 0.30
  else:
      percent_off = 0.05

  new_msrp = msrp * (1 - percent_off)
  out_the_door_price = new_msrp * 1.07
  return out_the_door_price

total_msrp = 0
total_sales_price = 0
r = input("Do you want to start this program? (Yes/No): ")

while r == "Yes":
  make = input("What is the make of the car: ")
  model = input("What is the model of the car: ")
  electric_vehicle_code = input("Is it an electric vehicle? (Y/N): ")
  msrp = float(input("What is the sticker price: "))
  
  electric_vehicle = electric_vehicle_code == "Y"
  
  out_the_door_price = out_of_door_price(msrp, make, model, electric_vehicle)

  total_msrp += msrp
  total_sales_price += out_the_door_price

  print(f'Out-the-door price of the car: {out_the_door_price}')

print(f'Total MSRP of all cars: {total_msrp}')
print(f'Total sales price of all cars: {total_sales_price}')





