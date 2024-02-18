lastName = input("Enter your last name: ")
nmbrDept = input("Enter the number of dependents: ")
grossIncome = int(input("Enter your gross income: "))

adjGrossPay = grossIncome - 12000.00 * float(nmbrDept)

if adjGrossPay > 50000.00:
  taxRate = adjGrossPay * 0.20
else:
  taxRate = adjGrossPay * 0.10


if taxRate < 0:  
  taxRate = 100.00 

print("Last name: " + lastName)
print('Gross income: ', grossIncome)
print('Number of dependents: ', nmbrDept)
print('Adjusted gross income: ', adjGrossPay)
print('Income tax: ', taxRate)
