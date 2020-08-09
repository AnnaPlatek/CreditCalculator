user_list = []
user_input = ''
while True:
    user_input = input()
    if user_input =='.':
        break
    else:
        user_list.append(user_input)
print(user_list)
print(len(user_list))
