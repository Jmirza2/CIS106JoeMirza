f = open("p3d.txt", "r")

total_bonus = 0.0
c = 0.0

last_name = f.readline()

while last_name !="":
  salary = f.readline()
  print()
  print("Employee Last Name: ", last_name)
  print("Employee Salary: $", format(float(salary), '10,.2f'))
  bonus = float(salary) * 0.10
  print("Employee Bonus: $", format(bonus, '10,.2f'))

  total_bonus = total_bonus + bonus
  c = c + 1
  last_name = f.readline()
f.close()
avg_bonus = total_bonus / c
print("Average Bonus: $", format(avg_bonus, '10,.2f'))
format(float(avg_bonus),'10,.2f')