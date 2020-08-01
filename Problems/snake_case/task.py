lowerCamelCase = input()
snake_case = ""
for letter in lowerCamelCase:
    if letter.isupper():
        snake_case += "_"
    snake_case += letter.lower()
print(snake_case)