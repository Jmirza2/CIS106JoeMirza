def calculate_payrate(job_code):
    pay_rate = 0.0
    if job_code == 'L':
        pay_rate = 25
    elif job_code == 'A':
        pay_rate = 30
    elif job_code == 'J':
        pay_rate = 50
    return pay_rate

total_gross_pay = 0.0

r = input("Do you want to start? (Yes or No): ").lower()

while r == "yes":
    last_name = input("Enter last name: ")
    job_code = input("Enter job code: ")
    hours = int(input("Enter hours worked: "))

    pay_rate = calculate_payrate(job_code)

    if hours > 40:
        gross_pay = (pay_rate * 40) + (1.5 * pay_rate) * (hours - 40)
    else:
        gross_pay = pay_rate * hours

    total_gross_pay += gross_pay

    print(f'Last name: {last_name}')
    print(f'Gross Pay   $: {gross_pay}')

    r = input("Do you want to continue? (Yes or No): ").lower()

print("Total Gross Pay for all employees: $", total_gross_pay)





