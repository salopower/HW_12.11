number = int(input('Enter a three-digit number: '))
reversed_number = 0
while number > 0:
    num = number % 10

    number = number // 10

    reversed_number = reversed_number * 10

    reversed_number = reversed_number + num

print(f'Reversed number is: {reversed_number}')



