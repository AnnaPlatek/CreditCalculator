scores = input().split()
# put your python code here
correct_nb = 0
incorrect_nb = 0
for char in scores:
    if char == 'C':
        correct_nb += 1
    if char == 'I':
        incorrect_nb += 1
    if incorrect_nb >= 3:
        break
if incorrect_nb >= 3:
    print('Game over')
    print(correct_nb)
else:
    print('You won')
    print(correct_nb)