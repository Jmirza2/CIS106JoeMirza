count = 0
total_exam = 0
user = input("Do you want to continue with the program? ")

while user == "yes" or user == "Yes":
    print("Okay, we will continue")
    lastName = input("What is your last name? ") 
    exam1 = int(input("What is your last exam1 score? "))
    exam2 = int(input("What is your last exam2 score? "))
    avgScore = (exam1 + exam2) / 2
    
    
    print(lastName, "has an average of", avgScore)
    total_exam = total_exam + exam1
    count = count + 1

    print("Total number of students:", count)
    user = input("Do you want to continue? ")


  

