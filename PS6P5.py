last_name = input("Enter your last name: ")
# Smith
salary = float(input("Enter your salary: "))
# 90000
job_Level = int(input("Enter your job level: "))
# 12

if job_Level >= 10:
  bonus_rate = 0.25
elif job_Level >= 5 and job_Level <= 9:
  bonus_rate = 0.20
else:
  bonus_rate = 0.10


bonus = salary * bonus_rate
# $22500.0

print(f"Last name: {last_name}")
print(f"Bonus: ${bonus:}")



