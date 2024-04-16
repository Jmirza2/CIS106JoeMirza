def display_names(l_names, exam_scores):
  for i in l_names, exam_scores:
    print(i)
  for j in exam_scores:
    print(j)
  l = len(l_names)
  for x in range(0, l, 1):
    print(x, " ", l_names[x], " ", exam_scores[x])

f = open("last_names.txt", "r")


def high_low(l_names, exam_scores):
  l = len(l_names)
  highsalary = -1.0
  lowsalary = 99999999.99
  for y in range(0, l, 1):
    if float(exam_scores[y]) > float(highsalary):
      hiindex = y
      highsalary = exam_scores[y]

    if float(exam_scores[y]) < float(lowsalary):
      loindex = y
      lowsalary = exam_scores[y]

  print("highest salary", l_names[hiindex], exam_scores[hiindex])
  print("lowest salary", l_names[loindex], exam_scores[loindex])



l_names = []
exam_scores = []

last_names = f.readline()  

while last_names != "":
  l_names.append(str(last_names).rstrip("\n"))
  s = float(f.readline())
  exam_scores.append(s)
  last_names = f.readline( )
f.close()
display_names(l_names, exam_scores)
