cafe = []
cats = []
while True:
    user_input = input()
    if user_input == 'MEOW':
        break
    else:
        cat_cafe = user_input.split()
        cafe.append(cat_cafe[0])
        cats.append(int(cat_cafe[1]))
max_nb_of_cats = (cats.index(max(cats)))
print(cafe[max_nb_of_cats])


