numList = int(input("Enter a number of lines for a list: ")) #1
list = []

for i in range(numList):
  numInt = int(input("Enter a number: "))
  list.append(numInt)
  
list.insert(0, 99) #2
print(list)

list[0] = 100 #3
print(list)

second_list = [500, 600, 700, 800, 900] #4
second_list.pop(3) #5
second_list.pop(2) #6
print(second_list)

list.extend(second_list)
print("First list after extending with the second list:", list)


grades = ['A', 'B', 'C', 'A', 'A', 'C'] #7

print("Number of A grades:", grades.count('A')) #8

print("B index", grades.index('B')) #9

print("Number of F grades:", grades.count('F')) #10

grades.clear() #11
print(grades)

del grades  #12

player_list = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"] #13

player_list.sort()

print(player_list) #14

players2 = (player_list) #15
print(players2)

players2.reverse() #16
print(players2)

