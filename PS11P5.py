total = 0.0
tax = 0.0
def compTotal(quantity, unit_Price):
  global total
  total = quantity * unit_Price
  global tax
  tax = total * .07
  return 





quantity = int(input("Enter the quantity of the item: "))
unit_Price = float(input("Enter the unit price of the item: "))

compTotal(quantity, unit_Price)


print("Your total is $", format(float(total),'10,.2f'))
print("The tax is:  $", format(float(tax),'10,.2f'))