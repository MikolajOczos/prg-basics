def sum_digits(any_number):
    # Convert the number to a string and sum its digits
    result = sum(int(digit) for digit in str(any_number))
    return result

any_number = int(input('Enter integer number: '))
ABSOLUT = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {ABSOLUT}')21