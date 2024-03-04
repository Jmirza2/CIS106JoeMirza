user = input("Do you want to do this program? ")
employee_count = 0
total_gross_pay = 0


while user == "yes" or user == "Yes":
    last_name = input("Enter your last name: ")
    hours = int(input("Enter the amount of hours worked: "))
    rate = float(input("Enter the hourly rate: "))
    gross_pay = hours * rate
    if hours > 40:
        gross_pay = (40 * rate) + ((hours - 40) * rate * 1.5)
    total_gross_pay += gross_pay
    employee_count = employee_count + 1
    print("Employee Last Name:", last_name)
    print("Gross Pay:", gross_pay)
    print("Total of employees: ", employee_count)
    user = input("Do you want to continue?  ")

average_pay = total_gross_pay / employee_count

print("Sum of all gross pays:", total_gross_pay)
print("Number of employees:", employee_count)
print("Average pay:", average_pay)


        
    
