examScore_1 = input("Enter your first exam score: ")
examScore_2 = input("Enter your second exam score: ")

total_1 = 0.6 * float(examScore_1)
total_2 = 0.4 * float(examScore_2)

print("The first exam is worth: ", total_1)
print("The second exam is worth: ", total_2)

total_score = total_1 + total_2
print("Your total score is: ", total_score)
