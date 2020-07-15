column = int(input())
row = int(input())

if column == 1 or column == 8:
    if row == 1 or row == 8:
        print(3)
    else:
        print(5)
else:
    if row == 1 or row ==8:
        print(5)
    else:
        print(8)