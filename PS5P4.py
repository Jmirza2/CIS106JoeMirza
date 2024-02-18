name = input("What is the name of your appliance? ")
applianceCost = float(input("What is the cost of your appliance? "))

if applianceCost >= 1000:
  warranty = applianceCost * 0.10
else:
  warranty = applianceCost * 0.05

total = applianceCost + warranty

print('Name: ', name)
print('The cost of Appliance: $',applianceCost)
print('Warranty: $',warranty)
print('Total: $',total)


      
