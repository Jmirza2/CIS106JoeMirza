books = int(input("Enter the amount of books to order: "))
costPerBook = float(input("Enter the cost of each book: "))
bookTotal = books * costPerBook



if bookTotal >= 50.00:
  shipping = 0
else: 
  shipping = 25.00

orderTotal = bookTotal + shipping

print("Book Total: " , bookTotal)
print("Shipping: " , shipping)
print("Order Total: " , orderTotal)