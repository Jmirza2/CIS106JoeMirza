def compute(examScore1, examScore2, examScore3):
    avg_score = (examScore1 + examScore2 + examScore3)  / 3
    total_points = examScore1 + examScore2 + examScore3
    return avg_score, total_points

last_name = input("Enter your last name: ")
examScore1 = float(input("Enter your first exam score: "))
examScore2 = float(input("Enter your second exam score: "))
examScore3 = float(input("Enter your third exam score: "))

avg_score, total_points = compute(examScore1, examScore2, examScore3)

print(f"Student's last name: {last_name}")
print(f"Student's total points: {total_points}")
print(f"Student's Average exam score: {avg_score}")

