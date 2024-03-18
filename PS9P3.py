def calculate_mpg(miles_traveled, gallons):
  return miles_traveled / gallons


gallons = 0  
miles_traveled = 0
total_miles_traveled = 0

r = input("Do you want to start? (Yes or No): ").lower()

while r == "yes":
    destination = input("Enter the destination you want to visit: ")
    miles_traveled = float(input("Enter the number of miles travled: "))
    gallons = int(input("Enter the amount of gallons used: "))
    
    total_number_trips = calculate_mpg(miles_traveled, gallons)

  
    print(f"Destination: {destination}")
    print(f"Miles traveled: {miles_traveled}")
    print(f"Miles per gallon each trip: {total_number_trips}")
    total_miles_traveled += 1
    print("Total number of trips: ", total_miles_traveled)
    r = input("Do you want to start? (Yes or No): ").lower()
print("Total number of trips: ", total_miles_traveled)





  

  

 