shirts = []
prices = []
total = 0
 
while True:
    shirt = input("enter a brand to buy (e to exit): ")
    if shirt.lower == "e":
        break
    else:
        price = float(input(f"enter the price of the {shirt}"))
        shirts.append(shirt)
        prices.append(price)