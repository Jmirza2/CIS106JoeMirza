def tuition_owed(credit_hours, district_code):
    tuition = 0.0
    if district_code == 'I':
        tuition = 250 * credit_hours
    elif district_code == 'O':
        tuition = 550 * credit_hours
    return tuition

total_tuition = 0.0

r = input("Do you want to start? (Yes or No): ").lower()

while r == "yes":
    last_name = input("Enter last name: ")
    district_code = input("Enter your district code: ")
    credit_hours = int(input("Enter your credit hours: "))

    tuition = tuition_owed(credit_hours, district_code)


    total_tuition += tuition
  
    print(f'Last name: {last_name}')
    print(f'Tuition owed   $: {tuition}')

  

    r = input("Do you want to continue? (Yes or No): ").lower()

print("Total Tuition owed for all students: $", total_tuition)




