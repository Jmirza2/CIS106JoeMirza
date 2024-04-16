def display_last_names(last_name):
  for i in range(0,5):
    print(last_name[i])

last_name = ["Smith", "Stone", "Williams", "Myers", "Brock"]

f = open("last_names.txt", "r")

for x in range(4, -1, -1):
  print("Reverse order: ", last_name[x])

