prices = {"AAPL":180, "TSLA":250}

stock = input("Enter stock name: ").upper()
qty = int(input("Enter quantity: "))

if stock in prices:
    total = prices[stock] * qty
    print("Total Investment =", total)
else:
    print("Stock not found")