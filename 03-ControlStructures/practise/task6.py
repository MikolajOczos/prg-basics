time = int(input("What is the number of hours you have been parked sir?"))
amount = 0
if time > 6:
    amount += 20
elif time > 3:
    amount += 15
else:
    amount += 5
print(f"You owe us {amount} for the parking fee!")