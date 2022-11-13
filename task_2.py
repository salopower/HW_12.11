numbers = input('Enter numbers separated by a space: ').split()
numbers_list = list(map(int, numbers))
max_number = max(numbers_list)
print(max_number)
