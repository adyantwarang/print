#Entering values
Cost_price = float(input("Enter the cost price: "))
Sell_price = float(input("Enter the sell price: "))

Amount = Sell_price - Cost_price

if Amount > 0:
  print("You got profit{0}".format(Amount))


else:
 print("No profit")
  
