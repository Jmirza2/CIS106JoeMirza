def value(county, mkt_value):
  if county == "Cook":
    assessed_value_percent = 0.90
  elif county == "DuPage":
    assessed_value_percent = 0.80
  elif county == "McHenry":
    assessed_value_percent = 0.75
  elif county == "Kane":
    assessed_value_percent = 0.60
  else:
    assessed_value_percent = 0.70
    
  assessed_value = mkt_value * assessed_value_percent
  return assessed_value
    
total_market_values = 0
total_assessed_values = 0

r = input("Do you want to start this program?: ")
while r == 'Yes':
  county = input('Enter your county: ')
  mkt_value = float(input("Enter your home's market value: "))


  assessed_value = value(county, mkt_value)
  print(f"The assessed value is: {assessed_value}")

  total_market_values += mkt_value
  total_assessed_values += assessed_value

  r = input("Do you want to continue this program?: ")


print(f"Total market values: {total_market_values}")
print(f"Total assessed values: {total_assessed_values}")
      
  