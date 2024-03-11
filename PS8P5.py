f = open("p5d.txt", "r")

last_name = f.readline().rstrip('\n') 
total_tuition = 0.0
num_students = 0

cost_per_credit = 1000.00
 
while last_name != "":
    district_code = f.readline() 
    credits_taken = float(f.readline())
  
    if district_code == "I":
        cost_per_credit = 250.00
    else:
        cost_per_credit = 500.00
      
    tuition_owed = credits_taken * cost_per_credit
    total_tuition += tuition_owed
    num_students += 1
  
    print(f'Student Last name:  {last_name}')
    print(f'District Code:  {district_code}')
    print(f'Credits taken:  {credits_taken}')
    print(f'Tuition owed:  {tuition_owed}')
    last_name = f.readline().rstrip('\n')

f.close()
print("Total tuition owed:   $", total_tuition)
print("Number of students:", num_students)


