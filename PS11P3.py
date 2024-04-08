def compute(sales):
  if sales > 100000:
    commission = .1
    next_years_target = sales * .1
  else:
    commission = .05
    next_years_target = sales * .05
  return commission, next_years_target
    
  

salesPerson_lastName = input("Enter Sales Person Last Name: ")
sales = int(input("Enter Sales: "))


commisison, next_years_target = compute(sales)


print(f"Sales person: {salesPerson_lastName}")
print(f"Commission: {commisison * 100}%")
print(f"Next year's target: ${next_years_target}")
