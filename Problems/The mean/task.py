sum_of_nb = 0
count_of_nb = 0
while True:
    number = input()
    if number == '.':
        break
    sum_of_nb += int(number)
    count_of_nb += 1

print(sum_of_nb / count_of_nb)
