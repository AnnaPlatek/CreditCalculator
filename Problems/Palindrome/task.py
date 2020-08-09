word = input()
backward = word[::-1]
if word == backward:
    print('Palindrome')
else:
    print('Not palindrome')