principle = float(input("Enter the principle amount: "))
rate = float(input("Enter the rate of interest: "))

for count in range(1,6):
  interest = principle * rate 
  endBalance = principle + interest
  print(count, "    ", principle, "    ", endBalance)
  principle = endBalance



 