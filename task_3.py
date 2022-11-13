number = int(input("Enter a three-digit number: "))
number_list = list(str(number))
number_list.reverse()
reversed_number = "".join(number_list)
print(f"Reversed number: {reversed_number}")

