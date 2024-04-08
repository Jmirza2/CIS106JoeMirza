def compute():
  average_Score = (score1 + score2 + score3) / 3
  average_Score_handi = (score1 + score2 + score3 + handicapped) / 4
  return average_Score, average_Score_handi


                   
last_Name = input("Enter your last name: ")
score1 = int(input("Enter game score one: "))
score2 = int(input("Enter game score two: "))
score3 = int(input("Enter game score three: "))
handicapped = int(input("Enter game score for handicapped: "))

average_Score, average_Score_handi = compute()


print(f"Last name: {last_Name}")
print(f"Average score: {average_Score}")
print(f"Average score Handicapped: {average_Score_handi}")
