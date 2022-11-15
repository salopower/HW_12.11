a, b, c = map(int, input('Enter numbers separated by a space: ').split())
if min(a, b, c) > 10 and a % 3 == 0 and b % 3 == 0:
    print("yes")
else:
    print("no")
