def calculate_batting_average(number_of_hits, bats):
  return number_of_hits / bats

player_count = 0  

r = input("Do you want to start? (Yes or No): ").lower()

while r == "yes":
      last_name = input("Enter Last Name: ")
      hits = int(input("Enter Number of Hits: "))
      at_bats = int(input("Enter Number of At Bats: "))

      bat_avg = calculate_batting_average(hits, at_bats)

      print("Last Name:", last_name)
      print("Batting Average:", bat_avg)
      player_count += 1
      print("Total Players:", player_count)
      r = input("Do you want to continue? (Yes or No): ").lower()
  
  


  
