def forecast(month, sales):
  forecast_percent = 0.0

  if month == "Jan" or "Feb" or "Mar":
    forecast_percent = 0.10
  elif month == "Apr" or "May" "Jun":
    forecast_percent = 0.15
  elif month == "Jul" or "Aug" or "Sep":
    forecast_percent = 0.20
  elif month == "Oct" or "Nov" or "Dec":
    forecast_percent = 0.25

  next_month_sales = sales * (1 + forecast_percent)
  return next_month_sales

r = input("Do you want to begin this program? (Yes or No): ")

while r == "Yes":
  last_name = input("Please enter your last name: ")
  month = input("What is your birth month? ")
  sales = float(input("How many sales did you make this month?: "))

  next_month_sales = forecast(month, sales)
  print(f"Next month's sales forecast for {last_name}: {next_month_sales}")
  r = input("Do you want to continue this program? (Yes or No): ")









 