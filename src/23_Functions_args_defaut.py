def discount_price(price, discount=0):
    return price - ((price / 100) * discount)

x = discount_price(919);

print(f"{x}")