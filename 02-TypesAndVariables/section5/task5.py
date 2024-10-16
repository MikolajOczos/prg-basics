product_price = float(input('what is the product price?'))
discount = float(input('what is the discount on the product in %?'))
discount_amount = (product_price*discount/100)
after_discount = (product_price - discount_amount)
print(f'Product price was {product_price}')
print(f'The discount amount is {discount_amount}')
print(f'The amount after discount is {after_discount}')


