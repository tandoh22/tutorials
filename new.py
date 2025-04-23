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