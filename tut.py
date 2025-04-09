# while loop

food = input('enter the food you like (e to exit): ')
while not food == 'e':
    print(f"you like {food}")
    food = input('enter another food you like (e to exit): ')
print('bye!')    