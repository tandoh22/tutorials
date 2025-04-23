brand = {"Lacoste": 120,
         "Prada": 200,
         "luis vuiton": 180,
         "gucci": 120,
         "balenciaga": 400,
         "casablanca": 100,
         "off-white": 150,
         "versace": 320}
cart = []
total = 0

print("--------- AVAILABLE ITEMS ----------")
for key, value in brand.items():
    print(f"{key:15} {value:.2f}")
print("------------------------------------")

while True:
    shirt = input("Select a brand to buy (e to exit): ")
    if shirt.lower() == "e":
        break
    elif brand.get(shirt) is not None:
        cart.append(shirt)

print("--------- YOUR ORDER ---------")
for shirt in cart:
    total += brand.get(shirt)
    print(shirt)

print()
print(f"The total cost of your items is: ${total:.2f}")