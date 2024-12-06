price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
before_discount= 0
for key,value in price_list.items():
    before_discount = before_discount + value

print()