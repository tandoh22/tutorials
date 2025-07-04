def net_price(list_price, discount, tax):
    return list_price * (1 - discount) * (1 + tax)
print(net_price(200, 0.5, 0.01))

