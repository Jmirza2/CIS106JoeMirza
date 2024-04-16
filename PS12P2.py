def display_names(l_names, exam_scores):
  for i in l_names, exam_scores:
    print(i)
  for j in exam_scores:
    print(j)
  l = len(l_names)
  for x in range(0, l, 1):
    print(x, " ", l_names[x], " ", exam_scores[x])

f = open("last_names.txt", "r")



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
  






    


    



    

