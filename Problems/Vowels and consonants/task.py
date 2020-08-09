word = input()
for char in word:
    if char in "aeiou":
        print('vowel')
    elif char in "bcdfghjklmnqprstvwxz":
        print('consonant')
    else:
        break