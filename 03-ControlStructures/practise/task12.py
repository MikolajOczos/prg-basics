price = int(input("What is the price of the product?"))
amount = int(input("What is the amount of the products you wanna purchase?"))
final_amount = 0
if amount <= 1:
    final_amount = amount*price
else:
    final_amount = price + ((price*0.75)*(amount-1))

print(f"The final amount to pay sums up to {final_amount}")

