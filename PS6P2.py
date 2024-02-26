part = int(input("Enter a part number: "))
quantity = int(input("Enter a quantity: "))

if part == 10 or part == 55:
  unit_Cost = 1.00
elif part == 99:
  unit_Cost = 2.00
elif part == 80 or part == 70:
  unit_Cost = 3.00
else:
  unit_Cost = 5.00


total = quantity * unit_Cost

print(f"Part: {part}")
print(f"Unit Price: ${unit_Cost}")
print(f"Total: ${total}")
