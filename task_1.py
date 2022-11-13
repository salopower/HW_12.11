a = int(input('Enter the number a '))
b = int(input('Enter the number b '))
c = int(input('Enter the number c '))
number = "Yes" if min(a, b, c) > 10 and min(a, b) % 3 == 0 else "No"
print(number)