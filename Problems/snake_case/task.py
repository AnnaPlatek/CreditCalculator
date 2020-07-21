camel_word = input()
snake_word = ""
for char in camel_word:
    if char.islower():
        snake_word += char
    elif char.isupper():
        snake_word += "_" + char.lower()
print(snake_word)
