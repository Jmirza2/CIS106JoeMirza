principle = float(input("Enter the principle amount: "))
year_Maturity = int(input("Enter the year of maturity: "))

if principle > 100000 and year_Maturity == 5:
  interest_Rate = 0.06
elif 50000 <= principle <= 100000 and year_Maturity == 10:
  interest_Rate = 0.05
elif 50000 <= principle <= 100000 and year_Maturity == 5:
  interest_Rate = 0.04
else: 
  interest_Rate = 0.02

interest_Amount = principle * interest_Rate

print(f"Princple amount: ${principle}")
print(f"Interest Rate: {interest_Rate}")
print(f"Interest Amount: ${interest_Amount}")
