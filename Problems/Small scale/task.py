numbers = []
while True:
    number_input = input()
    if number_input == '.':
        break
    else:
        numbers.append(float(number_input))
print(min(numbers))