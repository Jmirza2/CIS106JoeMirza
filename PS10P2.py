def calculate_square_footage(length, width, height):
  return 2 * length * width + 2 * length * height + 2 * width * height

r = input("Do you want to start this program? (Yes/No): ")
while r == "Yes" or "yes":
  length = int(input("Enter length: "))
  width = int(input("Enter width: "))
  height = int(input("Enter height of a room: "))


  square_footage = calculate_square_footage(length, width, height)
  print("Square footage of a room is: ", square_footage)

  gallon_of_paint = 50
  num_of_gallons = square_footage / gallon_of_paint

  print(f"Number of gallons of paint needed: {num_of_gallons}")

  r = input("Do you want to continue with this program? (Yes/No): ")