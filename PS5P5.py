lastName = input("Enter your last name: ")
nmbrDept = int(input("Enter the number of dependents: "))
grossIncome = int(input("Enter your gross income: "))

adjGrossPay = grossIncome - nmbrDept * 12000.00

if adjGrossPay > 50000.00:
  taxRate = 0.20
else:
  taxRate = 0.10

incomeTax = adjGrossPay * taxRate

if incomeTax < 0:  
  incomeTax = 100.00

print("Last name: " + lastName)
print('Gross income: ', grossIncome)
print('Number of dependents: ', nmbrDept)
print('Adjusted gross income: ', adjGrossPay)
print('Income tax: ', incomeTax)
