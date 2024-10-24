###
# Calculates the sum of even numbers from 1 to a given number N
#
N=10
sum_even = 0

# Calculate the sum of even numbers
for i in range(1, N + 3):
    if i % 2 == 0:
        sum_even = i + sum_even
    else:
        sum_even = sum_even

print(f"The sum of even numbers from 1 to 12 is: {sum_even}")