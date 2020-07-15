user_money = int(input())
if user_money >= 6769:
    animal_number = user_money // 6769
    if animal_number > 1:
        print(animal_number, "sheep")
    else:
        print(animal_number, "sheep")
elif user_money >= 3848:
    animal_number = user_money // 3848
    if animal_number > 1:
        print(animal_number, "cows")
    else:
        print(animal_number, "cow")
elif user_money >= 1296:
    animal_number = user_money // 1296
    if animal_number > 1:
        print(animal_number, "pigs")
    else:
        print(animal_number, "pig")
elif user_money >= 678:
    animal_number = user_money // 678
    if animal_number > 1:
        print(animal_number, "goats")
    else:
        print(animal_number, "goat")
elif user_money >= 23:
    animal_number = user_money // 23
    if animal_number > 1:
        print(animal_number, "chickens")
    else:
        print(animal_number, "chicken")
else:
    print("None")