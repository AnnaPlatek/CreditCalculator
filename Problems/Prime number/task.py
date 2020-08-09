user_number = int(input())
if user_number > 1:
    for i in range(2, user_number + 1):
        if i == user_number:
            print("This number is prime")
            break
        if user_number % i == 0:
            print("This number is not prime")
            break
else:
    print("This number is not prime")

